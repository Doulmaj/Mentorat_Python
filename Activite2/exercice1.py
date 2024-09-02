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

taille = int(checkTaille(input('Veuillez saisir votre taille (en cm) : ')))
poids = int(checkWeight(input('Veuillez saisir votre poids (en Kg) : ')))
sexe = checkSex(input('Veuillez entrer votre sexe (M/F) : '))

if sexe == 'M' : 
    varSex = 150
else : 
    varSex = 120

PI = taille - 100 - (taille -varSex) /4
print(f'Votre Poids idéal est de : {PI}Kg')

BMC = poids/(taille/100)**2
print(f'Votre Indice de masse corporel est de : {BMC}')
