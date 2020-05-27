from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

# Etape 2

Titre = 'Pytatra'

def cree(largeur, hauteur):
	fenetre = Tk()
	fenetre.geometry("{largeur}x{hauteur}".format(largeur=str(largeur),hauteur=str(hauteur)))
	fenetre.title(Titre)

	return (Canvas(fenetre,width=largeur, height=hauteur), largeur, hauteur, fenetre)

def toile(fenetre):
	return fenetre[0]

def largeur(fenetre):
	return fenetre[1]

def hauteur(fenetre):
	return fenetre[2]

def tk(fenetre):
	return fenetre[3]

def affiche(fenetre):
	toile(fenetre).pack()
	tk(fenetre).mainloop()

# Etape 5

TagGraphiques = 'graphique'

def effaceGraphiques(fenetre):
	toile(fenetre).addtag_all(TagGraphiques)
	toile(fenetre).delete(TagGraphiques)

def quandOuverte(fenetre, fonction, argument):
	def fonctionInterne(e):
		# pour éviter les invocations ultérieures
		tk(fenetre).unbind('<Map>')
		# invocation de la fonction principale
		fonction(argument)
	# liaison de l'évènement d'ouverture
	tk(fenetre).bind('<Map>', fonctionInterne)

def quitte(fenetre):
	tk(fenetre).quit()
