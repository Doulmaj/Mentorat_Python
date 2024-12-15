from tkinter import * 
from tkinter import ttk, messagebox, filedialog, simpledialog
from pathlib import Path
from Tab import Tab
from datetime import datetime


class Window(): 
    
    def __init__(self, generalFont = "Consolas", generalHeight = 11):
        #Attributs
        self.root: Tk = Tk() 
        self.notebook: ttk.Notebook = ttk.Notebook(self.root)
        self.tabManagerList: list [Tab] = [] #liste des onglets ouverts
        self.firstCreation: bool = True #Variable pour savoir si c'est la première fois qu'on crée la fenêtre ou pas

        #Paramètres de la fenêtre
        WIDTH = 900
        HEIGHT = 450
        #Gestion de la fenêtre
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.title("Notepad")
        self.root.config(bg="white")

        self.notebook.pack(fill=BOTH, expand=True)
        #Barre de choix
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        #Menu fichier
        fileMenu = Menu(menubar,tearoff=0,font=(generalFont,13))
        menubar.add_cascade(label="Fichier",menu=fileMenu)
        fileMenu.add_command(label="Nouvel Onglet", command=self.createTab, accelerator="Ctrl+T")
        fileMenu.add_command(label="Nouvel fenêtre", command=self.createWindow, accelerator="Ctrl+N") #Partie à revoir
        fileMenu.add_command(label="Ouvrir", command=self.openFile, accelerator="Ctrl+O")
        fileMenu.add_command(label="Enregistrer", command=self.saveFile, accelerator="Ctrl+S")
        fileMenu.add_command(label="Enregistrer sous", command=self.saveFileAs, accelerator="Ctrl+Maj+S")
        fileMenu.add_command(label="Fermer onglet", command=self.closeActualTab, accelerator="Ctrl+W")
        fileMenu.add_command(label="Fermer fenêtre",command=self.closeWindow, accelerator="Ctrl+Maj+W")
        fileMenu.add_command(label="Quitter", command=self.quitProgramm)

        #Menu modification
        modificationMenu = Menu(menubar, tearoff=0, font=(generalFont,13))
        menubar.add_cascade(label="Modifier", menu=modificationMenu)
        modificationMenu.add_command(label="Retour arrière", accelerator="Ctrl+Z", command=self.undo)
        modificationMenu.add_command(label="Retour avant", accelerator="Ctrl+Y", command=self.redo)
        modificationMenu.add_separator()
        modificationMenu.add_command(label="Couper", accelerator="Ctrl+X", command=self.Cut)
        modificationMenu.add_command(label="Copier", accelerator="Ctrl+C", command=self.Copy)
        modificationMenu.add_command(label="Coller", accelerator="Ctrl+V", command=self.Paste)
        modificationMenu.add_separator()
        modificationMenu.add_command(label="Rechercher", accelerator="Ctrl+F", command=self.search)
        modificationMenu.add_command(label="Atteindre", accelerator="Ctrl+G", command=self.Reach)
        modificationMenu.add_command(label="Remplacer", accelerator="Ctrl+H", command=self.replace)
        modificationMenu.add_separator()
        modificationMenu.add_command(label="Tout sélectionner", accelerator="Ctrl+A", command=self.selectAll)
        modificationMenu.add_command(label="Heure/date", accelerator="F5", command=self.insertHourAndDate)

        #Création de l'onglet qui permet d'ajouter un nouvel onglet en cliquant sur lui
        tab = Frame(self.notebook)
        self.notebook.add(tab, text = "+")
        self.notebook.bind("<<NotebookTabChanged>>", self.checkForNewTab)

        # Définit l'action à réaliser quand l'utilisateur tente de fermer la fenêtre (en cliquant sur la croix)
        self.root.protocol("WM_DELETE_WINDOW", self.closeWindow)

        #Gestion des raccourci
        self.root.bind("<Control-t>", self.createTab)
        self.root.bind("<Control-n>", self.createWindow)
        self.root.bind("<Control-o>", self.openFile)
        self.root.bind("<Control-s>", self.saveFile)
        self.root.bind("<Control-Shift-S>", self.saveFileAs)
        self.root.bind("<Control-w>", self.closeActualTab)
        self.root.bind("<Control-Shift-W>", self.closeWindow)
        self.root.bind("<Control-z>", self.undo)
        self.root.bind("<Control-y>", self.redo)
        self.root.bind("<Control-v>", self.Paste)
        self.root.bind("<Control-f>", self.search)
        self.root.bind("<Control-g>", self.Reach)
        self.root.bind("<Control-h>", self.replace)
        self.root.bind("<Control-a>", self.selectAll)
        self.root.bind("<F5>", self.insertHourAndDate)


    # Fonction permettant de savoir si on a cliqué sur l'onglet "+" et si c'est le cas, il créée un nouvel onglet
    def checkForNewTab(self, event=None):
        tabList = self.notebook.tabs()
        if len(tabList) == 1 and self.firstCreation == False : #Fermer la fenêtre lorsqu'il ne reste que l'onglet "+" et qu'on est pas à la première création de la fenêtre
            try :
                self.root.destroy()
                return
            except Exception as e : 
                print(e)
        index = self.notebook.index(self.notebook.select())
        if index == len(tabList)-1: #L'onglet "+" occupe toujours la 
            self.createTab()

    #Fonction permettant de créer un nouvel onglet
    def createTab(self, event = None, tabContent = "", tabTitle = "Nouvel onglet" ):
        tab = Tab(self, tabContent)
        self.tabManagerList.append(tab) #Ajout de l'onglet à la liste
        tabList = self.notebook.tabs()
        if len(tabList) == 0:
            self.notebook.add(tab.frame, text=tabTitle )
        else:
            self.notebook.insert(len(tabList)-1,tab.frame,text=tabTitle )
            tabList = self.notebook.tabs() #mettre à jour la liste des onglets
            self.notebook.select(tabList[len(tabList)-2]) #Visualiser automatiquement, l'onglet qui a été crée
        self.firstCreation = False # Changer la valeur de firstCreation, quand on est pas à la première création de la fenêtre
    
    #Fonction permettant de créer une nouvelle fenêtre
    def createWindow(self, event= None):
        window = Window()

    #Fonction permettant d'ouvrir un fichier et son contenu dans un nouvel onglet
    def openFile(self, event = None): 
        # Récupérer le chemin du fichier courant (script)
        script_path = Path(__file__).resolve()
        # Obtenir le répertoire du script
        script_dir = script_path.parent
        filepath = filedialog.askopenfilename(  #Utiliser os, pour récupérer le chemin d'accès courant du fichier
                                            initialdir=f"{script_dir}\\files",
                                            title= "Ouvrir",
                                            filetypes=(("text files", "*.txt"),("python file","*.py"),("all files","*.*"))
                                           )
        if len(filepath) == 0 : 
            return
        file = open(filepath, 'r')
        filename = filepath.split("/")[-1] #nom du fichier ouvert sans mention du chemin d'accès
        fileContent = file.read() #contenu du fiichier ouvert
        file.close()
        self.createTab(tabContent=fileContent, tabTitle=filename)
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        currentTab.defaultPath = file.name #Affecter le chemin du fichier ouvert à la variable de l'onglet qui lui est dédié
    
    #Fonction permettant de sauvegarder le contenu d'un fichier dans un repertoire spécifique
    def saveFileAs(self, event = None):
        # Récupérer le chemin du fichier courant (script)
        script_path = Path(__file__).resolve()
        # Obtenir le répertoire du script
        script_dir = script_path.parent
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        file = filedialog.asksaveasfile(initialdir=f"{script_dir}\\files",
                                        defaultextension=".txt",
                                        filetypes=[("Text file",".txt"),("Python file",".py"),("All files",".*")])
        if file is None :
            return
        fileContent = str(currentTab.contentArea.get("1.0",END))
        file.write(fileContent)
        currentTab.defaultPath = file.name #Pour changer le chemin d'accès par défaut de l'onglet
        newTabTitle = file.name.split("/")[-1] #Nom du fichier ouvert sans mention du chemin d'accès
        file.close
        currentTab.savingState = True #Pour indiquer le fichier a été enregistré
        self.notebook.tab(self.notebook.select(), text = newTabTitle)

    #Fonction permettant de sauvegarder le contenu d'un fichier
    def saveFile(self, event=None):
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        if len(currentTab.defaultPath) == 0: #S'il n'y a pas de chemin de sauvegarde par défaut
            self.saveFileAs(event)
        else:
            newFileContent = str(currentTab.contentArea.get("1.0",END))
            file = open(currentTab.defaultPath,'w')
            file.write(newFileContent)
            file.close()
            currentTab.savingState = True #Pour indiquer le fichier a été enregistré
    
    #Fonction permettant de fermer l'onglet en cours d'utilisation
    def closeActualTab(self, event=None):
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        currentTab.close_tab()
    
    #Fonction permettant de fermer la fenêtre
    def closeWindow(self, event=None):
        #Il faut procéder par indice et non par élément même
        tabList = list(self.notebook.tabs())
        for i in range(len(tabList)-2, -1, -1) :
            self.notebook.select(tabList[i])
            self.tabManagerList[i].close_tab()

    #Fonction permettant de fermer le programme
    def quitProgramm(self, event =None):
        response = messagebox.askyesno(title="quiter", message="Voulez-vous quitter ce programme ?")
        if response == True:
            self.root.quit()
    
    #Fonction permettant le retour en arrière sur l'onglet actuel
    def undo(self, event = None):
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        try:
            currentTab.contentArea.edit_undo()
        except Exception as e:
            # Vérifie si l'erreur est "Nothing to undo"
            if str(e) == "nothing to undo":
                pass  # Ne rien afficher dans la console si l'erreur est "Nothing to undo"
            else:
                messagebox.showerror(title="Erreur", message="Une erreur est survenue lors du retour arrière. Veuillez verifier votre console pour plus d'informations")
                print("Erreur Undo:", e)  # Affiche les autres erreurs dans la console

    #Fonction permettant le retour en avant sur l'onglet actuel
    def redo(self, event = None):
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        try:
            currentTab.contentArea.edit_redo()
        except Exception as e:
            #Si l'erreur est "Nothing to redo"
            if str(e) == "nothing to redo":
                pass # Ne rien afficher dans la console si l'erreur est "Nothing to undo"
            else:
                messagebox.showerror(title="Erreur", message="Une erreur est survenue lors du retour avant. Veuillez verifier votre console pour plus d'informations")
                print("Erreur Redo:", e)

    #Fonction permettant de copier le texte sélectionné
    def Copy(self, event = None):
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        try:
            selection = currentTab.contentArea.get("sel.first","sel.last") #Récupérer la sélection
            if selection:
                currentTab.contentArea.clipboard_clear() #Effacer le presse-papiers prrécédent
                currentTab.contentArea.clipboard_append(selection) #Copier dans le presse-papier
        except TclError :
            pass #lorsque la sélection est vide, ne rien faire

    #Fonction permettant de couper le texte sélectionné
    def Cut(self, event = None):
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        try:
            selection = currentTab.contentArea.get("sel.first","sel.last") #Récupérer la sélection
            if selection:
                currentTab.contentArea.clipboard_clear() #Effacer le presse-papiers prrécédent
                currentTab.contentArea.clipboard_append(selection) #Copier dans le presse-papier
                currentTab.contentArea.delete("sel.first", "sel.last")  # Supprimer la sélection
        except TclError :
            pass #lorsque la sélection est vide, ne rien faire

    #Fonction permettant de coller le texte du presse-papier
    def Paste(self, event = None):
        indexOfTab = self.notebook.index(self.notebook.select())
        currentTab = self.tabManagerList[indexOfTab]
        try : 
            content = currentTab.contentArea.clipboard_get() #Récupérer le contenu du presse-papier
            if currentTab.contentArea.tag_ranges("sel"): #Vérifier s'il y a sélection 
                currentTab.contentArea.delete("sel.first", "sel.last") #Supprimer la sélection si elle existe
                currentTab.contentArea.insert(INSERT, content)
            else:
                currentTab.contentArea.insert(INSERT, content)

        except TclError:
            pass #Lorsque la sélection est vide

    #Fonction permettant de rechercher toutes les occurences d'un mot
    def search(self, event = None):

        currentTab = self.tabManagerList[self.notebook.index(self.notebook.select())] #Pour connaitre l'onglet courant
        contentArea : Text= currentTab.contentArea
        found = False #Variable pour savoir si le mot cherché est dans le texte
        
        self.removeHighLight(contentArea)

        #texte a rechercher
        search_term = simpledialog.askstring(title="Rechercher", prompt="Entrer le texte à rechercher")
        if not search_term:

            return
        
        respect_casse = messagebox.askyesno(title="Casse", message="Respecter la casse ?")

        #Initialiser la recherche
        start_index = "1.0"

        #On parcourt tout le texte et si on voit une occurence du mot à chercher, on la surligne et ceci jusqu'à ce qu'on ait surligné toutes les occurences
        while True:
            if respect_casse:
                start_index = contentArea.search(search_term, index=start_index, stopindex=END)
            else:
                start_index = contentArea.search(search_term, index= start_index, stopindex=END, nocase=True)

            if not start_index :  
                if not found : 
                    messagebox.showinfo(title="Rechercher", message="Le mot recherché n'est pas dans le texte")
                
                break

            #Surlignage du mot trouvé
            found = True
            end_index = f"{start_index}+{len(search_term)}c"
            contentArea.tag_add("highlight", start_index, end_index)
            contentArea.tag_configure("highlight", background="yellow")
            start_index = end_index

    #Fonction pour retirer le surlignage d'un élément
    def removeHighLight (self, textArea: Text):
        try:
            # Supprimer le surlignage de tous les mots
            textArea.tag_remove("highlight", "1.0", "end")
        except Exception as e:
            print(e)

    #FOnction pour atteindre une ligne en en saisissant le numéro
    def Reach(self, event = None): 
        currentTab = self.tabManagerList[self.notebook.index(self.notebook.select())] #Pour connaitre l'onglet courant
        contentArea : Text= currentTab.contentArea
        #Demander à l'utilisateur de saisir la ligne à atteindre
        line_number = simpledialog.askinteger(title="Atteindre", prompt="Veuillez saisir la ligne à atteindre")
        if line_number : 
            try : 
                contentArea.mark_set(INSERT, index=f"{line_number}.0")
                contentArea.see(f"{line_number}.0")
            except TclError: 
                messagebox.showerror(title="Erreur", message=f"La ligne {line_number} n'existe pas ")

    #Fonction pour remplacer un mot dans le texte par un autre
    def replace(self, event = None): 
        currentTab = self.tabManagerList[self.notebook.index(self.notebook.select())] #Pour connaitre l'onglet courant
        contentArea : Text= currentTab.contentArea
        # Demander le texte à rechercher et celui de remplacement
        search_term = simpledialog.askstring(title="Rechercher", prompt="Entrez le texte à rechercher :")
        replace_term = simpledialog.askstring(title="Remplacer", prompt="Entrez le texte de remplacement :")
        if search_term and replace_term:
            content = contentArea.get("1.0", END)
            changed_content = content.replace(search_term, replace_term)
            contentArea.delete("1.0", END)
            contentArea.insert("1.0", changed_content)

    #Fonction pour sélectionner tout le contenu de la zone de texte
    def selectAll(self, event = None):
        currentTab = self.tabManagerList[self.notebook.index(self.notebook.select())] #Pour connaitre l'onglet courant
        contentArea : Text= currentTab.contentArea
        contentArea.tag_add("sel", "1.0", END)
        contentArea.mark_set("insert", "1.0")  # Déplace le curseur au début de la sélection
        contentArea.see("insert")  # Déplace la vue pour voir la sélection

    #Fonciton permettant d'insérer l'heure et la date à la position actuelle du curseur
    def insertHourAndDate(self, event = None):
        currentTab = self.tabManagerList[self.notebook.index(self.notebook.select())] #Pour connaitre l'onglet courant
        contentArea : Text= currentTab.contentArea
        actualTime = datetime.now() #Recupérer le temps actuel
        formatedTime = actualTime.strftime("%d-%m-%Y %H:%M:%S") #formaté le temps 
        contentArea.insert(INSERT, formatedTime) # Insertion à la position du curseur
