# Nescience — Build Brief

**Role:** You are helping build and extend *Nescience*, an interactive digital exhibit. Read this whole brief before writing code. Match the existing project's conventions; do not rebuild what already exists.

---

## 1. What Nescience is

Nescience is an interdisciplinary project about **what we do not yet understand about the human mind — and about the act of searching for those answers**. The word means *the state of not knowing*. It does not present "everything we know about neuroscience"; it asks what we don't know, why, what can be investigated, and where the evidence runs out. Where science stops, the exhibit writes **UNKNOWN** — that is the subject, not a failure. It is both scientific (evidence) and philosophical (what the evidence means), joined by the structure of an *investigation*.

## 2. Current state of the build (reuse, don't restart)

A working Flask exhibit already exists. Extend it; follow its patterns.

- `app.py` — Flask app (port 5001). Routes: `/` landing, `/interview` + `/api/interview`, `/archive` + `/archive/<index>`, `/atlas` + `/atlas/<name>`. **Add** a private, password-gated `/investigator` surface (see §11a).
- `atlas.py` — loads concepts from `knowledge.graph.py`; exposes `is_defined()`, `defined_concepts()`, `stub_concepts()`. "Defined" = has a non-empty definition; stubs are shown as mapped-but-UNKNOWN.
- `matcher.py` — `match_interview(record)` scores concepts against `interview_themes`, name, examples, connections, brain regions; returns ranked leads with the matched phrases as evidence.
- `database.py` — stores interview records + `load_interviews()`.
- Templates in `templates/`, one committed monochrome stylesheet `static/css/nescience.css`, stepper `static/js/interview.js`. **No network assets** — everything self-contained.
- Two roles from one landing page: **Participant** (takes the interview) and **Investigator** (browses archive + concept atlas).

## 3. The central question & the system

Central question: **How do life experiences shape the internal narratives people construct, and how do those narratives influence the people we become?**

Narrative is **one mechanism, not the whole project.** The real subject is a dynamic, non-linear loop:

> experience → memory / perception / emotion / learning → internal narrative → identity / beliefs / values / expectations → decisions / behavior → new experiences → (loops back).

Interpretations of the past shape future action, which creates new experiences, which can rewrite the story.

## 4. What Nescience is NOT — guardrails

- Not a crime investigation (borrow the *language* of investigation — case file, evidence, exhibit, open question, status — but never pretend to solve murders, diagnose, or interrogate).
- Not a therapy site, not a personality test, not a diagnostic tool.
- Not a scientific authority claiming the mind is solved.
- Not a pile of unrelated neuroscience facts — everything connects back to the central question.
- Not a pure philosophy essay, nor a pure lab report — hold both.
- Not an AI-generated portfolio: AI helps build; the intellectual direction, questions, interpretation, and design decisions are the human's.
- Aesthetically: not horror, not "serial-killer wall," not cyberpunk, not futuristic-AI-dashboard, not Web3.

## 5. Aesthetic & material world

Target feeling: **opening an ancient, leather-bound casebook inside a dimly lit university vault.** Something important is being investigated here, and the investigation isn't finished. Digitized history is treated as a *physical artifact*, not a web page.

