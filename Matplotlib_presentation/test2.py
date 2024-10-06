import matplotlib.pyplot as plt
names = ['group a', 'group b', 'group c']
values = [1, 10, 100]
plt.figure( figsize=(9, 3)) #Cette ligne crée une nouvelle figure avec une taille de 9 pouces de large et 3 pouces de haut.
plt.subplot(131) #plt.subplot(131) crée un sous-graphique dans une grille de 1 ligne par 3 colonnes, et le place dans la première position.
plt.bar(names, values) #plt.bar(names, values) crée un diagramme à barres avec les noms des groupes sur l’axe des x et les valeurs sur l’axe des y.
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting') #plt.suptitle('Categorical Plotting') ajoute un titre global à la figure.
plt.show() #plt.show() affiche la figure avec les trois sous-graphiques.