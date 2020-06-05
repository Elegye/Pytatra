###############################################################################
# Alexandre Halopé 05/06/2020 Version Finale
# Repository : https://github.com/Elegye/Pytatra
# Au premier démarrage, en l'absence de sauvegarde ou de replay disponibles,
# le jeu se lance. Avec une sauvegarde ou un replay, on peut choisir entre
# reprendre une sauvegarde, ou une partie normale.
#
###############################################################################

from tkinter import * # Juste pour créer les boutons.
from os import path # Vérifier si les fichiers existent.
import pickle #Pickle pour sauvegarder des données.
import Jeu
import Dialogue
import Fenetre

def partieNormale(event, fenetre=None):
    if fenetre != None:
        Fenetre.quitte(fenetre)
    jeu = Jeu.cree()
    Jeu.joue(jeu)

def partieReplay(event, fenetre):
    Fenetre.quitte(fenetre)
    jeu = Jeu.cree()
    Jeu.joue(jeu, is_replay=True)

def partieSauvegarde(event, fenetre):
    Fenetre.quitte(fenetre)
    sauvegarde = pickle.load(open("save.txt", "rb"))
    jeu = (
        Fenetre.cree(1000, 600),
        sauvegarde[0],
        sauvegarde[1],
        sauvegarde[2]
    )
    Jeu.joue(jeu, is_save=True)

if path.exists('save.txt') or path.exists('replay.txt'): #On regarde s'il existe une sauvegarde ou un replay
    fenetre = Fenetre.cree(300,300)

    normale = Button(Fenetre.toile(fenetre), text="Nouvelle partie")
    normale.bind("<Button-1>", lambda event : partieNormale(event, fenetre))

    save = Button(Fenetre.toile(fenetre), text="Charger dernière sauvegarde")
    save.bind("<Button-1>", lambda event : partieSauvegarde(event, fenetre))

    normale.pack()
    save.pack()

    if path.exists("replay.txt"):
        replay = Button(Fenetre.toile(fenetre), text="Replay dernière partie")
        replay.bind("<Button-1>", lambda event : partieReplay(event, fenetre))
        replay.pack()

    Fenetre.bouclePrincipale(fenetre)
else:
    partieNormale()
