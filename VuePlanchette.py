from tkinter import *

import Fenetre
import Planchette

Facteur = 10 # 1 cm = 10 pixels
CouleurFond = "light cyan"

def pixels(cm):
	return cm*Facteur

def dessine(fenetre, planchette, x0, y0, couleur):
	"""
	Dessine une planchette dans une fenetre Tkinter, en fonction des coordonnées
	choisies.

	:param fenetre: La fenêtre dans laquelle travailler.
	:param planchette: La planchette à dessiner.
	:param x0: La coordonnée x0 (en haut à gauche).
	:param y0: La coordonnée y0 (en bas à gauche).
	:param couleur: La couleur à donner.

	:type fenetre: Tkinter Windows
	:type planchette: Planchette
	:type x0: Entier
	:type y0: Entier
	:type couleur: String

	:return: Dessine dans une fenetre (retourne rien).
	:rtype: void
	"""
	longueur = pixels(Planchette.longueur(planchette))
	hauteur = pixels(Planchette.Epaisseur)
	marge = pixels(Planchette.marge(planchette))

	#Marge
	Fenetre.toile(fenetre).create_rectangle(x0, y0, x0 + longueur, y0 + hauteur, fill=CouleurFond)
	#Par dessus on met le "coeur" de la planchette.
	Fenetre.toile(fenetre).create_rectangle(x0 + marge, y0, x0 + (longueur-marge), y0 + hauteur, fill=couleur)

	#On crée le polygone du dessus
	Fenetre.toile(fenetre).create_polygon((x0,y0), (x0+longueur,y0), (x0+longueur+8,y0-8), (x0+8,y0-8), fill=CouleurFond, outline="black")
	Fenetre.toile(fenetre).create_polygon((x0+marge,y0), (x0+longueur-marge,y0), (x0+longueur+8-marge,y0-8), (x0+8+marge,y0-8), fill=couleur, outline="black")
	Fenetre.toile(fenetre).create_polygon((x0+longueur, y0+Facteur), (x0+longueur+8,y0+Facteur-8), (x0+longueur+8,y0-8), (x0+longueur,y0), fill=CouleurFond, outline="black")
