def calculator():
    try:
        a = float(input("Entrez le premier nombre: "))
    except ValueError:
        print("Erreur : Entrez un nombre valide.")
        
    operator = input("Entrez l'opérateur (+, -, *, /): ").strip()

    try:
        b = float(input("Entrez le second nombre: "))
    except ValueError:
        print("Erreur : Entrez un nombre valide.")

    if operator == "+":
        print (f"{a+b}")
    elif operator == "-":
        print (a - b)
    elif operator == "*":
        print (a*b)
    elif operator == "/":
        if b != 0:
            print(f"Résultat: {a / b}")
        else:
            print("Erreur : Division par zéro.")
    else:
        print("Erreur : Opérateur non valide.")

calculator()

#gérer input str
#demander à relancer le calcul en cas d'erreur
#try except valueerror
#boucle while pour que le programme ne s'arrête pas
#quand on try-except l'erreur, on relance la boucle
#pour historique, stocker en fichier .txt ou .JSON (si demande historique, faire lire le fichier)