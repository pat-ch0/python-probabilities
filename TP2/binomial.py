from math import *
from random import *
import random
import matplotlib.pyplot as plt
import numpy as np

#Fonction densité
def densite(L): #une liste tuplée de valeurs d'un tirage aléatoire qui représente la densité : (variable aléatoire, proba)
    L = list(L)
    distinctVal = np.unique(L)
    listDen = []
    distinctVal = list(distinctVal)
    for i in range(len(distinctVal)):
        #Nombre d'occurences d'une valeur divisé par le total
        val = L.count(distinctVal[i])
        listDen.append(val/len(L))
    return distinctVal, listDen


#Fonction répartition
def repartition(D): #prend la densité
    R = D
    for i in range(1, len(R)):
        R[i] += R[i-1]
        if R[i] > 0.99:
            return R
    return R


#Densité de la loi binomiale
def densBinom(n, p):
    L=[]
    M=[]
    for i in range(n):
        L.append(comb(n, i) * p**i * (1-p)**(n-i))
        M.append(i)
    return M, L


#Loi binomiale
binom5 = np.random.binomial(n=50, p=0.5, size=(1000))
binom7 = np.random.binomial(n=50, p=0.7, size=(1000))
binom2 = np.random.binomial(n=50, p=0.2, size=(1000))

#Densité
##Simulée
X5, Y5 = densite(binom5)
X7, Y7 = densite(binom7)
X2, Y2 = densite(binom2)

plt.figure()
plt.bar(X5, Y5, color="red")
plt.bar(X7, Y7, color="green")
plt.bar(X2, Y2, color="blue")
plt.legend(labels=['p=0.5', 'p=0.7', 'p=0.2'])
plt.title("Densité simulée de la loi binomiale")
plt.xlabel("Valeurs des variables aléatoires")
plt.ylabel("Probabilités de variables")

##Théorique
x5, y5 = densBinom(50, 0.5)
x7, y7 = densBinom(50, 0.7)
x2, y2 = densBinom(50, 0.2)

plt.figure()
plt.bar(x5,y5, color="darkred")
plt.bar(x7,y7, color="darkgreen")
plt.bar(x2,y2, color="darkblue")
plt.legend(labels=['p=0.5', 'p=0.7', 'p=0.2'])
plt.title("Densité théorique de la loi binomiale")
plt.xlabel("Valeurs des variables aléatoires")
plt.ylabel("Probabilités de variables")

#Répartition
##Simulée
repart5 = repartition(Y5)
repart7 = repartition(Y7)
repart2 = repartition(Y2)

plt.figure()
plt.bar(X5, repart5, color="yellow")
plt.bar(X7, repart7, color="cyan")
plt.bar(X2, repart2, color="pink")
plt.legend(labels=['p=0.5', 'p=0.7', 'p=0.2'])
plt.title("Répartition simulée de la loi binomiale")

##Théorique
repart5bis = repartition(y5)
repart7bis = repartition(y7)
repart2bis = repartition(y2)

plt.figure()
plt.bar(x5, repart5bis, color="yellow")
plt.bar(x7, repart7bis, color="cyan")
plt.bar(x2, repart2bis, color="pink")
plt.legend(labels=['p=0.5', 'p=0.7', 'p=0.2'])
plt.title("Répartition théorique de la loi binomiale")

plt.show()