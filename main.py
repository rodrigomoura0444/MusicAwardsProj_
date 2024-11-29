from candidate import manage_candidates
from election import manage_elections
from voting import handle_voting
from reports import generate_reports

def display_menu():
    print("\n--- Election Management System ---")
    print("1. Manage Candidates")
    print("2. Manage Elections")
    print("3. Voting")
    print("4. Generate Reports")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            manage_candidates()
        elif choice == "2":
            manage_elections()
        elif choice == "3":
            handle_voting()
        elif choice == "4":
            generate_reports()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
