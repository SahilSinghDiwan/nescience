# ==========================================================
# NESCIENCE — web exhibit
#
# An interactive digital exhibit framed as an ongoing investigation
# into what we do not yet understand about the human mind.
#
#   Participant  -> gives testimony (the interview)
#   Investigator -> explores the archive + the concept atlas
#
# A participant's testimony is matched against the concept atlas
# (knowledge.graph.py) via each concept's interview_themes, turning
# raw answers into "leads" the investigation can follow.
# ==========================================================

import datetime
import hashlib
import hmac
import math
import os
from functools import wraps

from flask import (
    Flask, render_template, request, jsonify, abort, url_for, redirect, session
)

import bibliography
import database
import identity
import notes
from protocol import INTERVIEW_PROTOCOL
from atlas import concepts, is_defined
from matcher import match_interview

app = Flask(__name__)
# Needed only to sign the investigator session cookie. Supply a stable value
# via NESCIENCE_SECRET_KEY in any real deployment; the random fallback just
# means investigator sessions don't survive a dev-server restart.
app.secret_key = os.environ.get("NESCIENCE_SECRET_KEY") or os.urandom(32)

MAX_ANSWER_LEN = 5000


# ----------------------------------------------------------
# Investigator auth (NESC-02)
#
# The investigator surface is owner-only: it shows everything public routes
# must never reveal — real names, unpublished testimony, the name->code map.
# It is gated by a password read from the environment; if that variable is
# unset the whole surface is disabled (404), so it can never sit open by
# default. No user accounts — a single shared password + a signed session.
# ----------------------------------------------------------

def _investigator_password():
    """The configured password, or None when the surface is disabled."""
    return os.environ.get("NESCIENCE_INVESTIGATOR_PASSWORD") or None


def investigator_required(view):
    """Gate a view: 404 when unconfigured, login prompt when unauthenticated."""
    @wraps(view)
    def wrapped(*args, **kwargs):
        if _investigator_password() is None:
            abort(404)
        if not session.get("investigator"):
            return render_template("investigator_login.html", error=None), 401
        return view(*args, **kwargs)
    return wrapped


# ----------------------------------------------------------
# Helpers
# ----------------------------------------------------------

def _module_order():
    """The interview modules, in protocol order, excluding the framing
    sections that are not question modules."""
    return [
        name for name in INTERVIEW_PROTOCOL
        if name not in ("Introduction", "Participant Information", "Publication")
    ]


def _numbered_protocol():
    """Yield (module, [(question_number, question_text), ...]) with the
    same global numbering the CLI uses, so client and server agree."""
    n = 1
    out = []
    for module in _module_order():
        items = []
        for question in INTERVIEW_PROTOCOL[module]:
            items.append((n, question))
            n += 1
        out.append((module, items))
    return out


