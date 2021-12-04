
class Jarvis:
    
    def __init__(self, fichier):
        print("Initialisation du fichier : "+fichier)
        
        self.fichier = fichier
        Jarvis.boucleread(self)
        #Jarvis.lecture(self)
        #Jarvis.get_sommet(self)
        #Jarvis.get_arc(self)
        
        print("Initialisation terminée")

    def lecture(self):
        data = open("./graphes/"+self.fichier+".txt", "r")
        self.data = data.readline()
        return self.data
    
    def affichage(self):
        print(self.data)
        #print(self.sommet)
        #print(self.arc)
        
    def get_sommet(self):
        self.sommet = Jarvis.numerisation(self,0)
    
    def get_arc(self):
        self.arc = Jarvis.numerisation(self,0)
        
    def matrice(self):
        mat = []
        for i in range(self.sommet):
            mat.append([0]*self.arc)

        print(mat)
        
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



graphe_test = Jarvis("test")
#graphe_test.affichage()
#graphe_test.matrice()

print("Hello world!")






