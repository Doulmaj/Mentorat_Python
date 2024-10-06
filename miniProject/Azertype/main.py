from tkinter import * 
from tkinter import messagebox
# -----------------------------------------------------------Functions ----------------------------------------------------------------------------
import json
from random import randint
import time
import threading

remainingTime = 60
score = 0
proposed = 0
donnees = 0

def checkChoice(): 
    global remainingTime
    if x.get() != 0 and x.get() != 1 : 
        messagebox.showinfo(title='Choix du jeu',message='Vous devez choisir une proposition entre "mots" et "phrase" ')
        remainingTime = FALSE
    elif x.get() == 0 : 
        remainingTime = 60 #1 minute pour les mots
    else :
        remainingTime = 3 * 60 # 3 minutes pour les phrases
    return remainingTime


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

def getRessources() : 
    global donnees
    try : 
        with open('ressources.json','r', encoding='utf-8') as ressources : 
            donnees = json.load(ressources)
            donnees = donnees[x.get()] # x.get() permet de choisir entre le tableau correspondant au choix utilisteur
            return donnees
    except FileNotFoundError : 
        donnees = False
        messagebox.showerror(title='ressources.json',message="Le fichier ressources.json n'a pas été trouvé ")
        return donnees
    except json.JSONDecodeError : 
        donnees = False
        messagebox.showerror(title='ressources.json',message="Echec dans la conversion du fichier")
        return donnees

#La fonction qui permet verifier la saisi de l'utilisateur puis de proposer un nouvel élément 
def proposeOneElement() : 
    global remainingTime
    global score
    global proposed
    global donnees
    if userEntry.get() == propositionLabel["text"] : 
        score += 1
    i = randint(0,len(donnees))
    proposition = donnees[i]
    propositionLabel.config(text=proposition)
    userEntry.delete(0,END)
    proposed += 1
    scoreLabel.config(text= f"Votre score : {score}/{proposed}")
    if(remainingTime<=0) : 
        return

def onGoingGame() : 
    global remainingTime
    verification = checkChoice()
    if (verification == False): 
        return
    verification = getRessources()
    if (verification == False) :
        return
    #Gestion du début du jeu
    global score
    global proposed
    global donnees
    i = randint(0,len(donnees))
    proposition = donnees[i]
    propositionLabel.config(text=proposition)
    proposed += 1
    validationButton.config(state=ACTIVE)
    startButton.config(state=DISABLED)
    userEntry.config(state=NORMAL)
    userEntry.bind("<Return>", lambda event: proposeOneElement())
    scoreLabel.config(text= f"Votre score : {score}/{proposed}")
    if(remainingTime<=0) : 
        return

def startGame() : 
    global remainingTime
    try : 
        onGoingGame_thread = threading.Thread(target=onGoingGame)
        onGoingGame_thread.start()
        chrono()

    except Exception as e  : 
        print("error : ",e)
# ------------------------------------------------------------------Interface-----------------------------------------------------------------------



WIDTH = 900
HEIGHT = 550
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
mainFrame.place( x = 0.25*WIDTH, y= 0.05 * HEIGHT )

headerFrame = Frame(mainFrame,
                    bg="white",
                    width= HEADER_WIDTH,
                    height= HEADER_HEIGHT
                    )
headerFrame.pack_propagate(False)
headerFrame.place(x=0, y=0)

titleLabel = Label( headerFrame,
                   text='AZerType',
                   font=(general_font, 20, "bold"),
                   bg="white",
                   fg= color_primary
                   )
titleLabel.place(relx=0.5, rely=0.2, anchor=CENTER) # relx=0.5 et rely=0.5 placent le centre du label au milieu de la Frame.

title2Label = Label( headerFrame,
                    text="L'application pour écrire plus vite",
                    font=(general_font,15),
                    bg= "white",
                    fg=color_secondary
                    )
title2Label.place(relx=0.5, rely=0.45, anchor=CENTER)

title3Label = Label(headerFrame,
                    text= "Azertype est une application pour apprendre à écrire plus vite",
                    font=(general_font, 10),
                    bg= "white",
                    fg= color_secondary
                    )
title3Label.place(relx=0.5, rely=0.7, anchor= CENTER)

bodyFrame = Frame(mainFrame,
                  bg=color_secondary,
                  width= BODY_WIDTH,
                  height= BODY_HEIGHT,
                  padx=4,
                  pady=8
                  )
bodyFrame.pack_propagate(False)
bodyFrame.place(x=0, y=HEADER_HEIGHT)

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
userFrame.pack(padx= (3,3), pady=(15,10))

userEntry = Entry(userFrame,
                  fg=color_primary,
                  bg="white",
                  font=(general_font, 15),
                  width= int(0.07 * BODY_WIDTH),
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
                          command= proposeOneElement
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
                   text="Votre score : 0/0",
                   font=(general_font,11),
                   bg= color_secondary,
                   fg="white"
                   )
scoreLabel.pack(anchor=CENTER)

window.mainloop()


