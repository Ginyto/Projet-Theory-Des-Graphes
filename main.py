from graphe import *

jarvis = Jarvis()


menu = True

while menu == True:
    jarvis.affiche_menu(1)
    choix_graphe = input("Quel graphe voulez-vous choisir ? (1 à 13) \n")
    
    while jarvis.is_it_int(choix_graphe,13) == False:
        choix_graphe = input("Erreur dans la saisie du graphe.\n Quel graphe voulez-vous choisir ? (1 à 13) \n")
    
    automate = Graphe(choix_graphe)
    
    menu_graphe = True
    
    while menu_graphe == True:
        jarvis.affiche_menu(2)
        
        choix_action = input("\nEntrez une action\n")
        
        if jarvis.verif(choix_action) == False:
            choix_action = input("\nEntrez une action correcte !\n")
        
        if choix_action == "exit":
            jarvis.jolieprint("Fin de programme")
            menu_graphe = False
            menu = False
        
        else:
            if automate.boucle_menu(menu,menu_graphe,choix_action):
                menu_graphe = False
                