class Pokemon() : 
    def __init__(self,nom,hp,atk) : 
        self.__nom = nom
        self.__hp = hp
        self.__atk = atk

    def getNom(self) : 
        return self.__nom
    
    def getHp(self) : 
        return self.__hp
    
    def setHp(self,hp) : 
        self.__hp = hp
    
    def getAtk(self) : 
        return self.__atk
    
    def isDead(self) : 
        if self.__hp <= 0 : 
            print("Le Pokémon est mort")
        else : 
            print("Pokémon toujours vivant ")
    def attaquer( self, p):
        reste = p.getHp() - self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)
    
    def afficher(self) : 
        print("Information du pokémon : ")
        print(f" Nom : {self.getNom()} \n type : {self.getSimpleName()} \n Attaque : {self.getAtk()} \n hp : {self.getHp()} ")
    
    def getClass(self) : 
        return  self.__class__
    
    def getName(self) : 
        return self.__class__.__name__+ "  " + self.__class__.__module__
    
    def getSimpleName(self) : 
        return self.__class__.__name__
    