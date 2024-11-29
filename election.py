import csv

ELECTION_FILE = "data/eleicao.csv"

def create_election():
    """Create a new election."""
    elections = read_elections()
    id_election = len(elections) + 1
    data_inicio = input("Enter the start date (YYYY-MM-DD): ").strip()
    data_fim = input("Enter the end date (YYYY-MM-DD): ").strip()
    metodo = input("Enter the election method (e.g., D'Hondt, majority): ").strip()
    regras = input("Enter admission rules (comma-separated): ").strip()
    elections.append({
        "idEleicao": id_election,
        "dataInicio": data_inicio,
        "dataFim": data_fim,
        "metodo": metodo,
        "regras": regras
    })
    write_elections(elections)
    print(f"Election {id_election} created successfully!")

def read_elections():
    """Read elections from the CSV file."""
    elections = []
    with open(ELECTION_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        elections = [row for row in reader]
    return elections




def write_elections(elections):
    """Write elections to the CSV file."""
    with open(ELECTION_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["idEleicao", "dataInicio", "dataFim", "metodo", "regras"])
        writer.writeheader()
        writer.writerows(elections)

def manage_elections():
    """Election management menu."""
    while True:
        print("\n--- Manage Elections ---")
        print("1. Create Election")
        print("2. View Elections")
        print("3. Back to Main Menu")
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            create_election()
        elif choice == "2":
            elections = read_elections()
            for e in elections:
                print(f"ID: {e['idEleicao']}, Start: {e['dataInicio']}, End: {e['dataFim']}, Method: {e['metodo']}, Rules: {e['regras']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
