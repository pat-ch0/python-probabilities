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
    return R


#Densité de la loi normale
def densNormal(mu, sigma, n):
    L=[]
    M=[]
    for i in range(n):
       L.append((exp((-1/2)*(i-mu/sigma)**2)) / (sigma*sqrt(2*pi)))
       M.append(i)
    return M, L
                

#Loi normale
norm = np.random.normal(loc=25, scale=sqrt(50*0.25), size=1000)
for i in range (len(norm)):
    norm[i]=round(norm[i])


##Densité simulée et théorique
##Théorème central limite vérifié, les variables aléatoires convergent vers la valeur μ = 25 
X, Y = densite(norm)
x, y = densNormal(25, sqrt(50*0.25), 1000)
plt.bar(X,Y, color="red")
plt.bar(x, y, color="darkred")
plt.xlim(xmax=40) ; plt.xlim(xmin=0)
plt.legend(labels=['simulée', 'théorique'])
plt.title("Densité de la loi normale")
plt.xlabel("Valeur des variables aléatoires")
plt.ylabel("Probabilité des variables")

##Répartition simulée et théorique
repartSimul = repartition(Y)
repartTheo = repartition(y)

plt.figure()
plt.bar(X, repartSimul, color="yellow")
plt.bar(x, repartTheo, color="pink")
plt.xlim(xmax=40) ; plt.xlim(xmin=0)
plt.legend(labels=['simulée', 'théorique'])
plt.title("Répartition de la loi normale")

plt.show()