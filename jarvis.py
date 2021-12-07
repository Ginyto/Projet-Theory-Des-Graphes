class Jarvis:
    
    def initialisation(self, fichier):
        print("Initialisation du fichier : "+fichier)
        
        self.fichier = fichier
        self.data = []
        #jarvis.boucleread()
        jarvis.lecture()
        #Jarvis.affichage()
        jarvis.doubletab()
        
        print("Initialisation terminée")

    def lecture(self):
        fiche = open("./graphes/"+self.fichier+".txt", "r")
        
        for i in range(0,17):
            y = fiche.readline(2)
            
            
            if y != "\n":
                x = int(y)
                self.data.append(x)
    
    def doubletab(self):
        
        for i in range(len(self.data)):
            print(i)
        


    def affichage(self):
        print(self.data)
        #print(self.sommet)
        #print(self.arc)
        
    def get_sommet(self):
        self.sommet = Jarvis.numerisation(self,0)
    
    def get_arc(self):
        self.arc = Jarvis.numerisation(self,0)
        
    def matrice(self):
        self.mat = []
        for i in range(self.sommet):
            self.mat.append([0]*self.arc)

        print(self.mat)
        
    def numerisation(self, pos):
        return int(self.data[pos])
    
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






