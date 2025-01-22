#
#Gestionaire de Tas Binaire
#By gShimatu
#

import heapq

def afficher_menu():
    print("\n--- Gestion de Tas Binaire ---")
    print("--- gShimatu ---\n")
    print("1. Ajouter une valeur")
    print("2. Afficher les tas")
    print("3. Quitter")

def ajouter_valeur(tas_min, tas_max):
    try:
        valeur = int(input("Entrez une valeur entière à ajouter : "))
        heapq.heappush(tas_min, valeur)  # Ajout dans le tas min
        heapq.heappush(tas_max, -valeur)  # Ajout dans le tas max (valeurs inversées pour simuler un tas max)
        print(f"Valeur {valeur} ajoutée avec succès !")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

def afficher_tas(tas_min, tas_max):
    print("\nTas Min :", tas_min)
    # Affichage des valeurs réelles pour le tas max
    print("Tas Max :", [-val for val in tas_max])

def main():
    tas_min = [] 
    tas_max = []  

    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_valeur(tas_min, tas_max)
        elif choix == "2":
            afficher_tas(tas_min, tas_max)
        elif choix == "3":
            print("Merci d'avoir utilisé le gestionnaire de tas. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
