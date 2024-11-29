import csv

CANDIDATE_FILE = "data/listas.csv"

def read_candidates():
    """Read candidates from the CSV file."""
    candidates = []
    with open(CANDIDATE_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        candidates = [row for row in reader]
    return candidates

def write_candidates(candidates):
    """Write candidates back to the CSV file."""
    with open(CANDIDATE_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["idLista", "nome", "orgao", "nomeElementos", "status"])
        writer.writeheader()
        writer.writerows(candidates)

def add_candidate():
    """Add a new candidate list."""
    candidates = read_candidates()
    id_lista = len(candidates) + 1
    nome = input("Enter the candidate list name: ")
    orgao = input("Enter the body (e.g., Council, Assembly): ")
    nomeElementos = input("Enter the names of list members (comma-separated): ")
    candidates.append({"idLista": id_lista, "nome": nome, "orgao": orgao, "nomeElementos": nomeElementos, "status": "Pending"})
    write_candidates(candidates)
    print(f"Candidate list '{nome}' added successfully!")

def remove_candidate():
    """Remove an existing candidate list."""
    candidates = read_candidates()
    id_lista = input("Enter the ID of the list to remove: ")
    candidates = [c for c in candidates if c["idLista"] != id_lista]
    write_candidates(candidates)
    print(f"Candidate list with ID {id_lista} removed successfully!")

def manage_candidates():
    """Candidate management menu."""
    while True:
        print("\n--- Manage Candidates ---")
        print("1. Add Candidate")
        print("2. Remove Candidate")
        print("3. View All Candidates")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            add_candidate()
        elif choice == "2":
            remove_candidate()
        elif choice == "3":
            candidates = read_candidates()
            for c in candidates:
                print(f"ID: {c['idLista']}, Name: {c['nome']}, Body: {c['orgao']}, Status: {c['status']}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
