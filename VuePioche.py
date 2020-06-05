from tkinter import *

import Exemplaires
import Planchette
import Pioche
import Fenetre
import VuePlanchette

Couleur1 = "orange"
Couleur2 = "cornflower blue"

def dessine(fenetre, pioche, gauche):
	# La largeur de la fenetre nous sera utile.
	largeur_fenetre = Fenetre.largeur(fenetre)
	hauteur_fenetre = Fenetre.hauteur(fenetre)
	y0 = hauteur_fenetre - len(pioche)*20

	if gauche:
		Fenetre.toile(fenetre).create_text(100, 300, text="Joueur 1", font=("Purisa", 16))
	else:
		Fenetre.toile(fenetre).create_text(880, 300, text="Joueur 2", font=("Purisa", 16))

	for iteration, exemplaires in enumerate(pioche):
		planchette = Exemplaires.planchette(exemplaires)
		if gauche: #Si on est à gauche
			x0 = 20
			Fenetre.toile(fenetre).create_text(x0, y0, text=Exemplaires.versChaine(exemplaires), anchor='w')
			VuePlanchette.dessine(fenetre, planchette, x0+40, y0, couleur=Couleur1)
		else: #Sinon on est à droite
			longueur_planchette = VuePlanchette.pixels(Planchette.longueur(planchette))
			x0 = largeur_fenetre - 40 - longueur_planchette
			Fenetre.toile(fenetre).create_text(x0+longueur_planchette, y0, text=Exemplaires.versChaine(exemplaires), anchor='e')
			VuePlanchette.dessine(fenetre, planchette, x0-40, y0, couleur=Couleur2)

		y0 += 20
