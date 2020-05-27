from tkinter import *

import Fenetre
import Planchette

Facteur = 10 # 1 cm = 10 pixels

def pixels(cm):
	return cm*Facteur

def dessine(fenetre, planchette, x0, y0):
	"""
	Dessine une planchette dans une fenetre Tkinter, en fonction des coordonnées
	choisies.

	:param fenetre: La fenêtre dans laquelle travailler.
	:param planchette: La planchette à dessiner.
	:param x0: La coordonnée x0 (en haut à gauche).
	:param y0: La coordonnée y0 (en bas à gauche).

	:type fenetre: Tkinter Windows
	:type planchette: Planchette
	:type x0: Entier
	:type y0: Entier

	:return: Dessine dans une fenetre (retourne rien).
	:rtype: void
	"""
	Fenetre.toile(fenetre).create_rectangle(x0, y0, x0+pixels(Planchette.longueur(planchette)), y0+pixels(Planchette.Epaisseur))
	Fenetre.toile(fenetre).create_rectangle(x0+pixels(Planchette.marge(planchette)), y0, x0+pixels(Planchette.longueur(planchette)-Planchette.marge(planchette)), y0+pixels(Planchette.Epaisseur), fill="blue")
