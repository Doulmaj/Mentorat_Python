#Temps : 7 min
# Difficultés : Trouvé un bibliothèque capable de généré un nombre aléatoire
import random

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