def _sanitise_interview(payload):
    """Turn an untrusted client payload into a clean interview record
    with the same shape the CLI produces."""
    record = {}

    # Participant information
    info = {}
    for field in INTERVIEW_PROTOCOL["Participant Information"]:
        value = payload.get("Participant Information", {}).get(field, "")
        info[field] = str(value)[:MAX_ANSWER_LEN].strip()
    record["Participant Information"] = info

    # Question modules
    for module, items in _numbered_protocol():
        answers = {}
        submitted = payload.get(module, {}) if isinstance(payload.get(module), dict) else {}
        for number, _question in items:
            key = f"Question {number}"
            answers[key] = str(submitted.get(key, ""))[:MAX_ANSWER_LEN].strip()
        record[module] = answers

    # Case metadata (string-only so the CLI archive view still renders it)
    record["Case File"] = {
        "Recorded": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    return record


def _case_number(index):
    return f"{index + 1:03d}"


# ----------------------------------------------------------
# Routes — the exhibit
# ----------------------------------------------------------

@app.route("/")
def landing():
    return render_template(
        "landing.html",
        intro=INTERVIEW_PROTOCOL["Introduction"],
    )


# ----------------------------------------------------------
# Routes — participant: the interview
# ----------------------------------------------------------

@app.route("/interview")
def interview():
    return render_template(
        "interview.html",
        intro=INTERVIEW_PROTOCOL["Introduction"],
        participant_fields=INTERVIEW_PROTOCOL["Participant Information"],
        publication=INTERVIEW_PROTOCOL["Publication"],
        modules=_numbered_protocol(),
    )


@app.route("/api/interview", methods=["POST"])
def api_interview():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid submission."}), 400

    record = _sanitise_interview(payload)

    # Identity & consent (NESC-01/05): the real name is collected up front but
    # kept private — it is stamped into the Case File block, never into the
    # public Participant Information. A code is assigned from the records that
    # already exist, and the participant's publication choice is recorded.
    name = str(payload.get("name", ""))[:MAX_ANSWER_LEN].strip()
    published = bool(payload.get("published", False))
    existing = database.load_interviews()
    code = identity.apply_identity(record, name, published, existing)

    database.save_interview(record)

    index = len(existing)  # position of the record just appended
    matches = match_interview(record)

    return jsonify(
        {
            "code": code,
            "published": published,
            "case_number": _case_number(index),
            "case_index": index,
            "matches": matches,
            # Public, code-only record — surfaced only if the participant published.
            "public_url": url_for("archive_witness", code=code) if published else None,
        }
    )


# ----------------------------------------------------------
# Routes — investigator: the archive hub (NESC-07)
#
# `/archive` is the hub: six numbered ways into the investigation.
# All six are now built and wired directly (the "in progress" placeholder
# the unbuilt ones used to resolve to retired with NESC-13).
# ----------------------------------------------------------

# The six ways into the archive, in order — the single source of truth for
# the hub.
_ARCHIVE_SECTIONS = [
    {
        "idx": "001",
        "name": "Case Files",
        "desc": "Deep investigations into single concepts of the mind, "
                "mapped and cross-referenced.",
        "endpoint": "atlas_index",
    },
    {
        "idx": "002",
        "name": "Witness Accounts",
        "desc": "Testimony on record from consenting participants, filed "
                "under code only.",
        "endpoint": "archive_witnesses",
    },
    {
        "idx": "003",
        "name": "Connections",
        "desc": "The corkboard — threads strung between concepts across the "
                "investigation.",
        "endpoint": "connections",
    },
    {
        "idx": "004",
        "name": "Open Questions",
        "desc": "Where the evidence runs out — the philosophical heart of the "
                "inquiry.",
        "endpoint": "open_questions",
    },
    {
        "idx": "005",
        "name": "Evidence Room",
        "desc": "Exhibits sorted by what we know, suspect, dispute, and do not "
                "know.",
        "endpoint": "evidence_room",
    },
    {
        "idx": "006",
        "name": "Investigation Notes",
        "desc": "How this investigation works — what it accepts as evidence, "
                "and where it agrees to stop.",
        "endpoint": "investigation_notes",
    },
]


@app.route("/archive")
def archive():
    """The archive hub — six ways into the question."""
    entries = [
        {
            "idx": section["idx"],
            "name": section["name"],
            "desc": section["desc"],
            "url": url_for(section["endpoint"]),
            "status": None,
        }
        for section in _ARCHIVE_SECTIONS
    ]
    return render_template("archive_hub.html", entries=entries)


@app.route("/archive/witnesses")
def archive_witnesses():
    """Witness Accounts — public, code-only (NESC-11 / §11a).

    Built strictly from identity.public_projection: only *published* records,
    each reduced to a code + responses. The private Case File (real name,
    timestamp, mapping) is dropped at the source, so no private field can
    reach this surface — identified by code alone."""
    published = identity.public_projection(database.load_interviews())
    cases = []
    for entry in published:
        responses = entry["responses"]
        cases.append(
            {
                "code": entry["code"],
                "info": responses.get("Participant Information", {}),
                "leads": [m["concept"] for m in match_interview(responses)],
            }
        )
    cases.reverse()  # newest first
    return render_template("archive.html", cases=cases)


@app.route("/archive/witnesses/<code>")
def archive_witness(code):
    """A single published witness account, under its code only."""
    published = identity.public_projection(database.load_interviews())
    entry = next((e for e in published if e["code"] == code), None)
    if entry is None:
        abort(404)
    responses = entry["responses"]
    return render_template(
        "witness.html",
        code=entry["code"],
        info=responses.get("Participant Information", {}),
        info_fields=INTERVIEW_PROTOCOL["Participant Information"],
        responses=responses,
        modules=_numbered_protocol(),
        matches=match_interview(responses),
    )


@app.route("/archive/<int:index>")
def archive_case(index):
    """A bare index is public only for *published* records, and redirects to
    the code-based witness view. Full case detail across all records (with
    private fields) belongs to the gated investigator surface (NESC-02)."""
    interviews = database.load_interviews()
    if 0 <= index < len(interviews) and identity.is_published(interviews[index]):
        code = identity.get_code(interviews[index])
        if code:
            return redirect(url_for("archive_witness", code=code))
    abort(404)


# Evidence Room tiers, in epistemic order (weakest claim of certainty last).
_EVIDENCE_TIERS = [
    ("what_we_know", "What we know"),
    ("evidence_suggests", "What the evidence suggests"),
    ("disagreement", "What researchers disagree about"),
    ("unknown", "What we don't know"),
]


@app.route("/archive/evidence-room")
def evidence_room():
    """[005] Evidence Room — every exhibit across the investigated concepts,
    sorted into the four epistemic tiers, each traced to a real reference."""
    grouped = []
    for key, label in _EVIDENCE_TIERS:
        items = []
        for name in concepts:
            if not is_defined(name):
                continue
            room = concepts[name].get("evidence_room", {}) or {}
            for entry in room.get(key, []) or []:
                items.append(
                    {
                        "concept": name,
                        "claim": entry.get("claim"),
                        "citation": bibliography.get(entry.get("citation")),
                    }
                )
        grouped.append(
            {"key": key, "label": label, "unknown": key == "unknown", "entries": items}
        )
    return render_template("evidence_room.html", grouped=grouped)


def _connection_layout():
    """A deterministic corkboard layout for the concept graph (NESC-12).

    Nodes are pinned around an ellipse with a stable per-name jitter (so the
    board looks hand-arranged but never moves between requests), and threads
    are the de-duplicated edges between connected concepts. Computed
    server-side so the view needs no physics engine and is reduced-motion safe."""
    names = list(concepts.keys())
    count = len(names) or 1
    cx, cy, rx, ry = 500.0, 330.0, 410.0, 250.0

    pos = {}
    for i, name in enumerate(names):
        angle = (2 * math.pi * i) / count - math.pi / 2
        seed = int(hashlib.md5(name.encode()).hexdigest(), 16)
        squeeze = 0.80 + (seed % 1000) / 1000 * 0.20  # 0.80–1.00, stable
        pos[name] = (
            round(cx + rx * math.cos(angle) * squeeze, 1),
            round(cy + ry * math.sin(angle) * squeeze, 1),
        )

    def links(name):
        raw = concepts[name].get("connected_files") or concepts[name].get("connects_to") or []
        return [o for o in raw if o in concepts]

    nodes = [
        {"name": name, "x": pos[name][0], "y": pos[name][1],
         "defined": is_defined(name), "neighbors": links(name)}
        for name in names
    ]

    seen, edges = set(), []
    for name in names:
        for other in links(name):
            key = tuple(sorted((name, other)))
            if key not in seen:
                seen.add(key)
                edges.append(
                    {"a": name, "b": other,
                     "x1": pos[name][0], "y1": pos[name][1],
                     "x2": pos[other][0], "y2": pos[other][1]}
                )
    return nodes, edges


@app.route("/archive/connections")
def connections():
    """[003] Connections — the dark corkboard: concepts pinned, threads strung
    between them, traversable into each case file."""
    nodes, edges = _connection_layout()
    return render_template("connections.html", nodes=nodes, edges=edges)


@app.route("/archive/open-questions")
def open_questions():
    """[004] Open Questions — the structured, unresolved questions gathered
    from every investigated concept."""
    groups = []
    for name in concepts:
        if not is_defined(name):
            continue
        questions = concepts[name].get("open_questions", []) or []
        if questions:
            groups.append(
                {
                    "concept": name,
                    "case_number": _case_number_for(name),
                    "questions": questions,
                }
            )
    return render_template("open_questions.html", groups=groups)


@app.route("/archive/notes")
def investigation_notes():
    """[006] Investigation Notes — the archive's methodology drawer (NESC-13).

    Public by design: how the investigation decides what counts as evidence
    is part of its argument, not backstage material. Notes are hand-authored
    markdown under docs/notes/, read fresh on each request so an edit shows
    up without a restart."""
    return render_template("notes.html", notes=notes.all_notes())


@app.route("/archive/notes/<slug>")
def investigation_note(slug):
    """One methodology note."""
    note = notes.get(slug)
    if note is None:
        abort(404)
    return render_template("note.html", note=note)


# ----------------------------------------------------------
# Routes — investigator: the concept atlas
# ----------------------------------------------------------

@app.route("/atlas")
def atlas_index():
    defined = [(name, concepts[name]) for name in concepts if is_defined(name)]
    stubs = [name for name in concepts if not is_defined(name)]
    return render_template("atlas.html", defined=defined, stubs=stubs)


def _case_number_for(name):
    """A concept's case number from its position in the atlas (Memory -> 001)."""
    order = list(concepts.keys())
    return f"{order.index(name) + 1:03d}"


@app.route("/atlas/<name>")
def atlas_concept(name):
    if name not in concepts:
        abort(404)
    concept = concepts[name]
    next_case = concept.get("next_case")
    return render_template(
        "concept.html",
        name=name,
        concept=concept,
        defined=is_defined(name),
        all_concepts=concepts,
        citations=bibliography.index_for(name),
        case_number=_case_number_for(name),
        next_case=next_case if next_case in concepts else None,
        next_case_number=_case_number_for(next_case) if next_case in concepts else None,
    )


# ----------------------------------------------------------
# Routes — investigator surface (password-gated, NESC-02)
# ----------------------------------------------------------

@app.route("/investigator/login", methods=["POST"])
def investigator_login():
    if _investigator_password() is None:
        abort(404)
    supplied = request.form.get("password", "")
    if hmac.compare_digest(supplied, _investigator_password()):
        session["investigator"] = True
        return redirect(url_for("investigator"))
    return render_template("investigator_login.html", error="Incorrect password."), 401


@app.route("/investigator/logout")
def investigator_logout():
    session.pop("investigator", None)
    return redirect(url_for("landing"))


@app.route("/investigator")
@investigator_required
def investigator():
    """The full case ledger — everything, including private fields."""
    interviews = database.load_interviews()
    rows = []
    for index, record in enumerate(interviews):
        rows.append(
            {
                "index": index,
                "code": identity.get_code(record) or "—",
                "name": identity.get_name(record) or "—",
                "published": identity.is_published(record),
                "recorded": record.get("Case File", {}).get("Recorded", "—"),
                "leads": [m["concept"] for m in match_interview(record)],
            }
        )
    rows.reverse()  # newest first
    return render_template(
        "investigator.html",
        rows=rows,
        count=len(interviews),
        mapping=identity.name_code_mapping(interviews),
    )


@app.route("/investigator/case/<int:index>")
@investigator_required
def investigator_case(index):
    """A full case file — real name, publication state, complete transcript."""
    interviews = database.load_interviews()
    if index < 0 or index >= len(interviews):
        abort(404)
    record = interviews[index]
    return render_template(
        "investigator_case.html",
        index=index,
        code=identity.get_code(record) or "—",
        name=identity.get_name(record) or "—",
        published=identity.is_published(record),
        recorded=record.get("Case File", {}).get("Recorded", "—"),
        record=record,
        info=record.get("Participant Information", {}),
        info_fields=INTERVIEW_PROTOCOL["Participant Information"],
        modules=_numbered_protocol(),
        matches=match_interview(record),
    )


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5001)
