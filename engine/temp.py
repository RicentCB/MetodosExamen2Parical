import numpy
import math
from scipy.stats import norm

#Algoritmo de templado simulado

def generateRandom():
    return abs(numpy.random.normal(0.5,1.0)*numpy.random.rand(1))
'''
MAX Z = 2 * cos(x) + 3 log(y)
Sujeto a:
0<=x<=10 ---- Lim a 0 <= x <= 10
1<=y<=5  ---- Lim b 1 <= y <= 5
'''
def evulateFunction(x: float, y: float):
    #Funcion que evalua la ecpresion matematica 
    return 3 * math.log(y)

#Variables de minimos y maximos (limites), obtenidas de en las restricciones
minResX = 0
maxResX = 10
minResY = 1
maxResY = 5
#Variables para el tempado simulado
medX = ((maxResX - minResX)/2) + minResX
medY = ((maxResY - minResY)/2) + minResY

sigmaX = (maxResX - minResX)/6
sigmaY = (maxResY - minResY)/6

#Calculo de la interacion 0
zc0 = evulateFunction(medX, medY)

print(zc0)
# print(invrand)



