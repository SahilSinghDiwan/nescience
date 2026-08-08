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

from flask import Flask, render_template, request, jsonify, abort, url_for, redirect

import database
import identity
from protocol import INTERVIEW_PROTOCOL
from atlas import concepts, is_defined
from matcher import match_interview

app = Flask(__name__)

MAX_ANSWER_LEN = 5000


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
# Surfaces that already exist are wired directly; those still to be
# built (NESC-09/10/12/13) resolve to an honest "in progress"
# placeholder rather than a dead link.
# ----------------------------------------------------------

# The six ways into the archive, in order — a single source of truth for
# both the hub and the placeholder route. A section with an `endpoint` is a
# built surface; one with a `slug` is not yet built (NESC-09/10/12/13) and
# resolves to the honest "in progress" placeholder.
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
        "slug": "connections",
        "desc": "The corkboard — threads strung between concepts across the "
                "investigation.",
        "blurb": "The corkboard of threads — how each concept pins to the "
                 "others — is still being strung.",
    },
    {
        "idx": "004",
        "name": "Open Questions",
        "slug": "open-questions",
        "desc": "Where the evidence runs out — the philosophical heart of the "
                "inquiry.",
        "blurb": "The philosophical heart: each question set beside what "
                 "science knows, what the evidence suggests, where it "
                 "disagrees, and what remains unknown.",
    },
    {
        "idx": "005",
        "name": "Evidence Room",
        "slug": "evidence-room",
        "desc": "Exhibits sorted by what we know, suspect, dispute, and do not "
                "know.",
        "blurb": "Exhibits sorted into four tiers — what we know, what the "
                 "evidence suggests, what researchers disagree about, and what "
                 "we don't know.",
    },
    {
        "idx": "006",
        "name": "Investigation Notes",
        "slug": "notes",
        "desc": "The investigator's working margins and running log.",
        "blurb": "The investigator's working margins — method, doubts, and the "
                 "running log of the inquiry.",
    },
]


@app.route("/archive")
def archive():
    """The archive hub — six ways into the question."""
    entries = []
    for section in _ARCHIVE_SECTIONS:
        if "endpoint" in section:
            url, status = url_for(section["endpoint"]), None
        else:
            url = url_for("archive_pending", section=section["slug"])
            status = "In progress"
        entries.append(
            {
                "idx": section["idx"],
                "name": section["name"],
                "desc": section["desc"],
                "url": url,
                "status": status,
            }
        )
    return render_template("archive_hub.html", entries=entries)


@app.route("/archive/pending/<section>")
def archive_pending(section):
    """Honest placeholder for archive surfaces not yet built."""
    meta = next((s for s in _ARCHIVE_SECTIONS if s.get("slug") == section), None)
    if meta is None:
        abort(404)
    return render_template(
        "placeholder.html", idx=meta["idx"], name=meta["name"], blurb=meta["blurb"]
    )


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


# ----------------------------------------------------------
# Routes — investigator: the concept atlas
# ----------------------------------------------------------

@app.route("/atlas")
def atlas_index():
    defined = [(name, concepts[name]) for name in concepts if is_defined(name)]
    stubs = [name for name in concepts if not is_defined(name)]
    return render_template("atlas.html", defined=defined, stubs=stubs)


@app.route("/atlas/<name>")
def atlas_concept(name):
    if name not in concepts:
        abort(404)
    return render_template(
        "concept.html",
        name=name,
        concept=concepts[name],
        defined=is_defined(name),
        all_concepts=concepts,
    )


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5001)
