import Dialogue
import Empilement
import Exemplaires
import Fenetre
import Joueur
import Pile
import Pioche
import Planchette
import VuePioche
import VuePile
import pickle

# Etape 5.1

def cree():
	return (
		Fenetre.cree(1000, 600),
		Pile.cree(),
		[Joueur.cree(1), Joueur.cree(2)],
		{'indiceJoueur': 0}
	)

def fenetre(jeu):
	return jeu[0]

def pile(jeu):
	return jeu[1]

def joueurs(jeu):
	return jeu[2]

def indiceJoueur(jeu):
	return jeu[3]['indiceJoueur']

def joueurCourant(jeu):
	return joueurs(jeu)[indiceJoueur(jeu)]

def passeJoueurSuivant(jeu):
	if indiceJoueur(jeu) == 0:
		jeu[3]['indiceJoueur'] = 1
	else:
		jeu[3]['indiceJoueur'] = 0

# Etape 5.2

def joue(jeu):
	majVues(jeu)
	activite(jeu)
	Fenetre.bouclePrincipale(fenetre(jeu))

def majVues(jeu):
	#D'abord on efface les graphiques.
	Fenetre.effaceGraphiques(fenetre(jeu))
	#Puis on dessine la pile (initialement vide)
	VuePile.dessine(fenetre(jeu), pile(jeu))
	#Puis pour chaque joueur, on affiche la pioche.
	for iteration, joueur in enumerate(joueurs(jeu)):
		if(iteration == 0): #Le premier joueur à gauche, l'autre à droite.
			gauche = True
		else:
			gauche = False
		VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueur), gauche)

# Etape 5.3

def activite(jeu):
	nombrePlanchettes = Pioche.nombrePlanchettes(Joueur.pioche(joueurCourant(jeu)))
	desequilibre = False
	debutPartie = True
	partieFinie = False
	while nombrePlanchettes != 0 and desequilibre == False and partieFinie != True:
		planchette = selectionnePlanchette(jeu)
		if planchette == None:
			partieFinie = True
		else:
			pioche = Joueur.pioche(joueurCourant(jeu))
			Pioche.retire(pioche, Planchette.numero(planchette)) #On retire la planchette de la pioche.
			if debutPartie: #Si c'est le début de partie
				Pile.empileEtCalcule(pile(jeu), planchette, 0)
				majVues(jeu)
				passeJoueurSuivant(jeu)
				debutPartie = False
			else: #Si ce n'est pas le début de partie
				passeJoueurSuivant(jeu)
				decalage = choisisDecalage(jeu, planchette)
				if decalage == None:
					partieFinie = True
				else:
					Pile.empileEtCalcule(pile(jeu), planchette, decalage)
					for empilement in pile(jeu):
						if Empilement.desequilibre(empilement):
							desequilibre = True
					nombrePlanchettes = Pioche.nombrePlanchettes(Joueur.pioche(joueurCourant(jeu)))
				majVues(jeu)

	if desequilibre: #S'il y a un déséquilibre
		Dialogue.afficheMessage("{joueur} gagne !".format(joueur=Joueur.nom(joueurCourant(jeu))))
	else: #S'il n'y en a pas.
		if Pioche.nombrePlanchettes(Joueur.pioche(joueurCourant(jeu))) == 0:
			Dialogue.afficheMessage("Egalité de la partie")
		else:
			Dialogue.afficheMessage("La partie est terminée ! Un des joueurs a abandonné")
			#SAUVEGARDE
			sauvegarde_jeu = (pile(jeu), joueurs(jeu), {'indiceJoueur': indiceJoueur(jeu)})
			pickle.dump(sauvegarde_jeu, open("save.txt", "wb"))

	#Rejouer une partie ?
	rejouer = Dialogue.yesNoMessage("Voulez-vous recommencer une partie ?")
	Fenetre.quitte(fenetre(jeu)) #On supprime dans tous les cas la fenêtre
	if rejouer:
		joue(cree()) #On recréer les données puis on nettoie et on peut joueur à nouveau.
	#Là je mettais un petit message pour dire au revoir mais ça faisait beaucoup de messageBox d'un coup : pas agréable du tout.

def selectionnePlanchette(jeu):
	numero = 0
	while Pioche.contient(Joueur.pioche(joueurCourant(jeu)), numero) != True:
		numero = Dialogue.saisisEntier("{joueur} | Indiquez le numéro de la planchette :".format(joueur=Joueur.nom(joueurCourant(jeu))))
		if numero == None: #Si c'est cancel
			return None
	numero = str(numero)
	marge = int(numero[0])
	longueur = int(numero[1]) + 2 * marge
	return Planchette.cree(longueur, marge)

def choisisDecalage(jeu, planchetteAPoser):
	decalage = Dialogue.saisisEntier("{joueur} | Précisez le décalage".format(joueur=Joueur.nom(joueurCourant(jeu))))
	sommet = Pile.sommet(pile(jeu)) #Récupération de la pile du sommet.
	longueur_sommet = Planchette.longueur(Empilement.planchette(sommet))
	while abs(decalage) > Planchette.marge(planchetteAPoser) or abs(decalage) > longueur_sommet:
		decalage = Dialogue.saisisEntier("{joueur} | Précisez le décalage".format(joueur=Joueur.nom(joueurCourant(jeu))))
		if numero == None:
			return None
	return decalage
