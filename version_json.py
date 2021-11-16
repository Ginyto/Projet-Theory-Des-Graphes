import json

print("hello there")

def lecture(fichier):
    with open(fichier) as data :
        return json.load(data)
    

data = lecture("datos.json")
