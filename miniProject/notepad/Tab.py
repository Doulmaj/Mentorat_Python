# Définition de la structure d'un onglet

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tab() : 

    def __init__(self, master, content: str, savingState: bool = True) :
        self.master = master #Désigne la fenêtre qui héberge l'onglet
        self.notebook:ttk.Notebook = master.notebook #Designe le notebook liée au à la fenêtre
        self.contentArea:Text #Designe le widget Text de la frame
        self.content:str = content #Designe le contenu de la zone de texte
        self.savingState:bool = savingState #Variable pour savoir si vous avez sauvegardé ce que vous saisissiez dans le notepad
        self.defaultPath:str = "" #Variable stockant le chemin par défaut pour enregistrer le contenu du notepad
        
        # Fenêtre principale
        self.frame = Frame(self.notebook, bg="white")
        self.frame.pack(fill=BOTH, expand=True)  # Pour occuper tout l'espace et rendre la fenêtre responsive

        #Button de fermeture
        closeButton = Button(self.frame, text="Fermer", command=self.close_tab)
        closeButton.pack(anchor=NE, padx=4, pady=4)  # Placer le bouton en haut à droite

        #Zone de saisi de texte
        self.contentArea = Text(self.frame, font=("Consolas", 14), undo=True)
        self.contentArea.insert(END, content)
        self.contentArea.pack(fill=BOTH, expand=True)  # Le Text prend tout l'espace disponible
        self.contentArea.bind('<Key>',self.occured_modification)
    
    #fonction de gestion de la fermeture de l'onglet en foction du choix de l'utilisateur
    def close_tab(self):
        #Traitement en fonction de l'état d'enregistrement du fichier
        if self.savingState == False:
            response = messagebox.askyesnocancel(title="Enregistrer" ,message="Voulez-vous enregistrer les modifications apportées à ce fichier ?")
        else:
            response = False
        
        #Gestion de la fermeture de l'onglet
        if response == True:
            self.master.saveFile()
            self.definitive_tab_close()
        elif response == False:
            self.definitive_tab_close()
        else :
            return
        
    # Fonction de fermeture de l'onglet à proprement dite
    def definitive_tab_close(self):
        try:
            indexOfTab = self.notebook.index(self.notebook.select()) #Récupérer l'index de l'onglet courant
            # Gestion danans le cas où c'est le dernier onglet qu'il faut fermer
            tabList = self.notebook.tabs()
            if len(tabList) > 2 and indexOfTab == len(tabList) - 2 : #On verifie si on est sur l'avant dernier onglet puisque le dernier est celui avec le titre "+" 
                self.notebook.select(tabList[len(tabList) - 3]) #On vient alors sur l'onglet précédent ce dernier onglet
            self.notebook.forget(indexOfTab)
            del self.master.tabManagerList[indexOfTab] #Retirer l'onglet fermé de la fenêtre
        except Exception as e : 
            messagebox.showerror(title="Erreur à la fermeture de l'onglet", message="Un problème inattendu vient de surgir, veuillez consulter votre console pour de plus ample explication")
            print(e)
    
    def occured_modification(self, event):
        self.savingState = False