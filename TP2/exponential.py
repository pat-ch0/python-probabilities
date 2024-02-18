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


#Densité de la loi exponentielle
def densExpo(lam, n):
    L = []
    M = []
    for i in range(n):
        L.append(lam * exp(-i*lam))
        M.append(i)
    return M, L
        

#Loi exponentielle
expo = np.random.exponential(scale=0.5, size=1000)
expo2 = np.random.exponential(scale=2, size=1000)
for i in range(1000):
    expo[i]=round(expo[i])
    expo2[i]=round(expo2[i])

#Densité
##Simulée    
X, Y = densite(expo)
X2, Y2 = densite(expo2)

plt.figure()
plt.bar(X, Y, color="red", edgecolor='red')
plt.bar(X2, Y2, color="green", edgecolor='green')
plt.title("Densité simulée de la loi exponentielle")
plt.xlabel("Valeurs des variables aléatoires")
plt.ylabel("Probabilités de variables")
plt.legend(labels=['lambda=0.5', 'lambda=2'])
plt.xlim(xmin=0.5) ; plt.xlim(xmax=12)
plt.ylim(ymax=0.5)

##Théorique
x, y = densExpo(0.5, 1000)
x2, y2 = densExpo(2, 1000)

plt.figure()
plt.bar(x, y, color="darkred", edgecolor='darkred')
plt.bar(x2, y2, color="darkgreen", edgecolor='darkgreen')
plt.title("Densité théorique de la loi exponentielle")
plt.xlabel("Valeurs des variables aléatoires")
plt.ylabel("Probabilités de variables")
plt.legend(labels=['lambda=0.5', 'lambda=2'])
plt.xlim(xmin=0.5) ; plt.xlim(xmax=12)
plt.ylim(ymax=0.5)

plt.show()