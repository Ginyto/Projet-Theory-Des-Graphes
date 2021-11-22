print("hello there")


def lecture(fichier):
    data = open(fichier, "r")
    datos = data
    #data.close()
    return datos.readlines()


data = lecture("./data.txt")

print(data[2])
