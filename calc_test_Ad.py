import datetime

history = []

def get_number(prompt):
    """Demande à l'utilisateur un nombre valide."""
    while True:
        try:
            return float(input(prompt))  # Convertir en nombre flottant
        except ValueError:  # Si l'utilisateur entre autre chose qu'un nombre
            print("Entrée invalide. Veuillez entrer un nombre valide.")

def get_operator():
    """Demande à l'utilisateur un opérateur valide."""
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Entrez un opérateur (+, -, *, /) : ").strip()
        if operator in valid_operators:
            return operator
        else:
            print("Opérateur invalide. Veuillez choisir parmi +, -, *, /.")

def calculate(a, b, operator):
    """Effectue l'opération spécifiée sur deux nombres."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Erreur : division par zéro."
        return a / b
    
def add_to_history(entry):
    """Ajoute une opération à l'historique avec la date et l'heure."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formater l'heure actuelle
    history.append(f"{timestamp} - {entry}")  # Ajouter la date et l'heure avant l'entrée

def show_history():
    """Affiche l'historique des opérations."""
    if not history:
        print("Aucun calcul effectué pour l'instant.")
    else:
        print("Historique des calculs :")
        for entry in history:
            print(entry) 

def get_yes_no_input(prompt):
    """Demande une réponse 'oui' ou 'non' et la valide."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['oui', 'non']:
            return response  # Retourne la réponse valide
        print("Erreur : veuillez répondre par 'oui' ou 'non'.")  # Message d'erreur

def main():
    print("Bienvenue dans la calculatrice Python !")
    keep_running = True

    while keep_running:
        # Obtenir les entrées utilisateur avec validation
        num1 = get_number("Entrez le premier nombre : ")
        operator = get_operator()
        num2 = get_number("Entrez le deuxième nombre : ")

        # Calculer le résultat
        result = calculate(num1, num2, operator)

        # Afficher le résultat
        print(f"Résultat : {num1} {operator} {num2} = {result}")

        # Ajouter à l'historique avec la date et l'heure
        add_to_history(f"{num1} {operator} {num2} = {result}")
        
        # Proposer de voir l'historique
        view_hist = get_yes_no_input("Voulez-vous voir l'historique de la calculatrice ? (oui/non) : ")
        if view_hist == 'oui':
            show_history()

        # Demander si l'utilisateur veut continuer
        again = get_yes_no_input("Voulez-vous effectuer un autre calcul ? (oui/non) : ")
        if again == 'non':
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            keep_running = False
        else:
            print("Très bien, continuons !")

if __name__ == "__main__":
    main()
