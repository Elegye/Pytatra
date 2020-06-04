from os import path
import pickle
import Jeu
import Dialogue
import Fenetre

def partieNormale():
    jeu = Jeu.cree()
    Jeu.joue(jeu)

if path.exists('save.txt'): #On regarde s'il existe une sauvegarde
    replay = Dialogue.yesNoMessage("Voulez-vous recommencer la dernière partie sauvegardée ?")
    if replay:
        print("REPRENDRE")
        sauvegarde = pickle.load(open("save.txt", "rb"))
        jeu = (
            Fenetre.cree(1000, 600),
            sauvegarde[0],
            sauvegarde[1],
            sauvegarde[2]
        )
        Jeu.joue(jeu)
    else:
        partieNormale()
else:
    partieNormale()
