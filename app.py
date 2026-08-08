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
        if name not in ("Introduction", "Participant Information")
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
    interviews = database.load_interviews()
    return render_template(
        "landing.html",
        intro=INTERVIEW_PROTOCOL["Introduction"],
        case_count=len(interviews),
        defined_count=len([c for c in concepts if is_defined(c)]),
        concept_count=len(concepts),
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
        modules=_numbered_protocol(),
    )


@app.route("/api/interview", methods=["POST"])
def api_interview():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid submission."}), 400

    record = _sanitise_interview(payload)
    database.save_interview(record)

    interviews = database.load_interviews()
    index = len(interviews) - 1
    matches = match_interview(record)

    return jsonify(
        {
            "case_number": _case_number(index),
            "case_index": index,
            "matches": matches,
            "archive_url": url_for("archive_case", index=index),
        }
    )


# ----------------------------------------------------------
# Routes — investigator: the archive
# ----------------------------------------------------------

@app.route("/archive")
def archive():
    interviews = database.load_interviews()
    cases = []
    for index, interview_record in enumerate(interviews):
        matches = match_interview(interview_record)
        cases.append(
            {
                "index": index,
                "number": _case_number(index),
                "recorded": interview_record.get("Case File", {}).get("Recorded", "—"),
                "info": interview_record.get("Participant Information", {}),
                "leads": [m["concept"] for m in matches],
            }
        )
    cases.reverse()  # newest first
    return render_template("archive.html", cases=cases)


@app.route("/archive/<int:index>")
def archive_case(index):
    interviews = database.load_interviews()
    if index < 0 or index >= len(interviews):
        abort(404)
    record = interviews[index]
    return render_template(
        "case.html",
        number=_case_number(index),
        record=record,
        info=record.get("Participant Information", {}),
        info_fields=INTERVIEW_PROTOCOL["Participant Information"],
        modules=_numbered_protocol(),
        recorded=record.get("Case File", {}).get("Recorded", "—"),
        matches=match_interview(record),
    )


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
