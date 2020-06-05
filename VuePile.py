from tkinter import *

import Planchette
import Empilement
import Fenetre
import VuePlanchette
import VuePioche

def dessine(fenetre, pile):
	for i in range(len(pile)) :
		# coordonnées du coin inférieur gauche de la planchette
		x0 = Fenetre.largeur(fenetre)/2 + VuePlanchette.pixels(Empilement.centreGeometrique(pile[i])-Planchette.longueur(pile[i][0])/2)
		y0 = Fenetre.hauteur(fenetre)-40-VuePlanchette.pixels((i+1)*Planchette.Epaisseur)

		if i % 2 == 0:
			couleur = VuePioche.Couleur1
		else:
			couleur = VuePioche.Couleur2

		VuePlanchette.dessine(fenetre, Empilement.planchette(pile[i]), x0 , y0, couleur)

		# coordonnées du centre de la croix
		x_croix = Fenetre.largeur(fenetre)/2 + VuePlanchette.pixels(Empilement.centreGravite(pile[i]))
		y_croix = Fenetre.hauteur(fenetre)-40-VuePlanchette.pixels((i+0.5)*Planchette.Epaisseur)

		if Empilement.desequilibre(pile[i]) == True :
			dessine_croix(fenetre, '#FF3200', x_croix, y_croix)

		else :
			dessine_croix(fenetre, 'dark green', x_croix, y_croix)

def dessine_croix(fenetre, color, x, y) :
	Fenetre.toile(fenetre).create_line(x-VuePlanchette.pixels(0.3), y-VuePlanchette.pixels(0.3), x+VuePlanchette.pixels(0.3), y+VuePlanchette.pixels(0.3), fill = color, width = 2)
	Fenetre.toile(fenetre).create_line(x-VuePlanchette.pixels(0.3), y+VuePlanchette.pixels(0.3), x+VuePlanchette.pixels(0.3), y-VuePlanchette.pixels(0.3), fill = color, width = 2)
