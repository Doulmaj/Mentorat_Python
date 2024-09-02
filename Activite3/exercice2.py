
equivalence = {'ordinaire' : 1000, 'augmenté' : 1300, 'responsable' : 1400}
debut = 0
ens = {}
class Employe() : 
    nombre_employe = 0
    def __init__(self,nom,matricule,indice,type = 'ordinaire') : 
        Employe.nombre_employe += 1
        self.nom = nom
        self.matricule = matricule
        self.indice = indice
        self.type = type
        if isinstance(self,Employe) and (not isinstance(self,Responsable) and not isinstance(self,Commercant)) :
            ens[nom] = self.getSalaire()

    def __str__(self) : 
        return f"l'employé {self.nom},de matricule {self.matricule}, est de type {self.type} "
    
    def getNom(self) : 
        return f"{self.nom}"
    
    def getMatricule (self) : 
        return f"{self.matricule}"
    
    def getIndice(self) : 
        return f"{self.indice}"
    
    def getSalaire(self) : 
        salaire  = self.indice * equivalence[self.type]
        return salaire
    
    def presenter(self) : 
        print(self,f"et à pour salaire {self.getSalaire()} " )


class Responsable(Employe) : 
    nombre_responsable = 0
    def __init__(self,nom,matricule,indice,type = 'ordinaire',listEmploye =[]):
        super().__init__(nom,matricule,indice,type)
        self.type = 'responsable'
        self.listEmploye = listEmploye
        ens[nom] = self.getSalaire()

    def afficherInferieur(self) : 
        print(f"Voici la liste des employés sous les ordres de {self.getNom()} :\n{'\n'.join(self.listEmploye)} ")

    def getInferieur(self) : 
        return self.listEmploye
    

class Commercant(Employe) : 
    def __init__(self, nom, matricule, indice, type='ordinaire',infoVente = {}):
        super().__init__(nom, matricule, indice, type)
        self.infoVente = infoVente
        ens[nom] = self.getSalaire()

    def getSalaire(self) : 
        #Supposons que les commerçants perçoivent 5% de tous ce qu'ils vendent
        pourc = 5
        augmentation = pourc/100 * sum( list(self.infoVente.values()))
        salaire  = self.indice * equivalence[self.type] + augmentation
        return salaire
    
    def getVente (self) : 
        return self.infoVente
    
    def setVente(self,produit,prix) : 
        self.infoVente[produit] = prix
        ens[self.nom] = self.getSalaire()

class Personnel() : 
    def __init__(self,listPersonnel = {}):
        self.listPersonnel = listPersonnel
    def presenterPersonnel(self) : 
        print(f"Voici les membres du personnel : \n{'\n'.join(self.listPersonnel.keys())}")
    def salaireVerse(self) : 
        print(f"Vous devez à la fin du mois un salaire de {sum(self.listPersonnel.values())}") 
        

print('\n','_'*25,"Test de la classe employé",'_'*25,'\n')
employe = Employe("jack",1567,4)
employe1 = Employe("Kapou",567,7)
employe.presenter()

print('\n','_'*25,'Test de la classe Responsable','_'*25,'\n')
responsable = Responsable("Tytoo",456,5,'responsable',['jack','cooper','kitou','reto'])
responsable.presenter()
responsable.afficherInferieur()
responsable.getSalaire()

print('\n','_'*25,'Test de la classe Commercant','_'*25,'\n')
comm = Commercant('pati',567,7,'ordinaire',{'chaise':400,'Fauteuil':500})
comm.presenter()
print()
print(comm.getVente())
comm.setVente('Tableau',600)
print(comm.getVente())
print("Salaire du commercant : ",comm.getSalaire())
print()
ensemble= Personnel(ens)
ensemble.presenterPersonnel()
ensemble.salaireVerse()