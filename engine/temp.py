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
kMaxInterationsNumber = 100

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
    return (2 * math.cos(x)) + (3 * math.log10(y))

def evaluateRestrictions(x: float, y:float):
    #Funcion que verifica el cumplimiento de las restircciones
    return (x>=minResX) and (x<=maxResX) and (y>=minResY) and (y<=maxResY)

#Funcion main
if __name__ == "__main__":
    arrValX = list()
    arrValY = list()
    bestProb = list()
    #Calculo de la interacion 0
    zc0 = evulateFunction(medX, medY)
    al1 = 0.0972414582262059
    al2 = 0.125047331544003
    obsAlX = norm.ppf(al1, 0, sigmaX)
    obsAlY = norm.ppf(al2, 0, sigmaY)
    arrValX.append(medX + obsAlX)
    arrValY.append(medY + obsAlY)
    
    #Se generaran nuevos numeros aleaatorios hasta que se cumplan las condiciones
    contInt = 0
    while (not evaluateRestrictions(arrValX[0], arrValY[0])):
        al1 = generateRandom()
        al2 = generateRandom()
        obsAlX = norm.ppf(al1, 0, sigmaX)
        obsAlY = norm.ppf(al2, 0, sigmaY)
        arrValX[0] = medX + obsAlX
        arrValY[0] = medY + obsAlY
        #Se incrementa el contador de interaciones
        contInt += 1
    #Una vez se han evaluado las condiciones podemos calcular valores correspondientes
    zn0 = evulateFunction(arrValX[0],arrValY[0])
    den0 = (zn0 - zc0) / (0.2*zc0)
    bestProb.append(math.exp(den0))

    print(zc0)
    print(arrValX[0])
    print(arrValY[0])
    print(obsAlX)
    print(obsAlY)
    print(zn0)
    print(den0)
    print(bestProb[0])




