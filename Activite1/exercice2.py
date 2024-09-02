# Ecrire un programme en Python qui permet de calculer et d’afficher la distance entre deux points dont les coordonnées sont données.
# Temps: 10min
from math import sqrt
def CheckFloat(x) : 
    if x.isdigit():
        x= float(x)
    else : 
        print("Ce que vous avez saisi n'est pas un nombre donc il pendra la valeur par défaut 0 ")
        x=0
    return x

Xa = input("Veuillez saisir l'abcisse du premier point : ")
Xa = CheckFloat(Xa)
Ya = input("Veuillez saisir l'ordonnée du premier point : ")
Ya = CheckFloat(Ya)
Xb = input("Veuillez saisir l'abcisse du second point : ")
Xb = CheckFloat(Xb)
Yb = input("Veuillez saisir l'ordonnée du second point : ")
Yb = CheckFloat(Yb)

distance = sqrt((Xa - Xb)**2 + (Ya - Yb)**2 )

print(f"La distance entre les points de coordonnée ({Xa},{Ya}) et ({Xb},{Yb}) est : {distance} ")
