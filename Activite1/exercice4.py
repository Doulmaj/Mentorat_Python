#Temps : 11min
import random
maximum = 0
choix = input("Veuillez choisir votre nivaeu de difficulté : \n 1. Facile (0 -100) ; \n 2. Moyen (0 - 500) ;\n 3. Difficile (0 -1000) : \n")

if choix == '1' : 
    maximum = 100
elif choix == '2' : 
    maximum = 500
elif choix == '3' : 
    maximum = 1000
else :
    print("La valeur saisi ne correspond à aucun choix proposé donc vous serez dirigé par défaut vers la difficulté facile") 
    maximum = 100

nbr = random.randint(1,maximum)
trouve = False
while not trouve : 
    x = int(input('Veuillez saisir un nombre : '))
    if x < nbr : 
        print("Plus grand")
    elif x > nbr : 
        print('Plus petit')  
    elif x==nbr : 
        print("Félicitaion, vous avez trouvé le nombre")
        trouve = True