from jarvis import *

class Graphe:
    
    jarvis = Jarvis()
    
    def __init__(self, fichier):
        self.name = fichier
        self.jarvis.initialisation(fichier)
    
    

automate = Graphe("test")

automate.jarvis.affichage(automate.jarvis.mat)






