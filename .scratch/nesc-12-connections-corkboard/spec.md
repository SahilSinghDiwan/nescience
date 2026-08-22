# NESC-12 — Connections: corkboard graph

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P2
- **Brief refs:** §9, §6
- **Depends on:** NESC-03

## Summary
The knowledge graph's public surface: a **dark corkboard** where concepts are pinned nodes and connections are threads, traversable as chains.

## Why
§9: the Connections view keeps Nescience from becoming isolated facts. Enter at one concept and traverse a chain (e.g. Rejection → Self-esteem → Attachment → Memory → Identity), threads pinned between nodes. Aim toward an interactive network over time.

## Scope / acceptance criteria
- [ ] Connections route (hub entry [003]) renders concepts as pinned cards on a dark corkboard with **threads** drawn between connected concepts (`connected_files`).
- [ ] Start at one concept and traverse: selecting a node highlights its threads and lets you walk a chain.
- [ ] Reflects the three pathways from §9 (experience→narrative, narrative→decisions, feedback loop) as the structure of the graph.
- [ ] Self-contained rendering (SVG/canvas/DOM) — no external graph libraries via CDN; if a library is used it is vendored into `static/`.
- [ ] Honors `prefers-reduced-motion`; readable and navigable without physics.

## Out of scope
- Full tactile cursor physics (NESC-15) — basic thread rendering + traversal first; polish later.

## Notes
- Incremental: a static-but-correct corkboard is acceptable first; grow toward an interactive network.
