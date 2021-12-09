from jarvis import *
from sommet import *

class Graphe:
    
    jarvis = Jarvis()
    
    def __init__(self, fichier):
        self.name = fichier
        self.registre = []
        self.poids = []
        self.jarvis.initialisation(fichier)
        
        Graphe.sommatisation(self)
        Graphe.arctisation(self)
        Graphe.poidisation(self)
        
        
    def sommatisation(self):
        for i in range(0, self.jarvis.sommet):
            y = Sommet(i) #création des sommet
            self.registre.append(y)

        #print(self.registre)
    
    def arctisation(self):
        for i in range(0, len(self.registre)):
            #print("index of registre -> ",i)
            
            for j in range(0, len(self.jarvis.mat)):
                if i == self.jarvis.mat[j][0]:
                    #print(self.jarvis.mat[j])
                    self.registre[i].chemin += self.jarvis.mat[j]
            
            #print(self.registre[i].chemin)
    
    def poidisation(self):
        print("Hello there!")

    
    
    

automate = Graphe("test")


#automate.jarvis.affichage(automate.jarvis.mat)






