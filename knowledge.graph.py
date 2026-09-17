# ==========================================================
# NESCIENCE
# Atlas Core v1.0
#
# The central knowledge architecture of Nescience.
# Every concept in the project connects to this file.
# ==========================================================


concepts = {

    "Memory": {

        "definition":
        "The ability to encode, store, and retrieve information over time.",

        "narrative_role":
        "Memories provide the raw material from which people construct the stories they tell about themselves.",

        "paradox":
        "Every time you remember something, you slightly rewrite it.",

        "brain_regions": [
            "Hippocampus",
            "Prefrontal Cortex",
            "Amygdala"
        ],

        "evidence": [
    {
        "type": "Patient Study",
        "title": "Patient H.M.",
        "year": 1953
    },
    {
        "type": "Behavioral Experiment",
        "title": "False Memory Studies"
    },
    {
        "type": "Neuroimaging",
        "title": "fMRI Encoding Studies"
    }
]
        ,

        "landmark_researchers": [
            "Brenda Milner",
            "Elizabeth Loftus"
        ],

        "connects_to": [
            "Identity",
            "Emotion",
            "Learning",
            "Trauma"
        ],

        "real_world_examples": [
            "Flashbulb memories",
            "PTSD",
            "Childhood amnesia"
        ],

        "questions": [
            "Why do memories change over time?",
            "Can memories be completely false?",
            "Why are emotional memories remembered more vividly?"
        ],

        "unresolved":
        "Is forgetting mainly a failure of storage or retrieval?",

        "interview_themes": [
            "Childhood",
            "Loss",
            "Family",
            "Nostalgia"
        ],

        # ---- Case File anatomy (NESC-03 schema expansion) --------------
        # See docs/concept-schema.md for the full field contract. Every
        # field below is ADDITIVE; the keys above remain the source of
        # truth for atlas.is_defined() and matcher.interview_themes.

        "key_experiments": [
            "Patient H.M. lesion studies",
            "Eyewitness misinformation experiments",
            "Fear-memory reconsolidation experiments"
        ],

        "investigators_note":
        "Memory is the first file opened in this investigation because every "
        "other case leans on it. The witness on the table is a moving target: "
        "the act of recalling a memory can quietly edit it, so a testimony is "
        "not a recording but the latest draft. Treat every recollection here "
        "as evidence about the rememberer, not proof of the remembered event.",

        "primary_question":
        "If remembering rewrites the memory, can we ever recover the past — "
        "or only reconstruct it?",

        "why_it_matters":
        "Memory underwrites identity, testimony, grief, and learning. Courts "
        "convict on it, relationships are built on it, and the self is stitched "
        "together from it — yet it is demonstrably editable. Understanding how "
        "far it can be trusted is the hinge the rest of the exhibit turns on.",

        # Richer companion to brain_regions (which is kept intact above).
        "neural_systems": [
            {
                "system": "Hippocampus & medial temporal lobe",
                "role":
                "Binds and consolidates new declarative (episodic/semantic) "
                "memories; its bilateral loss produces dense anterograde amnesia."
            },
            {
                "system": "Prefrontal cortex",
                "role":
                "Organises encoding and strategic retrieval, and supports the "
                "source-monitoring that keeps real and imagined events apart."
            },
            {
                "system": "Amygdala",
                "role":
                "Modulates the emotional salience of memories and gates the "
                "reconsolidation of fear memories after they are retrieved."
            }
        ],

        # Evidence Room — entries grouped into the four epistemic tiers
        # (NESC-09). Each entry carries a claim/summary and a `citation`
        # key that resolves against this concept's `citations` list.
        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "The hippocampus and adjacent medial temporal lobe are "
                    "required to form new long-term declarative memories. After "
                    "bilateral removal of these structures, patient H.M. could "
                    "no longer lay down new conscious memories (dense anterograde "
                    "amnesia) yet retained older memories and could still learn "
                    "new motor skills — showing declarative and procedural "
                    "memory are separable systems.",
                    "citation": "scoville_milner_1957"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Memory is reconstructive rather than a faithful recording. "
                    "Changing a single word in a question about a filmed car "
                    "crash ('smashed' vs. 'hit') significantly raised witnesses' "
                    "reported speeds and made them 'remember' broken glass that "
                    "was never there — suggesting post-event information is "
                    "folded into the memory itself.",
                    "citation": "loftus_palmer_1974"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Whole autobiographical events that never happened can be "
                    "implanted through suggestion — roughly a quarter of "
                    "participants came to 'remember' being lost in a shopping "
                    "mall as a child. Researchers still disagree over how far "
                    "this generalises to emotionally charged real-world memories "
                    "and how to tell an implanted memory from a true one.",
                    "citation": "loftus_pickrell_1995"
                },
                {
                    "claim":
                    "Reconsolidation theory holds that retrieving a consolidated "
                    "memory returns it to a labile state that must be re-stored, "
                    "so an already-stable memory can be disrupted after recall. "
                    "Whether this reflects genuine erasure/editing of the trace "
                    "or a temporary retrieval failure remains actively contested.",
                    "citation": "nader_2000"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "It is still unknown whether everyday forgetting is mainly "
                    "the decay or loss of the stored trace, or a failure to "
                    "retrieve a trace that is still physically present.",
                    "citation": "scoville_milner_1957"
                },
                {
                    "claim":
                    "The physical substrate of a single memory — how a specific "
                    "engram is written, stabilised, and re-stored across cells "
                    "and synapses — is not fully understood.",
                    "citation": "nader_2000"
                }
            ]
        },

        # Structured open questions (NESC-10). Each question is examined
        # through the same four epistemic lenses as the Evidence Room.
        "open_questions": [
            {
                "question":
                "Is forgetting a failure of storage or of retrieval?",
                "what_science_knows":
                "Amnesic patients such as H.M. show that damage to specific "
                "structures abolishes the ability to form or access memories, "
                "so both encoding and retrieval have identifiable neural bases.",
                "what_evidence_suggests":
                "Cues, context, and priming can revive 'forgotten' material, "
                "suggesting much of what seems lost is intact but temporarily "
                "inaccessible.",
                "where_evidence_disagrees":
                "Researchers disagree on the balance between true trace decay "
                "and retrieval failure, and whether the two can be cleanly "
                "separated at all.",
                "what_remains_unknown":
                "There is no reliable way to tell, for a given lost memory, "
                "whether the trace is gone or merely unreachable."
            },
            {
                "question":
                "Once a memory is formed, is it fixed?",
                "what_science_knows":
                "Consolidation stabilises new memories over hours to years, and "
                "the hippocampus is central to this process early on.",
                "what_evidence_suggests":
                "Retrieval can reopen a memory: fear memories in animals became "
                "vulnerable to disruption specifically after being recalled, "
                "implying stored memories are periodically rewritten.",
                "where_evidence_disagrees":
                "Whether reconsolidation edits the original trace or creates a "
                "competing new one — and how far animal findings apply to human "
                "autobiographical memory — is unresolved.",
                "what_remains_unknown":
                "It is unknown whether any memory can ever be recalled without "
                "being altered in the act of recalling it."
            }
        ],

        # Connections for the corkboard graph (NESC-12). Mirrors
        # connects_to; kept separate so the two can diverge later.
        "connected_files": [
            "Identity",
            "Emotion",
            "Learning",
            "Trauma"
        ],

        # Pointer to the next case in the numbered sequence (001 → 002).
        "next_case": "Identity",

        # Real, verifiable references. Keys are used by evidence_room and
        # open_questions above and mirror docs/bibliography.md (NESC-04).
        "citations": [
            {
                "key": "scoville_milner_1957",
                "author": "Scoville, W. B., & Milner, B.",
                "year": 1957,
                "title":
                "Loss of recent memory after bilateral hippocampal lesions",
                "source":
                "Journal of Neurology, Neurosurgery & Psychiatry, 20(1), 11–21"
            },
            {
                "key": "loftus_palmer_1974",
                "author": "Loftus, E. F., & Palmer, J. C.",
                "year": 1974,
                "title":
                "Reconstruction of automobile destruction: An example of the "
                "interaction between language and memory",
                "source":
                "Journal of Verbal Learning and Verbal Behavior, 13(5), 585–589"
            },
            {
                "key": "loftus_pickrell_1995",
                "author": "Loftus, E. F., & Pickrell, J. E.",
                "year": 1995,
                "title": "The formation of false memories",
                "source": "Psychiatric Annals, 25(12), 720–725"
            },
            {
                "key": "nader_2000",
                "author": "Nader, K., Schafe, G. E., & LeDoux, J. E.",
                "year": 2000,
                "title":
                "Fear memories require protein synthesis in the amygdala for "
                "reconsolidation after retrieval",
                "source": "Nature, 406(6797), 722–726"
            }
        ]
    },



    "Identity": {

        "definition":
        "A person's understanding of who they are across time.",

        "narrative_role":
        "Identity is the evolving story a person creates to explain themselves.",

        "paradox":
        "You constantly change, yet experience yourself as the same person.",

        "brain_regions": [
            "Medial Prefrontal Cortex",
            "Default Mode Network"
        ],

        "key_experiments": [
            "Self-referential Processing Studies",
            "Default Mode Network Research"
        ],

        "landmark_researchers": [
            "Dan McAdams",
            "Michael Gazzaniga"
        ],

        "connects_to": [
            "Memory",
            "Narrative",
            "Emotion",
            "Language"
        ],

        "real_world_examples": [
            "Identity crisis",
            "Migration",
            "Major life transitions"
        ],

        "questions": [
            "Who am I beyond my roles?",
            "Can identity completely change?",
            "How much of identity comes from memory?"
        ],

        "unresolved":
        "Is there a true self, or is identity continuously constructed?",

        "interview_themes": [
            "Purpose",
            "Belonging",
            "Self-image",
            "Change"
        ],

        "evidence": [
            {"type": "Patient Study", "title": "Split-brain commissurotomy patients", "year": 1962},
            {"type": "Neuroimaging", "title": "Self-referential encoding (fMRI)", "year": 2002},
            {"type": "Neuroimaging", "title": "Default mode network baseline", "year": 2001},
            {"type": "Narrative Psychology", "title": "Life-story interviews", "year": 2001}
        ],

        "investigators_note":
        "The second file is the one the witness thinks they are certain about. "
        "Everyone can name who they are; almost nobody can say where that "
        "answer is kept. What the evidence keeps returning is not a location "
        "but an activity — a brain narrating itself, in real time, with "
        "whatever material is to hand. When the material is cut in half, the "
        "narration does not stop. It simply invents.",

        "primary_question":
        "Is there a self underneath the story, or is the story all there is?",

        "why_it_matters":
        "Every claim a person makes about themselves — their values, their "
        "consistency, their responsibility for what they did ten years ago — "
        "rests on the assumption of a continuous self. Law, medicine, and "
        "grief all assume it. If that continuity is authored rather than "
        "found, the whole architecture of self-knowledge sits on a draft.",

        "neural_systems": [
            {
                "system": "Medial prefrontal cortex",
                "role":
                "Preferentially engaged when judgements are made about oneself "
                "rather than about another person or about a word's surface "
                "properties — the closest thing to a 'self-reference' signal."
            },
            {
                "system": "Default mode network",
                "role":
                "A set of midline and parietal regions more active at rest "
                "than during outward-directed tasks; associated with "
                "self-directed, autobiographical, and mind-wandering thought."
            },
            {
                "system": "Left-hemisphere interpretive systems",
                "role":
                "In split-brain patients, the speaking hemisphere generates "
                "plausible explanations for actions it did not initiate — "
                "evidence that self-explanation is generated, not read off."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Severing the corpus callosum leaves two hemispheres that "
                    "can be tested separately, and each can process "
                    "information the other has no access to. The classic "
                    "commissurotomy series showed that a stimulus presented to "
                    "one hemisphere could guide behaviour while the speaking "
                    "hemisphere reported no knowledge of it — a single body "
                    "with divided information.",
                    "citation": "gazzaniga_1962"
                },
                {
                    "claim":
                    "Judging whether an adjective describes yourself recruits "
                    "medial prefrontal cortex more than judging whether it "
                    "describes another person, and more than judging the "
                    "word's case. Self-reference is a distinguishable "
                    "processing mode, not a vague notion.",
                    "citation": "kelley_2002"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "The brain has a costly baseline: a specific set of "
                    "midline regions is *more* active when a person is doing "
                    "nothing in particular than during many demanding tasks. "
                    "This 'default mode' is widely, though not conclusively, "
                    "read as the machinery of self-directed and "
                    "autobiographical thought idling.",
                    "citation": "raichle_2001"
                },
                {
                    "claim":
                    "People do not merely have traits; they carry an "
                    "internalised, evolving life story that integrates past "
                    "and imagined future into a sense of unity and purpose. "
                    "On this account identity is authored — and the authoring "
                    "is measurable in how people narrate their lives.",
                    "citation": "mcadams_2001"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Whether the self is a real psychological entity or a "
                    "narrative artefact remains contested. Split-brain "
                    "findings are read by some as evidence that the unified "
                    "self is a story the left hemisphere tells after the fact; "
                    "others argue the patients' everyday behaviour stays "
                    "strikingly integrated and that laboratory dissociations "
                    "overstate the fracture.",
                    "citation": "gazzaniga_1962"
                },
                {
                    "claim":
                    "The default mode network's function is disputed. It is "
                    "variously interpreted as self-referential processing, "
                    "generic internally-directed cognition, or a physiological "
                    "baseline with no special relationship to selfhood at all.",
                    "citation": "raichle_2001"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "There is no measurement that distinguishes a person who "
                    "'has' a continuous self from a person who merely "
                    "constructs a convincing account of one. The question may "
                    "not currently be empirically decidable.",
                    "citation": "mcadams_2001"
                },
                {
                    "claim":
                    "How much of identity is memory is unknown. Amnesia shows "
                    "that people who cannot form new autobiographical memories "
                    "still behave as continuous persons with stable "
                    "dispositions — but why the sense of self survives the "
                    "loss of its record has no accepted explanation.",
                    "citation": "scoville_milner_1957"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Is there a true self, or is identity continuously constructed?",
                "what_science_knows":
                "Thinking about oneself is a distinguishable neural process: "
                "self-referential judgements reliably engage medial "
                "prefrontal cortex more than other-referential ones.",
                "what_evidence_suggests":
                "Identity behaves like an ongoing act of authorship — people "
                "carry internalised life stories that they revise, and the "
                "brain sustains a costly resting baseline associated with "
                "that inward narration.",
                "where_evidence_disagrees":
                "Split-brain work is read either as exposing the unified self "
                "as a post-hoc confabulation or as a laboratory artefact that "
                "everyday integrated behaviour contradicts.",
                "what_remains_unknown":
                "No experiment can currently separate having a self from "
                "convincingly narrating one."
            },
            {
                "question":
                "How much of identity comes from memory?",
                "what_science_knows":
                "Autobiographical memory supplies the raw material for the "
                "life story, and damage to medial temporal structures removes "
                "the ability to add to that record.",
                "what_evidence_suggests":
                "Personality and sense of self can persist through dense "
                "amnesia, suggesting identity is not simply the sum of "
                "retrievable episodes.",
                "where_evidence_disagrees":
                "Researchers disagree whether the persisting self is carried "
                "by semantic self-knowledge, by habit and disposition, or by "
                "something not reducible to memory at all.",
                "what_remains_unknown":
                "What, if anything, would remain of a person if every "
                "autobiographical memory were removed is unknown."
            }
        ],

        "connected_files": [
            "Memory",
            "Narrative",
            "Emotion",
            "Language"
        ],

        "next_case": "Emotion",

        "citations": [
            {
                "key": "gazzaniga_1962",
                "author": "Gazzaniga, M. S., Bogen, J. E., & Sperry, R. W.",
                "year": 1962,
                "title":
                "Some functional effects of sectioning the cerebral "
                "commissures in man",
                "source":
                "Proceedings of the National Academy of Sciences, 48(10), "
                "1765–1769"
            },
            {
                "key": "kelley_2002",
                "author":
                "Kelley, W. M., Macrae, C. N., Wyland, C. L., Caglar, S., "
                "Inati, S., & Heatherton, T. F.",
                "year": 2002,
                "title": "Finding the self? An event-related fMRI study",
                "source":
                "Journal of Cognitive Neuroscience, 14(5), 785–794"
            },
            {
                "key": "raichle_2001",
                "author":
                "Raichle, M. E., MacLeod, A. M., Snyder, A. Z., Powers, "
                "W. J., Gusnard, D. A., & Shulman, G. L.",
                "year": 2001,
                "title": "A default mode of brain function",
                "source":
                "Proceedings of the National Academy of Sciences, 98(2), "
                "676–682"
            },
            {
                "key": "mcadams_2001",
                "author": "McAdams, D. P.",
                "year": 2001,
                "title": "The psychology of life stories",
                "source": "Review of General Psychology, 5(2), 100–122"
            },
            {
                "key": "scoville_milner_1957",
                "author": "Scoville, W. B., & Milner, B.",
                "year": 1957,
                "title":
                "Loss of recent memory after bilateral hippocampal lesions",
                "source":
                "Journal of Neurology, Neurosurgery & Psychiatry, 20(1), 11–21"
            }
        ]
    },



    "Emotion": {

        "definition":
        "Mental and physiological responses that help us interpret and react to the world.",

        "narrative_role":
        "Emotion influences which experiences become meaningful enough to shape our personal stories.",

        "paradox":
        "Emotions feel automatic, yet they are influenced by interpretation and context.",

        "brain_regions": [
            "Amygdala",
            "Insula",
            "Anterior Cingulate Cortex"
        ],

        "key_experiments": [
            "Schachter-Singer Experiment",
            "Constructed Emotion Research"
        ],

        "landmark_researchers": [
            "Lisa Feldman Barrett",
            "Joseph LeDoux"
        ],

        "connects_to": [
            "Memory",
            "Decision Making",
            "Identity",
            "Attention"
        ],

        "real_world_examples": [
            "Fear",
            "Grief",
            "Joy",
            "Anxiety"
        ],

        "questions": [
            "Why do emotions sometimes override logic?",
            "Can emotions be learned?",
            "How does emotion shape memory?"
        ],

        "unresolved":
        "Are emotions universal biological states or constructed by the brain?",

        "interview_themes": [
            "Stress",
            "Love",
            "Fear",
            "Regret"
        ],

        "evidence": [
            {"type": "Behavioural Experiment", "title": "Adrenaline & misattribution of arousal", "year": 1962},
            {"type": "Cross-cultural Study", "title": "Facial expression recognition", "year": 1971},
            {"type": "Meta-analysis", "title": "Neuroimaging meta-analysis of emotion categories", "year": 2012},
            {"type": "Animal Study", "title": "Amygdala fear-conditioning circuits", "year": 2000}
        ],

        "investigators_note":
        "This is the file where the investigation stops being tidy. Emotion "
        "feels like the most direct evidence a person has — nobody doubts "
        "their own fear. Yet a century of experiments keeps finding the same "
        "thing: the body's signal is ambiguous, and the label is supplied "
        "afterwards. The witness is certain; the certainty is the part that "
        "needs explaining.",

        "primary_question":
        "Is an emotion something the body does, or something the brain names?",

        "why_it_matters":
        "Diagnosis, therapy, jury instructions, emotion-recognition software, "
        "and every claim that a feeling was 'read' off a face depend on "
        "emotions being discrete, recognisable states. If they are instead "
        "constructed in the moment from general arousal plus context, a very "
        "large amount of practice is built on a category error.",

        "neural_systems": [
            {
                "system": "Amygdala",
                "role":
                "Central to rapid threat learning and defensive responding; "
                "necessary for classical fear conditioning in animals, though "
                "it is not the seat of the feeling of fear."
            },
            {
                "system": "Insula",
                "role":
                "Maps interoceptive signals from the body — heart rate, gut, "
                "breath — that supply the raw arousal an emotion is built on."
            },
            {
                "system": "Anterior cingulate cortex",
                "role":
                "Involved in appraising affective significance and regulating "
                "conflict between bodily state and situational demand."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Defensive responding to threat runs on a traceable "
                    "circuit. Decades of animal fear-conditioning work map how "
                    "a neutral cue paired with shock comes to trigger "
                    "freezing, autonomic change, and hormonal release through "
                    "amygdala pathways — a mechanism that is well replicated "
                    "and conserved across species.",
                    "citation": "ledoux_2000"
                },
                {
                    "claim":
                    "The same physiological arousal can become different "
                    "emotions depending on context. Participants injected with "
                    "adrenaline without being told what to expect reported "
                    "euphoria or anger according to how a confederate in the "
                    "room behaved — arousal supplied the intensity, the "
                    "situation supplied the emotion.",
                    "citation": "schachter_singer_1962"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Some facial expressions are recognised at above-chance "
                    "rates across very different cultures, including in a "
                    "visually isolated preliterate group — evidence often read "
                    "as showing a small set of biologically basic emotions "
                    "with universal signals.",
                    "citation": "ekman_friesen_1971"
                },
                {
                    "claim":
                    "Emotions may be constructed: general-purpose systems for "
                    "affect, conceptual knowledge, and language may combine to "
                    "produce an experience the person then categorises as "
                    "'anger' or 'fear', rather than each emotion having its "
                    "own dedicated mechanism.",
                    "citation": "barrett_2006"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "A large meta-analysis of neuroimaging studies found that "
                    "discrete emotion categories are not consistently and "
                    "specifically localised to individual brain regions — no "
                    "clean 'fear spot', no 'disgust spot'. Basic-emotion "
                    "theorists dispute the inference, arguing that "
                    "distributed circuits can still be category-specific.",
                    "citation": "lindquist_2012"
                },
                {
                    "claim":
                    "Whether cross-cultural recognition of facial expressions "
                    "demonstrates universal emotions or reflects the forced-"
                    "choice methods, translation, and shared exposure used to "
                    "test it is one of the longest-running disputes in the "
                    "field.",
                    "citation": "ekman_friesen_1971"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "It is unknown how a bodily state becomes a felt "
                    "experience. The mechanisms of threat detection are well "
                    "mapped; why any of it feels like anything is not "
                    "explained by that mapping.",
                    "citation": "ledoux_2000"
                },
                {
                    "claim":
                    "There is no agreed way to determine whether two people "
                    "using the same emotion word are referring to the same "
                    "internal state, or whether emotion categories cut nature "
                    "at any joint at all.",
                    "citation": "barrett_2006"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Are emotions universal biological states or constructed by "
                "the brain?",
                "what_science_knows":
                "Threat-response circuitry is real, conserved, and "
                "well-characterised; bodily arousal is measurable and "
                "reliably accompanies strong emotion.",
                "what_evidence_suggests":
                "Arousal on its own is ambiguous — context and interpretation "
                "determine which emotion is reported — while cross-cultural "
                "recognition of some expressions suggests at least a partly "
                "biological signalling system.",
                "where_evidence_disagrees":
                "Neuroimaging meta-analyses find no region-specific signature "
                "for discrete emotions, which constructionists read as "
                "decisive and basic-emotion theorists read as a limitation of "
                "the method.",
                "what_remains_unknown":
                "Whether emotion categories name real natural kinds, or are "
                "conventions a culture teaches, is unresolved."
            },
            {
                "question":
                "Why do emotions sometimes override reasoning?",
                "what_science_knows":
                "Emotional arousal changes attention, memory encoding, and "
                "decision thresholds in measurable ways.",
                "what_evidence_suggests":
                "Affective signals appear to act as fast appraisals that reach "
                "behaviour before deliberate evaluation completes.",
                "where_evidence_disagrees":
                "Whether this is 'emotion beating reason' or simply one "
                "valuation system with an affective component is disputed; "
                "the two-systems framing is itself contested.",
                "what_remains_unknown":
                "It is unknown what determines, in a given moment, whether an "
                "affective signal is acted on or overridden."
            }
        ],

        "connected_files": [
            "Memory",
            "Decision Making",
            "Identity",
            "Attention"
        ],

        "next_case": "Decision Making",

        "citations": [
            {
                "key": "schachter_singer_1962",
                "author": "Schachter, S., & Singer, J. E.",
                "year": 1962,
                "title":
                "Cognitive, social, and physiological determinants of "
                "emotional state",
                "source": "Psychological Review, 69(5), 379–399"
            },
            {
                "key": "ekman_friesen_1971",
                "author": "Ekman, P., & Friesen, W. V.",
                "year": 1971,
                "title": "Constants across cultures in the face and emotion",
                "source":
                "Journal of Personality and Social Psychology, 17(2), 124–129"
            },
            {
                "key": "barrett_2006",
                "author": "Barrett, L. F.",
                "year": 2006,
                "title": "Are emotions natural kinds?",
                "source":
                "Perspectives on Psychological Science, 1(1), 28–58"
            },
            {
                "key": "lindquist_2012",
                "author":
                "Lindquist, K. A., Wager, T. D., Kober, H., Bliss-Moreau, E., "
                "& Barrett, L. F.",
                "year": 2012,
                "title": "The brain basis of emotion: A meta-analytic review",
                "source":
                "Behavioral and Brain Sciences, 35(3), 121–143"
            },
            {
                "key": "ledoux_2000",
                "author": "LeDoux, J. E.",
                "year": 2000,
                "title": "Emotion circuits in the brain",
                "source": "Annual Review of Neuroscience, 23, 155–184"
            }
        ]
    },



    # ==================================================
    # Templates for future concepts
    # ==================================================

    "Decision Making": {

        "definition":
        "The process of committing to one option when several were available.",

        "narrative_role":
        "Decisions are the hinges of a life story — the points a person "
        "returns to when explaining how they ended up here.",

        "paradox":
        "Choices feel deliberate and reasoned, yet they can be predicted from "
        "brain activity before the chooser feels they have decided.",

        "brain_regions": [
            "Ventromedial Prefrontal Cortex",
            "Orbitofrontal Cortex",
            "Anterior Cingulate Cortex",
            "Supplementary Motor Area"
        ],

        "key_experiments": [
            "Heuristics and biases judgement studies",
            "Prospect theory gambles",
            "The Iowa Gambling Task",
            "Libet readiness-potential timing",
            "fMRI prediction of free choices"
        ],

        "landmark_researchers": [
            "Daniel Kahneman",
            "Amos Tversky",
            "Antoine Bechara",
            "Benjamin Libet",
            "John-Dylan Haynes"
        ],

        "connects_to": [
            "Emotion",
            "Prediction",
            "Motivation",
            "Identity"
        ],

        "real_world_examples": [
            "Choosing a career",
            "Impulse purchases",
            "Medical consent",
            "Jury verdicts"
        ],

        "questions": [
            "Do I decide, or do I discover what I have decided?",
            "Why do I make worse choices when I am tired or afraid?",
            "How much of a choice is made before I notice it?"
        ],

        "unresolved":
        "Does conscious intention cause an action, or report one already "
        "underway?",

        "interview_themes": [
            "Choices",
            "Regret",
            "Risk",
            "Turning points"
        ],

        "evidence": [
            {"type": "Behavioural Experiment", "title": "Heuristics and biases", "year": 1974},
            {"type": "Formal Model", "title": "Prospect theory", "year": 1979},
            {"type": "Patient Study", "title": "Ventromedial prefrontal damage", "year": 1994},
            {"type": "Electrophysiology", "title": "Readiness potential and reported intention", "year": 1983},
            {"type": "Neuroimaging", "title": "Pre-conscious decoding of choice", "year": 2008}
        ],

        "investigators_note":
        "Every witness in this investigation believes they are the author of "
        "their choices. That belief is the evidence, not the finding. What "
        "the file contains instead is a set of results showing that the "
        "reasons people give are reliably not the reasons that operated — and "
        "a much more contested set suggesting the decision was already "
        "detectable before it was felt. Read the second group carefully; the "
        "headlines have outrun the data.",

        "primary_question":
        "Is the feeling of deciding the cause of the action or the report of "
        "it?",

        "why_it_matters":
        "Responsibility, consent, contract, and punishment all assume a "
        "deliberating agent who could have done otherwise. Whatever the "
        "neuroscience eventually shows, the demonstrated gap between the "
        "reasons people give and the processes that moved them is already "
        "enough to unsettle how we judge each other.",

        "neural_systems": [
            {
                "system": "Ventromedial prefrontal cortex",
                "role":
                "Integrates affective value into choice; damage leaves "
                "intelligence and reasoning intact while devastating "
                "real-world decision-making."
            },
            {
                "system": "Orbitofrontal cortex",
                "role":
                "Represents the subjective value of options on a common scale, "
                "allowing unlike things to be compared."
            },
            {
                "system": "Supplementary motor area",
                "role":
                "Source of the readiness potential — the slow build-up of "
                "activity that precedes a self-initiated movement."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Human judgement under uncertainty runs on heuristics that "
                    "produce systematic, predictable errors — representativeness, "
                    "availability, and anchoring — rather than on statistical "
                    "reasoning. These biases are robust and replicate across "
                    "populations and expertise levels.",
                    "citation": "tversky_kahneman_1974"
                },
                {
                    "claim":
                    "Choices depend on how outcomes are framed relative to a "
                    "reference point, not on final states of wealth: losses "
                    "loom larger than equivalent gains, and the same gamble "
                    "described two ways yields opposite preferences.",
                    "citation": "kahneman_tversky_1979"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Emotion is not the opposite of good decision-making but "
                    "part of its machinery. Patients with ventromedial "
                    "prefrontal damage retain intellect and memory yet choose "
                    "disastrously in a card task, persisting with "
                    "high-immediate-reward, high-penalty decks that healthy "
                    "participants learn to avoid.",
                    "citation": "bechara_1994"
                },
                {
                    "claim":
                    "Brain activity preceding a voluntary movement begins "
                    "before the moment participants report the urge to move — "
                    "a readiness potential measurable several hundred "
                    "milliseconds before the reported intention.",
                    "citation": "libet_1983"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Patterns in prefrontal and parietal cortex allowed a "
                    "simple left/right choice to be decoded above chance "
                    "several seconds before participants reported deciding. "
                    "Whether this shows the decision was already made, or "
                    "merely that a bias was accumulating, is heavily disputed "
                    "— decoding accuracy was modest and the choice was "
                    "arbitrary.",
                    "citation": "soon_2008"
                },
                {
                    "claim":
                    "Interpretation of the readiness potential is contested. "
                    "Critics argue it reflects ongoing spontaneous fluctuation "
                    "rather than a specific decision, and that the timing of a "
                    "subjectively reported 'urge' is not a reliable "
                    "measurement in the first place.",
                    "citation": "libet_1983"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "How the brain settles on one option is unknown for any "
                    "real decision of consequence. The laboratory tasks that "
                    "can be measured — arbitrary button presses, small gambles "
                    "— may not scale to choosing a career or a partner.",
                    "citation": "soon_2008"
                },
                {
                    "claim":
                    "Whether conscious deliberation ever changes an outcome, "
                    "or only annotates it, has no experimental answer. UNKNOWN.",
                    "citation": "libet_1983"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Does conscious intention cause an action or report one "
                "already underway?",
                "what_science_knows":
                "Preparatory brain activity reliably precedes self-initiated "
                "movements, and its onset can be measured.",
                "what_evidence_suggests":
                "Simple binary choices can be partially decoded from brain "
                "activity before the chooser reports having decided.",
                "where_evidence_disagrees":
                "Whether the early signal is a decision, a bias, or "
                "spontaneous noise is unresolved, as is whether reported "
                "timing of an intention can be trusted at all.",
                "what_remains_unknown":
                "Nothing in this literature bears directly on consequential "
                "real-world choices; that case is untested."
            },
            {
                "question":
                "Why do reasoned choices go so predictably wrong?",
                "what_science_knows":
                "Judgement under uncertainty follows heuristics that yield "
                "systematic, reproducible biases, and framing reliably "
                "reverses preferences.",
                "what_evidence_suggests":
                "Affective valuation is a component of choice rather than an "
                "intruder on it — removing it makes decisions worse, not "
                "more rational.",
                "where_evidence_disagrees":
                "Whether heuristics are flaws or ecologically rational "
                "shortcuts that fail only in artificial tasks is a long-"
                "running dispute.",
                "what_remains_unknown":
                "There is no accepted account of when a heuristic will help "
                "and when it will mislead."
            }
        ],

        "connected_files": [
            "Emotion",
            "Prediction",
            "Motivation",
            "Identity"
        ],

        "next_case": "Attention",

        "citations": [
            {
                "key": "tversky_kahneman_1974",
                "author": "Tversky, A., & Kahneman, D.",
                "year": 1974,
                "title":
                "Judgment under uncertainty: Heuristics and biases",
                "source": "Science, 185(4157), 1124–1131"
            },
            {
                "key": "kahneman_tversky_1979",
                "author": "Kahneman, D., & Tversky, A.",
                "year": 1979,
                "title":
                "Prospect theory: An analysis of decision under risk",
                "source": "Econometrica, 47(2), 263–291"
            },
            {
                "key": "bechara_1994",
                "author":
                "Bechara, A., Damasio, A. R., Damasio, H., & Anderson, S. W.",
                "year": 1994,
                "title":
                "Insensitivity to future consequences following damage to "
                "human prefrontal cortex",
                "source": "Cognition, 50(1–3), 7–15"
            },
            {
                "key": "libet_1983",
                "author":
                "Libet, B., Gleason, C. A., Wright, E. W., & Pearl, D. K.",
                "year": 1983,
                "title":
                "Time of conscious intention to act in relation to onset of "
                "cerebral activity (readiness-potential)",
                "source": "Brain, 106(3), 623–642"
            },
            {
                "key": "soon_2008",
                "author":
                "Soon, C. S., Brass, M., Heinze, H.-J., & Haynes, J.-D.",
                "year": 2008,
                "title":
                "Unconscious determinants of free decisions in the human brain",
                "source": "Nature Neuroscience, 11(5), 543–545"
            }
        ]
    },

    "Attention": {

        "definition":
        "The selection of some information for further processing at the "
        "expense of everything else.",

        "narrative_role":
        "Attention is the editor of a life — it decides, moment by moment, "
        "which fragments will ever be available to remember or recount.",

        "paradox":
        "Attention feels like a spotlight you aim, yet most of what captures "
        "it was selected before you were aware of the choice.",

        "brain_regions": [
            "Posterior Parietal Cortex",
            "Frontal Eye Fields",
            "Temporoparietal Junction",
            "Pulvinar"
        ],

        "key_experiments": [
            "Dichotic listening / the cocktail-party problem",
            "Posner spatial cueing task",
            "Visual search and illusory conjunctions",
            "The invisible gorilla"
        ],

        "landmark_researchers": [
            "Colin Cherry",
            "Anne Treisman",
            "Michael Posner",
            "Robert Desimone"
        ],

        "connects_to": [
            "Perception",
            "Memory",
            "Consciousness",
            "Emotion"
        ],

        "real_world_examples": [
            "Hearing your name across a room",
            "Missing a road sign",
            "Doomscrolling",
            "Losing an hour to a task"
        ],

        "questions": [
            "Why can I not choose what to think about?",
            "What happens to everything I do not attend to?",
            "Is multitasking real?"
        ],

        "unresolved":
        "Is attention a single mechanism, or a family of unrelated selection "
        "processes sharing one word?",

        "interview_themes": [
            "Focus",
            "Distraction",
            "Overwhelm",
            "Presence"
        ],

        "evidence": [
            {"type": "Behavioural Experiment", "title": "Dichotic listening", "year": 1953},
            {"type": "Behavioural Experiment", "title": "Spatial cueing", "year": 1980},
            {"type": "Theory & Experiment", "title": "Feature-integration theory", "year": 1980},
            {"type": "Review", "title": "Biased-competition account", "year": 1995}
        ],

        "investigators_note":
        "The most unsettling result in this file is the oldest one: play two "
        "messages, one in each ear, ask for one of them, and the other is "
        "gone. Not faint — gone. The witness cannot say what language it was "
        "in. Whatever attention is, it is not a spotlight brightening part of "
        "an already-visible room. It is closer to the reason there is a room "
        "at all.",

        "primary_question":
        "Does attention select what we experience, or does it create what "
        "there is to experience?",

        "why_it_matters":
        "Attention is the bottleneck every other faculty queues behind: "
        "unattended events are rarely remembered, seldom learned from, and "
        "often never consciously seen. Design, education, road safety, and "
        "the entire attention economy operate on this bottleneck, mostly "
        "without the people inside it noticing.",

        "neural_systems": [
            {
                "system": "Dorsal frontoparietal network",
                "role":
                "Intraparietal sulcus and frontal eye fields; associated with "
                "voluntary, goal-directed orienting — deciding where to look "
                "and what to prioritise."
            },
            {
                "system": "Ventral frontoparietal network",
                "role":
                "Right-lateralised temporoparietal and ventral frontal cortex; "
                "associated with stimulus-driven reorienting when something "
                "unexpected but behaviourally relevant appears."
            },
            {
                "system": "Sensory cortex under competition",
                "role":
                "Multiple objects in a receptive field compete; attention "
                "biases the competition so one object's representation wins "
                "rather than adding energy to a spotlight."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Unattended input is filtered early and deeply. Listeners "
                    "shadowing a message in one ear could report almost "
                    "nothing about a simultaneous message in the other — not "
                    "its content, not even a change of language — although "
                    "gross physical properties such as the speaker's sex were "
                    "noticed.",
                    "citation": "cherry_1953"
                },
                {
                    "claim":
                    "Attention can be moved without moving the eyes, and the "
                    "movement has a measurable cost and benefit: a valid "
                    "peripheral cue speeds detection at that location and an "
                    "invalid one slows it, even with fixation held constant.",
                    "citation": "posner_1980"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Attention appears to be what glues features into objects. "
                    "Without it, features registered in parallel can be "
                    "combined wrongly, producing 'illusory conjunctions' — a "
                    "red letter reported when only a red shape and a "
                    "differently-coloured letter were present.",
                    "citation": "treisman_gelade_1980"
                },
                {
                    "claim":
                    "Two partly separable systems seem to be involved: a "
                    "dorsal network that sets goal-directed priorities, and a "
                    "right-lateralised ventral network that interrupts it when "
                    "something unexpected demands attention.",
                    "citation": "corbetta_shulman_2002"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Whether attention is a spotlight or the outcome of "
                    "competition is disputed. On the biased-competition "
                    "account there is no separate attentional resource at all "
                    "— objects compete in sensory cortex and attention is "
                    "simply the bias that resolves the competition.",
                    "citation": "desimone_duncan_1995"
                },
                {
                    "claim":
                    "The 'invisible gorilla' result is agreed on; its "
                    "interpretation is not. Failure to report an unexpected "
                    "event under load may reflect a failure to perceive it, or "
                    "a failure to retain it long enough to report — the "
                    "experiment cannot distinguish these.",
                    "citation": "simons_chabris_1999"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "Whether 'attention' names one mechanism or several "
                    "unrelated ones — spatial orienting, feature selection, "
                    "sustained vigilance, executive control — is unresolved, "
                    "and the field has no agreed criterion for deciding.",
                    "citation": "desimone_duncan_1995"
                },
                {
                    "claim":
                    "What becomes of unattended information is unknown. "
                    "Whether it is discarded at the sensors, processed to "
                    "meaning and then dropped, or retained somewhere "
                    "inaccessible has no settled answer.",
                    "citation": "cherry_1953"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "What happens to everything we do not attend to?",
                "what_science_knows":
                "Unattended channels leave almost no reportable trace: "
                "listeners cannot say what an ignored message contained.",
                "what_evidence_suggests":
                "Some unattended material is nevertheless processed — a "
                "person's own name can break through — implying filtering is "
                "not absolute.",
                "where_evidence_disagrees":
                "Early-selection and late-selection accounts have each "
                "survived decades of experiments, and biased-competition "
                "accounts reject the framing entirely.",
                "what_remains_unknown":
                "There is no method that shows what an unattended stimulus did "
                "inside a brain that never reported it."
            },
            {
                "question":
                "Is attention one thing or many?",
                "what_science_knows":
                "Distinct networks support voluntary orienting and "
                "stimulus-driven reorienting, and they can be damaged "
                "independently.",
                "what_evidence_suggests":
                "The word covers processes with different time courses, "
                "different anatomy, and different failure modes.",
                "where_evidence_disagrees":
                "Whether these constitute one faculty with subsystems or "
                "several unrelated mechanisms sharing a label is actively "
                "argued.",
                "what_remains_unknown":
                "No agreed criterion exists for individuating attentional "
                "mechanisms. UNKNOWN."
            }
        ],

        "connected_files": [
            "Perception",
            "Memory",
            "Consciousness",
            "Emotion"
        ],

        "next_case": "Learning",

        "citations": [
            {
                "key": "cherry_1953",
                "author": "Cherry, E. C.",
                "year": 1953,
                "title":
                "Some experiments on the recognition of speech, with one and "
                "with two ears",
                "source":
                "The Journal of the Acoustical Society of America, 25(5), "
                "975–979"
            },
            {
                "key": "posner_1980",
                "author": "Posner, M. I.",
                "year": 1980,
                "title": "Orienting of attention",
                "source":
                "Quarterly Journal of Experimental Psychology, 32(1), 3–25"
            },
            {
                "key": "treisman_gelade_1980",
                "author": "Treisman, A. M., & Gelade, G.",
                "year": 1980,
                "title": "A feature-integration theory of attention",
                "source": "Cognitive Psychology, 12(1), 97–136"
            },
            {
                "key": "corbetta_shulman_2002",
                "author": "Corbetta, M., & Shulman, G. L.",
                "year": 2002,
                "title":
                "Control of goal-directed and stimulus-driven attention in "
                "the brain",
                "source": "Nature Reviews Neuroscience, 3(3), 201–215"
            },
            {
                "key": "desimone_duncan_1995",
                "author": "Desimone, R., & Duncan, J.",
                "year": 1995,
                "title": "Neural mechanisms of selective visual attention",
                "source": "Annual Review of Neuroscience, 18, 193–222"
            },
            {
                "key": "simons_chabris_1999",
                "author": "Simons, D. J., & Chabris, C. F.",
                "year": 1999,
                "title":
                "Gorillas in our midst: Sustained inattentional blindness for "
                "dynamic events",
                "source": "Perception, 28(9), 1059–1074"
            }
        ]
    },

    "Learning": {

        "definition":
        "A lasting change in behaviour or knowledge produced by experience.",

        "narrative_role":
        "Learning is how a life leaves marks — it turns what happened to a "
        "person into how that person now works.",

        "paradox":
        "The brain learns constantly and effortlessly, yet deliberate learning "
        "is slow, effortful, and easily lost.",

        "brain_regions": [
            "Hippocampus",
            "Striatum",
            "Midbrain Dopamine Neurons",
            "Cerebellum"
        ],

        "key_experiments": [
            "Long-term potentiation in the rabbit dentate gyrus",
            "Dopamine reward-prediction-error recordings",
            "Probabilistic classification in amnesia and Parkinson's disease",
            "Pavlovian contingency (not contiguity) studies"
        ],

        "landmark_researchers": [
            "Timothy Bliss",
            "Terje Lømo",
            "Robert Rescorla",
            "Wolfram Schultz",
            "Barbara Knowlton"
        ],

        "connects_to": [
            "Memory",
            "Prediction",
            "Habit",
            "Motivation"
        ],

        "real_world_examples": [
            "Practising an instrument",
            "Learning to drive",
            "Language immersion",
            "Superstitious routines"
        ],

        "questions": [
            "Why does some learning stick and other learning vanish?",
            "Can you learn something without knowing that you learned it?",
            "Why is practice so much better than reading?"
        ],

        "unresolved":
        "Is a synaptic change the same thing as a learned fact, or only its "
        "trace?",

        "interview_themes": [
            "Skills",
            "School",
            "Practice",
            "Failure"
        ],

        "evidence": [
            {"type": "Electrophysiology", "title": "Long-term potentiation", "year": 1973},
            {"type": "Single-unit Recording", "title": "Dopamine prediction error", "year": 1997},
            {"type": "Patient Study", "title": "Amnesic vs. Parkinson's classification learning", "year": 1996},
            {"type": "Theoretical Review", "title": "Contingency in Pavlovian conditioning", "year": 1988}
        ],

        "investigators_note":
        "Learning is the only file in this investigation where the mechanism "
        "is visible at the level of a single synapse and still does not "
        "explain the phenomenon. We can watch a connection strengthen. We "
        "cannot yet say that the strengthened connection is the thing the "
        "person now knows. The gap between those two sentences is where this "
        "case sits.",

        "primary_question":
        "Is learning the strengthening of connections, or something the "
        "strengthening merely enables?",

        "why_it_matters":
        "Schools, rehabilitation, addiction treatment, and every attempt to "
        "change a habit assume we know how experience rewires a person. Two "
        "separate learning systems — one deliberate and reportable, one silent "
        "and procedural — respond to completely different interventions, and "
        "mistaking which one is in play is why a great deal of well-intended "
        "advice fails.",

        "neural_systems": [
            {
                "system": "Hippocampus",
                "role":
                "Supports rapid, one-shot declarative learning; the site where "
                "long-term potentiation was first demonstrated in a living "
                "animal."
            },
            {
                "system": "Striatum",
                "role":
                "Supports slow, incremental, feedback-driven habit learning "
                "that can proceed without any conscious record of the "
                "training."
            },
            {
                "system": "Midbrain dopamine neurons",
                "role":
                "Fire in proportion to the difference between predicted and "
                "received reward — a biological reward-prediction-error signal."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Synapses can be durably strengthened by use. Brief "
                    "high-frequency stimulation of the perforant path in the "
                    "anaesthetised rabbit produced a potentiation of synaptic "
                    "transmission in the dentate area lasting hours — the "
                    "first demonstration of a lasting, experience-driven "
                    "change in synaptic strength in an intact brain.",
                    "citation": "bliss_lomo_1973"
                },
                {
                    "claim":
                    "There is more than one learning system, and they can "
                    "come apart. Amnesic patients with medial temporal damage "
                    "learned a probabilistic classification task normally "
                    "while being unable to remember the training sessions; "
                    "Parkinson's patients showed the opposite pattern — "
                    "gradual habit learning and declarative memory are "
                    "separable.",
                    "citation": "knowlton_1996"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Learning tracks prediction error, not mere pairing. "
                    "Dopamine neurons fire to an unexpected reward, shift "
                    "their response to the earliest cue that predicts it, and "
                    "dip below baseline when a predicted reward is withheld — "
                    "a signal with the profile of a teaching error term.",
                    "citation": "schultz_1997"
                },
                {
                    "claim":
                    "Conditioning is not the stamping-in of associations by "
                    "repetition. What animals learn is the informational "
                    "relationship between events: a cue that adds no "
                    "predictive information produces no learning however often "
                    "it is paired.",
                    "citation": "rescorla_1988"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Whether long-term potentiation is the mechanism of "
                    "memory, or a laboratory phenomenon that resembles it, has "
                    "been argued for fifty years. The correlations are strong "
                    "and the interventions suggestive, but demonstrating that "
                    "a particular potentiated synapse holds a particular "
                    "memory remains contested ground.",
                    "citation": "bliss_lomo_1973"
                },
                {
                    "claim":
                    "How cleanly declarative and procedural learning divide is "
                    "disputed. Dissociations in patients are real, but many "
                    "everyday tasks recruit both systems, and researchers "
                    "disagree on whether they compete, cooperate, or are "
                    "poorly individuated in the first place.",
                    "citation": "knowlton_1996"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "Why some experiences produce durable learning after a "
                    "single exposure while others resist hundreds of "
                    "repetitions is not understood, and cannot currently be "
                    "predicted in advance for a given person and material.",
                    "citation": "scoville_milner_1957"
                },
                {
                    "claim":
                    "It is unknown how a distributed pattern of synaptic "
                    "weights becomes a specific piece of knowledge — the step "
                    "from physical change to content has no accepted account.",
                    "citation": "bliss_lomo_1973"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Can a person learn something without knowing they learned it?",
                "what_science_knows":
                "Yes in a limited sense: amnesic patients acquire skills and "
                "probabilistic categories they cannot consciously recall being "
                "taught.",
                "what_evidence_suggests":
                "Much of everyday competence — social timing, motor skill, "
                "preference — may be acquired by the same silent, "
                "feedback-driven system.",
                "where_evidence_disagrees":
                "Claims about unconscious learning in healthy people are "
                "persistently disputed on the grounds that awareness is "
                "measured too crudely to rule out.",
                "what_remains_unknown":
                "How much of an ordinary adult's behaviour was learned without "
                "any conscious record is unknown."
            },
            {
                "question":
                "Is a synaptic change the same thing as a learned fact?",
                "what_science_knows":
                "Experience durably changes synaptic strength, and blocking "
                "the molecular machinery of that change impairs learning.",
                "what_evidence_suggests":
                "The correspondence is close enough that most researchers "
                "treat synaptic plasticity as the substrate of learning.",
                "where_evidence_disagrees":
                "Critics note that correlation and disruption do not establish "
                "that a given synapse stores a given content.",
                "what_remains_unknown":
                "The translation between weights and knowledge is UNKNOWN."
            }
        ],

        "connected_files": [
            "Memory",
            "Prediction",
            "Habit",
            "Motivation"
        ],

        "next_case": "Perception",

        "citations": [
            {
                "key": "bliss_lomo_1973",
                "author": "Bliss, T. V. P., & Lømo, T.",
                "year": 1973,
                "title":
                "Long-lasting potentiation of synaptic transmission in the "
                "dentate area of the anaesthetized rabbit following "
                "stimulation of the perforant path",
                "source": "The Journal of Physiology, 232(2), 331–356"
            },
            {
                "key": "knowlton_1996",
                "author":
                "Knowlton, B. J., Mangels, J. A., & Squire, L. R.",
                "year": 1996,
                "title": "A neostriatal habit learning system in humans",
                "source": "Science, 273(5280), 1399–1402"
            },
            {
                "key": "schultz_1997",
                "author": "Schultz, W., Dayan, P., & Montague, P. R.",
                "year": 1997,
                "title": "A neural substrate of prediction and reward",
                "source": "Science, 275(5306), 1593–1599"
            },
            {
                "key": "rescorla_1988",
                "author": "Rescorla, R. A.",
                "year": 1988,
                "title":
                "Pavlovian conditioning: It's not what you think it is",
                "source": "American Psychologist, 43(3), 151–160"
            },
            {
                "key": "scoville_milner_1957",
                "author": "Scoville, W. B., & Milner, B.",
                "year": 1957,
                "title":
                "Loss of recent memory after bilateral hippocampal lesions",
                "source":
                "Journal of Neurology, Neurosurgery & Psychiatry, 20(1), 11–21"
            }
        ]
    },

    "Perception": {

        "definition":
        "The process by which the brain turns sensory signals into an "
        "experienced world.",

        "narrative_role":
        "Perception decides what counts as an event at all — nothing can enter "
        "a person's story that their brain did not first construct.",

        "paradox":
        "You experience the world directly, yet everything you see is a model "
        "your brain built from incomplete signals.",

        "brain_regions": [
            "Primary Visual Cortex",
            "Superior Temporal Sulcus",
            "Posterior Parietal Cortex"
        ],

        "key_experiments": [
            "Cat visual cortex single-unit recordings",
            "The McGurk audiovisual illusion",
            "Inattentional blindness (the invisible gorilla)",
            "Change blindness with 'mudsplashes'"
        ],

        "landmark_researchers": [
            "David Hubel",
            "Torsten Wiesel",
            "Harry McGurk",
            "Daniel Simons"
        ],

        "connects_to": [
            "Attention",
            "Prediction",
            "Memory",
            "Consciousness"
        ],

        "real_world_examples": [
            "Optical illusions",
            "Missing an obvious detail",
            "Mishearing song lyrics",
            "Phantom phone vibrations"
        ],

        "questions": [
            "How much of what I see is actually there?",
            "Why do two people witness the same event differently?",
            "Can I trust my own senses?"
        ],

        "unresolved":
        "How does the brain bind separate features into one unified scene?",

        "interview_themes": [
            "Senses",
            "Illusion",
            "Noticing",
            "Attention to detail"
        ],

        "evidence": [
            {"type": "Single-unit Recording", "title": "Orientation-tuned cortical cells", "year": 1962},
            {"type": "Perceptual Illusion", "title": "The McGurk effect", "year": 1976},
            {"type": "Behavioural Experiment", "title": "Inattentional blindness", "year": 1999},
            {"type": "Computational Model", "title": "Predictive coding of visual cortex", "year": 1999}
        ],

        "investigators_note":
        "Every other file in this investigation depends on testimony, and all "
        "testimony arrives through this one. What the evidence shows is not "
        "that the senses are unreliable in the ordinary sense — they are "
        "extraordinarily good — but that they are not a window. They are a "
        "reconstruction, assembled fast, from fragments, under assumptions "
        "the witness never sees. The witness reports the reconstruction and "
        "believes they are reporting the room.",

        "primary_question":
        "If perception is a construction, what exactly is a person a witness "
        "to?",

        "why_it_matters":
        "Courtroom identification, medical observation, and every argument "
        "that begins 'but I saw it' assume perception delivers the world. It "
        "delivers a model instead — usually an excellent one, occasionally a "
        "confident fiction, and the person inside it cannot tell which from "
        "the inside.",

        "neural_systems": [
            {
                "system": "Primary visual cortex (V1)",
                "role":
                "Contains cells tuned to specific edge orientations and "
                "positions, organised into columns — the first stage at which "
                "raw light is recoded into features."
            },
            {
                "system": "Superior temporal sulcus",
                "role":
                "A convergence zone for multisensory information; implicated "
                "in integrating what is seen with what is heard."
            },
            {
                "system": "Cortical feedback pathways",
                "role":
                "Carry predictions from higher areas down to sensory ones. On "
                "predictive-coding accounts, only the mismatch between "
                "prediction and input is passed back up."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Vision begins by decomposing the scene into features. "
                    "Recording from single cells in cat visual cortex revealed "
                    "neurons that fire for a line at one specific orientation "
                    "and not another, arranged in an orderly columnar "
                    "architecture — perception is built, stage by stage, from "
                    "feature detectors rather than received whole.",
                    "citation": "hubel_wiesel_1962"
                },
                {
                    "claim":
                    "Senses are combined before they reach awareness. Dubbing "
                    "the sound of one syllable onto the lip movements of "
                    "another makes listeners hear a third syllable that was "
                    "never spoken, and the illusion persists even when it is "
                    "fully explained — integration is not optional.",
                    "citation": "mcgurk_macdonald_1976"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "The brain may work by prediction rather than "
                    "transmission: higher areas send down a model of the "
                    "expected input and lower areas return only the error. "
                    "This account explains otherwise puzzling "
                    "extra-classical receptive-field effects, such as neurons "
                    "responding less to a predictable stimulus.",
                    "citation": "rao_ballard_1999"
                },
                {
                    "claim":
                    "Conscious visual experience appears far sparser than it "
                    "feels. When brief local disruptions accompany a change, "
                    "observers can stare at a scene and fail to see a large "
                    "object appear, disappear, or change colour — suggesting "
                    "the sense of a rich, continuous scene is itself part of "
                    "the construction.",
                    "citation": "oregan_1999"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Roughly half of observers counting basketball passes fail "
                    "to notice a person in a gorilla suit walking through the "
                    "display. Whether this means the gorilla was never seen, "
                    "or was seen and immediately not remembered, is genuinely "
                    "disputed — 'inattentional blindness' and 'inattentional "
                    "amnesia' predict the same report.",
                    "citation": "simons_chabris_1999"
                },
                {
                    "claim":
                    "How much of perception is inference from prior "
                    "expectation versus bottom-up analysis of the signal is "
                    "unsettled. Predictive-coding accounts are influential but "
                    "hard to falsify, and critics argue they can be fitted to "
                    "almost any result.",
                    "citation": "rao_ballard_1999"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "The binding problem is unsolved: colour, motion, shape, "
                    "and sound are processed in separate populations, yet are "
                    "experienced as a single object. No accepted mechanism "
                    "explains how the brain composes one scene from many "
                    "parallel maps.",
                    "citation": "hubel_wiesel_1962"
                },
                {
                    "claim":
                    "Why any of this processing is accompanied by experience "
                    "at all — why there is a felt redness rather than only a "
                    "wavelength computation — is unknown, and is not the kind "
                    "of gap more feature-mapping is expected to close.",
                    "citation": "chalmers_1995"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "How much of what we see is actually there?",
                "what_science_knows":
                "The visual system decomposes input into features via tuned "
                "cells and reassembles them across hierarchical stages; the "
                "early machinery is well characterised.",
                "what_evidence_suggests":
                "Large, obvious events go unreported when attention is "
                "elsewhere, and cross-modal illusions show the brain will "
                "override one sense with another — implying experience is a "
                "constructed best guess rather than a transcript.",
                "where_evidence_disagrees":
                "Whether unnoticed events are never perceived or merely never "
                "retained cannot currently be separated by report-based "
                "methods.",
                "what_remains_unknown":
                "There is no measure of how much of a scene a person is "
                "actually conscious of at a given moment."
            },
            {
                "question":
                "How does the brain bind separate features into one object?",
                "what_science_knows":
                "Different features are demonstrably processed by different, "
                "spatially separate neural populations.",
                "what_evidence_suggests":
                "Attention appears to be involved in correct binding — when it "
                "is overloaded, features can be miscombined into objects that "
                "were not present.",
                "where_evidence_disagrees":
                "Proposals range from synchronised firing to hierarchical "
                "convergence to attention-based binding, with no consensus.",
                "what_remains_unknown":
                "The mechanism that produces a single unified percept is "
                "unknown. UNKNOWN is the honest entry here."
            }
        ],

        "connected_files": [
            "Attention",
            "Prediction",
            "Memory",
            "Consciousness"
        ],

        "next_case": "Consciousness",

        "citations": [
            {
                "key": "hubel_wiesel_1962",
                "author": "Hubel, D. H., & Wiesel, T. N.",
                "year": 1962,
                "title":
                "Receptive fields, binocular interaction and functional "
                "architecture in the cat's visual cortex",
                "source": "The Journal of Physiology, 160(1), 106–154"
            },
            {
                "key": "mcgurk_macdonald_1976",
                "author": "McGurk, H., & MacDonald, J.",
                "year": 1976,
                "title": "Hearing lips and seeing voices",
                "source": "Nature, 264(5588), 746–748"
            },
            {
                "key": "rao_ballard_1999",
                "author": "Rao, R. P. N., & Ballard, D. H.",
                "year": 1999,
                "title":
                "Predictive coding in the visual cortex: A functional "
                "interpretation of some extra-classical receptive-field "
                "effects",
                "source": "Nature Neuroscience, 2(1), 79–87"
            },
            {
                "key": "oregan_1999",
                "author": "O'Regan, J. K., Rensink, R. A., & Clark, J. J.",
                "year": 1999,
                "title": "Change-blindness as a result of 'mudsplashes'",
                "source": "Nature, 398(6722), 34"
            },
            {
                "key": "simons_chabris_1999",
                "author": "Simons, D. J., & Chabris, C. F.",
                "year": 1999,
                "title":
                "Gorillas in our midst: Sustained inattentional blindness for "
                "dynamic events",
                "source": "Perception, 28(9), 1059–1074"
            },
            {
                "key": "chalmers_1995",
                "author": "Chalmers, D. J.",
                "year": 1995,
                "title": "Facing up to the problem of consciousness",
                "source": "Journal of Consciousness Studies, 2(3), 200–219"
            }
        ]
    },

    "Consciousness": {

        "definition":
        "The fact that there is something it is like to be a given creature — "
        "subjective experience itself.",

        "narrative_role":
        "Consciousness is the room the whole investigation is being conducted "
        "inside, and the only exhibit that cannot be brought out for "
        "examination.",

        "paradox":
        "It is the one thing every person has direct access to and the one "
        "thing nobody can show to anyone else.",

        "brain_regions": [
            "Prefrontal Cortex",
            "Posterior Parietal Cortex",
            "Thalamus",
            "Posterior Cortical 'Hot Zone'"
        ],

        "key_experiments": [
            "Masking and attentional-blink threshold studies",
            "Motor-imagery fMRI in vegetative-state patients",
            "Integrated information measures of conscious level",
            "The knowledge-argument and 'what is it like' thought experiments"
        ],

        "landmark_researchers": [
            "Thomas Nagel",
            "David Chalmers",
            "Stanislas Dehaene",
            "Giulio Tononi",
            "Adrian Owen"
        ],

        "connects_to": [
            "Perception",
            "Attention",
            "Memory",
            "Identity"
        ],

        "real_world_examples": [
            "Anaesthesia",
            "Dreamless sleep",
            "Autopilot driving",
            "Coming to after a blackout"
        ],

        "questions": [
            "Why is there experience at all?",
            "Could something behave exactly like me and feel nothing?",
            "How would we know if someone unresponsive is still in there?"
        ],

        "unresolved":
        "Why physical processing is accompanied by subjective experience — the "
        "hard problem — has no accepted answer.",

        "interview_themes": [
            "Awareness",
            "Sleep",
            "Autopilot",
            "Being present"
        ],

        "evidence": [
            {"type": "Philosophical Argument", "title": "What is it like to be a bat?", "year": 1974},
            {"type": "Philosophical Argument", "title": "The hard problem of consciousness", "year": 1995},
            {"type": "Neuroimaging", "title": "Detecting awareness in the vegetative state", "year": 2006},
            {"type": "Theory", "title": "Global neuronal workspace", "year": 2011},
            {"type": "Theory", "title": "Integrated information theory", "year": 2004}
        ],

        "investigators_note":
        "This is the file the exhibit was built to reach. Everywhere else, "
        "UNKNOWN means the experiment has not been done yet. Here it may mean "
        "something stronger: that no experiment of the usual kind could "
        "settle it. We can measure when a person is conscious, and "
        "increasingly of what. We cannot say why any of that measuring is "
        "accompanied by an experience. That is not a gap in the record. It is "
        "the shape of the record.",

        "primary_question":
        "Why is there something it is like to be a brain?",

        "why_it_matters":
        "Everything in the other fourteen files is reported from inside "
        "consciousness, so its limits are the limits of all the testimony "
        "collected here. It also has immediate stakes: whether an unresponsive "
        "patient is aware, whether an animal suffers, and whether a machine "
        "could, all wait on an answer nobody has.",

        "neural_systems": [
            {
                "system": "Global frontoparietal workspace",
                "role":
                "On workspace accounts, information becomes conscious when it "
                "is broadcast widely across long-range prefrontal and parietal "
                "networks, marked by a late, all-or-none ignition."
            },
            {
                "system": "Posterior cortical regions",
                "role":
                "On competing accounts the content of experience is generated "
                "posteriorly, with frontal activity reflecting report rather "
                "than experience itself."
            },
            {
                "system": "Thalamocortical system",
                "role":
                "Its integrity tracks conscious level across sleep, "
                "anaesthesia, and coma — the practical marker clinicians use."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Awareness can be present without any behavioural sign. A "
                    "patient meeting the clinical criteria for the vegetative "
                    "state produced motor-imagery and spatial-navigation brain "
                    "activity indistinguishable from healthy volunteers when "
                    "asked to imagine playing tennis or walking through her "
                    "home — a wilful, repeatable response with no outward "
                    "behaviour at all.",
                    "citation": "owen_2006"
                },
                {
                    "claim":
                    "Consciousness has objective signatures that separate seen "
                    "from unseen stimuli of identical physical strength: a "
                    "late, widely distributed, non-linear 'ignition' of "
                    "activity accompanies reportable perception and is absent "
                    "for masked stimuli.",
                    "citation": "dehaene_changeux_2011"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Conscious experience may be what integrated information "
                    "is. On this account a system is conscious to the extent "
                    "that it generates information as a whole that exceeds the "
                    "sum of its parts, which yields a quantity in principle "
                    "measurable and predicts consciousness in systems very "
                    "unlike brains.",
                    "citation": "tononi_2004"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Workspace and integrated-information theories make "
                    "opposing predictions about where and when consciousness "
                    "arises — frontal broadcast versus posterior integration — "
                    "and both survive the existing data. Adversarial "
                    "collaborations have narrowed but not settled the dispute.",
                    "citation": "dehaene_changeux_2011"
                },
                {
                    "claim":
                    "Whether any physical or functional measure could "
                    "constitute an explanation of experience, rather than a "
                    "correlate of it, is contested. Integrated information "
                    "theory is criticised for stipulating rather than "
                    "explaining the identity between structure and feeling.",
                    "citation": "tononi_2004"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "The hard problem is unsolved: no account explains why "
                    "physical processing is accompanied by subjective "
                    "experience rather than proceeding in the dark. The "
                    "'easy' problems of discrimination, reportability, and "
                    "integration can be fully solved without touching it.",
                    "citation": "chalmers_1995"
                },
                {
                    "claim":
                    "The character of another creature's experience may be "
                    "inaccessible in principle. We can describe a bat's "
                    "echolocation completely and still not know what it is "
                    "like to be one, because objective description "
                    "systematically leaves out point of view.",
                    "citation": "nagel_1974"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Why is there experience at all?",
                "what_science_knows":
                "Specific, measurable neural events distinguish conscious from "
                "unconscious processing of the same stimulus.",
                "what_evidence_suggests":
                "Consciousness may correspond to global availability of "
                "information, or to the degree of integration a system "
                "achieves.",
                "where_evidence_disagrees":
                "Leading theories locate consciousness in different cortex and "
                "make different predictions about non-biological systems; "
                "neither has been decisively falsified.",
                "what_remains_unknown":
                "Why any of this is accompanied by experience is UNKNOWN, and "
                "may not be the kind of question further correlates can "
                "answer."
            },
            {
                "question":
                "How would we know if an unresponsive person is still aware?",
                "what_science_knows":
                "At least some patients diagnosed as vegetative can generate "
                "reliable, task-specific brain responses to instructions.",
                "what_evidence_suggests":
                "Covert awareness is present in a meaningful minority of "
                "unresponsive patients, and behavioural diagnosis alone "
                "misses it.",
                "where_evidence_disagrees":
                "A negative result is uninterpretable: absence of response may "
                "mean absence of awareness, or a lesion anywhere along the "
                "path from understanding to imagery.",
                "what_remains_unknown":
                "There is no test that can rule awareness out."
            }
        ],

        "connected_files": [
            "Perception",
            "Attention",
            "Memory",
            "Identity"
        ],

        "next_case": "Trauma",

        "citations": [
            {
                "key": "nagel_1974",
                "author": "Nagel, T.",
                "year": 1974,
                "title": "What is it like to be a bat?",
                "source": "The Philosophical Review, 83(4), 435–450"
            },
            {
                "key": "chalmers_1995",
                "author": "Chalmers, D. J.",
                "year": 1995,
                "title": "Facing up to the problem of consciousness",
                "source": "Journal of Consciousness Studies, 2(3), 200–219"
            },
            {
                "key": "owen_2006",
                "author":
                "Owen, A. M., Coleman, M. R., Boly, M., Davis, M. H., "
                "Laureys, S., & Pickard, J. D.",
                "year": 2006,
                "title": "Detecting awareness in the vegetative state",
                "source": "Science, 313(5792), 1402"
            },
            {
                "key": "dehaene_changeux_2011",
                "author": "Dehaene, S., & Changeux, J.-P.",
                "year": 2011,
                "title":
                "Experimental and theoretical approaches to conscious "
                "processing",
                "source": "Neuron, 70(2), 200–227"
            },
            {
                "key": "tononi_2004",
                "author": "Tononi, G.",
                "year": 2004,
                "title":
                "An information integration theory of consciousness",
                "source": "BMC Neuroscience, 5, 42"
            }
        ]
    },

    "Habit": {

        "definition":
        "A learned response that has been repeated until it is triggered by the situation rather than chosen for its outcome — behaviour that runs on context instead of intention.",

        "narrative_role":
        "Habit is the part of a life the internal narrative does not author. It is where the story a person tells about deciding parts company with what actually moved them.",

        "paradox":
        "The better you learn to do something on purpose, the less purpose has to do with your doing it.",

        "brain_regions": [
            "Dorsolateral Striatum (Putamen)",
            "Dorsomedial Striatum (Caudate)",
            "Basal Ganglia",
            "Infralimbic Cortex",
            "Substantia Nigra"
        ],

        "key_experiments": [
            "Reinforcer devaluation after extended instrumental training",
            "Probabilistic classification ('weather prediction') in amnesia and Parkinson's disease",
            "Overtraining and outcome devaluation with fMRI in humans",
            "Striatal task-bracketing during maze-running overtraining",
            "Five attempted inductions of experimental habit in humans"
        ],

        "landmark_researchers": [
            "Anthony Dickinson",
            "Christopher Adams",
            "Barbara Knowlton",
            "Bernard Balleine",
            "Ann Graybiel",
            "Wendy Wood",
            "Sanne de Wit"
        ],

        "connects_to": [
            "Learning",
            "Decision Making",
            "Motivation",
            "Identity",
            "Memory"
        ],

        "real_world_examples": [
            "Driving home when you meant to go somewhere else",
            "Reaching for the phone before deciding to",
            "A route walked so often you arrive without remembering the walk",
            "Reaching for the light switch in a room whose bulb is broken",
            "Smoking a cigarette you did not want"
        ],

        "questions": [
            "How much of what I did today did I choose?",
            "If I explain why I did it afterwards, is the explanation the reason?",
            "Why is a habit easier to replace than to delete?"
        ],

        "unresolved":
        "Whether a habit is a separate kind of behaviour with its own machinery, or simply a goal-directed act whose reasons have stopped being consulted.",

        "interview_themes": [
            "Routine",
            "Repetition",
            "Ritual",
            "Autopilot",
            "Change"
        ],

        "evidence": [
            {
                "type": "Animal Experiment",
                "title": "Instrumental responding after reinforcer devaluation",
                "year": 1982
            },
            {
                "type": "Patient Study",
                "title": "Neostriatal habit learning in amnesia and Parkinson's disease",
                "year": 1996
            },
            {
                "type": "Theoretical Review",
                "title": "The basal ganglia and the goal-directed/habitual divide",
                "year": 2006
            },
            {
                "type": "Neuroimaging",
                "title": "Overtraining and outcome devaluation in humans",
                "year": 2009
            },
            {
                "type": "Replication Study",
                "title": "Five failures in experimental habit induction",
                "year": 2018
            }
        ],

        "investigators_note":
        "This file is the one that embarrasses the rest of the investigation. Everywhere else the exhibit traces a line from experience through memory into a story and out again as a decision. Habit is the evidence that a large share of behaviour skips the story entirely. The action is triggered by the room, the hour, the cigarette packet on the table — and the account of why it happened is assembled afterwards, by a narrator who was not consulted at the time and does not know it. What makes the file harder still is that the laboratory finding is solid in rats and slippery in people: the paradigm that defines habit has proven difficult to reproduce in healthy human volunteers. So we are left with a phenomenon everyone recognises from their own life and a measure that will not reliably show it.",

        "primary_question":
        "How much of a life is authored by the story a person tells about it, and how much simply runs?",

        "why_it_matters":
        "Everything people try hardest to change about themselves — what they eat, drink, scroll, avoid, repeat — sits in this file. If those actions are driven by context rather than by intention, then insight into one's own reasons is not the lever it feels like, and the loop this exhibit is chasing has a stretch in it the narrator never touches.",

        "neural_systems": [
            {
                "system": "Dorsomedial striatum (human caudate)",
                "role": "Supports goal-directed action — behaviour still sensitive to the current value of its outcome and to the action–outcome contingency."
            },
            {
                "system": "Dorsolateral striatum (human posterior putamen)",
                "role": "Associated with stimulus–response habit: activity here grows with extended training, as behaviour comes to be cued by the situation rather than steered by its consequence."
            },
            {
                "system": "Basal ganglia loops and their dopaminergic input",
                "role": "Chunk repeated action sequences into single retrievable units, with striatal ensembles marking the beginning and end of a learned routine rather than its middle."
            },
            {
                "system": "Infralimbic / ventromedial prefrontal cortex",
                "role": "Implicated in the expression and suppression of established habits — a cortical switch that determines which striatal system is in control of the same behaviour."
            }
        ],

        "evidence_room": {
            "what_we_know": [
                {
                    "claim": "Amount of training changes the kind of behaviour, not just its strength. Rats trained briefly on a lever press stopped pressing once the food earned by that press was made aversive; rats given extended training kept pressing for a reward they no longer wanted. The same action, learned the same way, becomes insensitive to its own outcome with repetition.",
                    "citation": "adams_1982"
                },
                {
                    "claim": "Habit learning and declarative memory are separable systems in the human brain. On a probabilistic classification task, amnesic patients learned the cue–outcome associations at a normal rate while being unable to recall the training episode; patients with Parkinson's disease showed the opposite dissociation — intact memory for the task, impaired gradual learning. The striatum, not the medial temporal lobe, carries this form of learning.",
                    "citation": "knowlton_1996"
                }
            ],
            "evidence_suggests": [
                {
                    "claim": "The two modes of control appear to map onto different striatal territory. Converging lesion and recording work in rodents places goal-directed control in dorsomedial striatum and habitual control in dorsolateral striatum, with behaviour shifting from one to the other as training extends — an anatomical division of labour rather than a single strengthening process.",
                    "citation": "yin_knowlton_2006"
                },
                {
                    "claim": "Repetition compresses a sequence of actions into a unit. As a routine is overtrained, striatal ensembles come to fire at the start and end of the whole sequence rather than throughout it — a 'chunking' signature suggesting a habit is stored as one package that, once begun, tends to run to completion.",
                    "citation": "graybiel_2008"
                },
                {
                    "claim": "A comparable shift has been reported in people. After three days of overtraining, participants continued responding for a food outcome they had just been fed to satiety, and activity in posterior dorsolateral striatum increased across training — the closest human analogue of the animal devaluation result.",
                    "citation": "tricomi_2009"
                }
            ],
            "disagreement": [
                {
                    "claim": "The human devaluation paradigm may not be reliable. A coordinated series of five experiments explicitly designed to induce habit in healthy volunteers — varying training duration, schedule, and context — failed to produce the expected outcome-insensitivity. The authors conclude the field's standard laboratory measure of habit is not dependably reproducible in humans, which puts the human evidence for the two-system account under active dispute.",
                    "citation": "de_wit_2018"
                },
                {
                    "claim": "Researchers disagree about what habit even names. One tradition defines it negatively, by insensitivity to outcome value in a laboratory task; another defines it as a learned context–response association whose real signature is being cued by a stable environment in everyday life. The two definitions do not pick out the same behaviours, and arguments about the strength of the evidence are often arguments about which definition is in use.",
                    "citation": "wood_runger_2016"
                },
                {
                    "claim": "Whether habitual and goal-directed control are two systems competing for the same behaviour, or one graded process measured two ways, is unsettled. The anatomical dissociation is read by some as decisive and by others as compatible with a single learning mechanism whose expression varies with how strongly the action is trained.",
                    "citation": "yin_knowlton_2006"
                }
            ],
            "unknown": [
                {
                    "claim": "There is no established way to tell, for a particular action in a particular person's day, whether it was habitual or chosen. The laboratory criterion requires devaluing an outcome and watching what happens next; ordinary life provides no such test, and self-report cannot supply one, because the report is produced by the system that was bypassed.",
                    "citation": "de_wit_2018"
                },
                {
                    "claim": "How long a habit takes to form in a human being, and what determines that duration, is not known with any precision. Estimates vary widely across behaviours and individuals, and no mechanism has been identified that predicts the point at which an intended action stops requiring the intention.",
                    "citation": "wood_runger_2016"
                },
                {
                    "claim": "It is unknown whether an established habit can be erased or only overlaid. Old responses return under stress, fatigue, and reinstated context long after a replacement has been trained, which is consistent with the original chunk remaining intact and merely suppressed — but no method exists to look and confirm it is still there.",
                    "citation": "graybiel_2008"
                }
            ]
        },

        "open_questions": [
            {
                "question": "If a habit runs without the narrative, what is the narrative for?",
                "what_science_knows": "Behaviour that begins as goal-directed can become insensitive to the value of its own outcome with extended training, and the striatal learning that supports it can proceed in people who cannot consciously recall the training at all.",
                "what_evidence_suggests": "Control appears to migrate across striatal territory with repetition, and overtrained routines are stored as compressed sequences that tend to complete once triggered — implying the reasons a person gives were not the proximate cause of the act.",
                "where_evidence_disagrees": "Whether this is genuinely two systems or one graded process is argued, and the human demonstrations that support the strong version have repeatedly failed to replicate.",
                "what_remains_unknown": "What function the after-the-fact account serves — whether it steers future behaviour, maintains a coherent self, or does nothing causal at all — is UNKNOWN."
            },
            {
                "question": "Can a habit be removed, or only outvoted?",
                "what_science_knows": "New responses can be trained to compete with old ones, and prefrontal regions are implicated in which response is expressed on a given occasion.",
                "what_evidence_suggests": "The reappearance of old responses under stress and in the original context suggests the earlier learning survives intact beneath the replacement rather than being overwritten.",
                "where_evidence_disagrees": "Researchers disagree over whether relapse reflects a preserved habit structure or simply the ordinary context-dependence of any learned behaviour, and the animal and human literatures do not align cleanly.",
                "what_remains_unknown": "No technique can determine whether a specific habit still exists in a brain that is no longer performing it."
            },
            {
                "question": "Why will the laboratory not show in people what it shows plainly in rats?",
                "what_science_knows": "Outcome devaluation after extended training is a robust, repeatedly demonstrated effect in rodents and the defining operational test of habit.",
                "what_evidence_suggests": "Human participants may bring instructions, verbal rules, and explicit strategies into the task that keep behaviour tethered to its outcome, and the training given in a laboratory session may be trivial next to the repetitions behind a real habit.",
                "where_evidence_disagrees": "Some read the replication failures as a problem with the paradigm and its statistical power; others read them as evidence that the two-system account has been over-extended from animals to human behaviour.",
                "what_remains_unknown": "Whether human habit as lived is the same phenomenon the animal paradigm measures — and therefore whether the most familiar experience in this file has ever actually been captured in a laboratory — is UNKNOWN."
            }
        ],

        "connected_files": [
            "Learning",
            "Decision Making",
            "Motivation",
            "Identity",
            "Memory",
            "Narrative"
        ],

        "next_case":
        "Motivation",

        "citations": [
            {
                "key": "adams_1982",
                "author": "Adams, C. D.",
                "year": 1982,
                "title": "Variations in the sensitivity of instrumental responding to reinforcer devaluation",
                "source": "The Quarterly Journal of Experimental Psychology Section B, 34(2), 77–98"
            },
            {
                "key": "knowlton_1996",
                "author": "Knowlton, B. J., Mangels, J. A., & Squire, L. R.",
                "year": 1996,
                "title": "A neostriatal habit learning system in humans",
                "source": "Science, 273(5280), 1399–1402"
            },
            {
                "key": "yin_knowlton_2006",
                "author": "Yin, H. H., & Knowlton, B. J.",
                "year": 2006,
                "title": "The role of the basal ganglia in habit formation",
                "source": "Nature Reviews Neuroscience, 7(6), 464–476"
            },
            {
                "key": "graybiel_2008",
                "author": "Graybiel, A. M.",
                "year": 2008,
                "title": "Habits, rituals, and the evaluative brain",
                "source": "Annual Review of Neuroscience, 31, 359–387"
            },
            {
                "key": "tricomi_2009",
                "author": "Tricomi, E., Balleine, B. W., & O'Doherty, J. P.",
                "year": 2009,
                "title": "A specific role for posterior dorsolateral striatum in human habit learning",
                "source": "European Journal of Neuroscience, 29(11), 2225–2232"
            },
            {
                "key": "wood_runger_2016",
                "author": "Wood, W., & Rünger, D.",
                "year": 2016,
                "title": "Psychology of habit",
                "source": "Annual Review of Psychology, 67, 289–314"
            },
            {
                "key": "de_wit_2018",
                "author": "de Wit, S., Kindt, M., Knot, S. L., Verhoeven, A. A. C., Robbins, T. W., Gasull-Camos, J., Evans, M., Mirza, H., & Gillan, C. M.",
                "year": 2018,
                "title": "Shifting the balance between goals and habits: Five failures in experimental habit induction",
                "source": "Journal of Experimental Psychology: General, 147(7), 1043–1065"
            }
        ],
    },

    "Trauma": {

        "definition":
        "The lasting psychological and physiological alteration that can "
        "follow an overwhelming event.",

        "narrative_role":
        "Trauma is the part of a life story that refuses to become past "
        "tense.",

        "paradox":
        "The same event devastates one person and leaves another intact, and "
        "neither outcome can be predicted from the event alone.",

        "brain_regions": [
            "Amygdala",
            "Hippocampus",
            "Ventromedial Prefrontal Cortex"
        ],

        "key_experiments": [
            "Adverse Childhood Experiences cohort study",
            "Meta-analysis of PTSD risk factors",
            "Monozygotic twin study of hippocampal volume",
            "Propranolol reconsolidation blockade in humans"
        ],

        "landmark_researchers": [
            "Vincent Felitti",
            "Chris Brewin",
            "George Bonanno",
            "Merel Kindt",
            "Mark Gilbertson"
        ],

        "connects_to": [
            "Memory",
            "Emotion",
            "Identity",
            "Prediction"
        ],

        "real_world_examples": [
            "Intrusive flashbacks",
            "Hypervigilance",
            "Anniversary reactions",
            "Avoidance of a place"
        ],

        "questions": [
            "Why does the body keep responding to something that has ended?",
            "Why do most people recover and some do not?",
            "Can a traumatic memory be edited without erasing the person?"
        ],

        "unresolved":
        "Is post-traumatic disorder a disorder of memory, of fear learning, or "
        "of recovery failing to occur?",

        "interview_themes": [
            "Aftermath",
            "Fear",
            "Recovery",
            "Safety"
        ],

        "evidence": [
            {"type": "Cohort Study", "title": "Adverse Childhood Experiences (ACE)", "year": 1998},
            {"type": "Meta-analysis", "title": "Risk factors for PTSD", "year": 2000},
            {"type": "Twin Study", "title": "Hippocampal volume as pre-existing vulnerability", "year": 2002},
            {"type": "Human Experiment", "title": "Reconsolidation blockade of fear", "year": 2009}
        ],

        "investigators_note":
        "Handle this file carefully. It is the one place where the "
        "investigation's habit of writing UNKNOWN has consequences for living "
        "people. Two findings sit uncomfortably together here: that severe "
        "early adversity leaves a measurable dose-dependent mark decades "
        "later, and that most people exposed to a traumatic event do not "
        "develop a disorder. Both are well supported. Neither predicts the "
        "individual in front of you.",

        "primary_question":
        "Why does the same event become a wound in one person and a memory in "
        "another?",

        "why_it_matters":
        "Trauma is where memory, emotion, and identity fail together, and "
        "where the exhibit's central claim — that the mind reconstructs "
        "rather than records — stops being an abstraction. It also carries "
        "the field's most consequential open question: whether a memory can "
        "be therapeutically altered without falsifying a person's history.",

        "neural_systems": [
            {
                "system": "Amygdala",
                "role":
                "Acquires and expresses conditioned fear; implicated in the "
                "persistence of threat responses to cues that are no longer "
                "dangerous."
            },
            {
                "system": "Hippocampus",
                "role":
                "Places memories in context. Smaller hippocampal volume is "
                "associated with PTSD — and twin evidence suggests it may "
                "precede rather than result from the trauma."
            },
            {
                "system": "Ventromedial prefrontal cortex",
                "role":
                "Supports extinction learning — the signalling of safety that "
                "allows a fear response to be inhibited in a new context."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Childhood adversity is associated with adult health in a "
                    "graded, dose-dependent way. In a cohort of over 9,000 "
                    "adults, the number of categories of childhood abuse and "
                    "household dysfunction reported predicted risk of "
                    "depression, substance use, and several leading causes of "
                    "death decades later.",
                    "citation": "felitti_1998"
                },
                {
                    "claim":
                    "Risk of PTSD after a traumatic event depends less on the "
                    "event than on what surrounds it. Meta-analysis of "
                    "trauma-exposed adults found that peritraumatic factors "
                    "and lack of social support predicted PTSD more "
                    "consistently than pre-trauma demographic variables — and "
                    "that effect sizes were uniformly modest.",
                    "citation": "brewin_2000"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Resilience, not disorder, is the common outcome. Across "
                    "bereavement and potentially traumatic events, the "
                    "majority of people show a stable trajectory of healthy "
                    "functioning — suggesting the field long generalised from "
                    "the minority who sought treatment.",
                    "citation": "bonanno_2004"
                },
                {
                    "claim":
                    "Some vulnerability appears to pre-date the trauma. In "
                    "identical twins discordant for combat exposure, the "
                    "unexposed co-twins of veterans with PTSD had hippocampal "
                    "volumes as small as their affected siblings — implicating "
                    "a pre-existing familial risk factor rather than damage "
                    "caused by the trauma.",
                    "citation": "gilbertson_2002"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "Fear responses in humans could be weakened long-term by "
                    "giving propranolol during memory reactivation, apparently "
                    "targeting reconsolidation rather than adding extinction "
                    "learning. Whether this erases the emotional memory, "
                    "suppresses its expression, or works at all outside "
                    "tightly controlled laboratory conditions is contested, "
                    "with mixed replication.",
                    "citation": "kindt_2009"
                },
                {
                    "claim":
                    "Reconsolidation theory itself — that recall returns a "
                    "memory to a modifiable state — is disputed in its "
                    "application to human autobiographical trauma memories, "
                    "where the animal paradigms may not transfer.",
                    "citation": "nader_2000"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "There is no test that predicts, for an individual before "
                    "or shortly after a traumatic event, whether they will "
                    "develop a lasting disorder. Group-level risk factors do "
                    "not resolve to the person.",
                    "citation": "brewin_2000"
                },
                {
                    "claim":
                    "Whether a traumatic memory can be therapeutically "
                    "weakened without altering the person's factual record of "
                    "their own life is unknown — and the ethical question of "
                    "whether it should be is entirely unresolved.",
                    "citation": "kindt_2009"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Why do most people recover from trauma and some do not?",
                "what_science_knows":
                "Cumulative childhood adversity raises long-term risk in a "
                "dose-dependent way, and post-event social support is among "
                "the more consistent predictors of outcome.",
                "what_evidence_suggests":
                "Resilience is the statistical norm, and part of the "
                "vulnerability that distinguishes the minority may be present "
                "before the event ever occurs.",
                "where_evidence_disagrees":
                "Whether smaller hippocampal volume is a cause, a consequence, "
                "or a correlate of PTSD is still argued despite the twin "
                "evidence.",
                "what_remains_unknown":
                "Individual outcome cannot be predicted. UNKNOWN."
            },
            {
                "question":
                "Can a traumatic memory be edited?",
                "what_science_knows":
                "Retrieval can render some memories temporarily susceptible to "
                "pharmacological disruption in animals.",
                "what_evidence_suggests":
                "Human fear responses have been durably reduced by intervening "
                "during reactivation, without the return of fear that follows "
                "ordinary extinction.",
                "where_evidence_disagrees":
                "Replication is mixed, and whether the memory is altered or "
                "only its expression suppressed is unresolved.",
                "what_remains_unknown":
                "Whether the content of a human autobiographical trauma memory "
                "can be changed — and what it would mean for a person's "
                "history if it could — is unknown."
            }
        ],

        "connected_files": [
            "Memory",
            "Emotion",
            "Identity",
            "Prediction"
        ],

        "next_case": "Prediction",

        "citations": [
            {
                "key": "felitti_1998",
                "author":
                "Felitti, V. J., Anda, R. F., Nordenberg, D., Williamson, "
                "D. F., Spitz, A. M., Edwards, V., Koss, M. P., & Marks, J. S.",
                "year": 1998,
                "title":
                "Relationship of childhood abuse and household dysfunction to "
                "many of the leading causes of death in adults: The Adverse "
                "Childhood Experiences (ACE) Study",
                "source":
                "American Journal of Preventive Medicine, 14(4), 245–258"
            },
            {
                "key": "brewin_2000",
                "author": "Brewin, C. R., Andrews, B., & Valentine, J. D.",
                "year": 2000,
                "title":
                "Meta-analysis of risk factors for posttraumatic stress "
                "disorder in trauma-exposed adults",
                "source":
                "Journal of Consulting and Clinical Psychology, 68(5), 748–766"
            },
            {
                "key": "bonanno_2004",
                "author": "Bonanno, G. A.",
                "year": 2004,
                "title":
                "Loss, trauma, and human resilience: Have we underestimated "
                "the human capacity to thrive after extremely aversive events?",
                "source": "American Psychologist, 59(1), 20–28"
            },
            {
                "key": "gilbertson_2002",
                "author":
                "Gilbertson, M. W., Shenton, M. E., Ciszewski, A., Kasai, K., "
                "Lasko, N. B., Orr, S. P., & Pitman, R. K.",
                "year": 2002,
                "title":
                "Smaller hippocampal volume predicts pathologic vulnerability "
                "to psychological trauma",
                "source": "Nature Neuroscience, 5(11), 1242–1247"
            },
            {
                "key": "kindt_2009",
                "author": "Kindt, M., Soeter, M., & Vervliet, B.",
                "year": 2009,
                "title":
                "Beyond extinction: Erasing human fear responses and "
                "preventing the return of fear",
                "source": "Nature Neuroscience, 12(3), 256–258"
            },
            {
                "key": "nader_2000",
                "author": "Nader, K., Schafe, G. E., & LeDoux, J. E.",
                "year": 2000,
                "title":
                "Fear memories require protein synthesis in the amygdala for "
                "reconsolidation after retrieval",
                "source": "Nature, 406(6797), 722–726"
            }
        ]
    },

    "Language": {

        "definition":
        "The system by which a mind encodes thought into a shared signal, and "
        "recovers thought from the signals of others.",

        "narrative_role":
        "Language is the medium the internal narrative is written in — which "
        "makes it impossible to say where the story ends and the words begin.",

        "paradox":
        "Every speaker follows rules of grammar no speaker can state, learned "
        "in childhood from evidence that never contained the rules.",

        "brain_regions": [
            "Left Inferior Frontal Gyrus (Broca's Area)",
            "Posterior Superior Temporal Gyrus (Wernicke's Area)",
            "Arcuate Fasciculus",
            "Anterior Temporal Lobe"
        ],

        "key_experiments": [
            "Lesion-based localisation of articulate speech (Leborgne)",
            "FOXP2 mutation in the KE family",
            "Statistical segmentation of a speech stream by infants",
            "Functional localisation of the language network (fMRI)",
            "Colour discrimination across a lexical boundary"
        ],

        "landmark_researchers": [
            "Paul Broca",
            "Jenny Saffran",
            "Evelina Fedorenko",
            "Noam Chomsky",
            "Lera Boroditsky"
        ],

        "connects_to": [
            "Memory",
            "Perception",
            "Learning",
            "Identity",
            "Narrative"
        ],

        "real_world_examples": [
            "Losing a word that is plainly there",
            "Dreaming in a second language",
            "A feeling you have no name for",
            "Translation that carries everything but the point"
        ],

        "questions": [
            "Do I think in words, or translate afterwards?",
            "Is there a thought I cannot have in my language?",
            "Who is speaking when I talk to myself?"
        ],

        "unresolved":
        "Whether language is the vehicle thought travels in or the shape "
        "thought is forced into.",

        "interview_themes": [
            "Words",
            "Naming",
            "Silence",
            "Expression",
            "Conversation"
        ],

        "evidence": [
            {"type": "Patient Study", "title": "Broca's aphasia and the localisation of speech", "year": 1861},
            {"type": "Genetic Study", "title": "FOXP2 mutation in a speech and language disorder", "year": 2001},
            {"type": "Infant Study", "title": "Statistical learning by 8-month-old infants", "year": 1996},
            {"type": "Neuroimaging", "title": "Functional specificity of the language network", "year": 2011},
            {"type": "Psychophysics", "title": "Russian blues and categorical colour discrimination", "year": 2007}
        ],

        "investigators_note":
        "The difficulty with this file is that the investigation is being "
        "conducted in its own subject. Every question here had to be asked in "
        "words, which is exactly the instrument under examination. The record "
        "shows two findings that are not in doubt — that language depends on "
        "particular tissue, and that children extract its structure from "
        "input that never states it — sitting either side of a question "
        "nobody has closed: whether the words you have determine the thoughts "
        "you can hold. A century and a half after Broca opened Leborgne's "
        "skull, we can say with precision where language lives and almost "
        "nothing about how it means.",

        "primary_question":
        "Does the language you speak decide the thoughts you are able to "
        "have?",

        "why_it_matters":
        "If thought is shaped by language, then the internal narrative this "
        "investigation is chasing is not merely told in words — it is limited "
        "by them, and two people with different words are not describing the "
        "same inner life in different terms but living slightly different "
        "ones.",

        "neural_systems": [
            {
                "system": "Left inferior frontal gyrus (Broca's area)",
                "role":
                "Damage here disrupts the production of fluent, grammatically "
                "structured speech while leaving comprehension and general "
                "intelligence comparatively intact."
            },
            {
                "system": "Posterior superior temporal cortex",
                "role":
                "Associated with mapping speech sound onto meaning; damage "
                "produces fluent speech that is largely empty of content."
            },
            {
                "system": "The frontotemporal language network",
                "role":
                "Responds to linguistic structure specifically, and not to "
                "arithmetic, music, or general working-memory demand."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "Language depends on particular tissue, not on general "
                    "intelligence spread evenly through the brain. Broca's "
                    "patient Leborgne could produce almost no articulate "
                    "speech yet understood what was said to him; autopsy "
                    "found a lesion in the left frontal lobe. Damage to a "
                    "specific region takes speech and leaves the person.",
                    "citation": "broca_1861"
                },
                {
                    "claim":
                    "A mutation in a single gene can produce a severe, "
                    "inherited speech and language disorder. In the KE family, "
                    "affected members across three generations carry a point "
                    "mutation in FOXP2 — evidence that language development "
                    "has identifiable genetic dependencies.",
                    "citation": "lai_2001"
                },
                {
                    "claim":
                    "There is a maturational window. Among immigrants to the "
                    "United States, grammatical attainment in English declined "
                    "linearly with age of arrival up to puberty; those who "
                    "arrived after puberty scored low but highly variably, "
                    "with no further relation to age — a limit on acquisition "
                    "that experience alone does not remove.",
                    "citation": "johnson_newport_1989"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Infants extract structure from raw statistics. After two "
                    "minutes of a continuous, unbroken speech stream, "
                    "8-month-olds distinguished recurring 'words' from "
                    "syllable sequences that merely straddled a boundary — "
                    "segmenting on transitional probability alone, with no "
                    "pauses, stress, or meaning to help them.",
                    "citation": "saffran_1996"
                },
                {
                    "claim":
                    "The language network appears functionally selective. "
                    "Regions that respond to sentences over nonsense strings "
                    "show little response to arithmetic, music, or "
                    "general-purpose cognitive demand, suggesting machinery "
                    "specialised for language rather than borrowed from "
                    "thought in general.",
                    "citation": "fedorenko_2011"
                },
                {
                    "claim":
                    "Words appear to reach into perception itself. Russian "
                    "makes an obligatory lexical distinction between lighter "
                    "and darker blue; Russian speakers discriminated colours "
                    "faster across that boundary than within it, and the "
                    "advantage disappeared under a verbal interference task.",
                    "citation": "winawer_2007"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "What, if anything, is uniquely linguistic is openly "
                    "contested. One influential position holds that the only "
                    "component special to human language is recursion, with "
                    "the rest shared with other systems and species.",
                    "citation": "hauser_2002"
                },
                {
                    "claim":
                    "That position was answered directly: that far more of "
                    "language — speech perception, the lexicon, morphology, "
                    "syntax beyond recursion — bears the marks of "
                    "special-purpose adaptation. The exchange remains "
                    "unresolved and is one of the field's defining arguments.",
                    "citation": "pinker_jackendoff_2005"
                },
                {
                    "claim":
                    "How far linguistic relativity extends is disputed. "
                    "Reported effects of a language's metaphors for time on "
                    "its speakers' reasoning have been influential and also "
                    "difficult to replicate consistently, leaving the "
                    "strength of the effect unsettled.",
                    "citation": "boroditsky_2001"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "How a pattern of neural activity comes to be *about* "
                    "something is unknown. The brain regions that carry "
                    "language can be located to the millimetre; by what means "
                    "a signal in them refers to a thing in the world is not a "
                    "solved problem, and it is not obvious what solving it "
                    "would look like.",
                    "citation": "fedorenko_2011"
                },
                {
                    "claim":
                    "Whether thought requires language remains open. People "
                    "report wordless thinking, and the language network is "
                    "quiet during some demanding reasoning, but there is no "
                    "accepted method for examining a thought without "
                    "rendering it into words first — the measurement destroys "
                    "the thing measured.",
                    "citation": "hauser_2002"
                },
                {
                    "claim":
                    "How a child arrives at a grammar from the input actually "
                    "available is unresolved. Statistical learning is "
                    "demonstrably powerful and demonstrably insufficient on "
                    "its own; what supplies the remainder — richer input, "
                    "innate constraint, or something not yet described — is "
                    "UNKNOWN.",
                    "citation": "saffran_1996"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Does the language you speak shape the thoughts you can have?",
                "what_science_knows":
                "Language is processed by identifiable, functionally "
                "selective neural systems, and losing them takes specific "
                "linguistic abilities rather than thought in general.",
                "what_evidence_suggests":
                "Lexical distinctions measurably affect perceptual "
                "performance — Russian speakers discriminate blues faster "
                "across a boundary their language marks, and the advantage "
                "vanishes when verbal resources are occupied.",
                "where_evidence_disagrees":
                "Whether such effects reach thought itself or only the "
                "strategies used in a task is argued, and the more sweeping "
                "relativity results have proven hard to replicate.",
                "what_remains_unknown":
                "Nobody has devised a way to examine a thought without first "
                "putting it into language, so whether the words are the "
                "container or the content is UNKNOWN."
            },
            {
                "question":
                "Is language a dedicated faculty, or ordinary machinery doing "
                "an extraordinary job?",
                "what_science_knows":
                "Language depends on specific tissue and has identifiable "
                "genetic dependencies; damage and mutation both disrupt it in "
                "structured, repeatable ways.",
                "what_evidence_suggests":
                "The frontotemporal language network responds to linguistic "
                "structure and not to arithmetic, music, or general cognitive "
                "load — while infants also segment speech using "
                "domain-general statistical learning.",
                "where_evidence_disagrees":
                "Whether recursion is the only uniquely linguistic component "
                "or much of language is special-purpose adaptation is a live, "
                "openly-argued dispute between leading accounts.",
                "what_remains_unknown":
                "No experiment yet separates machinery built for language "
                "from general machinery that language has colonised."
            }
        ],

        "connected_files": [
            "Memory",
            "Perception",
            "Learning",
            "Identity",
            "Narrative"
        ],

        "next_case": "Habit",

        "citations": [
            {
                "key": "broca_1861",
                "author": "Broca, P.",
                "year": 1861,
                "title":
                "Remarques sur le siège de la faculté du langage articulé, "
                "suivies d'une observation d'aphémie (perte de la parole)",
                "source":
                "Bulletin de la Société Anatomique de Paris, 6, 330–357"
            },
            {
                "key": "lai_2001",
                "author": "Lai, C. S. L., Fisher, S. E., Hurst, J. A., "
                          "Vargha-Khadem, F., & Monaco, A. P.",
                "year": 2001,
                "title":
                "A forkhead-domain gene is mutated in a severe speech and "
                "language disorder",
                "source": "Nature, 413(6855), 519–523"
            },
            {
                "key": "johnson_newport_1989",
                "author": "Johnson, J. S., & Newport, E. L.",
                "year": 1989,
                "title":
                "Critical period effects in second language learning: The "
                "influence of maturational state on the acquisition of "
                "English as a second language",
                "source": "Cognitive Psychology, 21(1), 60–99"
            },
            {
                "key": "saffran_1996",
                "author": "Saffran, J. R., Aslin, R. N., & Newport, E. L.",
                "year": 1996,
                "title": "Statistical learning by 8-month-old infants",
                "source": "Science, 274(5294), 1926–1928"
            },
            {
                "key": "fedorenko_2011",
                "author": "Fedorenko, E., Behr, M. K., & Kanwisher, N.",
                "year": 2011,
                "title":
                "Functional specificity for high-level linguistic processing "
                "in the human brain",
                "source":
                "Proceedings of the National Academy of Sciences, 108(39), "
                "16428–16433"
            },
            {
                "key": "winawer_2007",
                "author": "Winawer, J., Witthoft, N., Frank, M. C., Wu, L., "
                          "Wade, A. R., & Boroditsky, L.",
                "year": 2007,
                "title":
                "Russian blues reveal effects of language on color "
                "discrimination",
                "source":
                "Proceedings of the National Academy of Sciences, 104(19), "
                "7780–7785"
            },
            {
                "key": "hauser_2002",
                "author": "Hauser, M. D., Chomsky, N., & Fitch, W. T.",
                "year": 2002,
                "title":
                "The faculty of language: What is it, who has it, and how did "
                "it evolve?",
                "source": "Science, 298(5598), 1569–1579"
            },
            {
                "key": "pinker_jackendoff_2005",
                "author": "Pinker, S., & Jackendoff, R.",
                "year": 2005,
                "title":
                "The faculty of language: What's special about it?",
                "source": "Cognition, 95(2), 201–236"
            },
            {
                "key": "boroditsky_2001",
                "author": "Boroditsky, L.",
                "year": 2001,
                "title":
                "Does language shape thought? Mandarin and English speakers' "
                "conceptions of time",
                "source": "Cognitive Psychology, 43(1), 1–22"
            }
        ]
    },

    "Social Cognition": {

        "definition":
        "The machinery by which a mind builds working models of other minds — inferring what another person knows, wants, feels, and believes about you — from behaviour that never states any of it.",

        "narrative_role":
        "The internal narrative is not written alone. A large part of its material is second-hand: what you believe other people think of you, which is itself a guess you made and then filed as fact.",

        "paradox":
        "You have never once observed another mind, yet almost everything you believe about yourself was assembled out of what you assumed other minds were thinking.",

        "brain_regions": [
            "Temporoparietal Junction",
            "Medial Prefrontal Cortex",
            "Posterior Superior Temporal Sulcus",
            "Precuneus",
            "Temporal Poles"
        ],

        "key_experiments": [
            "The unexpected-transfer (false belief) task in young children",
            "Chimpanzee inference of an actor's goal",
            "Selective temporoparietal response to another's beliefs (fMRI)",
            "Perspective-taking versus asking, in accuracy of reading others",
            "Anticipatory-looking measures of implicit belief attribution, and their replication attempts"
        ],

        "landmark_researchers": [
            "David Premack",
            "Heinz Wimmer",
            "Josef Perner",
            "Uta Frith",
            "Chris Frith",
            "Rebecca Saxe",
            "Robin Dunbar",
            "Gregory Hickok"
        ],

        "connects_to": [
            "Identity",
            "Emotion",
            "Narrative",
            "Perception",
            "Language",
            "Memory"
        ],

        "real_world_examples": [
            "Replaying a conversation to work out what they meant",
            "Being certain someone is annoyed with you",
            "Misreading a short message as cold",
            "Rehearsing how you will be seen before you walk in",
            "Finding out you were never on their mind at all"
        ],

        "questions": [
            "How much of what I believe about myself came from someone else?",
            "When I read a room, what am I actually reading?",
            "How often am I wrong about what someone is thinking?",
            "Who am I when nobody is modelling me?"
        ],

        "unresolved":
        "Whether understanding another person is genuine inference about a hidden mind, or a very good prediction of behaviour that never touches the mind at all.",

        "interview_themes": [
            "Other people",
            "Belonging",
            "Judgement",
            "Loneliness",
            "Friendship",
            "Being misunderstood"
        ],

        "evidence": [
            {
                "type": "Comparative Study",
                "title": "Does the chimpanzee have a theory of mind?",
                "year": 1978
            },
            {
                "type": "Developmental Experiment",
                "title": "The unexpected-transfer false belief task",
                "year": 1983
            },
            {
                "type": "Neuroimaging",
                "title": "Temporoparietal junction and the attribution of belief",
                "year": 2003
            },
            {
                "type": "Review",
                "title": "The neural basis of mentalizing",
                "year": 2006
            },
            {
                "type": "Behavioural Experiment",
                "title": "Perspective mistaking",
                "year": 2018
            },
            {
                "type": "Replication Study",
                "title": "Systematic replication of implicit theory of mind",
                "year": 2018
            }
        ],

        "investigators_note":
        "This is the last file in the numbered sequence, and it closes the circle back to 001. The reason is uncomfortable. Every earlier case treats the self as something assembled inward — experience into memory, memory into narrative, narrative into identity. This file records that a substantial part of the raw material was never yours. It arrived as inference: your reading of what someone thought of you, formed from a face, a pause, a message with no punctuation, then stored as if it were reported speech. The research here is unusually honest about its own limits — the field's headline finding has been replicated for forty years in one form and has failed to replicate repeatedly in another, and its most famous mechanism is openly disputed. Treat any confident claim in this file, including the participant's confident claims about other people, as a hypothesis that was never tested against the mind it describes.",

        "primary_question":
        "When you understand another person, are you reading their mind — or predicting their behaviour and calling it understanding?",

        "why_it_matters":
        "The loop this exhibit follows runs experience → narrative → identity → decision → new experience. Social cognition inserts a second author into that loop. What you believe others believe about you becomes part of the story you tell yourself, and that story then shapes what you do next — including who you approach, avoid, and become. If the inference is systematically unreliable, then part of the self is built on evidence that was never checked.",

        "neural_systems": [
            {
                "system": "Temporoparietal junction (especially right)",
                "role": "Responds more strongly when a task requires representing what another person believes than when it requires other facts about that person — the closest thing the field has to a belief-specific region, though its selectivity is debated."
            },
            {
                "system": "Medial prefrontal cortex",
                "role": "Engaged when attributing mental states to others and, overlapping substantially, when reflecting on oneself — the anatomical hint that self-modelling and other-modelling share machinery."
            },
            {
                "system": "Posterior superior temporal sulcus",
                "role": "Tracks biological motion, gaze direction, and the intentional structure of observed action — the front end that turns movement into something that looks like a goal."
            },
            {
                "system": "Precuneus and temporal poles",
                "role": "Recruited alongside the mentalizing network; associated with retrieving social scripts, autobiographical context, and prior knowledge about the particular person being modelled."
            }
        ],

        "evidence_room": {
            "what_we_know": [
                {
                    "claim": "Typically developing children reliably pass an explicit false-belief test somewhere around their fourth or fifth year, and reliably fail it before. Shown a character who puts chocolate in one place and leaves while it is moved, younger children say he will look where the chocolate actually is; older children say he will look where he last saw it. The developmental shift itself is one of the most replicated findings in developmental psychology.",
                    "citation": "wimmer_perner_1983"
                },
                {
                    "claim": "Attributing mental states to other people engages a consistent, identifiable set of regions — medial prefrontal cortex, temporoparietal junction, posterior superior temporal sulcus, and temporal poles — across stories, cartoons, animations, and games. Whatever mentalizing is, it is not distributed evenly across the brain.",
                    "citation": "frith_frith_2006"
                }
            ],
            "evidence_suggests": [
                {
                    "claim": "Part of that network appears specifically tuned to the contents of another mind rather than to people in general. The temporoparietal junction responded more to passages describing what a character thought than to equally complex passages describing their appearance, their body, or physical events — suggesting a region recruited for belief as such.",
                    "citation": "saxe_kanwisher_2003"
                },
                {
                    "claim": "The capacity may have been built by group life. Across primates, the relative size of the neocortex tracks the typical size of the social group, which has been read as evidence that brains grew to manage relationships rather than to manage the physical world. The correlation is robust; the causal story it is used to tell is an interpretation.",
                    "citation": "dunbar_1998"
                },
                {
                    "claim": "Reading another person is inference, and the inference is frequently wrong. Across twenty-five experiments, deliberately taking someone's perspective did not improve accuracy about their thoughts, feelings, preferences, or the meaning of their expressions — and sometimes made it worse. What did improve accuracy was obtaining the other person's perspective directly: asking them.",
                    "citation": "eyal_2018"
                }
            ],
            "disagreement": [
                {
                    "claim": "The question that opened the field has never been closed. Premack and Woodruff asked whether a chimpanzee, shown an actor struggling with a problem, imputes purpose and knowledge to him, and coined the term 'theory of mind' to name the capacity. The commentary published alongside the paper argued that no behavioural result could distinguish genuine mental-state attribution from sophisticated prediction of behaviour — an objection still in force.",
                    "citation": "premack_woodruff_1978"
                },
                {
                    "claim": "Belief attribution has been reported to run automatically and early: seven-month-old infants, and adults' reaction times, appeared sensitive to an agent's belief about an object's location even when that belief was irrelevant to the task. The finding was read as evidence for an efficient, non-verbal mentalizing system operating beneath deliberate reasoning.",
                    "citation": "kovacs_2010"
                },
                {
                    "claim": "Those implicit measures have since proved fragile. Systematic replication attempts of anticipatory-looking paradigms across children and adults failed to reproduce the original belief-congruent effects, leaving the field genuinely split over whether implicit theory of mind is a real phenomenon, a much weaker one than reported, or an artefact of particular stimuli.",
                    "citation": "kulke_2018"
                },
                {
                    "claim": "The most popular proposed mechanism is contested. Mirror neurons — cells discharging both when an action is performed and when it is observed — were offered as a direct route to understanding others from the inside, and the account became widely influential.",
                    "citation": "rizzolatti_craighero_2004"
                },
                {
                    "claim": "That account was answered point by point: that the evidence does not establish mirror neurons as the basis of action understanding in monkeys or humans, that action understanding survives damage to the proposed system, and that the mapping runs in the wrong direction for the theory to work as stated. The dispute is unresolved and sits underneath most popular claims about empathy.",
                    "citation": "hickok_2009"
                }
            ],
            "unknown": [
                {
                    "claim": "It is unknown whether mentalizing involves representing another person's mental state at all, or whether it is a very good model of their behaviour that never refers to a mind. No behavioural or imaging result yet distinguishes the two, because both predict the same actions — and it is not clear what a decisive experiment would look like.",
                    "citation": "premack_woodruff_1978"
                },
                {
                    "claim": "How the network's activity relates to the everyday experience of understanding someone is UNKNOWN. The regions can be located reliably; that a region is more active when beliefs are involved does not say what operation it performs, nor why the operation feels from the inside like knowing what someone means.",
                    "citation": "saxe_kanwisher_2003"
                },
                {
                    "claim": "Whether self-modelling and other-modelling are one system or two is unresolved. They overlap anatomically and both recruit medial prefrontal cortex, but no method yet establishes whether you model yourself by the machinery built for reading others, read others by the machinery built for yourself, or run two processes that merely look alike from outside.",
                    "citation": "frith_frith_2006"
                },
                {
                    "claim": "How much of a person's self-concept is actually second-hand — imported from inferred judgements that were never verified with the people who supposedly held them — has no measure. There is no way at present to audit a belief about yourself back to the social inference that produced it.",
                    "citation": "eyal_2018"
                }
            ]
        },

        "open_questions": [
            {
                "question": "When you understand another person, are you reading a mind or predicting a body?",
                "what_science_knows": "Explicit belief attribution develops on a reliable timetable and recruits a consistent network of regions; damage and task manipulation disrupt it in structured ways.",
                "what_evidence_suggests": "Parts of that network — the temporoparietal junction in particular — respond to the contents of another mind more than to other facts about the same person, which looks like machinery for belief rather than for people.",
                "where_evidence_disagrees": "The objection raised in the paper that founded the field still stands: any behaviour explained by attributing a mental state can also be explained by a learned rule about behaviour, and the mirror-neuron account offered as a mechanism is itself openly disputed.",
                "what_remains_unknown": "No experiment has been devised that separates representing a mind from predicting the body it moves. Whether the distinction is empirical or merely verbal is UNKNOWN."
            },
            {
                "question": "How much of the self is made of other people's imagined opinions?",
                "what_science_knows": "Thinking about one's own traits and thinking about another person's mental states recruit overlapping medial prefrontal regions, and social inference is continuous and largely involuntary.",
                "what_evidence_suggests": "Inferences about what others think are frequently inaccurate, and effortful perspective-taking does not correct them — so the material imported into the self-story is unreliable at the point of entry, not merely with age.",
                "where_evidence_disagrees": "Whether self-knowledge and other-knowledge share one mechanism or two overlapping ones is argued from the same imaging data by both sides.",
                "what_remains_unknown": "There is no way to trace a given belief about yourself back to the social inference that produced it, so the proportion of the self that is second-hand is UNKNOWN."
            },
            {
                "question": "Is belief attribution something the mind does automatically, or only when it is asked to?",
                "what_science_knows": "Explicit, verbally tested false-belief understanding emerges around age four and is one of developmental psychology's most replicated results.",
                "what_evidence_suggests": "Looking-time and reaction-time measures once suggested that infants and adults track others' beliefs spontaneously, without instruction and without language.",
                "where_evidence_disagrees": "Systematic replication attempts of those implicit paradigms have largely failed, and the field is now split between researchers who treat implicit mentalizing as established and those who treat the original effects as unreplicable.",
                "what_remains_unknown": "Whether there is a fast, non-verbal belief-tracking system at all — and if so, what it computes — is currently UNKNOWN."
            }
        ],

        "connected_files": [
            "Identity",
            "Emotion",
            "Narrative",
            "Perception",
            "Language",
            "Memory"
        ],

        "next_case":
        "Memory",

        "citations": [
            {
                "key": "premack_woodruff_1978",
                "author": "Premack, D., & Woodruff, G.",
                "year": 1978,
                "title": "Does the chimpanzee have a theory of mind?",
                "source": "Behavioral and Brain Sciences, 1(4), 515–526"
            },
            {
                "key": "wimmer_perner_1983",
                "author": "Wimmer, H., & Perner, J.",
                "year": 1983,
                "title": "Beliefs about beliefs: Representation and constraining function of wrong beliefs in young children's understanding of deception",
                "source": "Cognition, 13(1), 103–128"
            },
            {
                "key": "saxe_kanwisher_2003",
                "author": "Saxe, R., & Kanwisher, N.",
                "year": 2003,
                "title": "People thinking about thinking people: The role of the temporo-parietal junction in \"theory of mind\"",
                "source": "NeuroImage, 19(4), 1835–1842"
            },
            {
                "key": "frith_frith_2006",
                "author": "Frith, C. D., & Frith, U.",
                "year": 2006,
                "title": "The neural basis of mentalizing",
                "source": "Neuron, 50(4), 531–534"
            },
            {
                "key": "dunbar_1998",
                "author": "Dunbar, R. I. M.",
                "year": 1998,
                "title": "The social brain hypothesis",
                "source": "Evolutionary Anthropology: Issues, News, and Reviews, 6(5), 178–190"
            },
            {
                "key": "eyal_2018",
                "author": "Eyal, T., Steffel, M., & Epley, N.",
                "year": 2018,
                "title": "Perspective mistaking: Accurately understanding the mind of another requires getting perspective, not taking perspective",
                "source": "Journal of Personality and Social Psychology, 114(4), 547–571"
            },
            {
                "key": "rizzolatti_craighero_2004",
                "author": "Rizzolatti, G., & Craighero, L.",
                "year": 2004,
                "title": "The mirror-neuron system",
                "source": "Annual Review of Neuroscience, 27, 169–192"
            },
            {
                "key": "hickok_2009",
                "author": "Hickok, G.",
                "year": 2009,
                "title": "Eight problems for the mirror neuron theory of action understanding in monkeys and humans",
                "source": "Journal of Cognitive Neuroscience, 21(7), 1229–1243"
            },
            {
                "key": "kovacs_2010",
                "author": "Kovács, Á. M., Téglás, E., & Endress, A. D.",
                "year": 2010,
                "title": "The social sense: Susceptibility to others' beliefs in human infants and adults",
                "source": "Science, 330(6012), 1830–1834"
            },
            {
                "key": "kulke_2018",
                "author": "Kulke, L., von Duhn, B., Schneider, D., & Rakoczy, H.",
                "year": 2018,
                "title": "Is implicit theory of mind a real and robust phenomenon? Results from a systematic replication study",
                "source": "Psychological Science, 29(6), 888–900"
            }
        ],
    },

    "Motivation": {

        "definition":
        "The set of processes that decide what a person pursues, how hard they pursue it, and how long they keep going after the pleasure has gone.",

        "narrative_role":
        "Motivation is where the internal narrative is put to the test: the story supplies the reason, but something older and quieter supplies the push — and the two are not always talking about the same thing.",

        "paradox":
        "Wanting something and enjoying it are produced by different machinery, so it is entirely possible to chase what you no longer like.",

        "brain_regions": [
            "Nucleus Accumbens",
            "Ventral Tegmental Area",
            "Ventral Pallidum",
            "Orbitofrontal Cortex",
            "Anterior Cingulate Cortex"
        ],

        "key_experiments": [
            "Dopamine depletion and effort-based choice in rodents",
            "Incentive-salience ('wanting' vs. 'liking') hedonic reaction tests",
            "Reward-prediction-error recordings in midbrain dopamine neurons",
            "Externally mediated reward and free-choice persistence (the puzzle studies)",
            "Meta-analyses of tangible reward and intrinsic motivation",
            "Verbal reports of the causes of one's own preferences"
        ],

        "landmark_researchers": [
            "Kent Berridge",
            "Terry Robinson",
            "Wolfram Schultz",
            "Edward Deci",
            "Richard Ryan",
            "John Salamone",
            "Richard Nisbett"
        ],

        "connects_to": [
            "Decision Making",
            "Emotion",
            "Habit",
            "Learning",
            "Prediction",
            "Identity"
        ],

        "real_world_examples": [
            "Wanting something you know you will not enjoy",
            "Losing interest in a hobby once you are paid for it",
            "Scrolling long past the point of pleasure",
            "Finishing a thing only because it was started",
            "Explaining an ambition you cannot trace the origin of"
        ],

        "questions": [
            "Do I want this, or do I only want to have wanted it?",
            "Where does a want begin, if not in a reason?",
            "If nothing were watching, what would I still do?"
        ],

        "unresolved":
        "Whether the reasons people give for what they pursue play any causal part in the pursuing, or are assembled afterwards to explain it.",

        "interview_themes": [
            "Ambition",
            "Desire",
            "Drive",
            "Wanting",
            "Reward",
            "Effort",
            "Purpose"
        ],

        "evidence": [
            {
                "type": "Review",
                "title": "Incentive salience: wanting separated from liking",
                "year": 1998
            },
            {
                "type": "Electrophysiology",
                "title": "Reward prediction error in dopamine neurons",
                "year": 1997
            },
            {
                "type": "Behavioral Experiment",
                "title": "Externally mediated reward and intrinsic motivation",
                "year": 1971
            },
            {
                "type": "Meta-Analysis",
                "title": "Extrinsic rewards and intrinsic motivation — two opposed syntheses",
                "year": 1999
            },
            {
                "type": "Review",
                "title": "Mesolimbic dopamine and the willingness to work",
                "year": 2012
            },
            {
                "type": "Review",
                "title": "Verbal reports on mental processes",
                "year": 1977
            }
        ],

        "investigators_note":
        "This file was opened expecting to find the engine of the story and found instead that the story arrives late. Two things in the record are not seriously disputed: that the system which makes a thing attractive is separable from the system which makes it pleasant, and that people asked why they wanted something will answer fluently and confidently whether or not they have access to the answer. Put those together and the shape of the problem appears. A participant says they are driven by a childhood promise, a debt, a person they are trying to become — and the account may be entirely sincere and still be a reconstruction laid over machinery that was never verbal. Nothing here says the reasons are false. It says the reasons are testimony, not mechanism, and this investigation should stop treating the two as the same document.",

        "primary_question":
        "Do the reasons people give for what they pursue actually move them, or are those reasons written afterwards to explain a pull that came from somewhere else?",

        "why_it_matters":
        "The central loop of this investigation runs experience → memory and narrative → identity → decisions → new experience. Motivation is the joint where narrative is supposed to become action, and it is the joint where the evidence is thinnest. If wanting can run without liking, and if the explanation for a want can be assembled after the fact, then a person can spend years pursuing something the story says they chose and the machinery never asked about — and can rebuild the story again each time the pursuit changes, without ever noticing which one is leading.",

        "neural_systems": [
            {
                "system": "Mesolimbic dopamine projection (ventral tegmental area to nucleus accumbens)",
                "role": "Implicated in the vigour and persistence of reward-seeking and in the willingness to pay an effort cost — rather than in the pleasure obtained when the reward arrives."
            },
            {
                "system": "Midbrain dopamine neurons as an error signal",
                "role": "Fire to outcomes better than predicted and pause to outcomes worse than predicted, providing a teaching signal that shifts over training from the reward itself to whatever reliably precedes it."
            },
            {
                "system": "Hedonic hotspots in nucleus accumbens shell and ventral pallidum",
                "role": "Small opioid- and endocannabinoid-sensitive sites that amplify the hedonic impact of a reward — anatomically far more restricted than the systems governing how hard an animal will work for it."
            },
            {
                "system": "Orbitofrontal and anterior cingulate cortex",
                "role": "Associated with representing the current value of an outcome and with weighing effort against expected gain when deciding whether a pursuit is worth continuing."
            }
        ],

        "evidence_room": {
            "what_we_know": [
                {
                    "claim": "Wanting and liking are dissociable. Manipulations that sharply reduce dopamine function can leave the orofacial hedonic reactions to a sweet taste intact while collapsing the pursuit of it, and manipulations that amplify dopamine can raise pursuit without raising the hedonic reaction — evidence that the attractiveness of a reward (incentive salience) and the pleasure of consuming it are produced by overlapping but separable systems.",
                    "citation": "berridge_robinson_1998"
                },
                {
                    "claim": "Midbrain dopamine neurons do not simply report reward. They fire to rewards that are better than predicted, fall silent for rewards exactly as predicted, and dip below baseline when a predicted reward fails to arrive — the signature of a prediction error, and over training the response transfers backwards from the reward to the cue that reliably announces it.",
                    "citation": "schultz_1997"
                },
                {
                    "claim": "People report the causes of their own preferences and choices confidently and often wrongly. Across a range of studies, participants influenced by a factor they were demonstrably sensitive to denied its influence, and cited plausible causes that had none — indicating that introspective reports of why one wanted something draw on commonsense theories about what ought to have mattered, not on privileged access to the process.",
                    "citation": "nisbett_wilson_1977"
                }
            ],
            "evidence_suggests": [
                {
                    "claim": "Mesolimbic dopamine looks less like a pleasure signal and more like a signal governing the exertion of effort. Animals with reduced accumbens dopamine still prefer the richer reward and still consume it readily, but stop paying a high work cost to obtain it and shift to whatever is freely available — suggesting the system sets how much effort a goal is worth rather than how good it feels.",
                    "citation": "salamone_correa_2012"
                },
                {
                    "claim": "Paying someone for something they already did willingly can reduce how much they do it once the payment stops. Participants paid for solving puzzles spent less of a subsequent unobserved free-choice period on them than unpaid participants — the first experimental demonstration that an external reward can displace, rather than add to, an existing internal reason.",
                    "citation": "deci_1971"
                },
                {
                    "claim": "The narrative account of a want and the machinery of the want can come apart in the same person at the same moment. Where introspective reports are accurate, this appears to be because the person's commonsense theory of what should have influenced them happened to be correct — accuracy without access, which is a much weaker result than it looks.",
                    "citation": "nisbett_wilson_1977"
                }
            ],
            "disagreement": [
                {
                    "claim": "A large meta-analysis concluded that tangible rewards reliably undermine intrinsic motivation — particularly expected rewards contingent on doing, completing, or performing a task well — and that the effect is robust enough to be a genuine risk in classrooms and workplaces.",
                    "citation": "deci_koestner_ryan_1999"
                },
                {
                    "claim": "An earlier meta-analysis of a broadly overlapping literature reached close to the opposite conclusion: that reinforcement does not generally harm intrinsic motivation, that verbal praise increases it, and that the apparent undermining effect is narrow and partly an artefact of how studies were selected and pooled. Both syntheses are competent, both are cited, and the dispute over coding decisions and moderators has never fully closed.",
                    "citation": "cameron_pierce_1994"
                },
                {
                    "claim": "What dopamine actually encodes remains argued. Prediction-error accounts, incentive-salience accounts, and effort-and-activation accounts each explain large parts of the data and disagree about what the signal is for; the popular reading of dopamine as the brain's pleasure chemical is rejected by researchers on all sides of that argument.",
                    "citation": "salamone_correa_2012"
                }
            ],
            "unknown": [
                {
                    "claim": "It is unknown whether a stated reason for a pursuit has any causal role in that pursuit. The reasons can be recorded, and the machinery can be measured, but no method exists for showing that a particular verbal reason was the thing that moved a particular person on a particular day. The record on this reads UNKNOWN.",
                    "citation": "nisbett_wilson_1977"
                },
                {
                    "claim": "Why a want survives the loss of the liking is not understood. That incentive salience can be attached to something that no longer gives pleasure is well documented; what determines which pursuits detach in this way, in which people, and whether they can be re-coupled, is not.",
                    "citation": "berridge_robinson_1998"
                },
                {
                    "claim": "How an internal reason is represented in the brain at all is unknown. Prediction errors, effort costs, and hedonic impact are all measurable; a value that a person holds — the thing an interview answer is reaching for — has no established neural description, so the step from narrative to motivation cannot currently be traced in tissue.",
                    "citation": "schultz_1997"
                }
            ]
        },

        "open_questions": [
            {
                "question": "Is wanting something the same as liking it?",
                "what_science_knows": "Pursuit and pleasure can be separated experimentally: the hedonic reaction to a reward and the effort spent obtaining it respond differently to the same neurochemical manipulations, and the anatomy supporting hedonic impact is far more restricted than the anatomy supporting pursuit.",
                "what_evidence_suggests": "Mesolimbic dopamine appears to govern how much effort a goal is worth rather than how good it feels, which would explain pursuits that continue long after the enjoyment has gone.",
                "where_evidence_disagrees": "Whether that signal is best described as prediction error, incentive salience, or effort-related activation is an open argument between accounts that each capture much of the data.",
                "what_remains_unknown": "What determines whether a given want detaches from its liking in a given person — and whether the two can be deliberately re-coupled — is UNKNOWN."
            },
            {
                "question": "Do the reasons people give for their ambitions cause them?",
                "what_science_knows": "Verbal reports about the causes of one's own preferences are frequently inaccurate in demonstrable, repeatable ways: people deny influences they were measurably subject to and name causes that had no effect.",
                "what_evidence_suggests": "Such reports appear to be generated from plausible theories about what should have mattered rather than from access to the process itself — the explanation is constructed after the behaviour, in the same way a narrative is constructed after an experience.",
                "where_evidence_disagrees": "How far this generalises from laboratory judgements to long-running life projects is contested; deliberate, effortful goals may be better introspected than snap preferences, and no clean test separates the two.",
                "what_remains_unknown": "Whether a sincere, well-examined reason ever does part of the causal work is UNKNOWN. It cannot currently be measured without asking, and asking is the unreliable instrument."
            },
            {
                "question": "Can paying someone for something take away their reason for doing it?",
                "what_science_knows": "Adding an expected, contingent external reward to an activity someone already performed freely can reduce the time they spend on it afterwards when nobody is measuring and no reward is on offer.",
                "what_evidence_suggests": "The undermining appears strongest for rewards that are expected, tangible, and contingent on doing or completing the task, and weakest or absent for unexpected rewards and verbal praise.",
                "where_evidence_disagrees": "Two large meta-analyses of overlapping literatures reached opposed conclusions about whether the effect is general or narrow, and the argument over how studies were coded and pooled has never been settled.",
                "what_remains_unknown": "What is actually lost when an internal reason is displaced — whether the want itself weakens, the story about the want changes, or only the behaviour outside the reward — is UNKNOWN."
            }
        ],

        "connected_files": [
            "Decision Making",
            "Prediction",
            "Habit",
            "Emotion",
            "Learning",
            "Identity",
            "Narrative"
        ],

        "next_case":
        "Social Cognition",

        "citations": [
            {
                "key": "berridge_robinson_1998",
                "author": "Berridge, K. C., & Robinson, T. E.",
                "year": 1998,
                "title": "What is the role of dopamine in reward: hedonic impact, reward learning, or incentive salience?",
                "source": "Brain Research Reviews, 28(3), 309–369"
            },
            {
                "key": "schultz_1997",
                "author": "Schultz, W., Dayan, P., & Montague, P. R.",
                "year": 1997,
                "title": "A neural substrate of prediction and reward",
                "source": "Science, 275(5306), 1593–1599"
            },
            {
                "key": "salamone_correa_2012",
                "author": "Salamone, J. D., & Correa, M.",
                "year": 2012,
                "title": "The mysterious motivational functions of mesolimbic dopamine",
                "source": "Neuron, 76(3), 470–485"
            },
            {
                "key": "deci_1971",
                "author": "Deci, E. L.",
                "year": 1971,
                "title": "Effects of externally mediated rewards on intrinsic motivation",
                "source": "Journal of Personality and Social Psychology, 18(1), 105–115"
            },
            {
                "key": "deci_koestner_ryan_1999",
                "author": "Deci, E. L., Koestner, R., & Ryan, R. M.",
                "year": 1999,
                "title": "A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation",
                "source": "Psychological Bulletin, 125(6), 627–668"
            },
            {
                "key": "cameron_pierce_1994",
                "author": "Cameron, J., & Pierce, W. D.",
                "year": 1994,
                "title": "Reinforcement, reward, and intrinsic motivation: A meta-analysis",
                "source": "Review of Educational Research, 64(3), 363–423"
            },
            {
                "key": "nisbett_wilson_1977",
                "author": "Nisbett, R. E., & Wilson, T. D.",
                "year": 1977,
                "title": "Telling more than we can know: Verbal reports on mental processes",
                "source": "Psychological Review, 84(3), 231–259"
            }
        ],
    },

    "Prediction": {

        "definition":
        "The brain's continuous generation of expectations about what will "
        "happen next, and its use of the resulting errors to update itself.",

        "narrative_role":
        "Prediction is why the future has a texture before it arrives — and "
        "why being wrong is what changes a person.",

        "paradox":
        "The brain works hardest on what it did not expect, yet what you "
        "experience is mostly what it expected.",

        "brain_regions": [
            "Midbrain Dopamine Neurons",
            "Primary Visual Cortex",
            "Cerebellum",
            "Anterior Insula"
        ],

        "key_experiments": [
            "Reward-prediction-error recordings in dopamine neurons",
            "Predictive coding models of extra-classical receptive fields",
            "Expectation-sharpening in V1 (fMRI)",
            "Free-energy formulations of brain function"
        ],

        "landmark_researchers": [
            "Wolfram Schultz",
            "Rajesh Rao",
            "Karl Friston",
            "Floris de Lange"
        ],

        "connects_to": [
            "Perception",
            "Learning",
            "Emotion",
            "Decision Making"
        ],

        "real_world_examples": [
            "Flinching before impact",
            "Placebo effects",
            "The last step that is not there",
            "Anxiety about an outcome that never comes"
        ],

        "questions": [
            "Why does surprise feel physical?",
            "Am I seeing the world or my model of it?",
            "Why does expecting pain make it hurt more?"
        ],

        "unresolved":
        "Is prediction one principle the whole brain runs on, or a useful "
        "metaphor stretched across unrelated mechanisms?",

        "interview_themes": [
            "Expectations",
            "Surprise",
            "Anticipation",
            "Uncertainty"
        ],

        "evidence": [
            {"type": "Single-unit Recording", "title": "Dopamine reward prediction error", "year": 1997},
            {"type": "Computational Model", "title": "Hierarchical predictive coding", "year": 1999},
            {"type": "Neuroimaging", "title": "Expectation sharpens V1 representations", "year": 2012},
            {"type": "Theoretical Review", "title": "The free-energy principle", "year": 2010}
        ],

        "investigators_note":
        "This file was opened late and immediately began pulling on the "
        "others. If the brain is fundamentally a prediction machine, then "
        "perception is a controlled hallucination corrected by error, "
        "learning is error made permanent, and emotion is the body's report "
        "on how the prediction is going. That is either the unifying finding "
        "of modern neuroscience or the most seductive over-generalisation in "
        "it. The investigation does not yet know which.",

        "primary_question":
        "Is experience the arrival of the world, or the brain's best guess "
        "corrected by it?",

        "why_it_matters":
        "If perception is prediction, then expectation is not a bias to be "
        "corrected but the substance of experience itself. That reframes "
        "placebo, chronic pain, anxiety, and prejudice as the same "
        "computational problem seen from different angles.",

        "neural_systems": [
            {
                "system": "Midbrain dopamine neurons",
                "role":
                "Signal the difference between predicted and received reward, "
                "and transfer their response to the earliest reliable "
                "predictor of that reward."
            },
            {
                "system": "Cortical feedback connections",
                "role":
                "Carry predictions downward in the hierarchy; feedforward "
                "connections are proposed to carry only the residual error."
            },
            {
                "system": "Primary visual cortex",
                "role":
                "Responds less overall but more sharply and specifically to "
                "expected stimuli — the signature predicted by "
                "error-based accounts."
            }
        ],

        "evidence_room": {

            "what_we_know": [
                {
                    "claim":
                    "The brain contains an explicit prediction-error signal. "
                    "Dopamine neurons fire to unexpected reward, stop firing "
                    "to the reward once a predictive cue is learned, and are "
                    "suppressed below baseline when an expected reward fails "
                    "to arrive — the exact profile of a temporal-difference "
                    "error term.",
                    "citation": "schultz_1997"
                }
            ],

            "evidence_suggests": [
                {
                    "claim":
                    "Visual cortex behaves as if it were computing prediction "
                    "error. A hierarchical model in which higher areas predict "
                    "lower-level activity and only the residual is passed "
                    "upward reproduces extra-classical receptive-field "
                    "effects that classical feedforward models cannot.",
                    "citation": "rao_ballard_1999"
                },
                {
                    "claim":
                    "Expectation does not merely add signal — it sharpens it. "
                    "Expected gratings produced a smaller overall response in "
                    "primary visual cortex yet one from which orientation "
                    "could be decoded more accurately: less activity, better "
                    "representation.",
                    "citation": "kok_2012"
                }
            ],

            "disagreement": [
                {
                    "claim":
                    "The free-energy principle proposes that perception, "
                    "action, and learning are all the minimisation of a single "
                    "quantity — surprise about sensory input. Whether this is "
                    "a genuine unifying theory or an unfalsifiable framework "
                    "that can accommodate any result is one of the most "
                    "openly argued questions in theoretical neuroscience.",
                    "citation": "friston_2010"
                },
                {
                    "claim":
                    "Whether reduced neural responses to expected stimuli "
                    "reflect prediction error, sharpening of a representation, "
                    "or simple adaptation and repetition suppression is not "
                    "settled; the same data support competing readings.",
                    "citation": "kok_2012"
                }
            ],

            "unknown": [
                {
                    "claim":
                    "How the brain sets the confidence it assigns to a "
                    "prediction — the weighting that decides whether an error "
                    "revises the model or is dismissed as noise — is not "
                    "understood.",
                    "citation": "friston_2010"
                },
                {
                    "claim":
                    "Whether the same predictive machinery that explains "
                    "reward learning also explains perception, or whether the "
                    "resemblance is a shared mathematics over different "
                    "biology, is unknown.",
                    "citation": "rao_ballard_1999"
                }
            ]
        },

        "open_questions": [
            {
                "question":
                "Is the brain fundamentally a prediction machine?",
                "what_science_knows":
                "At least one explicit prediction-error signal exists in the "
                "brain and drives reward learning.",
                "what_evidence_suggests":
                "Sensory cortex behaves in ways predictive-coding models "
                "anticipate, including responding less but more informatively "
                "to expected input.",
                "where_evidence_disagrees":
                "Whether prediction is a unifying principle or an appealing "
                "metaphor applied across unrelated mechanisms is actively "
                "contested, and the strongest versions of the theory are "
                "criticised as unfalsifiable.",
                "what_remains_unknown":
                "No experiment currently distinguishes a brain that predicts "
                "from a brain that merely behaves as if it does."
            },
            {
                "question":
                "Why does expectation change what is felt?",
                "what_science_knows":
                "Expectation measurably alters neural responses to identical "
                "physical stimuli.",
                "what_evidence_suggests":
                "Experience appears to be weighted toward the prior model, "
                "with sensory input acting as correction rather than content.",
                "where_evidence_disagrees":
                "How much of an experience is prior and how much is input — "
                "and whether that ratio is fixed — is disputed.",
                "what_remains_unknown":
                "The mechanism by which a belief about a stimulus becomes part "
                "of the felt stimulus is UNKNOWN."
            }
        ],

        "connected_files": [
            "Perception",
            "Learning",
            "Emotion",
            "Decision Making"
        ],

        "next_case": "Language",

        "citations": [
            {
                "key": "schultz_1997",
                "author": "Schultz, W., Dayan, P., & Montague, P. R.",
                "year": 1997,
                "title": "A neural substrate of prediction and reward",
                "source": "Science, 275(5306), 1593–1599"
            },
            {
                "key": "rao_ballard_1999",
                "author": "Rao, R. P. N., & Ballard, D. H.",
                "year": 1999,
                "title":
                "Predictive coding in the visual cortex: A functional "
                "interpretation of some extra-classical receptive-field "
                "effects",
                "source": "Nature Neuroscience, 2(1), 79–87"
            },
            {
                "key": "kok_2012",
                "author": "Kok, P., Jehee, J. F. M., & de Lange, F. P.",
                "year": 2012,
                "title":
                "Less is more: Expectation sharpens representations in the "
                "primary visual cortex",
                "source": "Neuron, 75(2), 265–270"
            },
            {
                "key": "friston_2010",
                "author": "Friston, K.",
                "year": 2010,
                "title": "The free-energy principle: A unified brain theory?",
                "source": "Nature Reviews Neuroscience, 11(2), 127–138"
            }
        ]
    },

    "Narrative": {
        "definition": "",
        "narrative_role": "",
        "paradox": "",
        "brain_regions": [],
        "key_experiments": [],
        "landmark_researchers": [],
        "connects_to": [],
        "real_world_examples": [],
        "questions": [],
        "unresolved": "",
        "interview_themes": []
    }

}


