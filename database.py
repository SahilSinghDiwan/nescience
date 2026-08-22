import json
import os

# Collected testimony is personal (brief §11a), so where it is written has to
# be movable: in the container it belongs on a mounted volume, never in an
# image layer. NESCIENCE_DATA_DIR overrides the location; unset, it stays
# exactly where it has always been, beside the code.
_DATA_DIR = os.environ.get("NESCIENCE_DATA_DIR") or os.path.dirname(
    os.path.abspath(__file__)
)
FILE_NAME = os.path.join(_DATA_DIR, "participants.json")


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