import Joueur
import Pioche

joueurs = [Joueur.cree(1), Joueur.cree(2)]

for j in joueurs:
	print(Joueur.numero(j))
	print(Joueur.nom(j))
	print(Pioche.versChaine(Joueur.pioche(j)))
