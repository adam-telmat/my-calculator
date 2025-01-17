# Liste pour stocker l'historique
history = []

def get_number(prompt):
    """Demande à l'utilisateur un nombre et vérifie sa validité."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def add(a, b):
    result = a + b
    add_to_history(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    add_to_history(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    add_to_history(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        add_to_history(f"{a} / {b} = Erreur (division par zéro)")
        return "Erreur : Division par zéro"
    result = a / b
    add_to_history(f"{a} / {b} = {result}")
    return result

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

def clear_history():
    """Efface l'historique."""
    history.clear()
    print("Historique effacé.")

# Exemple d'utilisation
while True:
    print("\nCalculatrice")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Afficher l'historique")
    print("6. Effacer l'historique")
    print("7. Quitter")

    choice = input("Choisissez une option : ")

    if choice == "1":
        a = get_number("Entrez le premier nombre : ")
        b = get_number("Entrez le deuxième nombre : ")
        print("Résultat :", add(a, b))
    elif choice == "2":
        a = get_number("Entrez le premier nombre : ")
        b = get_number("Entrez le deuxième nombre : ")
        print("Résultat :", subtract(a, b))
    elif choice == "3":
        a = get_number("Entrez le premier nombre : ")
        b = get_number("Entrez le deuxième nombre : ")
        print("Résultat :", multiply(a, b))
    elif choice == "4":
        a = get_number("Entrez le premier nombre : ")
        b = get_number("Entrez le deuxième nombre : ")
        print("Résultat :", divide(a, b))
    elif choice == "5":
        show_history()
    elif choice == "6":
        clear_history()
    elif choice == "7":
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")