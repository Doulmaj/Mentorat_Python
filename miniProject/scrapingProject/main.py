# Programme permettant d'obtenir les informations à travers des librairies de pypi.org
import requests
from bs4 import BeautifulSoup
import csv 

choice = input("Veuillez saisir la librairie python que vous voulez chercher : ").strip()
url = f"https://pypi.org/search/?q={choice}&o="
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
header = ['name', 'version', 'creation', 'description', 'lien']
with open('./database/file.csv', 'w', encoding='utf-8') as file :
    writer = csv.writer(file,delimiter=',')
    writer.writerow(header)

listResult = []
searchResults = soup.find_all('a',class_="package-snippet")
for result in searchResults : 
    link =  "https://pypi.org"+result.get('href')
    listSpan = result.h3.find_all('span')
    name = listSpan[0].string
    version = listSpan[1].string
    creation = listSpan[2].time.get_text().strip()
    description = result.p.string
    info = [name, version, creation, description, link]
    listResult.append(info)
    with open('./database/file.csv', 'a', encoding='utf-8') as file :
        writer = csv.writer(file,delimiter=',')
        writer.writerow(info)

print("Les données relatifs à votre requête ont été crée") 

# print(listResult)