- **Reference flat-lay** (`docs/refs/evidence-flatlay.jpg`): on a **near-black** surface, an aged **manila / kraft evidence folder** — coffee-stained, worn-edged — stamped with a **faded red `EVIDENCE` rubber stamp**; beside it a typewritten institutional form (`REAGENT FILE`, printed field labels: NAME · D.O.B. · PLACE OF BIRTH …) and a handwritten card (`MUGSHOT INFORMATION`) with small physical **sample wells**. Papers **overlap, layer, and sit slightly rotated**, lit like a photographed desk. Reproduce that material realism.
- **Palette:** near-black ground; manila/kraft folder tones; aged off-white forms; **ink blue-black** handwriting; **one faded evidence-red** reserved for stamps and the word **UNKNOWN**. High contrast, dim ambient lighting.
- **Surfaces:** deep, textured charcoals and aged-parchment backdrops; subtle paper grain, faint ink bleeds, weathered/coffee-stained edges — every layout has physical weight.
- **Typography:** elegant editorial **serifs** (rare-manuscript feel) paired with raw **typewriter** text for case tags and form labels, e.g. `EXHIBIT 001/A`. Printed field labels filled by hand. Institutional terminology throughout.
- **Props & marks:** stamped seals, red rubber stamps, brass paperclips, handwritten marginal notes, case/exhibit numbers, evidence cards, sample wells, thin rules.
- **Guardrail:** the mugshot/forensic props are **visual borrowings only** — the subject remains the human mind, never actual crime, suspects, or diagnosis (see §4).
- **Restraint:** richness serves the research — atmospheric, never a theme-park. Anatomical imagery, brain scans, and scientific diagrams belong here as artifacts.

## 6. Experience & interaction (tactile / analog)

The bar is **extremely interactive — never a basic static site.** Navigation is a **physical dossier interface**: sliding through case files feels like opening heavy manila folders. Concrete interactions to build toward:

- Evidence cards that **snap into place** with a soft mechanical lock.
- Witness transcripts with **redacted ink lines that dissolve on hover**.
- The Knowledge Graph / Connections view as **threads strung across a dark corkboard**.
- Handwritten marginalia that **glows faintly under the cursor**; tactile cursor physics (weight, drag, easing) rather than instant snaps.
- **Ambient analog audio**, quiet and optional: paper slides, fountain-pen scratches, soft mechanical snaps when locking an evidence card.
- Drag-and-drop parchment sheets where it deepens the "handling an artifact" feeling.

**Benchmark:** the **Morgan Library & Museum digital archives** combined with **Resn's interactive physics** — high-contrast serif typography, ambient lighting, drag-and-drop artifacts, tactile cursor physics, reading research as if solving an unsolved mystery. Use these as the bar for polish and physicality. Keep motion purposeful — physics should feel like real materials, not decoration.

## 7. Site architecture

**Landing** (feels like opening an active file): title *NESCIENCE — The Study of What We Do Not Yet Know*; a **CURRENT INVESTIGATION** block stating the central question; *Status: Evidence continues to be collected.*; **ENTER THE ARCHIVE**. Don't dump six pages of info up front.

**Archive hub** — six ways of investigating the question:

```
[001] CASE FILES · [002] WITNESS ACCOUNTS · [003] CONNECTIONS · [004] OPEN QUESTIONS · [005] EVIDENCE ROOM · [006] INVESTIGATION NOTES
```

**Witness Accounts (public)** show interview responses of consenting participants **under their code only** (e.g. `AL`), never real names, and only when the participant opted to publish (see §11a).

**A Case File** = a deep investigation into one concept (001 MEMORY is first; later IDENTITY, ATTACHMENT, DECISION, SELF…). Each contains: investigator's note · primary question · why it matters · collected evidence · neural systems · evidence room · open questions · connected files · next case.

**Evidence Room** (where aesthetic becomes real research) — four epistemic tiers, always distinguished: **what we know · what the evidence suggests · what researchers disagree about · what we don't know.** Example exhibits for Memory: Patient H.M., Elizabeth Loftus / false memory, memory reconsolidation.

**Open Questions** — format each as: *Question · What science knows · What the evidence suggests · Where the evidence disagrees · What remains unknown.* This is the philosophical heart.

## 8. The interview (Witness Accounts)

Real human experience as lived data. Participants are **participants** — not suspects, patients, or graded subjects — with consent, anonymity, ethical handling. **Nescience itself asks the questions** (no investigator/witness role-play). Opening tone:

> *"There's no right answer here. I'm interested in how you remember and make sense of things… whatever that looks like for you. Only share what you're comfortable with."*

