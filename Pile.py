import Planchette
import Empilement

def cree():
	"""
	Créé une liste d'empilement, qui correspond à une Pile
	"""
	return []

def estVide(pile):
	if len(pile) == 0 :
		return True
	else:
		return False

def sommet(pile):
	if estVide(pile) == True :
		return None
	else:
		return pile[-1]

def empile(pile, planchette, decalage):
	if estVide(pile) == True :
		pile.append(Empilement.cree(planchette, decalage))
	else:
		pile.append(Empilement.cree(planchette, decalage+Empilement.centreGeometrique(sommet(pile))))

def versChaine(pile):
	string = '---------------------\n'
	for empilement in pile :
		string += str(Empilement.versChaine(empilement))+'\n'
	string += '^^^^^^^^^^^^^^^^^^^^'
	return string

def empileEtCalcule(pile, planchette, decalage):
	empile(pile, planchette, decalage)
	calculeCentresGravite(pile)
	calculeEquilibre(pile)

def calculeCentresGravite(pile):
	for i in range(len(pile)-1, 0, -1) :
		masse_dessus = pile[i][2]['masse']
		longueur = pile[i-1][0][0]
		centre = pile[i-1][1]
		centreG_dessus = pile[i][2]['centreGravite']

		masse = longueur + masse_dessus
		centreG = (longueur*centre+masse_dessus*centreG_dessus)/masse

		pile[i-1][2]['masse'] = masse
		pile[i-1][2]['centreGravite'] = centreG

def calculeEquilibre(pile):
	for i in range(len(pile)-1, 0, -1) :
		if abs(pile[i][2]['centreGravite']-pile[i-1][1]) > pile[i-1][0][0]/2 :
			pile[i][2]['desequilibre'] = True
