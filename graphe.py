from jarvis import *
from sommet import *

class Graphe:
    
    jarvis = Jarvis()
    
    def __init__(self, fichier):
        self.name = fichier
        self.registre = []
        self.jarvis.initialisation(fichier)
        Graphe.sommatisation(self)
        Graphe.arctisation(self)
        
    def sommatisation(self):
        for i in range(0, self.jarvis.sommet):
            y = Sommet(i) #création des sommet
            self.registre.append(y)

        #print(self.registre)
    
    def arctisation(self):
        print("Hello there!")
    
    
    

automate = Graphe("test")


#automate.jarvis.affichage(automate.jarvis.mat)