The system records what the participant actually enters (nothing pre-filled or pre-written).

Modules: **I Experience · II The Story · III Decisions · IV The Unknown · V Reflection.** Module IV turns the participant toward what they *don't* know about themselves; Module V acknowledges the questions may have changed their thinking.

A name field is collected up front (see §11a for how it is handled). The interview **ends with a publication choice**: *"Would you like your responses displayed in the public archive?"* — Yes publishes them under an anonymized code; No keeps them for the investigation only.

## 9. The knowledge graph

The conceptual map that keeps Nescience from becoming isolated facts — every concept relates to others. Three pathways:

1. **Life experiences → internal narratives** (childhood adversity, attachment, culture, autobiographical memory, default mode network, self-schema…).
2. **Internal narratives → decisions** (self-concept, identity, values, cognitive biases, risk perception, predictive processing, somatic markers…).
3. **The feedback loop** — decisions → new experiences → narrative may change (resilience, coping, avoidance, behavioral patterns).

The **Connections** view is the graph's public surface — a **dark corkboard**: enter at one concept and traverse a chain (e.g. Rejection → Self-esteem → Attachment → Memory → Identity), threads pinned between nodes. Aim toward an interactive network over time.

## 10. The visitor's intended arc

Curiosity → Investigation → Science ("there's real neuroscience here") → Recognition ("I've felt this") → Questioning ("does science know why?") → Uncertainty ("apparently not fully") → Reflection ("what does that mean about me?").

## 11. Content & epistemic principles

Ground every philosophical question in evidence; leave unresolved questions visible. Always separate know / evidence-suggests / disagreement / unknown. Reaching UNKNOWN is the point, not a weakness.

**Real research, cited.** Every Evidence Room exhibit and factual claim must trace to a **real, verifiable paper** — author, year, journal/source — surfaced in the UI as an artifact (a reference card / footnote). No invented or unattributed studies. Concept entries carry a `citations` list; the canonical list lives in `docs/bibliography.md`. Starter references per theme are seeded (e.g. Memory: Scoville & Milner 1957 on H.M.; Loftus & Palmer 1974 and Loftus & Pickrell 1995 on false memory; Nader, Schafe & LeDoux 2000 on reconsolidation) — verify each before display and expand per new theme.

## 11a. Privacy, identity & consent (firm spec)

- **Real names are private.** The participant enters their name; it is stored owner-side only and is **never rendered on any public route**.
- **Public code = first two letters of the name, uppercased.** On collision with an existing code, append the smallest unused integer: `AL`, then `AL1`, `AL2`, … (numbering is per-code and assigned at save time from existing records; the real-name→code mapping is stored privately).
- **Publication is opt-in.** If the participant declines at the end of the interview, their responses are stored but **not shown in the public archive / Witness Accounts** — visible only to the investigator. If they accept, responses appear publicly **under the code only**, never the name.
- **Public surfaces** (`/archive`, Witness Accounts, etc.) render **published entries only, codes only**.
- **Investigator surface** (`/investigator`): a **password-gated** route (password from an environment variable, not committed) that shows everything — real names, unpublished responses, the code mapping, and the interview→concept matches. Public templates must never leak private fields.

## 12. How to proceed

- Build **incrementally**; the core already exists. Don't add features for their own sake — no 40-feature sprawl. Layer the tactile experience onto working structure, not before it.
- Reuse existing patterns and files above before adding new ones. The current CSS is a minimal starting point — this brief deliberately evolves it toward the vault/casebook direction.
- Keep assets **self-contained**: textures, fonts, and audio are bundled locally in `static/` and committed — no CDNs or external network calls. Ambient audio must be optional/muted-by-default and never autoplay loudly.
- Respect performance and accessibility: honor `prefers-reduced-motion`, keep the parchment/serif contrast readable, and don't let physics block content.
- The human owns the research direction, questions, interpretation, and design intent — surface decisions rather than inventing them.
