from aleatorio import Aleatorio
import random
import matplotlib.pyplot as plt

listExponencial = []
listNormal = []

ciclos = 10000

for i in range(ciclos):
	listExponencial.append(Aleatorio().exponencial(random.randint(0, 99), 25))
for i in range(ciclos):
	listNormal.append(Aleatorio().normal(random.randint(0, 99), [200, 15]))

plt.hist(listExponencial)
plt.hist(listNormal)
plt.show()