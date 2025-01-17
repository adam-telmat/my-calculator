history = []

def get_number(prompt):
    """Demande à l'utilisateur un nombre valide."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

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
    """Ajoute une opération à l'historique."""
    history.append(entry)

def show_history():
    """Affiche l'historique des opérations."""
    if not history:
        print("Aucun calcul effectué pour l'instant.")
    else:
        print("Historique des calculs :")
        for entry in history:
            print(entry) 

def main():
    print("Bienvenue dans la calculatrice Python !")
    while True:
        # Obtenir les entrées utilisateur
        num1 = get_number("Entrez le premier nombre : ")
        operator = get_operator()
        num2 = get_number("Entrez le deuxième nombre : ")

        # Calculer le résultat
        result = calculate(num1, num2, operator)

        # Afficher le résultat
        print(f"Résultat : {num1} {operator} {num2} = {result}")

        # Ajouter à l'historique
        add_to_history(f"{num1} {operator} {num2} = {result}")
        
        # Proposer de voir l'historique
        while True:
            view_hist = input("Voulez-vous voir l'historique de la calculatrice ? (oui/non) : ").strip().lower()
            if view_hist in ['oui', 'non']:
                break  # Sortir de la boucle si la réponse est valide
        print("Erreur : veuillez répondre par 'oui' ou 'non'.")  # Message d'erreur si réponse invalide

        if view_hist == 'oui':
            show_history()
        

        # Demander si l'utilisateur veut continuer
        again = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ").strip().lower()
        if again != 'oui':
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            break

if __name__ == "__main__":
    main()