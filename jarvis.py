class Jarvis:
    
    
    def initialisation(self, fichier):
        self.saut_de_ligne("")
        print("Initialisation du fichier : "+fichier)
        
        #self.saut_de_ligne("test")
        
        self.fichier = fichier

        self.data = []
        
        self.mat = []
        
        self.test = []
        
        #Jarvis.boucleread()
        Jarvis.sizefiche(self) #recupere le nombre de sommet et d'arc
        Jarvis.lecture(self) # cree un tableau avec tout les valeur du fichier 1D
        #Jarvis.affichage(self, self.data) 


        #self.sommet = self.data[0]
        #self.arc = self.data[1]
        
        #Jarvis.matrice(self) #cree un tableau 2D pour les chemin (arc+poids)
        self.mat = self.crea_mat(self.arc, 3)
        #Jarvis.affichage(self, self.sommet)
        #Jarvis.affichage(self, self.arc)
        #Jarvis.affichage(self, self.mat)
        
        Jarvis.fill_arc(self)#Remplis le tableau 2D
        
        #self.affichage(self.mat)
        

        print("Initialisation terminée")
        
    def sizefiche(self):
        fiche = open("./graphes/"+self.fichier+".txt", "r")
        
        self.sommet = int(fiche.readline(2))
        #print(self.sommet)
        self.arc = int(fiche.readline(2))
        #print(self.arc)
        
        fiche.close()

    def lecture(self):
        fiche = open("./graphes/"+self.fichier+".txt", "r")
        
        
        for i in range(0,(self.arc*4)):
            y = fiche.readline(2)
            #print("y = ",y)
            if y != "\n" and y != "":
                #print("y prit dans le tab = ",y)
                x = int(y)
                self.data.append(x)
            
    

    def affichage(self,cible):
        print(cible)
        self.saut_de_ligne("affichage")
        
        
    def matrice(self):
        self.mat = []
        for i in range(self.arc):
            self.mat.append([0]*3)
    
    def crea_mat(self, n, m):
        tab = []
        for i in range(n):
            tab.append([0]*m)
        
        #print(tab)
        
        return tab
    
    def fill_arc(self):
        j = 0
        k = 0
        
        for i in range(2,len(self.data)):
            #print(self.data[i], "-> index: ", i)
            
            self.mat[j][k] = self.data[i]
            
            k += 1
            
            if k > 2:
                #print(self.mat[j])
                j += 1
                k = 0
                
            
            
        

            


    def saut_de_ligne(self, text):
        if text != "":
            print("\n <--------------------",text,"------------------->\n")
        
        else :
            print("\n <-------------------------------------------->\n")

    
    def fill(self,tab,cosa):
        tab.append(cosa)
    
    def is_it_int(self,x, baro):
        allow = []
        
        for i in range(1,baro+1):
            allow.append(str(i))
        
        for i in range(len(allow)):
            if x == allow[i]:
                return True
        
        return False
    
    def hellothere(self):
        print("Hello there!")
        x = input("appuie sur une touche!")
        print(x)
    
    def clear_console(self):
        print(chr(27) + "[2J")
    
    def tapez_sur_pour(self, sur, pour):
        print("    Tapez sur : ",sur,"pour ->",pour)
    
    def affiche_menu(self,x):
        self.saut_de_ligne("")
        print("        Bonjour ! Voici notre programme")
        self.saut_de_ligne("")
        
        if x == 1:
            self.jolieprint("Selectionner votre graphe")
        
        if x == 2:
            print("    Voici les differentes actions dont vous\n    disposez : \n")
            self.tapez_sur_pour("A","Afficher le graphe")
            self.tapez_sur_pour("F","Floyd-Warshall")
            self.tapez_sur_pour("R","Resultats")
            self.tapez_sur_pour("T","Tout executer")
            self.tapez_sur_pour("exit","Quitter")
            self.saut_de_ligne("")
    
    def verif(self,x):
        verification = ["a","A","f","F","r","R","t","T","exit"]
        
        for i in range(len(verification)):
            if x == verification[i]:
                #print("SUCCES")
                return True
        
        #print("ECHEC")
        return False
    
    def jolieprint(self,message):
        self.saut_de_ligne("")
        print("         ",message)
        self.saut_de_ligne("")
    
    def here_we_go_again(self):
        choix = input("Voulez vous continuez ? oui ou non\n")
        
        while choix != "oui" and choix != "non":
            choix = input("Voulez vous continuez ? oui ou non\n")
        
        if choix == "oui":
            return True
        
        if choix == "non":
            return False


#jarvis = Jarvis()

#jarvis.affiche_menu()

#jarvis.hellothere()
#jarvis.initialisation("13")
#jarvis = Jarvis()






