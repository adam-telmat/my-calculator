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

        # Demander si l'utilisateur veut continuer
        again = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ").strip().lower()
        if again != 'oui':
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            break

if __name__ == "__main__":
    main()