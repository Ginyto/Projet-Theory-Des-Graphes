from graphe import *

menu = True

while menu == True:
    choix_graphe = int(input("Quel graphe voulez-vous choisir ? (1 à 13) \n"))
    
    while choix_graphe < 1 and choix_graphe > 13:
        choix_graphe = int(input("Erreur dans la saisie du graphe.\n Quel graphe voulez-vous choisir ? (1 à 13) \n"))
    
    automate = Graphe(str(choix_graphe))
        
    print("Lecture du graphe x et stockage en mémoire de x\n")
    print("Affichage de x\n")
    print("Floyd-Warshall de x\n")
    print("Existance de circuit absorbant\n") #(variable  booléan circuit par exemple)
    
    if circuit == True:
        g = int(input("Voulez vous voir un autre graphe ? (1 : Oui. 2 : Non.)\n"))
        if g !=1:
            print("Fin du programme")
            menu = False
    else:
        print("Affichage des chemins de x\n")
        g = int(input("Voulez vous voir un autre graphe ? (1 : Oui. 2 : Non.)\n"))
        if g != 1:
            print("Fin du programme")
            menu = False