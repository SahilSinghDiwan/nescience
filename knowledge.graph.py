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
        ]
    },



    # ==================================================
    # Templates for future concepts
    # ==================================================

    "Decision Making": {
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

    "Attention": {
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

    "Learning": {
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

    "Perception": {
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

    "Consciousness": {
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