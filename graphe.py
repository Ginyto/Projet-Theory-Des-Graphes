from jarvis import *
from sommet import *

class Graphe:
    
    jarvis = Jarvis()
    global INF 
    INF = "∞"
    
    def __init__(self, fichier):
        """__init__ constructeur de Graphe

        Args:
            fichier (Graphe): Tableau d'objet sommet
        """
        self.name = fichier
        self.registre = []
        self.poids = []
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
        for i in range(0,self.jarvis.arc):
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
        """check si le sommet est present dans le graphes

        Args:
            x (int): sommet x

        Returns:
            [bool]: renvoie true si le sommet x existe&
        """
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
        """Voyage entre 2 sommet avec le poids

        Args:
            point_a (int): sommet a
            point_b (int): sommet b
        """
        
        self.jarvis.saut_de_ligne("paseo")
        
        print("Je veux aller du sommet", self.registre[point_a].nom,"au", self.registre[point_b].nom)
        
        self.affichage_sommet(point_a)
        
        self.affichage_sommet(point_b)
        
        if self.are_you_here(point_b, self.registre[point_a].next) == True:
            print()
            print(point_a,"--------", self.registre[point_a].heavy,"------>",point_b)
        
        else:
            print()
            print("Il n'y a pas de chemin directe entre ces 2 sommets")
    
    def matriceMg(self):
        """cree la matrice Mg vierge"""
        self.mat_Mg = self.jarvis.crea_mat(self.jarvis.sommet,self.jarvis.sommet)
        #self.affiche_mat(self.mat_Mg)
        #print(self.mat_Mg)
    
    def matrice_dist(self):
        self.matdist = self.jarvis.crea_mat(self.jarvis.sommet,self.jarvis.sommet)
        self.fill_2Dtab_with(self.matdist, -1)
        self.jarvis.saut_de_ligne("matrice distances")
        self.affiche_mat(self.matdist)
    
    def affiche_mat(self, tab):
        """Affiche la matrice

        Args:
            tab (tableau 2D): matrice à afficher
        """
        print("            ", end = "")
        
        for i in range(len(tab[0])):
            print(i," ", end="")
        
        print()
        
        for i in range(len(tab)):
            print("       ",i,"|", end='')            
            for j in range(len(tab[i])):

                print("",tab[i][j], end =" ")
            print()
    
    def fill_2Dtab_with(self, tab, x):
        """remplie un tableau 2D avec la valeur de x    

        Args:
            tab (tab): tableau en parametre
            x (int): variable de remplissage
        """
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                tab[i][j] = x

    
    def fill_matriceMg(self):
        """Remplie la matrice Mg en partant de la matrice initiale
        """
        self.jarvis.saut_de_ligne("mat initiale")
        
        self.affiche_mat(self.jarvis.mat)
        
        self.jarvis.saut_de_ligne("mat Mg")
        
        for i in range(len(self.jarvis.mat)):
            x = self.jarvis.mat[i][0]
            y = self.jarvis.mat[i][1]
            poids = self.jarvis.mat[i][2]
            
            self.mat_Mg[x-1][y-1] = poids
        
        
        self.affiche_mat(self.mat_Mg)
    
    def replace_matrice(self, x, y):
        """remplace les x par y sans toucher à la diagonale
        """
        for i in range(len(self.mat_Mg)):
            for j in range(len(self.mat_Mg[i])):
                if self.mat_Mg[i][j] == x and i != j:
                    self.mat_Mg[i][j] = y
                    
        self.jarvis.saut_de_ligne("mat ∞")
        self.affiche_mat(self.mat_Mg)


automate = Graphe("1")

automate.matriceMg()
automate.fill_matriceMg()
automate.replace_matrice(0, INF)
automate.matrice_dist()

#automate.paseo(2,3)

#automate.affichage_sommet(0)
#automate.jarvis.affichage(automate.jarvis.mat)






