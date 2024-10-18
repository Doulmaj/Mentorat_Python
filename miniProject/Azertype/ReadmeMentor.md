# REMARQUES PAR RAPPORT AU PROJET "AZERTYPE"

## LES APPRECIATIONS POSITIVES

### LA STRUCTURE ET LA LOGIQUE DU CODE : VALIDE 100%

Tu as fait un bel effort avec la structure du code. Tu as su mettre une différence entrer les données à utiliser et le programme principale. ```Un "hi five" pour ça ✋```

### SEPARATION DU FRONTEND D'AVEC LE BACKEND

J'ai beaucoup apprécié l'organisation du code et la manière dont tu as pu spérarer la logique même c'est-à-dire le backend et l'interface c'est-à-dire le frontend. ```Un petit like pour ça 👍```

### LA LOGIQUE DU CODE

L'organisation du programme en petites fonctions est très bien pensée. ```Chapeau 🤠```




## LES SUGGESTIONS D'AMELIORATION

### LE SCORE : FONCTIONNEMENT DU SCORE

1. D'après le message de présentation sur l'application, cette dernière va permettre à l'utilisateur d'améliorer ses saisies ou du moins sa vitesse au clavier. Sur ce le score devrait être présenté en mots par minute (**WPM: Word Per Minute**) ou en caractère par minute (**CPM: Character Per Minute**). Cela permettra à l'utilisateur de connaître sa vitesse au clavier dans les unités internationales et pourra la comparer selon les standards actuels de classification (c'est-à-dire **lent, moyen, rapide, ...**)
2. Aussi si tu augmentais le nombre de mots à saisir, ce serait bien parce que taper une mot et valider avant de voir le mot second, réfléchir à où commencer avant de commencer, taper valider et ainsi de suite fait perdre du temps (petit mais très significatif) Par exemple, pour un individu qui a une vitesse normale ou moyenne (entre **40** et **50 WPM**)
3. Pour l'option **Phrases**, il n'y a pas d'arrêt

### LE POSITIONNEMENT DES ELEMENTS

1. _Utiliser la méthode_ **```pack()```** _au lieu de_ **```place()```** _pour les objects **headerFrame, bodyFrame, les labels**, ... comme :_
```python
bodyFrame.pack()
```


### LA LOGIQUE DU CODE

1. ```Ligne 12```, _la déclaration de la variable donnees: pas un entier mais typer cela dès le départ comme ceci donnees :_
```python
donnees:list[str] = []
OR
donnees = []
```
2. ```Ligne 51 et 55```, _au lieu de :_
```python
donnees = False
```
_plutôt_
```python
donnees = None
OR
donnees = [] # Une liste vide
```
3. ```Ligne 18``` : _déjà après avoir typé la variable_ ```remainingTime``` _à_ ```int``` _à la ligne 9 plutôt remplacer sa valeur par_ ```0``` _ou faire un directement ..._
```python
return False
``` 
4. **```getRessources()```** : _autant faire un return directement que de faire une assignation de False à la variable donnees, vu qu'il est déjà une liste. Le fait est de respecter le typage des variables, car cela facilite dans la rédaction du code et une fluidité dans la compréhension de son fonctionnement_
5. _A la création du bouton de validation, tu pourras aussi donner un_ ```state False``` _par défaut et l'activer après au début du jeu_
6. _L'intérêt des_ ```lignes 73 et 74```_, des ```lignes 97 et 98```_
7. _Pour le score, ce n'est pas le même fonctionnement pour les deux options :_ ```Mots``` & ```Phrases```
8. ```Ligne 68``` : _au lieu de_
```python
i = randint(0, len(donnees))
``` 
_faire plutôt_
```python
i = randint(0, len(donnees) - 1)
```
9. _Remplir la base de données avec des données json. Pour les apostrophes, les accents, les émojis, ... json les représente sous format ascii genre_ ```"\u5013"``` _par exemple. J'ai écrit ce bout de code qui se trouve dans le fichier [fill_database](fill_database.py)_


## INSPIRATION A TRAVERS LES APPLICATIONS (LOGICIELS) OU SITES DE DACTYLOGRAPHIE DEJA DISPONIBLES

...
