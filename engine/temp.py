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
    arrayZc = list()
    #Calculo de la interacion 0
    arrayZc.append(evulateFunction(medX, medY))
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
    den0 = (zn0 - arrayZc[0]) / (0.2*arrayZc[0])
    bestProb.append(math.exp(den0))
    #Iteracion Cero
    print("Interacion 0")
    # print(arrayZc[0])
    print(arrValX[0])
    print(arrValY[0])
    # print(obsAlX)
    # print(obsAlY)
    # print(zn0)
    # print(den0)
    print(bestProb[0])
    #---------------------------------------------------------------------------------
    #Comenzar con las interaciones (100 individuos) *(100 poblaciones)
    for i in range(0 , 2):
        xAux = arrValX[i]
        yAux = arrValY[i]
        facTemp = 0.2 if (i == 0) else 0.5 # 0.2 solo para la primer interacion
        t = arrayZc[i] * facTemp
        arrAuxValX = list()
        arrAuxValY = list()
        arrAuxProb = list()
        for j in range(0, 4):
            #Generacion de numeros Aleatorios
            alA = generateRandom()[0]
            alB = generateRandom()[0]
            obsAlX = norm.ppf(alA, 0, sigmaX)
            obsAlY = norm.ppf(alB, 0, sigmaY)
            #Calcular resto de valores
            tempValX = (xAux + obsAlX)
            tempValY = (yAux + obsAlY)
            #TODO: Evaluar primero restricciones
            tempValZn = evulateFunction(tempValX, tempValY)
            tempValDen = (tempValZn - arrayZc[i]) / t
            tempProb = math.exp(tempValDen)

            #Revisar si se han cumpliado las restricciones y la probabilidad calculada es mejor que la anterior
            while not(evaluateRestrictions(tempValX, tempValY) and tempProb >= bestProb[i]):
                #Recalcular con nuevos numeros aleatorios
                alA = generateRandom()[0]
                alB = generateRandom()[0]
                obsAlX = norm.ppf(alA, 0, sigmaX)
                obsAlY = norm.ppf(alB, 0, sigmaY)
                tempValX = (xAux + obsAlX)
                tempValY = (yAux + obsAlY)
                tempValZn = evulateFunction(tempValX, tempValY)
                tempValDen = (tempValZn - arrayZc[i]) / t
                tempProb = math.exp(tempValDen)
            
            #Guardar Valores de X,Y y la probabalidad
            arrAuxValX.append(tempValX)
            arrAuxValY.append(tempValY)
            arrAuxProb.append(tempProb)
        #Ya se han obtenido los individuos elegeir el mejor
        maxProb = numpy.amax(arrAuxProb)
        #Buscar inidice
        indexAux = arrAuxProb.index(maxProb)
        arrValX.append(arrAuxValX[indexAux])
        arrValY.append(arrAuxValY[indexAux])
        arrayZc.append(evulateFunction(arrAuxValX[indexAux], arrAuxValY[indexAux]))
        bestProb.append(arrAuxProb[indexAux])




    




