import json
import os

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "participants.json")


def load_interviews():
    """Return every saved interview as a list (empty if none/corrupt).

    Shared by the CLI and the web app so there is a single source of truth
    for the archive."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_interview(interview_data):

    interviews = []

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            try:

                interviews = json.load(file)

            except json.JSONDecodeError:

                interviews = []

    interviews.append(interview_data)

    with open(FILE_NAME, "w") as file:

        json.dump(interviews, file, indent=4)

    print("\nInterview successfully saved.")


def view_interviews():

    if not os.path.exists(FILE_NAME):

        print("\nNo interviews found.")

        return

    with open(FILE_NAME, "r") as file:

        try:

            interviews = json.load(file)

        except json.JSONDecodeError:

            interviews = []

    if len(interviews) == 0:

        print("\nNo interviews found.")

        return

    print("\n" + "=" * 70)
    print("NESCIENCE ARCHIVE")
    print("=" * 70)

    for number, interview in enumerate(interviews, start=1):

        print(f"\nCASE {number:03}")

        print("-" * 70)

        for module, responses in interview.items():

            print(f"\n{module}")

            for question, answer in responses.items():

                print(f"\n{question}")

                print(answer)

        print("\n" + "=" * 70)