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
	return str(indiceJoueur(jeu))

def passeJoueurSuivant(jeu):
	if indiceJoueur(jeu) == 0:
		jeu[3]['indiceJoueur'] = 1
	else:
		jeu[3]['indiceJoueur'] = 0

# Etape 5.2

def joue(jeu):
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
		VuePioche.dessine(fenetre(jeu), joueur[1], gauche)

# Etape 5.3

def activite(jeu):
	joueurActuel = joueurs(jeu)[indiceJoueur(jeu)]
	desequilibre = False
	for empilement in pile(jeu):
		desequilibre = Empilement.desequilibre(empilement)

	if Pioche.nombrePlanchettes(Joueur.pioche(joueurActuel)) != 0 AND desequilibre != True:

		print("Différent de 0 !")

def selectionnePlanchette(jeu):
	return None

def choisisDecalage(jeu, planchetteAPoser):
	return None
