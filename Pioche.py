import Exemplaires
import Planchette

LONGUEUR_MIN = 10
LONGUEUR_MAX = 14
NOMBRE_EXEMPLAIRES = 3

def cree():
	"""
	Retourne une liste d’exemplaires correspondant à une pioche complète,
	c’est-à-dire contenant 27 planchettes
	"""
	pioche = []
	increment = 1
	# Deux petites boucles imbriquées qui générent automatiquement en fonction
	# des paramètres LONGUEUR_MAX, LONGUEUR_MIN et NOMBRE_EXEMPLAIRES (par catégorie)
	# Là on essaye de faire une boucle qui nous retourne les valeurs 10, 12, 14. (Avec un pas de 2. LONGUEUR_MAX+1 parce que la fonction range s'arrête toujours à n-1)
	for longueur in range(LONGUEUR_MIN, LONGUEUR_MAX+1, 2):
		# Là on fait une boucle qui fait nombre = 1 puis =2 puis =3
		for nombre in range(0, NOMBRE_EXEMPLAIRES):
			#Création de la planchette à donner à l'exemplaire à créer. Elle prend en paramètre la longueur et le nombre
			planchette = Planchette.cree(longueur, nombre+increment)
			#Une fois qu'on a la planchette, on peut créer l'Exemplaires avec la planchette et le nombre (soit 1, 2, 3 puis 2,3,4 puis 3,4,5 parce qu'on a nombre+increment)
			pioche.append(Exemplaires.cree(planchette, nombre+increment))
		increment += 1 # Petit increment pour faire 3 tours de boucle.

	return pioche

def nombrePlanchettes(pioche):
	"""
	Retourne le nombre total de planchettes présentes dans la pioche.

	:param pioche: La pioche à considérer
	:type pioche: Type Pioche

	:return: Nombre de Planchettes
	:rtype: Entier
	"""

	#Le nb de planchettes dans la pioche c'est le nombre de planchettes dans chaque exemplaire, qu'on additionne à chaque tour de boucle.
	nombre = 0
	for jeu in pioche:
		nombre += Exemplaires.nombre(jeu)
	return nombre

def versChaine(pioche):
	"""
	Retourne une chaîne de caractères représentant textuellement le contenu de
	la pioche. Par exemple, la représentation textuelle d’une pioche complète
	est : « 1x181 2x262 3x343 2x282 3x363 4x444 3x383 4x464 5x545 ».

	:param pioche: La pioche à considérer
	:type pioche: Type Pioche

	:return: Chaine formatée
	:rtype: String
	"""
	chaine = ""
	for exemplaires in pioche:
		chaine += Exemplaires.versChaine(exemplaires) + " " #On réutilise la fonction vers chaine, comme dans la fonction précédente.
	return chaine

def recherche(pioche, numero):
	"""
	Recherche dans la pioche la planchette donnée par son numero.
	Retourne l’indice correspondant si la planchette est trouvée, -1 sinon.

	:param pioche: La pioche à considérer
	:param numero: Le numéro de la planchette

	:type pioche: Type Pioche
	:type numero: Entier
	"""
	liste_numero = []
	for exemplaires in pioche:
		liste_numero.append(Planchette.numero(Exemplaires.planchette(exemplaires)))
	if numero in liste_numero:
		return liste_numero.index(numero)
	else:
		return -1


def contient(pioche, numero):
	"""
	Retourne vrai si la planchette donnée par son numero est présente dans
	la pioche, faux sinon. Équivalent à recherche(pioche, numero) == -1.

	:param pioche: La pioche à considérer
	:param numero: Le numéro de la planchette

	:type pioche: Type Pioche
	:type numero: Entier

	:return: Contient ou ne contient pas le numero indiqué dans la pioche
	:rtype: Boolean
	"""
	liste_numero = []
	for exemplaires in pioche:
		liste_numero.append(Planchette.numero(Exemplaires.planchette(exemplaires)))
	if numero in liste_numero:
		return True
	else:
		return False

def retire(pioche, numero):
	index = recherche(pioche, numero) #Evite de faire appel 2 fois à la fonction
	if index != -1:
		#Là il faut retirer un exemplaire
		Exemplaires.retireUn(pioche[index])
		#Si le nombre d'exemplaires atteint 0, alors:
		if Exemplaires.nombre(pioche[index]) == 0:
			pioche.pop(index)
	else:
		pass
