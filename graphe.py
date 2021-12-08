from jarvis import *

class Graphe:
    
    jarvis = Jarvis()
    
    def __init__(self):
        self.name = ""
        self.sommet = [] #Tableau d'objet sommet
        self.sauvegarde = [[]]#graphe sous la forme d'un double tableau
    
    def start_graphe(self, fichier):
        self.sauvgarde = self.jarvis.initialisation(fichier)


automate = Graphe()    

automate.start_graphe("test")

print(automate.sauvgarde)






