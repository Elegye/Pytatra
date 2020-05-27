import Pioche

def cree(numero):
	"""
	Crée une structure de typle tuple pour stocker nos joueurs et leur pioche.

	:param numero: Le numéro du joueur
	:type numero: Entier

	:return: Structure de Joueur
	:rtype: tuple
	"""
	return (numero, Pioche.cree())

def numero(joueur):
	"""
	Getter numéro de joueur

	:param joueur: un Joueur
	:return: Numéro de joueur
	:rtype: Int
	"""
	return joueur[0]

def nom(joueur):
	"""
	Getter du Nom du Joueur

	:param joueur: Un Joueur
	:return: Chaine formatée du numéro de joueur
	:rtype: String
	"""
	return "Joueur {numero}".format(numero=numero(joueur))

def pioche(joueur):
	"""
	Getter pioche de joueur

	:param joueur: un Joueur
	:return: Pioche de Joueur
	:rtype: Pioche
	"""
	return joueur[1]
