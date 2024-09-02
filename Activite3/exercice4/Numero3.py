from Pokemon import Pokemon

class PokemonFeu(Pokemon) :
    def attaquer(self, p:Pokemon):
        if p.getSimpleName() == "PokemonPlante" : 
            reste = p.getHp() - 2 * self.getAtk()
        elif p.getSimpleName() == "PokemonFeu" or p.getSimpleName() == "PokemonEau" : 
            reste = p.getHp() - 0.5 * self.getAtk()
        else : 
            reste = p.getHp() - self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)

class PokemonEau(Pokemon) :
    def attaquer(self, p:Pokemon):
        if p.getSimpleName() == "PokemonFeu" : 
            reste = p.getHp() - 2 * self.getAtk()
        elif p.getSimpleName() == "PokemonEau" or p.getSimpleName() == "PokemonPlante" : 
            reste = p.getHp() - 0.5 * self.getAtk()
        else : 
            reste = p.getHp() - self.getAtk()
        print(f"Le pokémon {self.getNom()} inflige {p.getHp() - reste} au Pokémon {p.getNom()} ")
        if reste >0 : 
            p.setHp(reste)
        else : 
            p.setHp(0)

class PokemonPlante(Pokemon) :
    def attaquer(self, p:Pokemon):
        if p.getSimpleName() == "PokemonEau" : 
            reste = p.getHp() - 2 * self.getAtk()
        elif p.getSimpleName() == "PokemonFeu" or p.getSimpleName() == "PokemonPlante" : 
            reste = p.getHp() - 0.5 * self.getAtk()
        else : 
            reste = p.getHp() - self.getAtk()
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
bulbizarre.attaquer(carapuce)
carapuce.afficher()
bulbizarre.attaquer(salameche)
salameche.afficher()