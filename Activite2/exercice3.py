import json

#Saisir taille, sexe et poids

#Fonction pour vérifier un réel
def checkTaille(saisirInput) :
    while True: 
        try:
            int(saisirInput)
            return saisirInput
        except ValueError:
            saisirInput =input("La taille que vous avez saisi n'est pas un entier, veuillez réessayer : ")

def checkWeight(saisirInput) :
    while True: 
        try:
            float(saisirInput)
            return saisirInput
        except ValueError:
            saisirInput =input("Le poids que vous avez saisi n'est pas un réel, veuillez réessayer : ")

def checkSex(sexSaisi) : 
    while(sexSaisi != 'M' and sexSaisi !='F' ) : 
        input('Veuillez saisir votre sexe : ') 
    return sexSaisi

def checkBMI():
    taille = int(checkTaille(input('Veuillez saisir votre taille (en cm) : ')))
    poids = int(checkWeight(input('Veuillez saisir votre poids (en Kg) : ')))
    sexe = checkSex(input('Veuillez entrer votre sexe (M/F) : '))

    if sexe == 'M' : 
        varSex = 150
    else : 
        varSex = 120
    print('\n')
    print("_"*100)
    print('\n')

    PI = taille - 100 - (taille -varSex) /4
    print(f'Votre Poids idéal est de : {PI}Kg')

    BMC = poids/(taille/100)**2
    print(f'Votre Indice de masse corporel est de : {BMC}')

    if BMC < 18.5 : 
        decision = 'Maigreur/ Sous-poids'
        id = 0
    elif 18.5<=BMC and BMC< 25 : 
        decision = "Corpulence normale"
        id = 1
    elif 25<=BMC and BMC < 30 : 
        decision = "Surpoids"
        id = 2
    elif 30<=BMC and BMC<35 : 
        decision = "Obésité (modérée)"
        id = 3
    elif 35<=BMC and BMC<40 : 
        decision = "Obésité sévère"
        id = 4
    else :
        decision = "Obésité morbide ou massive"
        id = 5

    print(f"D'après votre IMC, vous êtes en état de : {decision}")


    #Gestion lié au fichier json
    try : 
        with open('./Database/sante.json','r') as sante : 
            donnees = json.load(sante)
    except FileNotFoundError : 
        print("Le fichier n'a pas été trouvé") 
    except json.JSONDecodeError : 
        print("Echec de la conversion du fichier")

    trouve = False
    for donnee in donnees : 
        if donnee["id"] == id : 
            trouve = True
            break
    if  trouve == False : 
        print('\n')
        print("Votre cas semble ne pas repertorié dans notre base de données, c'est suremet une erreur de notre côté et elle sera vite résolue.") 
    else : 
        print("_"*100)
        print('\n')
        print("Voici les informations relatives à votre situation : ")
        print(f"Diagnostic : {donnee["diag"]} \nRaison : {donnee["raison"]}\nConseil: {donnee["conseil"]} ")
    return(sexe,poids,taille,BMC,id)

if __name__ == "__main__":
    checkBMI()

