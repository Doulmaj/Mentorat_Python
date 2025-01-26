from tkinter import * 
from tkinter import ttk
from Window import Window

class WindowManager(): 
    def __init__(self):
        #Valeur par défaut de variable
        self.generalFont = "Consolas"
        self.generalHeight = 14
        self.fontValues = ["Arial", "Courier", "Consolas", "Times New Roman", "Verdana"]
        self.heightValues = ["8", "9", "10", "11", "12","14","16","18","20","24","28","32","36","40"]
        self.windowList = [] #Liste des fenêtes

newWindowManager = WindowManager()

Root = Window(newWindowManager)
Root.root.mainloop()