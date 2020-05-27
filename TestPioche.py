import Pioche

pioche = Pioche.cree()
Pioche.nombrePlanchettes(pioche)
print(Pioche.versChaine(pioche))
print(Pioche.recherche(pioche, 181))
print(Pioche.recherche(pioche, 444))
print(Pioche.recherche(pioche, 545))
print(Pioche.recherche(pioche, 999))

Pioche.retire(pioche, 181)
print(Pioche.versChaine(pioche))
print(Pioche.recherche(pioche, 181))

Pioche.retire(pioche, 262)
Pioche.retire(pioche, 262)
print(Pioche.versChaine(pioche))
print(Pioche.recherche(pioche, 262))

Pioche.retire(pioche, 999)
print(Pioche.versChaine(pioche))
