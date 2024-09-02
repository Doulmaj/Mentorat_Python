import json
from exercice3 import checkBMI

print('\n')
print("_"*100)
print('\n')

def nonVide(saisi, typeSaisi) : 
    while(len(saisi) <= 2) : 
        saisi= input(f"Veuillez saisir un {typeSaisi} valide : ")
    return saisi.strip()

def checkAge(saisirInput) :
    while True: 
        try:
            int(saisirInput)
            return saisirInput
        except ValueError:
            saisirInput =input("L'âge que vous avez saisi n'est pas un entier, veuillez réessayer : ")

#Fonction de lecture de base de données 
def readDatabase(src) :
    try : 
        with open(src,'r') as database : 
            donnees = json.load(database)
    except FileNotFoundError :
        print("le fichier n'a pas été retrouvé")
        return
    except json.JSONDecodeError :
        print("Echec lors de la conversion du fichier")
        return
    return donnees

def upadteDatabase(src,data) : 
    try : 
        with  open(src,'w') as database :
            json.dump(data,database)
            print()
            print("_"*100)
            print()
            print("Vos données ont été mis à jour avec succès")
    except : 
        print("Echec de l'enregistrement des données relatives à l'utilisateur")

def register() : 
    print("Bienvenue dans l'interface d'inscription de vos données ")
    nom = nonVide(input("Veuillez saisir votre nom : "),"nom")
    prenom = nonVide(input("Veuillez saisir votre prénom : "),"prénom")
    travail = input("Veuillez saisir votre travail : ").strip()
    age = checkAge(input("Veuillez saisir votre age : "))
    BMI_Data = checkBMI()
    print('\n'*2)
    print('_'*100)
    print('\n'*2)
    #Enregistrement du nom et du prénom 
    donnees = readDatabase('./Database/users.json')
    userId = len(donnees) + 1
    data = {"id": userId, "nom" : nom, "prenom" : prenom}
    donnees.append(data)
    upadteDatabase('./Database/users.json',donnees)
    print("Enregistrement des données relatives à l'identité de l'utilisateur effectué avec succès")
    print()

    #Enregistrement des données de l'utilisateur
    donnees = readDatabase('./Database/infos.json')
    infoId = len(donnees) + 1
    infoData = {"id": infoId,"age": age,"sex" : BMI_Data[0] , "travail" : travail, "poids" : BMI_Data[1], "taille" : BMI_Data[2]/100, "IMC" : BMI_Data[3], "classe_sante": BMI_Data[4]}
    donnees.append(infoData)
    upadteDatabase('./Database/infos.json',donnees)
    print()
    print("Enregistrement des données relatives aux infos utilisateur effectué avec succès")


def updateInformation() : 
    print("Bienvenue dans l'interface de modification des données ")
    nom = input("Veuillez saisir votre nom : ").strip()
    prenom = input("Veuillez saisir votre prénom : ").strip()
    donnees = readDatabase('./Database/users.json')
    trouve = False
    for donnee in donnees : 
        if donnee["nom"] == nom and donnee["prenom"] == prenom :
            id = donnee["id"]
            trouve = True
            dataType = input("Veuillez saisir le type de données que vous voulez modifier : \n 1-Nom et/ou prénom \n 2-informations médicales \n")
            if dataType == "1" :
                nouvNom = nonVide(input("Veuillez saisir votre nom : "),"nom")
                nouvPrenom = nonVide(input("Veuillez saisir votre prénom :"),"prénom")
                newDonne = {"id": id, "nom" : nouvNom, "prenom" : nouvPrenom}
                donnee.update(newDonne)
                upadteDatabase('./Database/users.json',donnees)
            elif dataType == "2" :
                travail = input("Veuillez saisir votre travail : ").strip()
                age = checkAge(input("Veuillez saisir votre age : "))
                BMI = checkBMI()
                donnees = readDatabase('./Database/infos.json')
                newInfoData = {"id": id,"age": age,"sex" : BMI[0] , "travail" : travail, "poids" : BMI[1], "taille" : BMI[2]/100, "IMC" : BMI[3], "classe_sante": BMI[4]}
                for info in donnees : 
                    if info["id"] == id : 
                        info.update(newInfoData)
                upadteDatabase('./Database/infos.json',donnees)
                print()
            else :
                print("Le choix que vous avez fait est invalide, vous serez donc rediriger vers l'interface de choix.")
                return
    if trouve == False :
        print("L'utilisateur ne fais pas partie de notre base de données")

def checkInformation():
    print("Bienvenue dans l'interface de vérification des données ")
    nom = input("Veuillez saisir votre nom : ").strip()
    prenom = input("Veuillez saisir votre prénom : ").strip()
    donnees1 = readDatabase('./Database/users.json')
    trouve = False
    for donnee in donnees1 : 
        if donnee["nom"] == nom and donnee["prenom"] == prenom :
            trouve = True
            id = donnee["id"]
            donnees2 = readDatabase('./Database/infos.json') 
            for info in donnees2 : 
                if info["id"] == id :
                    break
            donnees3 = readDatabase('./Database/sante.json')
            for etat in donnees3 :
                if etat["id"] == info["classe_sante"] :
                    break
            print()
            print('_'*100)
            print()
            print("Voici vos données : ")
            print()
            print(f"nom : {donnee['nom']}")
            print(f"prénom : {donnee['prenom']}")
            print(f"age : {info['age']}")
            print(f"sex : {info['sex']}")
            print(f"travail : {info['travail']}")
            print(f"poids : {info['poids']}Kg")
            print(f"taille : {info['taille']}m")
            print(f"IMC : {info['IMC']}")
            print('\n' + '_'*100)
            print("Voici les informations relatives à votre classe santé : ")
            print()
            print(f"Diagnostic : {etat['diag']}")
            print(f"Raison : {etat["raison"]}")
            print(f"Conseil : {etat["conseil"]}")
    if trouve == False :
        print("L'utilisateur ne fais pas partie de notre base de données. Veuillez vous inscrire")
        return

while True : 
    print()
    print("_"*100)
    print()
    print("Bienvenue dans l'interface de choix")
    print()
    choice = input("Veuillez choisir une option : \n 1-Enregistrement des informations \n 2-Modification des informations \n 3-Verification de vos informations \n 4-Quitter \n")
    if choice == "1" :
        register()
    elif choice == "2" :
        updateInformation()
    elif choice == "3" :
        checkInformation()
    elif choice == "4" : 
        break
    else :
        print("Le choix que vous avez éffectué est invalide. Vous serez rediriger vers l'interface de choix.")
                