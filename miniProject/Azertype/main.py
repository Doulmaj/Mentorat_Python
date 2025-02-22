from tkinter import * 
from tkinter import messagebox
# -----------------------------------------------------------Functions ----------------------------------------------------------------------------
import json
from random import randint
import time
import threading

remainingTime = 60
totalTime = 0
score = 0 #Cette variable sera utilisé pour connaitre le nombre de caractères que l'utilisateur à trouver
proposed = 0
classification = [] #Liste des classifications en fonction de la vitesse de l'utilisateur
donnees:list [str] = []

def checkChoice(): 
    global remainingTime
    global totalTime
    if x.get() != 0 and x.get() != 1 : 
        messagebox.showinfo(title='Choix du jeu',message='Vous devez choisir une proposition entre "mots" et "phrase" ')
        remainingTime = 0
    elif x.get() == 0 : 
        remainingTime = 60 #1 minute pour les mots      
        totalTime = 1 #Pour indiquer une minute
        chrono()
    elif x.get() ==1 :
        totalTime = remainingTime = 3 * 60 # 3 minutes pour les phrases
        totalTime = 3 #Pour indiquer 3 minutes
        chrono()
    #Actualiser le temps après le choix utilisateur
    timeLabel.config(text= f"Temps restant : {remainingTime//60 :02}:{remainingTime % 60 :02} ")
    return remainingTime

#Pour vérifier si un nombre fait parti d'un intervalle
def checkInIntervall(valMin,valeur , valMax) : 
    return valMin <= valeur < valMax

#Fonction pour connaitre le niveau de l'utilisateur
def getUserLevel(): 
    global classification
    for level in classification : 
        if checkInIntervall(level["wpm_min"], score / 5 * totalTime, level["wpm_max"]): 
            return level

def chrono() : 
    global remainingTime
    if remainingTime > 0 : 
        minutes = remainingTime // 60
        seconds = remainingTime % 60
        timeLabel.config(text= f"Temps restant : {minutes:02}:{seconds:02} ")
        time.sleep(1)
        remainingTime -= 1
        window.after(1000,chrono)
    else : 
        # Gestion à la fin du jeu
        timeLabel.config(text= f"Temps écoulé ")
        validationButton.config(state=DISABLED)
        userEntry.config(state=DISABLED)
        userEntry.unbind("<Return>")
        startButton.config(state=ACTIVE)
        #A la fin du jeu, on affiche le score
        global totalTime
        global score
        scoreLabel.config(text=f"Votre score est de : {score/ 5*totalTime : .2f} WPM (Word Per Minute)  ")
        userLevel = getUserLevel()
        classificationLabel.config(text=f"Vous êtes au niveau : {userLevel['catégorie']}")
        classificationDescrition.config(text=f"Description : {userLevel['description']}")

def getRessources() : 
    global donnees
    global classification
    try : 
        with open('ressources.json','r', encoding='utf-8') as ressources : 
            donnees = json.load(ressources)
            donnees = donnees[x.get()] # x.get() permet de choisir entre le tableau correspondant au choix utilisteur

        with open('classification.json','r', encoding='utf-8') as ressources2 :
            classification = json.load(ressources2) # TODO : liste des classifications en fonction de la vitesse
        
    except FileNotFoundError : 
        donnees = []
        messagebox.showerror(title='ressources.json',message="Le fichier ressources.json ou classification.json n'a pas été trouvé ")
    except json.JSONDecodeError : 
        donnees = []
        messagebox.showerror(title='ressources.json',message="Echec dans la conversion du fichier")
    return donnees

#La fonction qui permet verifier la saisi de l'utilisateur puis de proposer un nouvel élément 
def proposeOneElement() : 
    global remainingTime
    global score
    global donnees
    if (remainingTime > 0) : 
        tabUserEntry = userEntry.get()
        tabProposition = propositionLabel["text"]
        minLength = min(len(tabUserEntry), len(tabProposition))
        for cpt in range(minLength) : 
            if tabProposition[cpt] == tabUserEntry[cpt] : 
                score += 1
        i = randint(0, len(donnees) - 1)
        proposition = donnees[i]
        propositionLabel.config(text=proposition)
        userEntry.delete(0,END)

def onGoingGame() : 
    global remainingTime
    verification = checkChoice()
    if (verification == False): 
        return
    verification = getRessources()
    if (len(verification) == 0) :
        return
    #Gestion du début du jeu
    if (remainingTime >0):
        global donnees
        i = randint(0,len(donnees))
        proposition = donnees[i]
        propositionLabel.config(text=proposition)
        validationButton.config(state=ACTIVE)
        startButton.config(state=DISABLED)
        userEntry.config(state=NORMAL)
        userEntry.bind("<Return>", lambda event: proposeOneElement())

def startGame() : 
    global remainingTime
    global score
    score = 0 #Réunitialisation du score
    userEntry.delete(0,END)
    validationButton.config(state=ACTIVE)
    scoreLabel.config(text="Votre score est en cours de calcul... ")
    classificationLabel.config(text="Votre niveau est en cours de calcul... ")
    classificationDescrition.config(text="La description sera affiché à la fin du jeu")
    try : 
        onGoingGame_thread = threading.Thread(target=onGoingGame)
        onGoingGame_thread.start()

    except Exception as e  : 
        print("error : ",e)
# ------------------------------------------------------------------Interface-----------------------------------------------------------------------



WIDTH = 900
HEIGHT = 620
HEADER_WIDTH = 0.5 * WIDTH
HEADER_HEIGHT = 0.25 * HEIGHT
BODY_WIDTH = 0.5 * WIDTH
BODY_HEIGHT = 0.7 * HEIGHT


