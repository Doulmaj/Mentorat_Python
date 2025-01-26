import json
from random import randint

def WriteRessource(): 
    minLetter =10 #Nombre de lettre minimum pour être accepté
    maxLetter = 15 #Nombre de lettre maximum pour être accepté
    maxWord = 260 #Nombre de mots nécéssaire

    if minLetter <= 0 or maxLetter <= 0 or maxWord <=0 :
        print("Erreur dans les valeurs dans les mots")
        return
    
    if minLetter >= maxLetter :
        print("Erreur : ce type de mot n'existe pas")
        return

    with open ('dictionnaire.txt', 'r', encoding='utf-8') as fichier : 
        dictionnary = {}
        Lines = fichier.readlines() #Lecture de l'ensemble du fichier

        #Classage de tout les mots du fichier en fonction de leur première lettre
        for line in Lines : 
            line = line.strip()
            if len(line) >= minLetter and len(line) <= maxLetter : 
                firstLetter = line[0] 
                if firstLetter in dictionnary : 
                    dictionnary[firstLetter].append(line)
                else : 
                    dictionnary[firstLetter] = [line]

    #Création de la liste contenant les mots pour le fichier ressources.json
    ressourceList = []

    combinedList = [] #Liste contenant tout les mots du dictionnaire
    for liste in list(dictionnary.values()): 
        combinedList.extend(liste)

    if len(combinedList) == 0 :
        print(" Erreur : Le dictionnaire est vide")
        return
    
    elif len(combinedList) <= maxWord :
        ressourceList = combinedList

    else : 
        #une boucle for qui va de 0 a maxWord et qui ajoute des mots au hasard dans la liste ressourceList
        for i in range(maxWord) : 
            cpt = i % len(list(dictionnary.keys())) #compteur permettant d'ajouter des mots au hasard tout en considérant l'ordre des lettres
            dicoKey = list(dictionnary.keys())[cpt] #clé associé au compteur
            dicoValues = dictionnary[dicoKey] #valeur associé au clé
            index = randint(0, len(dicoValues) - 1) #generation aléatoire de l'index du mot
            ressourceList.append(dicoValues[index]) #ajout du mot au ressourceList
            dicoValues.remove(dicoValues[index]) #suppression du mot dans les valeurs pour éviter les répétitions
            if len(dicoValues) == 0 : #Suppression de la clé du dictionnaire si elle ne contient plus de mots
                del dictionnary[dicoKey]
            
    with open('ressources.json', 'r', encoding='utf-8') as ressources :
        data = json.load(ressources)

    with open('ressources.json', 'w', encoding='utf-8') as ressources2 :
        data[0] = ressourceList
        json.dump(data, ressources2, indent = 4)

    print("Fichier ressources.json mis à jour")

    

if __name__ == "__main__" : 
    WriteRessource()