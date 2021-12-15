class Jarvis:
    
    def initialisation(self, fichier):
        print("Initialisation du fichier : "+fichier)
        
        #Jarvis.saut_de_ligne(self)
        
        self.fichier = fichier

        self.data = []
        
        
        
        self.test = []
        
        #Jarvis.boucleread()
        Jarvis.sizefiche(self) #recupere le nombre de sommet et d'arc
        Jarvis.lecture(self) # cree un tableau avec tout les valeur du fichier 1D
        #Jarvis.affichage(self, self.data) 


        #self.sommet = self.data[0]
        #self.arc = self.data[1]
        
        Jarvis.matrice(self) #cree un tableau 2D pour les chemin (arc+poids)
        #self.test = self.carré_mat(self.arc)
        #Jarvis.affichage(self, self.sommet)
        #Jarvis.affichage(self, self.arc)
        #Jarvis.affichage(self, self.mat)
        
        Jarvis.fill_arc(self)#Remplis le tableau 2D
        
        Jarvis.affichage(self, self.mat)
        

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
        
        
        for i in range(0,self.sommet*self.arc):
            y = fiche.readline(2)
            
            
            if y != "\n":
                x = int(y)
                self.data.append(x)
    

    def affichage(self,cible):
        print(cible)
        Jarvis.saut_de_ligne(self)
        
        
    def matrice(self):
        self.mat = []
        for i in range(self.arc):
            self.mat.append([0]*3)
    
    def carré_mat(self, n):
        tab = []
        for i in range(n):
            tab.append([0]*n)
        
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
                
            
            
        

            


    def saut_de_ligne(self):
        print("\n --------------------------->\n")

    
    def fill(self,tab,cosa):
        tab.append(cosa)


#jarvis = Jarvis()

#jarvis.initialisation("test")
#jarvis = Jarvis()






