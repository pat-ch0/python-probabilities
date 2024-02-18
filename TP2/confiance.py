from math import *
from random import *
import random
import matplotlib.pyplot as plt
import numpy as np

conduc = [0.98, 1.4, 0.84, 0.88, 0.54, 0.68, 1.35, 0.76, 0.72,
0.99, 0.88, 0.75, 0.49, 1.09, 0.68, 0.60, 1.13, 1.35, 1.13, 0.91]
taille = len(conduc)

#Moyenne empirique
def moyEmp(L):
    return sum(L)/len(L)
print("La moyenne empirique est de", moyEmp(conduc))

#Intervalle de confiance
def interConf(moy, s, t, n):
    L = [moy-t*s/sqrt(n), moy+t*s/sqrt(n)]
    return L

#Ecart type empirique
def ecartTypeEmp(L):
    moy = moyEmp(L)
    som = 0
    for i in L:
        som += abs(i-moy)**2
    som = som/len(L)
    return sqrt(som)


#Variance connue
li95 = interConf(moyEmp(conduc), sqrt(0.2), 1.645, taille)
print("Intervalle de confiance lorsque 1-alpha=95% :", li95)
li99 = interConf(moyEmp(conduc), sqrt(0.2), 2.33, taille)
print("Intervalle de confiance lorsque 1-alpha=99% :", li99)

print("-"*75)

#Variance empirique
liS95 = interConf(moyEmp(conduc), ecartTypeEmp(conduc), 1.7291, taille)
print("Intervalle de confiance lorsque 1-alpha=95% avec variance empirique :", liS95)
liS99 = interConf(moyEmp(conduc), ecartTypeEmp(conduc), 2.5395, taille)
print("Intervalle de confiance lorsque 1-alpha=99% avec variance empirique :", liS99)

plt.hist(conduc)
plt.title("Histogramme de l'échantillon")
plt.show()


#Estimation d'une proportion
L = [637-1.645*sqrt(0.637*(1-0.637)/1000), 637+1.645*sqrt(0.637*(1-0.637)/1000)]
print("L'intervalle de confiance de la population suivant le cours d'algorithmique est ", L)