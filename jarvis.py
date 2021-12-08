class Jarvis:
    
    def initialisation(self, fichier):
        print("Initialisation du fichier : "+fichier)
        
        self.fichier = fichier
        self.data = []
        
        #Jarvis.boucleread()
        Jarvis.lecture(self)
        Jarvis.affichage(self, self.data)
        
        self.sommet = self.data[0]
        self.arc = self.data[1]
        
        Jarvis.affichage(self, self.sommet)
        Jarvis.affichage(self, self.arc)
        
        print("Initialisation terminée")

    def lecture(self):
        fiche = open("./graphes/"+self.fichier+".txt", "r")
        
        for i in range(0,17):
            y = fiche.readline(2)
            
            
            if y != "\n":
                x = int(y)
                self.data.append(x)
    


    def affichage(self,cible):
        print(cible)
        
        
    def matrice(self):
        self.mat = []
        for i in range(self.sommet):
            self.mat.append([0]*self.arc)

        print(self.mat)
        
    
    def miniligne(ligne):
        mat = []
        min = 0
        
        for i in range(len(ligne)):
        #print("Iteration : ", i, "\n")
            if ligne[i] != " ":
                if ligne[i] != "\n":
                    if ligne[i] == "-":
                        min = 1
                        continue

                    else:
                        if min == 1:
                            mat.append("-"+ligne[i])
                        else:
                            mat.append(ligne[i])
        
        return mat
    
    def boucleread(self):
        data = open("./graphes/"+self.fichier+".txt", "r")
        
        mat = []
        
        for i in range(5):
            datos = data.readline()
        
        print(datos)
        
        mat = Jarvis.miniligne(datos)
        
        print(mat)
    
    
    
    def fill(self,tab,cosa):
        tab.append(cosa)


jarvis = Jarvis()

jarvis.initialisation("test")
#jarvis = Jarvis()






