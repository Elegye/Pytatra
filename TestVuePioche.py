import Pioche
import Fenetre
import VuePioche

pioche = Pioche.cree()
print(Pioche.versChaine(pioche))

f = Fenetre.cree(1000, 600)
VuePioche.dessine(f, pioche, gauche=True)
VuePioche.dessine(f, pioche, gauche=False)
Fenetre.affiche(f)