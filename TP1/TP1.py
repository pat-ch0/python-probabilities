import sklearn
import random
import numpy as np
import matplotlib.pyplot as plt
from math import *

tempSummer = np.array([10, 13, 20, 25, 30, 22, 18, 11])
tempWinter = np.array([-15, -11, 0, 3, 10, 2, -2, -13])
height = np.array([3500, 2800, 1300, 750, 300, 900, 1800, 3100])
nbTry = 1000

h = [300, 750, 900, 1300, 1800, 2800, 3100, 3500]
tW = [10, 3, 2, 0, -2, -11, -13, -15]
tS = [30, 25, 22, 20, 18, 13, 11, 10]

def moindreCarre(alt, temp):
    p1 = 0; p2 = 0; p3 = 0; p4 = 0
    st = 0
    sa = 0
    n = len(alt)
    for i in range(0, n):
        p1 += temp[i]*alt[i]
        st += alt[i]
        sa += temp[i]
        p3 += alt[i]*alt[i]
    p1 *= n
    p2 = st*sa
    p3 *= n
    p4 = st**2

    a = (p1-p2) / (p3-p4)
    b = sa/n - a*(st/n)
    return (a,b)

np.random.seed(0)
x = np.random.rand(nbTry, 1)
y = 2*x + 1 + np.random.rand(nbTry, 1)/5 - 0.1

def maxVraisemblance(alt, temp):
    (a,b) = moindreCarre(alt, temp)
    s = 0
    n = len(alt)
    for i in range(0, n):
        s += (temp[i] - a*alt[i] - b)**2
    sigma = sqrt(s*(1/n))
    return sigma


#Optimisation
def gradient(a, b, x, y, n):
    s = 0
    s2 = 0
    for i in range(0, n):
        s += x[i]*(a*x[i] + b - y[i])
        s2 += a*x[i] + b - y[i]
    s = s*(1/n)
    s2 = s2*(1/n)
    return (s, s2)

def J(a, b, x, y):
    s = 0
    n = len(x)
    for i in range(0, n):
        s += (a*x[i] + b - y[i])**2
    return s

def opti(alt, temp):
    a = 1
    b = 0
    n = len(alt)
    (ga, gb) = gradient(a, b, alt, temp, n)
    Jprec = J(a, b, alt, temp)
    a = a - 0.5*ga
    b = b - 0.5*gb
    i = 1
    while (i<10000 and abs(J(a, b, alt, temp) - Jprec) >= 10**(-6)):
        (ga, gb) = gradient(a, b, alt, temp, n)
        Jprec = J(a, b, alt, temp)
        a = a - 0.5*ga
        b = b - 0.5*gb
        i += 1
    return (a,b)

#print("Moindre carre : ", moindreCarre(x, y))
#print("Maximum de vraisemblance : ", maxVraisemblance(x, y))
#print("Optimisation : ", opti(x, y))
#Modèle le plus précis : optimisation

plt.plot(h, tW, color='b')
print(np.interp(1000, h, tW)) #1000m en hiver : 1.5°C
plt.plot(h, tS, color='r')
print(np.interp(1000, h, tS)) #1000m en été : 21.5°C
#plt.show()
#15°C à 300m, il devrait faire 6.5°C à 1000m

#RMSE
def rmse(a, b, meth, alt, temp):
    n = len(alt)
    yb = []
    y = []
    (aObs, bObs) = meth(alt, temp)
    for i in range(0, n):
        yb.append(a*alt[i] + b)
        y.append(aObs*alt[i] + bObs)
    s = 0
    for i in range(0, n):
        s += (yb[i] - y[i])**2
    s /= n
    return sqrt(s)

#Coef de deter
def coef(a, b, meth, alt, temp):
    n = len(alt)
    yb = []
    y = []
    s = 0
    s2 = 0
    (aObs, bObs) = meth(alt, temp)
    for i in range(0, n):
        yb.append(a*alt[i] + b)
        y.append(aObs*alt[i] + bObs)
    m = 0
    for i in range(0, n):
        m += yb[i]
    m /= n
    for i in range(0, n):
        s += (yb[i] - m)**2
        s2 += (y[i] - m)**2
    return sqrt(s/s2)