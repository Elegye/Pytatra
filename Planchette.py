 # Etape 2

Epaisseur = 1
# Ici nous choisirons la structure tuple car nous ne devons pas modificer ces données dans notre programme.
def cree(longueur, marge):
	return (longueur, marge)

def longueur(planchette):
	return planchette[0]

def marge(planchette):
	return planchette[1]

def numero(planchette):
	return int(str(marge(planchette)) + str(longueur(planchette) - 2*marge(planchette)) + str(marge(planchette)))
