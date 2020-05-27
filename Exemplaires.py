import Planchette

def cree(planchette, nombre):
	"""
	Retourne un dictionnaire des planchettes voulues, avec la planchette
	et le nombre d'Exemplaires.
	
	:param planchette: Une planchette
	:param nombre: Nombre de planchette
	:type planchette: Planchette
	:type nombre: Entier (int)

	:return: Une structure correspondant à l'exemplaire créé.
	:rtype: Dictionnaire
	"""
	return {"planchette": planchette, "nombre": nombre}

def planchette(exemplaires):
	"""
	Retourne la planchette considérée par les exemplaires en question

	:param exemplaires: Exemplaires considérés
	:type exemplaires: Type Exemplaires

	:return: La planchette concernée
	:rtype: Planchette
	"""
	return exemplaires["planchette"]

def nombre(exemplaires, valeur=None):
	"""
	Modifie le nombre d’occurrences des exemplaires considérés en lui donnant la
	nouvelle valeur, dans le cas où cette valeur est définie ; retourne le
	nombre d’occurrences des exemplaires considérés.

	:param exemplaires: Exemplaires considérés
	:param valeur: Nouveau nombre d'exemplaire (facultatif)

	:type exemplaires: Type Exemplaires
	:type valeur: Entier

	:return: Le nombre de planchette
	:rtype: Entier
	"""
	if valeur != None:
		exemplaires["nombre"] = valeur
	return exemplaires["nombre"]

def retireUn(exemplaires):
	"""
	Retire un exemplaire des exemplaires considérés et renvoie le nombre
	d’exemplaires restants.

	:param exemplaires: Exemplaires considérés
	:type exemplaires: Type Exemplaires

	:return: Le nombre d'exemplaires moins UN.
	:rtype: nombre() => Entier
	"""
	return nombre(exemplaires, (nombre(exemplaires)-1) )

def versChaine(exemplaires):
	"""
	Retourne une chaîne de caractères représentant textuellement les exemplaires
	considérés. Le format est le suivant : « n x p » où n est le nombre
	d’exemplaires de la planchette numéro p.
	Par exemple, la chaîne « 2x464 » représente 2 exemplaires de la planchette 464.

	:param exemplaires: Exemplaires considérés
	:type exemplaires: Type Exemplaires

	:return: Une chaine formatée type "n X p"
	:rtype: String
	"""
	return "{n}x{p}".format(n=nombre(exemplaires), p=Planchette.numero(planchette(exemplaires)))
