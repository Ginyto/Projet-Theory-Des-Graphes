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
        Graphe.peser(self)
        
        
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
    
    def peser(self):
        for i in range(len(self.registre)):
            
            if len(self.registre[i].chemin) > 3:
                print(self.registre[i].chemin)
                
                for k in range(len(self.registre[i].chemin)):
                    if k%3 == 2:
                        #print(self.registre[i].chemin[k])
                        print("voici le poids ---->", self.registre[i].chemin[k])
                    
            
            else:
                print(self.registre[i].chemin)
                print("voici le poids ---->", self.registre[i].chemin[2])

    
    
    

automate = Graphe("test")


#automate.jarvis.affichage(automate.jarvis.mat)






