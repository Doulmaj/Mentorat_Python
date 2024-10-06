import matplotlib.pyplot as plt
plt.figure(1)
plt.pie(x = [25285,14255,15225,12670,13905,16500], labels = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June'],
           colors = ['#5830f3', '#7644e3', '#16369b', '#16e5cb', '#7ecff1','#c7d8f0'],
           autopct = lambda x: str(round(x, 2)) + '%') # autopct = lambda x: str(round(x, 2)) + '%' : Une fonction lambda qui formate les pourcentages affichés sur chaque secteur. Elle arrondit les valeurs à deux décimales et ajoute un symbole de pourcentage.
plt.legend()
plt.show()