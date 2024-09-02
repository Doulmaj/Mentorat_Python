#Opération sur nombre complexe
from math import sqrt

def checkFloat(saisirInput) :
    try:
        float(saisirInput)
        return saisirInput
    except ValueError:
        print("Vous avez mal saisi une donnée")
        return False 
    

#Pour vérifier qu'un complexe est sous la forme a+bi
def checkComplex(form = '') :
    if form == '' : 
        form = input("Veuillez saisir votre nombre complexe sous la forme (a+bi) : ")
    else : 
        form = str(form)
    real = "0"
    imaginary = "0"
    found = False
    start=''
    if form.startswith("-") or form.startswith('+') : 
        start = form[0]
        form = form.replace(form[0],'',1)
    for element in form : 
        if element == "+" or element == "-" : 
            found = True
            form = form.split(element)
            if len(form) == 2 : 
                real =  checkFloat(start+form[0])
                imaginary = checkFloat(element+form[1].replace("i",""))
            elif len(form) > 2 :
                return (False,real,imaginary)
    if found == False : 
        if form.find("i") != -1 : 
            imaginary = checkFloat(start+form.replace("i",""))
        else : 
            real = checkFloat(start+form)
    if imaginary == False or real == False :
        print("Le format que vous avez saisi n'est pas valide")
        return (False,float(real),float(imaginary))
    else : 
        return (True,float(real),float(imaginary)) 
        

class Complex() : 
    def __init__(self) : 
        self.real = 0
        self.imaginary = 0

    def sumComplex(self,nb  ) :
        result = Complex() 
        result.real = self.real + nb.real
        result.imaginary = self.imaginary + nb.imaginary
        print(self.real)
        print(self.imaginary)
        print(nb.real)
        print(nb.imaginary)
        return result
    
    def multiplyComplex(self,nb) : 
        result = Complex()
        real = self.real*nb.real - self.imaginary*nb.imaginary 
        imaginary =self.real*nb.imaginary +self.imaginary*nb.real
        if imaginary >0 : 
            inter = '+'
        else : 
            inter = ''
        result.setComplex(f"{real}{inter}{imaginary}i")
        return result

    def module (self) : 
        return sqrt(self.real**2+self.imaginary**2)
    
    def square(self) : 
        return self.multiplyComplex(self)

    def compare(self,nb) :
        if(self.real==nb.real and self.imaginary == nb.imaginary ) : 
            return "égalité"
        else : 
            return "Pas égal"


    def setComplex(self,value='') :
        valid = False
        while not valid :
            if value == '' : 
                test=checkComplex()
            else : 
                test = checkComplex(value)
            valid = test[0]
        self.real = test[1]
        self.imaginary = test[2]

    def getComplex(self) : 
        return (self.real, self.imaginary)
    
    def __str__(self) :
        real = self.real
        imaginary = self.imaginary
        if self.imaginary == 0 : 
            return f"{real}"
        elif self.imaginary > 0 : 
            imaginary = "+" + str(imaginary)
            return f"{real}{imaginary}i"
        else : 
            return f"{real}{imaginary}i"
    

while True : 
    print()
    print("Que voulez vous faire ? ")
    choice = input("1-Somme de complexe \n2-Produit \n3-module \n4-carrée \n5-comparaison \n6-arrêter \n")
    if choice == '1' : 
        nb1 = Complex()
        nb2 = result = Complex()
        nb1.setComplex()
        nb2.setComplex()
        result = nb1.sumComplex(nb2)
        print(result)
    elif choice =='2' : 
        nb1 = Complex()
        nb2 = result = Complex()
        nb1.setComplex()
        nb2.setComplex()
        result = nb1.multiplyComplex(nb2)
        print(result)
    elif choice == '3' : 
        nb1 = Complex()
        nb1.setComplex()
        print(f"Module de {nb1} : {nb1.module()}")
    elif choice == '4' : 
        nb1 = Complex()
        nb1.setComplex()
        print(f"Carrée de {nb1} : {nb1.square()}")
    elif choice == '5' : 
        nb1 = nb2 = Complex()
        nb1.setComplex()
        nb2.setComplex()
        print(f"Le nombre {nb1} est {nb1.compare(nb2)} à {nb2}")
    elif choice == '6' :
        break
    else : 
        print('Choix invalide')