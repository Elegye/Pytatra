from tkinter import *

import Exemplaires
import Planchette
import Pioche
import Fenetre
import VuePlanchette

def dessine(fenetre, pioche, gauche):
	# La largeur de la fenetre nous sera utile.
	largeur_fenetre = Fenetre.largeur(fenetre)
	hauteur_fenetre = Fenetre.hauteur(fenetre)
	y0 = hauteur_fenetre - len(pioche)*20
	print(pioche)

	for iteration, exemplaires in enumerate(pioche):
		planchette = Exemplaires.planchette(exemplaires)
		if gauche: #Si on est à gauche
			x0 = 20
			Fenetre.toile(fenetre).create_text(x0, y0, text=Exemplaires.versChaine(exemplaires), anchor='w')
			VuePlanchette.dessine(fenetre, planchette, x0+40, y0)
		else: #Sinon on est à droite
			longueur_planchette = VuePlanchette.pixels(Planchette.longueur(planchette))
			x0 = largeur_fenetre - 40 - longueur_planchette
			Fenetre.toile(fenetre).create_text(x0+longueur_planchette, y0, text=Exemplaires.versChaine(exemplaires), anchor='e')
			VuePlanchette.dessine(fenetre, planchette, x0-40, y0)

		y0 += 20
