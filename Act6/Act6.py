import itertools
import matplotlib.pyplot as plt
from collections import defaultdict


cubo = range(1, 21) 
S = list(itertools.product(cubo, repeat=3))  

# variable aleatoria
X = [sum(respuesta) for respuesta in S]

repe_X = defaultdict(int)
for valor in X:
    repe_X[valor] += 1


print("Valor de X | Frecuencia")
print("-----------------------")
for valor in sorted(repe_X.keys()):
    print(f"{valor:^10} | {repe_X[valor]:^9}")


plt.bar(repe_X.keys(), repe_X.values(), color='blue')
plt.xlabel('Sumatoria de las caras en los dados:')
plt.ylabel('Frecuencia')
plt.title('La variable es:')
plt.show()