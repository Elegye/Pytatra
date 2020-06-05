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
#Un fichier VueJeu est créé pour respecter la séparation des vues du contrôleur.
import VueJeu

import os
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

def joue(jeu, is_replay=False):
	majVues(jeu)
	if is_replay:
		replay(jeu)
	else:
		#Si on joue, on supprime le dernier replay pour repartir sur un fichier vide.
		if os.path.exists("replay.txt"):
			os.remove("replay.txt")
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
		VueJeu.affichageMessage(Fenetre.toile(fenetre(jeu)), "Tour : "+Joueur.nom(joueurCourant(jeu)), 120, 50, 24)
		planchette = selectionnePlanchette(jeu)
		if planchette == None:
			partieFinie = True
		else:
			#### REPLAY ####
			saveReplay(indiceJoueur(jeu)) #Toujours l'indice du joueur en 1er
			saveReplay(str(Planchette.longueur(planchette))+","+str(Planchette.marge(planchette))) #Puis on sauvegarde la planchette dans un format prédéfini.

			#### JEU COURANT ####
			pioche = Joueur.pioche(joueurCourant(jeu))
			Pioche.retire(pioche, Planchette.numero(planchette)) #On retire la planchette de la pioche.
			if debutPartie: #Si c'est le début de partie
				Pile.empileEtCalcule(pile(jeu), planchette, 0)
				saveReplay(0) #On met le décalage à 0.
				majVues(jeu)
				passeJoueurSuivant(jeu)
				debutPartie = False
			else: #Si ce n'est pas le début de partie
				passeJoueurSuivant(jeu)
				decalage = choisisDecalage(jeu, planchette)
				saveReplay(decalage)
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
			save = Dialogue.yesNoMessage("La partie est terminée ! Voulez-vous sauvegarder ?")
			#SAUVEGARDE
			if save:
				sauvegarde_jeu = (pile(jeu), joueurs(jeu), {'indiceJoueur': indiceJoueur(jeu)})
				pickle.dump(sauvegarde_jeu, open("save.txt", "wb"))

	#Rejouer une partie ?
	rejouer = Dialogue.yesNoMessage("Voulez-vous recommencer une partie ?")
	Fenetre.quitte(fenetre(jeu)) #On supprime dans tous les cas la fenêtre
	if rejouer:
		joue(cree()) #On recrée les données puis on nettoie et on peut joueur à nouveau.
	#Là je mettais un petit message pour dire au revoir mais ça faisait beaucoup de messageBox d'un coup : pas agréable du tout.

def saveReplay(a_ecrire):
	with open("replay.txt", "a") as file:
		file.write(str(a_ecrire)+";")

def replay(jeu, iteration=0):
	"""
	Fonction qui s'occupe d'afficher le replay d'une partie.
	Cette fonction lit le fichier replay.txt s'il existe. Les données sont stockées sous la
	forme: indiceJoueur;planchette;decalage
	indiceJoueur est un entier, planchette est de la forme longueur,marge
	et decalage est un entier.
	Entre chaque lecture de ligne, donc chaque tour on met un petit timer de 2 secondes.
	Aucun retour, juste de l'affichage.
	Pour l'affichage, on utilise la fonction tkinter.after, équivalent de time.sleep.
	time.sleep ne fonctionne pas avec Tkinter : l'affichage ne se faisait qu'à la toute fin.
	Pause de 2 secondes entre chaque tour.

	:param jeu: Tuple fourni par Jeu.cree()
	:type jeu: tuple

	:return: Nothing
	:rtype: Nothing
	"""
	#On regarde si le fichier replay.txt existe avec un try/catch simple.
	try:
		file = open("replay.txt")
	except IOError:
		print("Fichier de replay introuvable.")
		VueJeu.affichageMessage(Fenetre.toile(fenetre(jeu)), "Fichier introuvable.\nRééssayez")
	else:
		with file:
			contenu = file.read().split(";") #On split les données par ";"
			#Compréhension de listes parce que c'est joli et qu'on l'a fait nulle part dans le projet. Et on prend le 1er élément.
			tour = [contenu[i:i+3] if len(contenu[i:i+3]) == 3 else None for i in range(iteration, iteration+3, 3)][0]
			if tour != None:
				joueurCourant = int(tour[0])
				piocheJoueur = Joueur.pioche(joueurs(jeu)[joueurCourant]) #On récupère sa pioche
				planchette_brute = tour[1].split(",")
				longueur, marge = int(planchette_brute[0]), int(planchette_brute[1])
				planchette = Planchette.cree(longueur, marge)
				decalage = int(tour[2])
				Pioche.retire(piocheJoueur, Planchette.numero(planchette))
				Pile.empileEtCalcule(pile(jeu), planchette, decalage)
				majVues(jeu)
				# Documentation : http://tkinter.fdex.eu/doc/uwm.html#after
				Fenetre.tk(fenetre(jeu)).after(1000, replay, jeu, iteration+3)
				#Une aide pour mieux comprendre la partie : qui joue ?
				#On le place après le after sinon le message est supprimé avant même que nous l'ayons vu.
				VueJeu.affichageMessage(Fenetre.toile(fenetre(jeu)), "Tour : "+Joueur.nom(joueurs(jeu)[joueurCourant]), 120, 50, 24)
			else:
				# On remet à zéro comme ça ça efface le texte mis auparavant.
				Fenetre.effaceGraphiques(fenetre(jeu))
				majVues(jeu)
				#Et on affiche.
				VueJeu.affichageMessage(Fenetre.toile(fenetre(jeu)), "PARTIE TERMINEE")
				dernier_joueur = int(contenu[-4])
				VueJeu.affichageMessage(Fenetre.toile(fenetre(jeu)), Joueur.nom(joueurs(jeu)[dernier_joueur])+" perd !", 500,300)

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
	if decalage == None:
		return None

	sommet = Empilement.planchette(Pile.sommet(pile(jeu))) #Récupération de la pile du sommet.
	longueur_sommet = Planchette.longueur(sommet)
	marge_sommet = Planchette.marge(sommet)
	longueur_planchette = Planchette.longueur(planchetteAPoser)

	limite_inf = (longueur_sommet/2 - marge_sommet) - longueur_planchette/2
	limite_sup = (marge_sommet - longueur_sommet/2) + longueur_planchette/2
	while (limite_inf < decalage < limite_sup):
		decalage = Dialogue.saisisEntier("{joueur} | Précisez le décalage".format(joueur=Joueur.nom(joueurCourant(jeu))))
		if decalage == None:
			return None
	return decalage