color_primary = "#f76c5e"
color_secondary = "#f68e5f"
color_tertiary = "#ffeee6" 
general_font = "Roboto"

window = Tk()

azertypeIcon = PhotoImage(file="images/icon.png")

window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Azertype")
window.iconphoto(True, azertypeIcon)
window.config(bg="white")

mainFrame = Frame(window,
                  width= 0.5 * WIDTH,
                  height= 0.9 * HEIGHT,
                  bg="red")
mainFrame.pack_propagate(False) # Empêche la frame de redimensionner selon les widgets
mainFrame.pack()

headerFrame = Frame(mainFrame,
                    bg="white",
                    width= HEADER_WIDTH,
                    height= HEADER_HEIGHT
                    )
headerFrame.pack_propagate(False)
headerFrame.pack()

titleLabel = Label( headerFrame,
                   text='AZerType',
                   font=(general_font, 20, "bold"),
                   bg="white",
                   fg= color_primary
                   )
titleLabel.pack(anchor=CENTER)

title2Label = Label( headerFrame,
                    text="L'application pour écrire plus vite",
                    font=(general_font,15),
                    bg= "white",
                    fg=color_secondary
                    )
title2Label.pack(anchor=CENTER)

title3Label = Label(headerFrame,
                    text= "Azertype est une application pour apprendre à écrire plus vite",
                    font=(general_font, 10),
                    bg= "white",
                    fg= color_secondary
                    )
title3Label.pack(anchor=CENTER)

bodyFrame = Frame(mainFrame,
                  bg=color_secondary,
                  width= BODY_WIDTH,
                  height= BODY_HEIGHT,
                  padx=4,
                  pady=8
                  )
bodyFrame.pack_propagate(False)
bodyFrame.pack()

propLabel = Label(bodyFrame,
                  text="Choisissez votre option et tapez la proposition qui s'affiche dans le champ en-dessous",
                  bg=color_secondary,
                  wraplength=BODY_WIDTH - 8, # -8 pour enlever l'espace pris par le padding
                  fg="white",
                  justify=CENTER,
                  )
propLabel.pack()

radioFrame = Frame(bodyFrame,
                   width = BODY_WIDTH,
                   height = 0.07 * BODY_HEIGHT,
                   bg=color_secondary
                   )
radioFrame.pack_propagate(False)
radioFrame.place(rely = 0.15, relx=0.77, anchor = CENTER)

choice= ["Mots","Phrases"]
x= IntVar()
for index in range(len(choice)) : 
    choiceRadio = Radiobutton(radioFrame,
                              text=choice[index],
                              variable = x,
                              bg=color_secondary,
                              activebackground=color_secondary,
                              fg="white",
                              activeforeground='white',
                              value= index,
                              font=(general_font,12),
                              selectcolor=color_secondary,
                          )
    choiceRadio.pack(side=LEFT, padx=6)

timeLabel = Label(bodyFrame,
                  text= "Temps restant : 00:00 ",
                  fg=color_primary,
                  bg="white",
                  font=(general_font, 12),
                  justify=CENTER,
                  wraplength = 120,
                  width= int(0.8 * BODY_WIDTH),
                  padx=8,
                  pady=6
                  )
timeLabel.pack(pady=(50,10))

propositionLabel = Label(bodyFrame,
                  text= "",
                  fg=color_primary,
                  bg="white",
                  font=(general_font, 12),
                  justify=CENTER,
                  wraplength = 0.8 * BODY_WIDTH,
                  width= int(0.8 * BODY_WIDTH),
                  padx=9,
                  pady= 10
                  )
propositionLabel.pack()

userFrame = Frame(bodyFrame,
                  bg=color_secondary,
                  width= BODY_WIDTH,
                  height= 27,
                  )
userFrame.pack_propagate(False)
userFrame.pack(padx= (0,1.5), pady=(10,10))

userEntry = Entry(userFrame,
                  fg=color_primary,
                  bg="white",
                  font=(general_font, 15),
                  width= int(0.073 * BODY_WIDTH),
                  )
userEntry.bind("<Return>", lambda event: proposeOneElement())

userEntry.pack(side=LEFT)

validationButton = Button(userFrame,
                          text="Valider",
                          font=(general_font,13),
                          padx=4,
                          pady=4,
                          bg="white",
                          activebackground="white",
                          fg=color_primary,
                          activeforeground=color_primary,
                          command= proposeOneElement,
                          state=DISABLED
                          )
validationButton.pack(side=RIGHT)

startButton = Button(bodyFrame,
                          text="Commencer",
                          font=(general_font,11),
                          padx=4,
                          pady=1,
                          bg="white",
                          activebackground="white",
                          fg=color_primary,
                          activeforeground=color_primary,
                          command= startGame
                          )
startButton.pack(pady= (10,10) ,anchor=CENTER)

scoreLabel = Label(bodyFrame,
                   text=f"Votre score est de : 0 CPM (Character Per Minute) ",
                   font=(general_font,11),
                   bg= color_secondary,
                   fg="white"
                   )
scoreLabel.pack(pady= (10,10),anchor=CENTER)

classificationLabel = Label(bodyFrame,
                            text=f"Vous êtes de niveau : ", #! Changer le contenu en fonction pour afficher le niveau de l'utilisateur
                            font=(general_font,11),
                            bg=color_secondary,
                            fg="white"
                    )

classificationLabel.pack(anchor=CENTER)

classificationDescrition = Label(bodyFrame,
                                 text="Desciption : ",
                                 font=(general_font,11),
                                 bg=color_secondary,
                                 fg="white",
                                 wraplength= 0.95 * BODY_WIDTH 
                    )

classificationDescrition.pack(anchor=CENTER)

window.mainloop()


