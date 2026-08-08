# NESCIENCE

**The study of what we do not yet know.**

Nescience is an interactive digital exhibit framed as an ongoing *investigation* into the human mind — not a museum of settled facts. The visitor is cast as an investigator: reading testimony, comparing evidence, following leads through a map of concepts, and — where the science genuinely stops — writing **UNKNOWN**.

It runs as a small [Flask](https://flask.palletsprojects.com/) web application with an archival, forensic aesthetic: monochrome ink-on-paper, case numbers, evidence cards, and typewriter typography.

---

## The idea

The exhibit is built around one question:

> **How do life experiences shape the internal narratives people construct, and how do those narratives influence the people we become?**

Narrative is only *one* mechanism. The real subject is a **dynamic feedback loop**, not a straight line of cause and effect:

```
experience → memory → perception → emotion → learning → narrative →
identity → beliefs → values → expectations → decisions → behaviour →
                        ↳ new experience ↲   (and the loop repeats)
```

Nescience treats the mind as this living system. It never claims to have solved it — it reads the evidence, looks for pattern, and is honest about the gaps.

---

## Two ways in

From the landing page, a visitor chooses a role:

### 🗣 Participant — *give testimony*
Sit for a structured interview about memory, identity, decisions, and the unknown. Questions are asked **one at a time**, investigation-style. When you "seal the file," your testimony is:
1. saved to the archive as a numbered case, and
2. **cross-checked against the concept atlas** — the exhibit reports which questions of the mind your account appears to touch.

### 🔎 Investigator — *enter the archive*
Browse every case on record, open individual case files (full transcript + the concepts each one triggered), and explore the **concept atlas** — the map of the inquiry. Some concepts have been researched; most are only *mapped*, and are shown honestly as `UNKNOWN`.

---

## How it works inside

Nescience began as a command-line prototype and now has a web layer on top of it. Here's the anatomy.

### Architecture at a glance

```
Browser ──► Flask (app.py) ──► protocol.py     (the interview script)
                │
                ├─► database.py                 (persistence → participants.json)
                │
                ├─► atlas.py ──► knowledge.graph.py   (the concept atlas)
                │
                └─► matcher.py                  (testimony ⇄ concept bridge)
```

### The concept atlas — `knowledge.graph.py` + `atlas.py`
`knowledge.graph.py` is the heart of the project: a dictionary of mind concepts (Memory, Identity, Emotion, …), each with a definition, brain regions, landmark researchers, real-world examples, open questions, what remains **unresolved**, and — crucially — a list of `interview_themes` (the words to listen for in testimony).

The filename contains a dot, so Python can't `import` it normally. **`atlas.py`** loads it by file path (via `importlib`) and re-exposes it cleanly:
- `concepts` — the full dictionary
- `is_defined(name)` — has this concept actually been researched, or is it still a template stub?
- `defined_concepts()` / `stub_concepts()` — the researched set vs. the mapped-but-unknown set

This is why the atlas can honestly separate *investigated* concepts from ones that are only *mapped*.

### The bridge — `matcher.py`
This is what connects a human's answers to the knowledge graph. `match_interview(record)`:
1. flattens every free-text answer (skipping participant demographics),
2. scans it for each concept's signals — weighted highest for `interview_themes`, then the concept name, real-world examples, and connections,
3. returns ranked **leads**, each carrying the *exact words in the testimony that triggered it*.

It's deliberately transparent — every match shows its evidence, so nothing is a black box. Matching is recomputed on demand rather than stored, so improving the matcher instantly re-scores the whole archive.

### The interview — `protocol.py` + `interview.py`
`protocol.py` defines the interview: participant fields, an introduction, and five modules of open-ended questions (Experience, The Story, Decisions, The Unknown, Reflection). On the web, the questions are rendered as a one-at-a-time stepper (`static/js/interview.js`). `interview.py` is the original CLI version of the same flow.

### Persistence — `database.py`
Interviews are stored as JSON in `participants.json`. Each saved record keeps the original structure plus a small `Case File` metadata block (timestamp). `load_interviews()` is the shared read path for both the web app and the CLI. *(The file is auto-created on first save and is git-ignored — it may contain personal testimony.)*

### Routes — `app.py`

| Route | Role | Purpose |
|---|---|---|
| `GET /` | — | Landing page: the question, the loop, two entrances |
| `GET /interview` | Participant | The one-question-at-a-time interview |
| `POST /api/interview` | Participant | Save testimony, run the matcher, return leads |
| `GET /archive` | Investigator | All cases on record (newest first) |
| `GET /archive/<index>` | Investigator | A single case file: transcript + matched concepts |
| `GET /atlas` | Investigator | The concept atlas (investigated vs. mapped) |
| `GET /atlas/<name>` | Investigator | A concept file, or an `UNKNOWN` stub |

---

## Quickstart

**Requirements:** Python 3.9+

```bash
# 1. Clone
git clone https://github.com/SahilSinghDiwan/nescience.git
cd nescience

# 2. Create a virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Run the exhibit
flask --app app run --port 5001
```

Then open **http://127.0.0.1:5001** in your browser.

> During development you can enable auto-reload with `flask --app app run --port 5001 --debug`.

---

## Project structure

```
nescience/
├── app.py                # Flask app: routes, persistence glue, matching
├── atlas.py              # Loads knowledge.graph.py + defined/stub helpers
├── matcher.py            # Bridges testimony → concepts via interview_themes
├── protocol.py           # The interview script (fields, intro, 5 modules)
├── database.py           # JSON persistence (save/load interviews)
├── knowledge.graph.py    # The concept atlas (the knowledge graph itself)
├── interview.py          # Original CLI interview flow
├── main.py               # Original CLI entry point (menu)
├── requirements.txt
├── templates/            # Jinja2: landing, interview, archive, case, atlas, concept, 404
└── static/
    ├── css/nescience.css # The monochrome / forensic aesthetic
    └── js/interview.js   # The one-question-at-a-time stepper
```

---

## Extending it

**Investigate a new concept:** open `knowledge.graph.py` and fill in one of the empty template stubs (e.g. `Decision Making`, `Attention`, `Trauma`). Give it a `definition` — that alone promotes it from *mapped* to *investigated* — and populate `interview_themes` so it starts catching relevant testimony. No other file needs to change; the atlas, matcher, and pages pick it up automatically.

**Change the interview:** edit `protocol.py`. Add or reword questions inside the modules; the web stepper and CLI both regenerate from it. Question numbering is global and stays in sync across client and server.

**Tune the matching:** adjust the weights in `matcher.py`'s `_signals_for()` to change how strongly each field (themes, name, examples, connections) pulls a concept into the leads.

---

## The original CLI

The terminal prototype still works and shares the same data file:

```bash
python3 main.py
```

It offers the same interview and an archive viewer, printed in plain text.

---

## Tech stack

- **Python 3.9+** and **Flask** (server + Jinja2 templates)
- **Vanilla JavaScript** for the interview stepper (no build step, no framework)
- **Plain CSS**, system fonts only — fully self-contained, no external/network assets
- **JSON** file storage — zero-setup, no database to provision

---

## Data & privacy

Interview responses can contain personal, sensitive testimony. They're stored locally in `participants.json`, which is **git-ignored by default** so it is never committed. If you deploy this, treat that file as confidential and secure it accordingly.

---

## Roadmap

- Fill in the remaining stub concepts (12 of 15 are still `UNKNOWN`).
- A visual node-and-connection **map** of the mind's feedback loop (the atlas is currently a list/grid).
- Richer anatomical imagery and brain-scan visuals to deepen the archive aesthetic.
- Optional export of a case file as a printable "dossier."

---

*Nescience — we are not pretending to have the answer. We are looking.*
