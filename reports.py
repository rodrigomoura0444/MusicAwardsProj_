import csv

VOTES_FILE = "data/votos.csv"
CANDIDATE_FILE = "data/listas.csv"

def load_votes():
    """Load votes from the votos.csv file."""
    votes = []
    try:
        with open(VOTES_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                votes.append(row["vote"])  # Assuming "voto" contains the candidate ID
    except FileNotFoundError:
        print("Votes file not found.")
    return votes

def load_candidates():
    """Load candidates from the listas.csv file."""
    candidates = {}
    try:
        with open(CANDIDATE_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                candidates[row["idLista"]] = row["nome"]
    except FileNotFoundError:
        print("Candidates file not found.")
    return candidates

def generate_reports():
    """Generate and display voting reports with percentages."""
    votes = load_votes()
    candidates = load_candidates()

    if not votes:
        print("No votes found. Cannot generate report.")
        return

    # Calculate total votes and count votes for each candidate
    total_votes = len(votes)
    vote_count = {candidate_id: 0 for candidate_id in candidates.keys()}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1

    # Display report
    print("\n--- Election Report ---")
    print(f"Total Votes: {total_votes}")
    print("Results:")
    for candidate_id, count in vote_count.items():
        percentage = (count / total_votes) * 100
        candidate_name = candidates.get(candidate_id, "Unknown")
        print(f"Candidate: {candidate_name} | Votes: {count} | Percentage: {percentage:.2f}%")
