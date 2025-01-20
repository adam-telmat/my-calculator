import datetime  # Module pour manipuler les dates et heures
import json  # Module pour manipuler les fichiers au format JSON

# Nom du fichier utilisé pour stocker l'historique des opérations
HISTORY_FILE = "history.json"

# Charger l'historique au démarrage
def load_history():
    """
    Charge l'historique depuis un fichier JSON.
    Si le fichier n'existe pas, retourne une liste vide.
    Si le fichier est corrompu, affiche un message d'erreur et retourne une liste vide.
    """
    try:
        # Ouvrir le fichier JSON en mode lecture
        with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)  # Charger et retourner les données du fichier JSON
    except FileNotFoundError:
        # Si le fichier n'existe pas, retourner une liste vide
        return []
    except json.JSONDecodeError:
        # Si le fichier JSON est corrompu, afficher une erreur et réinitialiser l'historique
        print("Erreur : le fichier d'historique est corrompu. L'historique sera réinitialisé.")
        return []

# Sauvegarder l'historique dans un fichier JSON
def save_history():
    """
    Sauvegarde la liste actuelle d'historique dans un fichier JSON.
    Le fichier est formaté avec une indentation pour être lisible.
    """
    with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
        json.dump(history, file, indent=4, ensure_ascii=False)  # Écrire les données avec une mise en forme lisible

# Ajouter une entrée à l'historique
def add_to_history(entry):
    """
    Ajoute une nouvelle entrée dans l'historique.
    Chaque entrée inclut une horodatation au moment de l'ajout.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format de la date et heure
    history.append(f"{timestamp} - {entry}")  # Ajouter l'entrée au format "date - opération"
    save_history()  # Sauvegarder automatiquement l'historique après chaque ajout

# Afficher l'historique
def show_history():
    """
    Affiche toutes les opérations présentes dans l'historique.
    Si l'historique est vide, informe l'utilisateur.
    """
    if not history:
        # Cas où l'historique est vide
        print("Aucun calcul effectué pour l'instant.")
    else:
        # Afficher chaque entrée dans l'historique
        print("Historique des calculs :")
        for entry in history:
            print(entry)

# Demander un nombre valide
def get_number(prompt):
    """
    Demande à l'utilisateur d'entrer un nombre.
    Si l'utilisateur entre une valeur invalide, une nouvelle tentative est demandée.
    """
    while True:
        try:
            # Tenter de convertir l'entrée utilisateur en nombre flottant
            return float(input(prompt))
        except ValueError:
            # Afficher un message d'erreur en cas d'entrée invalide
            print("Entrée invalide. Veuillez entrer un nombre valide.")

# Demander un opérateur valide
def get_operator():
    """
    Demande à l'utilisateur d'entrer un opérateur mathématique valide.
    Seuls '+', '-', '*', '/' sont acceptés.
    """
    valid_operators = ['+', '-', '*', '/']  # Liste des opérateurs autorisés
    while True:
        operator = input("Entrez un opérateur (+, -, *, /) : ").strip()  # Supprimer les espaces inutiles
        if operator in valid_operators:
            return operator  # Retourner l'opérateur valide
        else:
            print("Opérateur invalide. Veuillez choisir parmi +, -, *, /.")

# Effectuer un calcul
def calculate(a, b, operator):
    """
    Effectue un calcul basé sur deux nombres et un opérateur.
    Gère la division par zéro en renvoyant un message d'erreur.
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            # Gérer la division par zéro
            return "Erreur : division par zéro."
        return a / b

# Demander une réponse 'oui' ou 'non'
def get_yes_no_input(prompt):
    """
    Demande à l'utilisateur de répondre par 'oui' ou 'non'.
    En cas de réponse invalide, une nouvelle tentative est demandée.
    """
    while True:
        response = input(prompt).strip().lower()  # Convertir en minuscules et supprimer les espaces
        if response in ['oui', 'non']:
            return response  # Retourner la réponse valide
        print("Erreur : veuillez répondre par 'oui' ou 'non'.")

# Programme principal
def main():
    """
    Programme principal de la calculatrice.
    Gère le flux général : entrée utilisateur, calcul, affichage des résultats, historique.
    """
    global history  # Déclarer la variable 'history' comme globale pour qu'elle soit modifiée dans toutes les fonctions
    history = load_history()  # Charger l'historique au démarrage
    print("Bienvenue dans la calculatrice Python !")

    keep_running = True  # Contrôle de la boucle principale
    while keep_running:
        # Étape 1 : Obtenir les données nécessaires pour le calcul
        num1 = get_number("Entrez le premier nombre : ")
        operator = get_operator()
        num2 = get_number("Entrez le deuxième nombre : ")

        # Étape 2 : Effectuer le calcul
        result = calculate(num1, num2, operator)

        # Étape 3 : Afficher le résultat
        print(f"Résultat : {num1} {operator} {num2} = {result}")

        # Étape 4 : Ajouter le résultat à l'historique
        add_to_history(f"{num1} {operator} {num2} = {result}")
        
        # Étape 5 : Proposer d'afficher l'historique
        view_hist = get_yes_no_input("Voulez-vous voir l'historique de la calculatrice ? (oui/non) : ")
        if view_hist == 'oui':
            show_history()

        # Étape 6 : Demander si l'utilisateur veut continuer
        again = get_yes_no_input("Voulez-vous effectuer un autre calcul ? (oui/non) : ")
        if again == 'non':
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            keep_running = False  # Sortir de la boucle principale
        else:
            print("Très bien, continuons !")

# Point d'entrée du programme
if __name__ == "__main__":
    main()
