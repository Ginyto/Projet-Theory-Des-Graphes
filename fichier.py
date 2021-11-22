print("hello there")


def lecture(fichier):
    data = open(fichier, "r")
    datos = data
    return datos.readlines()


data = lecture("./test.txt")

print(data[2])
