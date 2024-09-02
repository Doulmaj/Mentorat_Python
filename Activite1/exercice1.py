#Écrire un programme qui, à partir de la saisie de deux réels et un opérateur affiche le résultat après exécution de l’opération choisie. 

def CheckFloat(x) : 
    if x.isdigit():
        x= float(x)
    else : 
        print("Ce que vous avez saisi n'est pas un nombre donc il pendra la valeur par défaut 0 ")
        x=0
    return x

a = input('Veuillez saisir le premier nombre : ')
a = CheckFloat(a)
b = input('Veuillez saisir le second nombre : ')
b= CheckFloat(b)

op = input("Choisissez l'opération à effectuer (+ , -, * /) : ")

if b==0 and op=='/' :
    print('La division par 0 est impossible')
else : 
    operation = {
        '+' : a+b,
        '-' : a-b,
        '*' : a*b,
        '/' : a/b
    }

    try: 
        result = operation[op]
        print(a,op,b,'=',result)
    except: 
        print('Cette opération n\'est pas défini')