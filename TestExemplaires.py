import Exemplaires
import Planchette

p343 = Planchette.cree(10, 3)

e = Exemplaires.cree(p343, 3)
print(str(e))
print(Planchette.numero(Exemplaires.planchette(e)))
print(Exemplaires.nombre(e))
print(Exemplaires.versChaine(e))

for i in range(3):
	n = Exemplaires.retireUn(e)
	print(str(n) + "=" + str(Exemplaires.nombre(e)))
	print(str(e))
