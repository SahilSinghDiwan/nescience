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
    },

    "Social Cognition": {
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
    },

    "Motivation": {
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

        "next_case": "Memory",

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