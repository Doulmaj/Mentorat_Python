import matplotlib.pyplot as plt
import numpy as np

plt.figure(0)
x = np.arange(0,15,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,'r',x,z,'y') #Les paramètres 'r','y' indique la couleur de fonctions, les paramètres (x,y) et (x,z) sont les coordonnées des points à placer pour tracer la fonction
plt.xlabel('abcisse')
plt.ylabel('ordonnee')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()

