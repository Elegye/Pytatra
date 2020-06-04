 # Etape 2

Epaisseur = 1
# Ici nous choisirons la structure tuple car nous ne devons pas modificer ces données dans notre programme.
def cree(longueur, marge):
	""" Créé une planchette """
	return (longueur, marge)

def longueur(planchette):
	"""
	Retourne la longueur de la planchette.
	"""
	return planchette[0]

def marge(planchette):
	"""
	Retourne la marge de la planchette.
	"""
	return planchette[1]

def numero(planchette):
	"""
	Retourne le numéro de la planchette
	"""
	return int(str(marge(planchette)) + str(longueur(planchette) - 2*marge(planchette)) + str(marge(planchette)))
