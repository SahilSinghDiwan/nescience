from protocol import INTERVIEW_PROTOCOL


def run_interview():

    print("\n" + "=" * 70)
    print("NESCIENCE")
    print("=" * 70)

    intro = INTERVIEW_PROTOCOL["Introduction"]

    print("\n" + intro["title"])
    print()
    print(intro["question"])
    print()
    print(intro["message"])

    input("\nPress ENTER to begin the investigation...")

    interview = {}

    # ---------- Participant Information ----------

    print("\n" + "=" * 70)
    print("PARTICIPANT INFORMATION")
    print("=" * 70)

    participant = {}

    for item in INTERVIEW_PROTOCOL["Participant Information"]:

        participant[item] = input(f"{item}: ")

    interview["Participant Information"] = participant

    # ---------- Interview ----------

    question_number = 1

    for module, questions in INTERVIEW_PROTOCOL.items():

        if module in ("Introduction", "Participant Information"):
            continue

        print("\n" + "=" * 70)
        print(module.upper())
        print("=" * 70)

        interview[module] = {}

        for question in questions:

            print(f"\nQuestion {question_number}")
            print("-" * 40)
            print(question)

            answer = input("\n> ")

            interview[module][f"Question {question_number}"] = answer

            question_number += 1

    return interview