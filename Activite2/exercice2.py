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

if BMC < 18.5 : 
    decision = 'Maigreur/ Sous-poids'
elif 18.5<=BMC and BMC< 25 : 
    decision = "Corpulence normale"
elif 25<=BMC and BMC < 30 : 
    decision = "Surpoids"
elif 30<=BMC and BMC<35 : 
    decision = "Obésité (modérée)"
elif 35<=BMC and BMC<40 : 
    decision = "Obésité sévère"
else :
    decision = "Obésité morbide ou massive"

print(f"D'après votre IMC, vous êtes en état de : {decision}")
