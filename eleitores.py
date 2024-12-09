import csv
import os

ELECTOR_FILE = "data/eleitores.csv"

def read_electors():
    """Read electors from the CSV file."""
    electors = []
    # Verifica se o arquivo existe e cria se necessário
    if not os.path.exists(ELECTOR_FILE):
        with open(ELECTOR_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["idEleitor", "nome", "nif", "cidade", "concelho", "distrito"])
            writer.writeheader()  # Cria o cabeçalho
    else:
        with open(ELECTOR_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            electors = [row for row in reader]
    return electors

def write_electors(electors):
    """Write electors back to the CSV file."""
    with open(ELECTOR_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["idEleitor", "nome", "nif", "cidade", "concelho", "distrito"])
        writer.writeheader()
        writer.writerows(electors)

def add_elector():
    """Add a new elector."""
    electors = read_electors()
    id_eleitor = len(electors) + 1  # ID será o próximo número disponível
    nome = input("Enter the elector's name: ").strip()
    nif = input("Enter the elector's NIF: ").strip()
    cidade = input("Enter the city: ").strip()
    concelho = input("Enter the municipality: ").strip()
    distrito = input("Enter the district: ").strip()

    # Adiciona o novo eleitor à lista
    electors.append({
        "idEleitor": id_eleitor,
        "nome": nome,
        "nif": nif,
        "cidade": cidade,
        "concelho": concelho,
        "distrito": distrito
    })
    
    # Salva a lista de eleitores de volta no arquivo CSV
    write_electors(electors)
    print(f"Elector '{nome}' added successfully!")

def view_electors():
    """View all electors."""
    electors = read_electors()
    if not electors:
        print("No electors available.")
        return

    print("\n--- Elector List ---")
    for e in electors:
        print(f"ID: {e['idEleitor']}, Name: {e['nome']}, NIF: {e['nif']}, City: {e['cidade']}, Municipality: {e['concelho']}, District: {e['distrito']}")

def manage_electors():
    """Elector management menu."""
    while True:
        print("\n--- Manage Electors ---")
        print("1. Add Elector")
        print("2. View All Electors")
        print("3. Back to Main Menu")
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            add_elector()
        elif choice == "2":
            view_electors()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")