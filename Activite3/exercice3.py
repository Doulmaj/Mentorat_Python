"""
titre : string (Le titre du livre) auteur : string (L'auteur du livre)
 isbn : integer (Le numéro ISBN du livre)

disponible : boolean (Un booléen indiquant si le livre est disponible à l'emprunt)
"""

class Livre(): 
    def __init__(self,titre,isbn,disponible = True):
        self.__titre = titre
        self.__isbn = isbn
        self.__disponible = disponible

    def getDisponible(self) : 
        return self.__disponible
    
    def getTitre(self) : 
        return self.__titre

    def getDisponibilite(self) : 
        return self.__disponible

    def emprunter(self) : 
        if self.getDisponibilite() == True : 
            self.__disponible = False
            print("livre disponible, prêt accordé")
        else : 
            print("Livre non disponible")

    def retourner(self) : 
        if self.getDisponibilite() == False : 
            self.__disponible = True
            print("Merci d'avoir retourné le livre")
        else : 
            print("Vous n'avez pas emprunter ce livre")

"""
Classe `Membre` :

- Attributs :
nom : string (Le nom du membre)
id_membre : integer (Un identifiant unique pour le membre)
livres_empruntes : list<Livre> (Une liste des livres empruntés par le membre) - 

Méthodes :
emprunter_livre(livre : Livre) : boolean (Permet au membre d'emprunter un livre s'il est disponible)
retourner_livre(livre : Livre) : boolean (Permet au membre de retourner un livre emprunté)
"""
class Membre() : 
    def __init__(self,nom,idMembre,livresEmpruntes = []):
        self.__nom = nom
        self.__idMembre = idMembre 
        self.__livresEmpruntes = livresEmpruntes

    def emprunter_livre(self,livre : Livre) : 
        livre.emprunter()
        self.__livresEmpruntes.append(livre)
        print(f"{self.__nom} a emprunté le livre {livre.getTitre()} ")
    
    def retourner_livre(self,livre : Livre) : 
        livre.retourner()
        self.__livresEmpruntes.remove(livre)
        print(f"{self.__nom} a retourné le livre {livre.getTitre()} ")
    
    def getName(self) : 
        return self.__nom

"""
Classe `Bibliotheque` :
- Attributs : nom : string (Le nom de la bibliothèque)
livres : list (Une liste des livres disponibles dans la bibliothèque) 
membres : list (Une liste des membres inscrits à la bibliothèque)
"""

class Bibliotheque():
    def __init__(self,nom,listeLivres = [],listeMembres = []):
        self.__nom = nom
        self.__listeLivres = listeLivres
        self.__listeMembres = listeMembres

    def ajouterLivre(self,livre:Livre) : 
        self.__listeLivres.append(livre)
        print("Votre livre a été ajouté à la bibliothèque ")

    def inscrireMembre(self,membre : Membre) : 
        self.__listeMembres.append(membre)
        print(f"Le nouveau membre {membre.getName()} a été ajouté à la bibliothèque ")

    def listeLivresDisponibles(self) : 
        a = []
        for livre in self.__listeLivres : 
            if livre.getDisponibilite() == True : 
                a.append(livre.getTitre())
        if len(a)>1 :
            print(f"Voici la liste des livres disponible : '\n' {'\n'.join(a)} " )
        elif len(a) == 1 :
            print(f"Le seul livre disponible est {a[0]}")
        else : 
            print("Aucun livre n'est disponible")
    def listeLivresEmpruntes(self):
        a = []
        for livre in self.__listeLivres : 
            if livre.getDisponibilite() == False : 
                a.append(livre.getTitre())
        if len(a)>0 :
            print(f"Voici la liste des livres Empruntés : '\n'{'\n'.join(a)} " )
        elif len(a) == 1 :
            print(f"Le seul livre emprunté est {a[0]}")
        else : 
            print("Aucun livre n'a été emprunté")

# Création des livres
livre1 = Livre("Le Petit Prince", 123456,True)
livre2 = Livre("1984",234567,True)
livre3 = Livre("Moby Dick",345678,True)

# Création des membres
membre1 = Membre("Alice", 1)
membre2 = Membre("Bob", 2)

# Création de la bibliothèque
bibliotheque = Bibliotheque("Bibliothèque ")

# Ajout des livres à la bibliothèque
bibliotheque.ajouterLivre(livre1)
bibliotheque.ajouterLivre(livre2)
bibliotheque.ajouterLivre(livre3)

# Inscription des membres à la bibliothèque
bibliotheque.inscrireMembre(membre1)
bibliotheque.inscrireMembre(membre2)

# Emprunt de livres
membre1.emprunter_livre(livre1)
membre2.emprunter_livre(livre2)

# Affichage des livres disponibles
bibliotheque.listeLivresDisponibles()

# Affichage des livres empruntés
bibliotheque.listeLivresEmpruntes()

# Retour des livres
membre1.retourner_livre(livre1)
membre2.retourner_livre(livre2)

# Affichage des livres disponibles après retour
bibliotheque.listeLivresDisponibles()
bibliotheque.listeLivresEmpruntes()
        
