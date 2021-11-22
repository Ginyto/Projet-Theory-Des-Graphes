
class Jarvis:
    
    def __init__(self, fichier):
        self.fichier = fichier
        Jarvis.lecture(self)

    
    def lecture(self):
        data = open(self.fichier, "r")
        datos = data
        self.data = datos.readlines()
        return self.data
    
    def affichage(self):
        print(self.data)


graphe_test = Jarvis("./g_test.txt")

graphe_test.affichage()



