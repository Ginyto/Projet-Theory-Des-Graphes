from jarvis import *
from sommet import *

class Graphe:
    
    jarvis = Jarvis()
    
    def __init__(self, fichier):
        """__init__ constructeur de Graphe

        Args:
            fichier (Graphe): Tableau d'objet sommet
        """
        self.name = fichier
        self.registre = []
        self.poids = []
        self.matMg = []
        self.jarvis.initialisation(fichier)
        
        Graphe.crea_sommet(self)
        Graphe.fill_sommet(self)
        #Graphe.all_affichage_sommet(self)
        
    
    def aiguillage_sommet(self, num,content,aiguille):
        """permet de retrouver un sommet grace a son numero d'identification et de lui ajouter du contenue dans un des deux champs suivant : 
        si 66 -> on ajoute dans next (prochain sommet)
        si 99 -> on ajoute dans heavy (poids)

        :param num: id
        :type num: int
        :param content: contenue
        :type content: variable
        :param aiguille: permet de choisir entre next et heavy
        :type aiguille: int
        """
        
        for i in range(0, len(self.registre)):
            if num == self.registre[i].nom:
                #print("num == ", self.registre[i].nom)
                if aiguille == 66:
                    self.registre[i].next.append(content)
                #print(self.registre[i].heavy)
                if aiguille == 99:
                    self.registre[i].heavy.append(content)
    
    
    def affichage_sommet(self,num):
        """Affiche le sommet ainsi que tout ses attribut

        Args:
            num (int): numeros du sommet a
        """
        print()
        
        for i in range(0, len(self.registre)):
            
            if num == self.registre[i].nom:
                print("---sommet--------->", self.registre[i].nom)
                print("---destination---->", self.registre[i].next)            
                print("---poids---------->", self.registre[i].heavy)
    
    def all_affichage_sommet(self):
        """Affiche tout les sommet du graphes
        """
        
        print("================================\n\n")
        
        for i in range(0,self.jarvis.sommet):
            Graphe.affichage_sommet(self,i)
            print("\n")
        
        print("================================")
            
            
    def fill_sommet(self):
        """permet de remplir les sommet dans les champs next (prochain sommet) et le poids
        """
        
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
        """permet de crée des sommet vierge selon les instruction de jarvis qui recupere le nombre de sommet
        """
        for i in range(0, self.jarvis.sommet):
            y = Sommet(i) #création des sommet
            self.registre.append(y)

        #print(self.registre)
    
    def CheckIfSommet(self, x):
        if int(x) > 0 and int(x) < Graphe.jarvis.sommet:
            return True
    
    def are_you_here(self, x, tab):
        """check si x est contenue dans tab

        Args:
            x (int): nom du sommet 
            tab (int): tableau de int

        Returns:
            Booléen: True si occurence
        """
        for i in range(len(tab)):
            if x == tab[i]:
                return True
        
        return False

    def paseo(self, point_a, point_b):
        
        print("Je veux aller du sommet : ", self.registre[point_a].nom,"au", self.registre[point_b].nom)
        
        self.affichage_sommet(point_a)
        
        self.affichage_sommet(point_b)
        
        if self.are_you_here(point_b, self.registre[point_a].next) == True:
            print()
            print(point_a,"--------", self.registre[point_a].heavy,"------>",point_b)
    
    def matriceMg(self):
        print("Hello, world!")
        


#automate = Graphe("test")

#automate.paseo(2,0)
#automate.jarvis.affichage(automate.jarvis.mat)






