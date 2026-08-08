# Bibliography

The canonical reference list for Nescience. Every Evidence Room exhibit and
every factual claim must trace to an entry here (brief §11) — **no invented or
unattributed studies**.

The machine-readable source of truth is each concept's `citations` list in
`knowledge.graph.py`; `bibliography.py` aggregates those into a keyed registry
and this file mirrors them for humans. When you add a citation to a concept,
add it here too (same key). `bibliography.unresolved_citation_keys()` fails
loudly if an Evidence Room / Open Question references a key with no reference.

## Verification

Each entry below has been checked to be a real, published paper. Verify any
new reference against a primary source (journal, DOI) before it is displayed.

## References

| Key | Reference |
|-----|-----------|
| `scoville_milner_1957` | Scoville, W. B., & Milner, B. (1957). Loss of recent memory after bilateral hippocampal lesions. *Journal of Neurology, Neurosurgery & Psychiatry, 20*(1), 11–21. |
| `loftus_palmer_1974` | Loftus, E. F., & Palmer, J. C. (1974). Reconstruction of automobile destruction: An example of the interaction between language and memory. *Journal of Verbal Learning and Verbal Behavior, 13*(5), 585–589. |
| `loftus_pickrell_1995` | Loftus, E. F., & Pickrell, J. E. (1995). The formation of false memories. *Psychiatric Annals, 25*(12), 720–725. |
| `nader_2000` | Nader, K., Schafe, G. E., & LeDoux, J. E. (2000). Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval. *Nature, 406*(6797), 722–726. |

## Concepts covered

- **001 Memory** — Scoville & Milner 1957 (H.M.); Loftus & Palmer 1974 and
  Loftus & Pickrell 1995 (false memory); Nader, Schafe & LeDoux 2000
  (reconsolidation).

_Expand this list per new concept as the investigation grows._
