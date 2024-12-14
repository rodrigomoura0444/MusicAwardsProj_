import csv
import random
import os

# Constantes para os arquivos
LISTAS_FILE = "data/listas.csv"
VOTOS_FILE = "data/votos.csv"
KEY_LENGTH = 6  # Comprimento da chave do voto

def read_lists():
    """Read valid lists from the file listas.csv."""
    valid_lists = {}
    try:
        with open(LISTAS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                valid_lists[int(row["idLista"])] = row["nome"]
    except FileNotFoundError:
        print(f"Error: {LISTAS_FILE} not found. Please ensure the file exists.")
    return valid_lists

def register_vote(votes):
    """Register the vote if it is valid."""
    lists = read_lists()
    if not lists:
        print("No valid lists available for voting.")
        return

    print("\n--- Available Lists ---")
    for id_list, name in lists.items():
        print(f"ID: {id_list} - Name: {name}")

    try:
        id_list = int(input("Enter the ID of the list to vote for: ").strip())
        if id_list in lists:
            # Generate a random key for the vote
            key = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=KEY_LENGTH))
            votes.append({"key": key, "vote": id_list})
            save_votes(votes)
            print(f"Vote successfully registered! (Key: {key})")
        else:
            print("Invalid ID! The vote was not registered.")
    except ValueError:
        print("Invalid input! The vote was not registered.")

def save_votes(votes):
    """Save the votes to the file votos.csv."""
    try:
        with open(VOTOS_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["key", "vote"])
            writer.writeheader()
            for vote in votes:
                writer.writerow(vote)
    except IOError as e:
        print(f"Error saving votes: {e}")

def load_votes():
    """Load votes from the file votos.csv."""
    votes = []
    if not os.path.exists(VOTOS_FILE):
        return votes  # Return empty if file doesn't exist

    try:
        with open(VOTOS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                votes.append({"key": row["key"], "vote": int(row["vote"])})
    except FileNotFoundError:
        print(f"Warning: {VOTOS_FILE} not found. Starting with no votes.")
    except ValueError as e:
        print(f"Error reading votes: {e}")
    return votes

def display_votes(votes):
    """Display all registered votes."""
    if not votes:
        print("No votes have been registered yet.")
        return

    print("\n--- Registered Votes ---")
    for vote in votes:
        print(f"Key: {vote['key']} - List ID: {vote['vote']}")

def handle_voting():
    """Main function to handle voting menu."""
    votes = load_votes()

    while True:
        print("\n--- Voting Menu ---")
        print("1. Register a vote")
        print("2. Display registered votes")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            register_vote(votes)
        elif choice == "2":
            display_votes(votes)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    handle_voting()
