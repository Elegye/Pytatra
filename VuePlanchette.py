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
	#Marge
	Fenetre.toile(fenetre).create_rectangle(x0, y0, x0+pixels(Planchette.longueur(planchette)), y0+pixels(Planchette.Epaisseur), fill="sky blue")
	#Par dessus on met le "coeur" de la planchette.
	Fenetre.toile(fenetre).create_rectangle(x0+pixels(Planchette.marge(planchette)), y0, x0+pixels(Planchette.longueur(planchette)-Planchette.marge(planchette)), y0+pixels(Planchette.Epaisseur), fill="blue")
	#On crée le polygone du dessus
"""
fenetre[0].create_polygon((x0,y0),(x0+longueur,y0),(x0+longueur+5,y0-5),(x0+5,y0-5), fill='light blue',outline="black")#haut
    fenetre[0].create_polygon((x0+marge,y0),(x0+longueur-marge,y0),(x0+longueur+5-marge,y0-5),(x0+5+marge,y0-5), fill="blue",outline="black")#haut
    fenetre[0].create_polygon((x0+longueur, y0+Facteur),(x0+longueur+5,y0+Facteur-5),(x0+longueur+5,y0-5),(x0+longueur,y0), fill='light blue',outline="black")
"""
