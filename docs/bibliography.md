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

Each entry below has been checked to be a real, published paper. Every
reference added in the NESC-03 content pass was confirmed against Crossref
metadata (authors, year, title, journal, volume/issue/pages) before it was
written into a concept; the two references not indexed in Crossref in their
original form (Chalmers 1995, Nagel 1974) were confirmed against the
publishers' own records. Verify any new reference against a primary source
(journal, DOI) before it is displayed. If a claim cannot be traced to a real
paper, the Evidence Room entry reads UNKNOWN instead.

## References

| Key | Reference |
|-----|-----------|
| `barrett_2006` | Barrett, L. F (2006). Are emotions natural kinds?. *Perspectives on Psychological Science, 1(1), 28–58*. |
| `bechara_1994` | Bechara, A., Damasio, A. R., Damasio, H., & Anderson, S. W (1994). Insensitivity to future consequences following damage to human prefrontal cortex. *Cognition, 50(1–3), 7–15*. |
| `bliss_lomo_1973` | Bliss, T. V. P., & Lømo, T (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *The Journal of Physiology, 232(2), 331–356*. |
| `bonanno_2004` | Bonanno, G. A (2004). Loss, trauma, and human resilience: Have we underestimated the human capacity to thrive after extremely aversive events?. *American Psychologist, 59(1), 20–28*. |
| `boroditsky_2001` | Boroditsky, L (2001). Does language shape thought? Mandarin and English speakers' conceptions of time. *Cognitive Psychology, 43(1), 1–22*. |
| `brewin_2000` | Brewin, C. R., Andrews, B., & Valentine, J. D (2000). Meta-analysis of risk factors for posttraumatic stress disorder in trauma-exposed adults. *Journal of Consulting and Clinical Psychology, 68(5), 748–766*. |
| `broca_1861` | Broca, P (1861). Remarques sur le siège de la faculté du langage articulé, suivies d'une observation d'aphémie (perte de la parole). *Bulletin de la Société Anatomique de Paris, 330–357*. |
| `chalmers_1995` | Chalmers, D. J (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies, 2(3), 200–219*. |
| `cherry_1953` | Cherry, E. C (1953). Some experiments on the recognition of speech, with one and with two ears. *The Journal of the Acoustical Society of America, 25(5), 975–979*. |
| `corbetta_shulman_2002` | Corbetta, M., & Shulman, G. L (2002). Control of goal-directed and stimulus-driven attention in the brain. *Nature Reviews Neuroscience, 3(3), 201–215*. |
| `dehaene_changeux_2011` | Dehaene, S., & Changeux, J.-P (2011). Experimental and theoretical approaches to conscious processing. *Neuron, 70(2), 200–227*. |
| `desimone_duncan_1995` | Desimone, R., & Duncan, J (1995). Neural mechanisms of selective visual attention. *Annual Review of Neuroscience, 18, 193–222*. |
| `ekman_friesen_1971` | Ekman, P., & Friesen, W. V (1971). Constants across cultures in the face and emotion. *Journal of Personality and Social Psychology, 17(2), 124–129*. |
| `fedorenko_2011` | Fedorenko, E., Behr, M. K., & Kanwisher, N (2011). Functional specificity for high-level linguistic processing in the human brain. *Proceedings of the National Academy of Sciences, 108(39), 16428–16433*. |
| `felitti_1998` | Felitti, V. J., Anda, R. F., Nordenberg, D., Williamson, D. F., Spitz, A. M., Edwards, V., Koss, M. P., & Marks, J. S (1998). Relationship of childhood abuse and household dysfunction to many of the leading causes of death in adults: The Adverse Childhood Experiences (ACE) Study. *American Journal of Preventive Medicine, 14(4), 245–258*. |
| `friston_2010` | Friston, K (2010). The free-energy principle: A unified brain theory?. *Nature Reviews Neuroscience, 11(2), 127–138*. |
| `gazzaniga_1962` | Gazzaniga, M. S., Bogen, J. E., & Sperry, R. W (1962). Some functional effects of sectioning the cerebral commissures in man. *Proceedings of the National Academy of Sciences, 48(10), 1765–1769*. |
| `gilbertson_2002` | Gilbertson, M. W., Shenton, M. E., Ciszewski, A., Kasai, K., Lasko, N. B., Orr, S. P., & Pitman, R. K (2002). Smaller hippocampal volume predicts pathologic vulnerability to psychological trauma. *Nature Neuroscience, 5(11), 1242–1247*. |
| `hauser_2002` | Hauser, M. D., Chomsky, N., & Fitch, W. T (2002). The faculty of language: What is it, who has it, and how did it evolve?. *Science, 298(5598), 1569–1579*. |
| `hubel_wiesel_1962` | Hubel, D. H., & Wiesel, T. N (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *The Journal of Physiology, 160(1), 106–154*. |
| `johnson_newport_1989` | Johnson, J. S., & Newport, E. L (1989). Critical period effects in second language learning: The influence of maturational state on the acquisition of English as a second language. *Cognitive Psychology, 21(1), 60–99*. |
| `kahneman_tversky_1979` | Kahneman, D., & Tversky, A (1979). Prospect theory: An analysis of decision under risk. *Econometrica, 47(2), 263–291*. |
| `kelley_2002` | Kelley, W. M., Macrae, C. N., Wyland, C. L., Caglar, S., Inati, S., & Heatherton, T. F (2002). Finding the self? An event-related fMRI study. *Journal of Cognitive Neuroscience, 14(5), 785–794*. |
| `kindt_2009` | Kindt, M., Soeter, M., & Vervliet, B (2009). Beyond extinction: Erasing human fear responses and preventing the return of fear. *Nature Neuroscience, 12(3), 256–258*. |
| `knowlton_1996` | Knowlton, B. J., Mangels, J. A., & Squire, L. R (1996). A neostriatal habit learning system in humans. *Science, 273(5280), 1399–1402*. |
| `kok_2012` | Kok, P., Jehee, J. F. M., & de Lange, F. P (2012). Less is more: Expectation sharpens representations in the primary visual cortex. *Neuron, 75(2), 265–270*. |
| `lai_2001` | Lai, C. S. L., Fisher, S. E., Hurst, J. A., Vargha-Khadem, F., & Monaco, A. P (2001). A forkhead-domain gene is mutated in a severe speech and language disorder. *Nature, 413(6855), 519–523*. |
| `ledoux_2000` | LeDoux, J. E (2000). Emotion circuits in the brain. *Annual Review of Neuroscience, 23, 155–184*. |
| `libet_1983` | Libet, B., Gleason, C. A., Wright, E. W., & Pearl, D. K (1983). Time of conscious intention to act in relation to onset of cerebral activity (readiness-potential). *Brain, 106(3), 623–642*. |
| `lindquist_2012` | Lindquist, K. A., Wager, T. D., Kober, H., Bliss-Moreau, E., & Barrett, L. F (2012). The brain basis of emotion: A meta-analytic review. *Behavioral and Brain Sciences, 35(3), 121–143*. |
| `loftus_palmer_1974` | Loftus, E. F., & Palmer, J. C (1974). Reconstruction of automobile destruction: An example of the interaction between language and memory. *Journal of Verbal Learning and Verbal Behavior, 13(5), 585–589*. |
| `loftus_pickrell_1995` | Loftus, E. F., & Pickrell, J. E (1995). The formation of false memories. *Psychiatric Annals, 25(12), 720–725*. |
| `mcadams_2001` | McAdams, D. P (2001). The psychology of life stories. *Review of General Psychology, 5(2), 100–122*. |
| `mcgurk_macdonald_1976` | McGurk, H., & MacDonald, J (1976). Hearing lips and seeing voices. *Nature, 264(5588), 746–748*. |
| `nader_2000` | Nader, K., Schafe, G. E., & LeDoux, J. E (2000). Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval. *Nature, 406(6797), 722–726*. |
| `nagel_1974` | Nagel, T (1974). What is it like to be a bat?. *The Philosophical Review, 83(4), 435–450*. |
| `oregan_1999` | O'Regan, J. K., Rensink, R. A., & Clark, J. J (1999). Change-blindness as a result of 'mudsplashes'. *Nature, 398(6722), 34*. |
| `owen_2006` | Owen, A. M., Coleman, M. R., Boly, M., Davis, M. H., Laureys, S., & Pickard, J. D (2006). Detecting awareness in the vegetative state. *Science, 313(5792), 1402*. |
| `pinker_jackendoff_2005` | Pinker, S., & Jackendoff, R (2005). The faculty of language: What's special about it?. *Cognition, 95(2), 201–236*. |
| `posner_1980` | Posner, M. I (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology, 32(1), 3–25*. |
| `raichle_2001` | Raichle, M. E., MacLeod, A. M., Snyder, A. Z., Powers, W. J., Gusnard, D. A., & Shulman, G. L (2001). A default mode of brain function. *Proceedings of the National Academy of Sciences, 98(2), 676–682*. |
| `rao_ballard_1999` | Rao, R. P. N., & Ballard, D. H (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience, 2(1), 79–87*. |
| `rescorla_1988` | Rescorla, R. A (1988). Pavlovian conditioning: It's not what you think it is. *American Psychologist, 43(3), 151–160*. |
| `saffran_1996` | Saffran, J. R., Aslin, R. N., & Newport, E. L (1996). Statistical learning by 8-month-old infants. *Science, 274(5294), 1926–1928*. |
| `schachter_singer_1962` | Schachter, S., & Singer, J. E (1962). Cognitive, social, and physiological determinants of emotional state. *Psychological Review, 69(5), 379–399*. |
| `schultz_1997` | Schultz, W., Dayan, P., & Montague, P. R (1997). A neural substrate of prediction and reward. *Science, 275(5306), 1593–1599*. |
| `scoville_milner_1957` | Scoville, W. B., & Milner, B (1957). Loss of recent memory after bilateral hippocampal lesions. *Journal of Neurology, Neurosurgery & Psychiatry, 20(1), 11–21*. |
| `simons_chabris_1999` | Simons, D. J., & Chabris, C. F (1999). Gorillas in our midst: Sustained inattentional blindness for dynamic events. *Perception, 28(9), 1059–1074*. |
| `soon_2008` | Soon, C. S., Brass, M., Heinze, H.-J., & Haynes, J.-D (2008). Unconscious determinants of free decisions in the human brain. *Nature Neuroscience, 11(5), 543–545*. |
| `tononi_2004` | Tononi, G (2004). An information integration theory of consciousness. *BMC Neuroscience, 5, 42*. |
| `treisman_gelade_1980` | Treisman, A. M., & Gelade, G (1980). A feature-integration theory of attention. *Cognitive Psychology, 12(1), 97–136*. |
| `tversky_kahneman_1974` | Tversky, A., & Kahneman, D (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185(4157), 1124–1131*. |
| `winawer_2007` | Winawer, J., Witthoft, N., Frank, M. C., Wu, L., Wade, A. R., & Boroditsky, L (2007). Russian blues reveal effects of language on color discrimination. *Proceedings of the National Academy of Sciences, 104(19), 7780–7785*. |

## Concepts covered

- **001 Memory** — Scoville & Milner 1957 (H.M.); Loftus & Palmer 1974 and
  Loftus & Pickrell 1995 (false memory); Nader, Schafe & LeDoux 2000
  (reconsolidation).
- **002 Identity** — Gazzaniga, Bogen & Sperry 1962 (split brain); Kelley et
  al. 2002 (self-referential fMRI); Raichle et al. 2001 (default mode);
  McAdams 2001 (life stories); Scoville & Milner 1957.
- **003 Emotion** — Schachter & Singer 1962 (misattribution of arousal);
  Ekman & Friesen 1971 (cross-cultural expressions); Barrett 2006 and
  Lindquist et al. 2012 (constructed emotion); LeDoux 2000 (fear circuits).
- **004 Decision Making** — Tversky & Kahneman 1974 and Kahneman & Tversky
  1979 (heuristics, prospect theory); Bechara et al. 1994 (Iowa Gambling
  Task); Libet et al. 1983 and Soon et al. 2008 (timing of intention).
- **005 Attention** — Cherry 1953 (dichotic listening); Posner 1980 (spatial
  cueing); Treisman & Gelade 1980 (feature integration); Corbetta & Shulman
  2002 and Desimone & Duncan 1995 (networks, biased competition); Simons &
  Chabris 1999 (inattentional blindness).
- **006 Learning** — Bliss & Lømo 1973 (long-term potentiation); Knowlton,
  Mangels & Squire 1996 (neostriatal habit learning); Schultz, Dayan &
  Montague 1997 (prediction error); Rescorla 1988 (contingency); Scoville &
  Milner 1957.
- **007 Perception** — Hubel & Wiesel 1962 (orientation tuning); McGurk &
  MacDonald 1976 (audiovisual integration); Rao & Ballard 1999 (predictive
  coding); O'Regan, Rensink & Clark 1999 (change blindness); Simons & Chabris
  1999; Chalmers 1995.
- **008 Consciousness** — Nagel 1974 and Chalmers 1995 (the hard problem);
  Owen et al. 2006 (covert awareness); Dehaene & Changeux 2011 (global
  workspace); Tononi 2004 (integrated information).
- **010 Trauma** — Felitti et al. 1998 (ACE study); Brewin, Andrews &
  Valentine 2000 (risk factors); Bonanno 2004 (resilience); Gilbertson et al.
  2002 (twin hippocampal volume); Kindt, Soeter & Vervliet 2009 and Nader et
  al. 2000 (reconsolidation).
- **014 Prediction** — Schultz, Dayan & Montague 1997 (reward prediction
  error); Rao & Ballard 1999 (predictive coding); Kok, Jehee & de Lange 2012
  (expectation sharpening); Friston 2010 (free-energy principle).

Still stubs, no citations yet: **009 Habit**, **011 Language**, **012 Social
Cognition**, **013 Motivation**, **015 Narrative**.

_Expand this list per new concept as the investigation grows._
