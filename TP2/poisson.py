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


#Densité de la loi de Poisson
def densPois(lam, n):
    L = []
    M= []
    for i in range(n):
        M.append(i)
        L.append(exp(-lam)*(lam**i)/factorial(i))
    return M, L

#Loi de poisson
#La loi de poisson est un cas particulier de la loi binomiale
#Lorsque n devient grand et p devient petit, les résultats sont similaires
shark = np.random.poisson(lam=1, size=100)
shark2 = np.random.poisson(lam=10, size=100)
shark3 = np.random.poisson(lam=30, size=100)

#Densité
##Simulée
X, Y = densite(shark)
X2, Y2 = densite(shark2)
X3, Y3 = densite(shark3)

plt.bar(X, Y, color="red")
plt.bar(X2, Y2, color="green")
plt.bar(X3, Y3, color="blue")
plt.legend(labels=['lambda=1', 'lambda=10', 'lambda=30'])
plt.title("Densité simulée de Poisson")
plt.xlabel("Valeur des variables aléatoires")
plt.ylabel("Probabilité des variables")

##Théorique
m, l= densPois(1, 19)
m2, l2= densPois(10, 45)
m3, l3= densPois(30, 45)

plt.figure()
plt.bar(m, l, color="darkred")
plt.bar(m2, l2, color="darkgreen")
plt.bar(m3, l3, color="darkblue")
plt.legend(labels=['lambda=1', 'lambda=10', 'lambda=30'])
plt.xlabel("Valeurs des variables aléatoires")
plt.ylabel("Probabilités des variables")
plt.title("Densité théorique de Poisson")

#Répartition
##Simulée
fishR = repartition(Y)
fishR2 = repartition(Y2)
fishR3 = repartition(Y3)

plt.figure()
plt.bar(X, fishR, color="yellow")
plt.bar(X2, fishR2, color="cyan")
plt.bar(X3, fishR3, color="pink")
plt.legend(labels=['lambda=1', 'lambda=10', 'lambda=30'])
plt.title("Répartition simulée de Poisson")

##Théorique
fishr = repartition(l)
fishr2 = repartition(l2)
fishr3 = repartition(l3)

plt.figure()
plt.bar(m, fishr, color="yellow")
plt.bar(m2, fishr2, color="cyan")
plt.bar(m3, fishr3, color="pink")
plt.legend(labels=['lambda=1', 'lambda=10', 'lambda=30'])
plt.title("Répartition théorique de Poisson")

plt.show()