import csv
import random

# Arquivo CSVs
LISTAS_FILE = "data/listas.csv"
VOTOS_FILE = "data/votos.csv"

def ler_listas():
    """Ler as listas válidas a partir do arquivo listas.csv."""
    listas_validas = {}
    with open(LISTAS_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            listas_validas[int(row["idLista"])] = row["nome"]
    return listas_validas

def registrar_voto(votos):
    """Registrar o voto se for válido."""
    listas = ler_listas()
    print("\n--- Listas Disponíveis ---")
    for id_lista, nome in listas.items():
        print(f"ID: {id_lista} - Nome: {nome}")

    try:
        id_lista = int(input("Digite o ID da lista para votar: ").strip())
        if id_lista in listas:
            # Gerar uma chave aleatória para o voto
            key = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
            votos.append({"key": key, "voto": id_lista})
            salvar_votos(votos)
            print(f"Voto registrado com sucesso! (Chave: {key})")
        else:
            print("ID inválido! O voto não foi registrado.")
    except ValueError:
        print("Entrada inválida! O voto não foi registrado.")

def salvar_votos(votos):
    """Salvar os votos no arquivo votos.csv."""
    with open(VOTOS_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["key", "voto"])
        writer.writeheader()
        for voto in votos:
            writer.writerow(voto)

def carregar_votos():
    """Carregar votos do arquivo votos.csv."""
    votos = []
    try:
        with open(VOTOS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                votos.append({"key": row["key"], "voto": int(row["voto"])})
    except FileNotFoundError:
        pass  # Arquivo ainda não existe
    return votos

def exibir_votos(votos):
    """Exibir todos os votos registrados."""
    if not votos:
        print("Nenhum voto registrado ainda.")
        return

    print("\n--- Votos Registrados ---")
    for voto in votos:
        print(f"Chave: {voto['key']} - ID da Lista: {voto['voto']}")

def handle_voting():
    votos = carregar_votos()

    while True:
        print("\n--- Menu de Votação ---")
        print("1. Registrar um voto")
        print("2. Exibir votos registrados")
        print("3. Sair")

        escolha = input("Escolha uma opção (1-3): ").strip()
        if escolha == "1":
            registrar_voto(votos)
        elif escolha == "2":
            exibir_votos(votos)
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
