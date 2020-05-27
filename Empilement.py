import Planchette

def cree(planchette, centre):
	"""
	Cette fonction crée une planchette et retourne une structure de données de type tuple non modifiable
	:param planchette: Un objet Planchette pour initialiser l'empilement
	:param centre: Le centre de l'Empilement

	:type planchette:  Type Planchette
	:type centre: un Entier

	:return: Retourne un tuple

	:Example:
	import Planchette, Empilement

	planchette = Planchette.cree(10, 2)
	empilement = Empilement.cree(planchette, 6)
	"""
	return (planchette, centre, {'masse' : Planchette.longueur(planchette), 'centreGravite' : centre, 'desequilibre' : False})

def planchette(empilement):
	"""
	Accesseur de la planchette d'un empilement

	:param empilement: Un empilement initialisé préalablement
	:type empilement: Empilement

	:return: Un objet Planchette
	"""
	return empilement[0]

def centreGeometrique(empilement):
	"""
	Accesseur du centre d'un empilement

	:param empilement: Un empilement initialisé préalablement
	:type empilement: Empilement

	:return: Entier qui représente le centre
	"""
	return empilement[1]

def masse(empilement, valeur=None):
	"""
	Accesseur/Mutateur de la masse d'un empilement

	:param empilement: Un empilement initialisé préalablement
	:type empilement: Empilement

	:param valeur: Si précisé, assigne la nouvelle valeur à la masse de l'empilement.
	:type valeur: int

	:return: Entier
	"""
	if valeur != None :
		empilement[2]['masse'] = valeur
	return empilement[2]['masse']

def centreGravite(empilement, valeur=None):
	"""
	Accesseur/Mutateur du centre de Gravité d'un empilement

	:param empilement: Un empilement initialisé préalablement
	:type empilement: Empilement

	:param valeur: Si précisé, assigne la nouvelle valeur à la masse de l'empilement.
	:type valeur: int

	:return: Entier
	"""
	if valeur != None :
		empilement[2]['centreGravite'] = valeur
	return empilement[2]['centreGravite']

def desequilibre(empilement, valeur=None):
	if valeur != None :
		empilement[2]['desequilibre'] = valeur
	return empilement[2]['desequilibre']

def versChaine(empilement):
	etat = "!" if desequilibre(empilement) == True else "" #Donne l'état
	return "n°{numero} m={masse} c={centre} g={gravite} {desequilibre}".format(
		numero=Planchette.numero(planchette(empilement)),
		masse=masse(empilement),
		centre=centreGeometrique(empilement),
		gravite=centreGravite(empilement),
		desequilibre=etat
	)
