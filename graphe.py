from jarvis import *
from sommet import *

class Graphe:
    
    jarvis = Jarvis()
    
    def __init__(self, fichier):
        self.name = fichier
        self.registre = []
        self.poids = []
        self.jarvis.initialisation(fichier)
        
        Graphe.crea_sommet(self)
        Graphe.fill_sommet(self)
        
    
    def aiguillage_sommet(self, num,content,aiguille):
        for i in range(0, len(self.registre)):
            if num == self.registre[i].nom:
                #print("num == ", self.registre[i].nom)
                if aiguille == 66:
                    self.registre[i].next.append(content)
                #print(self.registre[i].heavy)
                if aiguille == 99:
                    self.registre[i].heavy.append(content)
    
    
    def affichage_sommet(self,num):
        """permet l'affichage complet d'un sommet

        :param num: numero d'identification
        :type num: int
        """
        for i in range(0, len(self.registre)):
            
            if num == self.registre[i].nom:
                print("---sommet--------->", self.registre[i].nom)
                print("---destination---->", self.registre[i].next)            
                print("---poids---------->", self.registre[i].heavy)
                
                
    def fill_sommet(self):
        
        #print(self.jarvis.affichage(self.jarvis.mat))
        for i in range(0,self.jarvis.sommet + 1):
            #print("---sommet---->",self.jarvis.mat[i][0])
            #print("---destination---->",self.jarvis.mat[i][1])
            
            Graphe.aiguillage_sommet(self,self.jarvis.mat[i][0],self.jarvis.mat[i][1],66)
            
            #print("---poids---->",self.jarvis.mat[i][2])
            
            Graphe.aiguillage_sommet(self,self.jarvis.mat[i][0],self.jarvis.mat[i][2],99)
            
            #print("\n")
        
        #Graphe.affichage_sommet(self,0)
        #print("\n")
        #Graphe.affichage_sommet(self,1)
        #print("\n")
        #Graphe.affichage_sommet(self,2)
        #print("\n")
        #Graphe.affichage_sommet(self,3)
            
        
        
        
    def crea_sommet(self):
        for i in range(0, self.jarvis.sommet):
            y = Sommet(i) #création des sommet
            self.registre.append(y)

        #print(self.registre)

automate = Graphe("test")


#automate.jarvis.affichage(automate.jarvis.mat)






