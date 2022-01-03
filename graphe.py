from jarvis import *
from sommet import *

class Graphe:
    
    jarvis = Jarvis()
    
    global INF
    INF = float('inf')
    
    def __init__(self, fichier):
        """__init__ constructeur de Graphe

        Args:
            fichier (Graphe): Tableau d'objet sommet
        """
        self.name = fichier
        self.registre = []
        self.poids = []
        self.circuit = False
        self.jarvis.initialisation(fichier)
        
        self.crea_sommet()
        self.fill_sommet()
        #Graphe.all_affichage_sommet(self)
        
        self.matriceMg()
        self.fill_matriceMg()
        self.replace_matrice(self.mat_Mg,0, INF)
        self.matrice_camino()
        self.fill_camino()
        
        
    
    
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
        
        poids = 0
        
        self.jarvis.saut_de_ligne("paseo")
        
        #print("Je veux aller du sommet", self.registre[point_a].nom,"au", self.registre[point_b].nom)
        
        self.affichage_sommet(point_a)
        
        self.affichage_sommet(point_b)
        
        if self.are_you_here(point_b, self.registre[point_a].next) == True:
            print()
            print(point_a,"--------", self.registre[point_a].heavy,"------>",point_b)
        
        else:
            print()
            #print("Il n'y a pas de chemin directe entre ces 2 sommets")
    
    def matriceMg(self):
        """cree la matrice Mg vierge"""
        self.mat_Mg = self.jarvis.crea_mat(self.jarvis.sommet,self.jarvis.sommet)
        #self.affiche_mat(self.mat_Mg)
        #print(self.mat_Mg)
    
    def matrice_camino(self):
        self.camino = self.jarvis.crea_mat(self.jarvis.sommet,self.jarvis.sommet)
        self.fill_2Dtab_with(self.camino, -1)
        #self.jarvis.saut_de_ligne("camino")
        #self.affiche_mat(self.camino)
    
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
        #self.jarvis.saut_de_ligne("mat initiale")
        
        #self.affiche_mat(self.jarvis.mat)
        
        #self.jarvis.saut_de_ligne("mat Mg")
        
        for i in range(len(self.jarvis.mat)):
            x = self.jarvis.mat[i][0]
            y = self.jarvis.mat[i][1]
            poids = self.jarvis.mat[i][2]
            
            #print("x =",x,"et y =", y,"et poids =",poids)
            
            self.mat_Mg[x][y] = poids
        
        
        #self.affiche_mat(self.mat_Mg)
    
    def fill_camino(self):
        for i in range(len(self.mat_Mg)):
            for j in range(len(self.mat_Mg[i])):
                if self.mat_Mg[i][j] != 0 and self.mat_Mg[i][j] != INF:
                    self.camino[i][j] = i
        
        #self.jarvis.saut_de_ligne("camino")
        #self.affiche_mat(self.camino)
                
    
    def replace_matrice(self,tab, x, y):
        """remplace les x par y sans toucher à la diagonale
        """
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if tab[i][j] == x and i != j:
                    tab[i][j] = y
                    
        #self.jarvis.saut_de_ligne("mat ∞")
        #self.affiche_mat(tab)
    
    def floydwarshall(self):
        
        for way in range(self.jarvis.sommet):
            for first in range(self.jarvis.sommet):
                for last in range(self.jarvis.sommet):
                    #print("Est ce que le racourcis",self.mat_Mg[first][way] + self.mat_Mg[way][last],"est inferieur a",self.mat_Mg[first][last])
                    #si le chemin parcouru entre a et b en passant par c est inferieur au parcour a et b alors on update le chemin a et b
                    
                    if self.mat_Mg[first][way] + self.mat_Mg[way][last] < self.mat_Mg[first][last]:
                        self.jarvis.saut_de_ligne("explications")
                        print("point de départ",first ,"à raccourcis",way," =",self.mat_Mg[first][way])
                        print("point de racourcis",way, "à arrivée",last, " =",self.mat_Mg[way][last], "somme =>",self.mat_Mg[first][way] + self.mat_Mg[way][last])
                        print("point de départ",first, "à arrivé",last, " =",self.mat_Mg[first][last],">",self.mat_Mg[first][way] + self.mat_Mg[way][last],"\n")
                        
                        self.mat_Mg[first][last] = self.mat_Mg[first][way] + self.mat_Mg[way][last]
                        print("Nouveau poids entre",first,"et",last,"=",self.mat_Mg[first][way] + self.mat_Mg[way][last])
                        self.camino[first][last] = self.camino[way][last]
                        print("Nouveau chemin entre",first,"et",last,"passe par",self.camino[way][last])
                        
                        self.jarvis.saut_de_ligne("chemin")
                        self.affiche_mat(self.camino)
                        self.jarvis.saut_de_ligne("poids")
                        self.affiche_mat(self.mat_Mg)
            
                if self.mat_Mg[first][first] < 0:
                    print("Cycle absorbant")
                    self.circuit = True
        
        #self.absorption()
    
    def absorption(self):
        somme = 0
        #print()
        #self.affiche_mat(self.mat_Mg)
        #print()
        
        for i in range(self.jarvis.sommet):
            for j in range(self.jarvis.sommet):
                for k in range(self.jarvis.sommet):
                    for l in range(self.jarvis.sommet):
                    
                        if self.jarvis.sommet == 4:
                            if self.mat_Mg[i][j] != INF and i != j:
                                if self.mat_Mg[j][k] != INF and j != k:
                                    if self.mat_Mg[k][l] != INF and k != l and i == l:
                                        somme += self.mat_Mg[i][j] + self.mat_Mg[j][k] + self.mat_Mg[k][l]
                                        #print(i,j,k,l,"=",somme)
                                        if somme < 0:
                                            print("Il ya un circuit absorbant")
                                            self.circuit = True
                                            return
                                        somme = 0
    
    def resultat(self):
        self.jarvis.saut_de_ligne("resultats")
        
        for i in range(len(self.camino)):
            chemin = [i]
            for j in range(len(self.camino[i])):
                if i != j and self.camino[i][j] != -1:
                    chemin.append(j)
                    print("\nle chemin le plus cours pour aller de",i,"à",j,"est :",chemin,"\n")
    
    def affiche_all(self):
        self.jarvis.jolieprint("Mat initiale")
        self.affiche_mat(self.jarvis.mat)
        self.jarvis.jolieprint("Mat poids")
        self.affiche_mat(self.mat_Mg)
        self.jarvis.jolieprint("Mat chemin")
        self.affiche_mat(self.camino)
        self.jarvis.saut_de_ligne("")
    
    def boucle_menu(self,menu,menu_graphe, choix):
        if choix == "a" or choix == "A":
            self.affiche_all()
            
        if choix == "f" or choix == "F":
            self.floydwarshall()
            
        if choix == "r" or choix == "R":
            self.resultat()
        
        if choix == "t" or choix == "T":
            self.affiche_all()
            self.floydwarshall()
            if self.circuit == False:
                self.resultat()
            else:
                self.jarvis.jolieprint("Circuit absorbant")
        
        
            
        if self.jarvis.here_we_go_again() == False:
            return True


#automate = Graphe("13")



#automate.affiche_all()

#automate.floydwarshall() 


#automate.resultat()

#automate.absorption(6)







