import tkinter as tk 

#fenetre de base
Page_garde = tk.Tk()
Page_garde.title("Casino Game")
Page_garde.geometry("1920x1080")
Page_garde.config(bg="white")

Gros_titre = tk.Label(Page_garde, text="BIENVENUE SUR LE CASINO GAME")
Gros_titre.config(font=("Calibri", 30))  
Gros_titre.config(bg="#6A5ACD", fg="white")  
Gros_titre.config(width=85, height=5)
Gros_titre.place(x=0, y=0)

regles = tk.Label(Page_garde, text="Pour afficher les regles appuyez sur la touche H du clavier")
regles.config(font=("Calibri", 15))  
regles.config(bg="white", fg="black")
regles.place(x=500, y=250)

from tkinter import messagebox
def affiche_règles(h):
    messagebox.showinfo("Règles", "Bonjour, bienvenue sur le casino en ligne réalisé par Tonin pour découvrir tkinter, dans ce casino tu trouveras trois mini jeux : pile ou face, les gobelets, chiffre aléatoire. Clique sur le bouton du jeu pour le lancer. Pour afficher les proba des jeux appuis sur J")
Page_garde.bind("h", affiche_règles)

choix_jeu = tk.Label(Page_garde, text="Choisi ton mini jeu :")
choix_jeu.config(font=("Calibri", 30))  
choix_jeu.config(bg="white", fg="black")
choix_jeu.place(x=600, y=350)


def valider1():
    global entree1
    global frame_jeu1
    global bouton
    frame_jeu1 = tk.Frame(Page_garde, width=2000, height=2000)
    frame_jeu1.pack_propagate(False)
    frame_jeu1.config(bg="#FADADD") 
    frame_jeu1.pack()
    Gros_titre = tk.Label(Page_garde, text="JEU DE LA PIECE")
    Gros_titre.config(font=("Calibri", 30))  
    Gros_titre.config(bg="#E1AD01", fg="white")  
    Gros_titre.config(width=85, height=5)
    Gros_titre.place(x=0, y=0)
    demande_age = tk.Label(frame_jeu1, text="Ecris ton choix en lettre minuscule (pile/face):",font=("Arial",20))
    demande_age.config(bg="#FADADD")
    demande_age.place(x=540,y=300)
    entree1 = tk.Entry(frame_jeu1, font=("Calibri", 30))
    entree1.place(x=600,y=400)
    bouton = tk.Button(frame_jeu1, text="Valider", command=control_jeu1)
    bouton.config(width=30, height=2)
    bouton.place(x=670,y=500)

import random
import time 

def control_jeu1():
    global entree1
    global gagne
    global gagne1
    global gagne2
    global perdu
    global perdu1
    global perdu2
    texte = entree1.get()
    choix = random.choice(["pile", "face"])
    if texte != "pile" or texte != "face" :
        erreur = tk.Label(frame_jeu1,text= "il y a une erreur d'orthographe ou un espace en trop")
        erreur.config(bg="#FADADD")
        erreur.config(font=("Calibri", 50)) 
        erreur.place(x=530,y=700)
        time.sleep(3)
        erreur.place_forget()
    elif texte == choix:
        gagne = tk.Label(frame_jeu1,text="     Félicitation tu as gagné        ")
        gagne.config(bg="#FADADD")
        gagne.config(font=("Calibri", 30)) 
        gagne.place(x=480,y=700)
        gagne1 = tk.Label(frame_jeu1,text= str(choix))
        gagne1.config(bg="#FADADD")
        gagne1.config(font=("Calibri", 50)) 
        gagne1.place(x=880,y=600)
        gagne2 = tk.Label(frame_jeu1,text= "resultat :")
        gagne2.config(bg="#FADADD")
        gagne2.config(font=("Calibri", 50)) 
        gagne2.place(x=530,y=600)
    else:
        perdu = tk.Label(frame_jeu1,text="Dommage tu as perdu retente ta chance")
        perdu.config(bg="#FADADD")
        perdu.config(font=("Calibri", 30)) 
        perdu.place(x=480,y=700)
        perdu1 = tk.Label(frame_jeu1,text= str(choix))
        perdu1.config(bg="#FADADD")
        perdu1.config(font=("Calibri", 50)) 
        perdu1.place(x=880,y=600)
        perdu2 = tk.Label(frame_jeu1,text= "resultat :")
        perdu2.config(bg="#FADADD")
        perdu2.config(font=("Calibri", 50)) 
        perdu2.place(x=530,y=600)
    
def valider2():
    frame_jeu2 = tk.Frame(Page_garde, width=2000, height=2000)
    frame_jeu2.pack_propagate(False)
    frame_jeu2.config(bg="#FADADD") 
    frame_jeu2.pack()
    
def valider3():
    frame_jeu3 = tk.Frame(Page_garde, width=2000, height=2000)
    frame_jeu3.pack_propagate(False)
    frame_jeu3.config(bg="#FADADD") 
    frame_jeu3.pack()
    
#FF6600
bouton_jeu1 = tk.Button(Page_garde, text="PILE OU FACE", width=50, height=7, command=valider1)
bouton_jeu1.place(x=200, y=550)
bouton_jeu1.config(bg="#E1AD01")
bouton_jeu2 = tk.Button(Page_garde, text="GOBELET", width=50, height=7, command=valider2)
bouton_jeu2.place(x=600, y=550)
bouton_jeu2.config(bg="#E1AD01")
bouton_jeu3 = tk.Button(Page_garde, text="ALEA CHIFFRE", width=50, height=7, command=valider3)
bouton_jeu3.place(x=1000, y=550)
bouton_jeu3.config(bg="#E1AD01")

#frame verif age 
frame_age = tk.Frame(Page_garde, width=2000, height=2000)
frame_age.pack_propagate(False)
frame_age.config(bg="#FADADD") 
frame_age.pack()

frame_age.lift()

#verif de l'age entry
def valider():
    frame_age.pack_forget()
    
def controle():
    texte = entry.get()
    if int(texte) >= 18:
        valider()
    else:
        tk.Label(frame_age, text="Le Casino est interdit au moins de 18 ans",bg="#FADADD", fg="red").pack()
demande_age = tk.Label(frame_age, text="ENTREZ VOTRE AGE :",font=("Arial",20))
demande_age.config(bg="#FADADD")
demande_age.pack(pady=30)
entry = tk.Entry(frame_age, font=("Calibri", 14))
entry.pack(pady=10)
bouton = tk.Button(frame_age, text="Valider", command=controle)
bouton.pack(pady=30)

#affichage texte page principale

Page_garde.mainloop()

#pas encore terminé xD
