from Pokemon import Pokemon

class PokemonFeu(Pokemon) : 
    def __init__(self, nom, hp, atk):
        super().__init__(nom, hp, atk)

    def attaquerPlante(self, p : Pokemon) :
        reste = p.getHp() - 2 * self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0) 

    def attaquerFeuEau(self,p:Pokemon):
        reste = p.getHp() - 0.5 * self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)

class PokemonEau(Pokemon) : 
    def __init__(self, nom, hp, atk):
        super().__init__(nom, hp, atk)

    def attaquerFeu(self, p):
        reste = p.getHp() - 2 * self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)

    def attaquerPlanteEau(self,p) : 
        reste = p.getHp() - 0.5 * self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)

class PokemonPlante(Pokemon) : 
    def __init__(self, nom, hp, atk):
        super().__init__(nom, hp, atk)
    
    def attaquerEau(self,p) : 
        reste = p.getHp() - 2 * self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)

    def attaquerPlanteFeu(self,p) : 
        reste = p.getHp() - 0.5 * self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)
        

pikachu = Pokemon("Pikachu", 100, 20)
salameche = PokemonFeu("Salamèche", 80, 25)
carapuce = PokemonEau("Carapuce", 90, 15)
bulbizarre = PokemonPlante("Bulbizarre", 85, 18)

print("Avec Pokémon Normal")

pikachu.afficher()
salameche.afficher()
print("Attaquer Salameche")
pikachu.attaquer(salameche)
salameche.afficher()

print()
print("Pokémon spéciale ")

carapuce.afficher()
bulbizarre.afficher()
bulbizarre.attaquerEau(carapuce)
carapuce.afficher()
bulbizarre.attaquerPlanteFeu(salameche)
salameche.afficher()