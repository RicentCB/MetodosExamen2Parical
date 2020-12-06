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
#Funciones axiliares para la evaluacion
def evulateFunction(x: float, y: float):
    #Funcion que evalua la ecpresion matematica dada por el problema
    return (2 * math.cos(x)) + 3 * math.log10(y)

def evaluateRestrictions(x: float, y:float):
    #Funcion que verifica el cumplimiento de las restircciones
    return
    (x>=minResX) and (x<=maxResX) and (y<=minResY) and (y<=maxResY)

#Funcion main
if __name__ == "__main__":
    #Calculo de la interacion 0
    zc0 = evulateFunction(medX, medY)
    al1 = 0.0972414582262059
    al2 = 0.125047331544003
    obsAlx = norm.ppf(al1, 0, sigmaX)
    obsAly = norm.ppf(al2, 0, sigmaY)
    valx = 

    print(zc0)
    print(obsAlx)
    print(obsAly)




