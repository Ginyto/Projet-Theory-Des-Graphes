from graphe import *

jarvis = Jarvis()


menu = True

while menu == True:
    choix_graphe = input("Quel graphe voulez-vous choisir ? (1 à 13) \n")
    
    while jarvis.is_it_int(choix_graphe,13) == False:
        choix_graphe = input("Erreur dans la saisie du graphe.\n Quel graphe voulez-vous choisir ? (1 à 13) \n")
    
    automate = Graphe(choix_graphe)
    
    menu_graphe = True
    
    while menu_graphe == True:
        jarvis.affiche_menu()
        
        choix_action = input("\nEntrez une action\n")
        
        if choix_action == "exit":
            menu_graphe = False
            menu = False
        
        if choix_action == "a" or choix_action == "A":
            automate.affiche_all()
            if jarvis.here_we_go_again() == False:
                menu_graphe = False
                menu = False
        
        if choix_action == "f" or choix_action == "F":
            automate.floydwarshall()
            if jarvis.here_we_go_again() == False:
                menu_graphe = False
                menu = False
        
        if choix_action == "r" or choix_action == "R":
            automate.resultat()
            if jarvis.here_we_go_again() == False:
                menu_graphe = False
                menu = False