# ==========================================================
# Functions
# ==========================================================

def show_concept(name):
    """Display information about a concept."""

    if name not in concepts:
        print("Concept not found.")
        return

    concept = concepts[name]

    print("\n" + "=" * 60)
    print(name.upper())
    print("=" * 60)

    print("\nDefinition:")
    print(concept["definition"])

    print("\nNarrative Role:")
    print(concept["narrative_role"])

    print("\nParadox:")
    print(concept["paradox"])

    print("\nBrain Regions:")
    for region in concept["brain_regions"]:
        print(f"• {region}")

    print("\nKey Experiments:")
    for experiment in concept["key_experiments"]:
        print(f"• {experiment}")

    print("\nLandmark Researchers:")
    for researcher in concept["landmark_researchers"]:
        print(f"• {researcher}")

    print("\nConnects To:")
    for item in concept["connects_to"]:
        print(f"• {item}")

    print("\nReal World Examples:")
    for example in concept["real_world_examples"]:
        print(f"• {example}")

    print("\nQuestions:")
    for question in concept["questions"]:
        print(f"• {question}")

    print("\nWhat We Still Don't Know:")
    print(concept["unresolved"])

    print("\nInterview Themes:")
    for theme in concept["interview_themes"]:
        print(f"• {theme}")


def get_connections(concept_name):
    """Return all concepts connected to the selected concept."""

    if concept_name not in concepts:
        return None

    return concepts[concept_name]["connects_to"]


def explore(concept_name):
    """Explore a concept and its immediate connections."""

    show_concept(concept_name)

    print("\nExplore Next:\n")

    connections = get_connections(concept_name)

    if connections:
        for connection in connections:
            print(f"→ {connection}")

if __name__ == "__main__":
    explore("Memory")