import interview
print(interview.__file__)
import database


def menu():

    while True:

        print("\n" + "=" * 60)
        print("                     NESCIENCE")
        print("=" * 60)

        print("\nThe Study of What We Do Not Yet Know\n")

        print("1. Begin Investigation")
        print("2. View Archive")
        print("3. Exit")

        print("\n" + "=" * 60)

        choice = input("\nSelect an option: ")

        if choice == "1":

            interview_data = interview.run_interview()

            database.save_interview(interview_data)

            print("\nInterview successfully saved.")

        elif choice == "2":

            database.view_interviews()

        elif choice == "3":

            print("\nInvestigation closed.")

            break

        else:

            print("\nInvalid option. Please try again.")


if __name__ == "__main__":

    menu()