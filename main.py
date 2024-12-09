from candidate import manage_candidates
from election import manage_elections
from voting import handle_voting
from reports import generate_reports
from eleitores import manage_electors  # Importa o módulo de eleitores

def display_menu():
    print("\n--- Election Management System ---")
    print("1. Manage Candidates")
    print("2. Manage Elections")
    print("3. Voting")
    print("4. Generate Reports")
    print("5. Manage Electors")  # Adiciona a opção para gerenciar eleitores
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()  # Atualiza para 6 opções
        if choice == "1":
            manage_candidates()
        elif choice == "2":
            manage_elections()
        elif choice == "3":
            handle_voting()
        elif choice == "4":
            generate_reports()
        elif choice == "5":
            manage_electors()  # Chama a função de gerenciar eleitores
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again please.")

if __name__ == "__main__":
    main()
