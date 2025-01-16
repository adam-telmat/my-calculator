#liste pour accéder à l'historique

history = []

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
    print("5. Afficher l'historique")
    print("6. Effacer l'historique")
    print("7. Quitter")

    choice = input("Choisissez une option : ")


    if choice == "5":
        show_history()
    elif choice == "6":
        clear_history()
    elif choice == "7":
        print("Au revoir !")
        break
    else:
        print("Option Invalide")
        print("Cheh")