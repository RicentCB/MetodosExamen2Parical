import numpy
import math
import time
import sys
import json
from scipy.stats import norm

#Algoritmo de templado simulado
def generateRandom():
    return (abs(numpy.random.normal(0.5,1.0)*numpy.random.rand(1))[0])
'''
MAX Z = 2 * cos(x) + 3 log(y)
Sujeto a:
0<=x<=10 ---- Lim a 0 <= x <= 10
1<=y<=5  ---- Lim b 1 <= y <= 5
'''
kMaxInterationsNumber = 100

#Variables de minimos y maximos (limites), obtenidas de en las restricciones
minResX = 0
maxResX = 24
minResY = 0
maxResY = 20
#Variables para el tempado simulado
medX = ((maxResX - minResX)/2) + minResX
medY = ((maxResY - minResY)/2) + minResY

sigmaX = (maxResX - minResX)/6
sigmaY = (maxResY - minResY)/6
#Funciones axiliares para la evaluacion
def evulateFunction(x: float, y: float):
    #Funcion que evalua la expresion matematica dada por el problema
    # if(y<=0):
    #     return (2 * math.cos(x))
    # else:
    return 8*x + 12*y

def evaluateRestrictions(x: float, y:float):
    #Funcion que verifica el cumplimiento de las restircciones
    return (x>=minResX) and (y>=minResY) and (102*x +124*y <= 2400)

#Funcion main
if __name__ == "__main__":
    #Variable de inicio de tiempo
    iniTime = time.time()
    #Arreglos de probabilidad
    arrValX = list()
    arrValY = list()
    bestProb = list()
    arrayZc = list()
    #Calculo de la interacion 0
    arrayZc.append(evulateFunction(medX, medY))
    al1 = generateRandom()
    al2 = generateRandom()
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
        #Revisar tiempo de ejecucion
        if time.time() - iniTime > 28:
            print("PRIMERA INTERACION")
            sys.exit()
                    
    #Una vez se han evaluado las condiciones podemos calcular valores correspondientes
    zn0 = evulateFunction(arrValX[0],arrValY[0])
    den0 = (zn0 - arrayZc[0]) / (0.2*arrayZc[0])
    bestProb.append(math.exp(den0))
    # # Iteracion Cero
    # print("Interacion 0")
    # # print(arrayZc[0])
    # print(arrValX[0])
    # print(arrValY[0])
    # print(obsAlX)
    # print(obsAlY)
    # print(zn0)
    # print(den0)
    # print(bestProb[0])
    #---------------------------------------------------------------------------------
    #Comenzar con las interaciones (100 individuos) *(100 poblaciones)
    for i in range(0 , 100):
        xAux = arrValX[i]
        yAux = arrValY[i]
        facTemp = 0.2 if (i == 0) else 0.5 # 0.2 solo para la primer interacion
        t = arrayZc[i] * facTemp
        arrAuxValX = list()
        arrAuxValY = list()
        arrAuxProb = list()
        for j in range(0, 100):
            #Generacion de numeros Aleatorios
            alA = generateRandom()
            alB = generateRandom()
            obsAlX = norm.ppf(alA, 0, sigmaX)
            obsAlY = norm.ppf(alB, 0, sigmaY)
            tempValX = (xAux + obsAlX)
            tempValY = (yAux + obsAlY)
            #Calcular resto de valores
            tempValZn = evulateFunction(tempValX, tempValY)
            tempValDen = (tempValZn - arrayZc[i]) / t
            tempProb = math.exp(tempValDen)

            #Revisar si se han cumpliado las restricciones y la probabilidad calculada es mejor que la anterior
            while not(evaluateRestrictions(tempValX, tempValY) and tempProb >= bestProb[i]):
                #Recalcular con nuevos numeros aleatorios
                alA = generateRandom()
                alB = generateRandom()
                obsAlX = norm.ppf(alA, 0, sigmaX)
                obsAlY = norm.ppf(alB, 0, sigmaY)
                tempValX = (xAux + obsAlX)
                tempValY = (yAux + obsAlY)
                tempValZn = evulateFunction(tempValX, tempValY)
                tempValDen = (tempValZn - arrayZc[i]) / t
                tempProb = math.exp(tempValDen)
                #Revisar tiempo de ejecucion
                if time.time() - iniTime > 40:
                    print(json.dumps({"P":bestProb[i],"X":arrValX[i],"Y":arrValY[i],"Z":arrayZc[i]}))
                    # print("P:",bestProb[i])
                    # print("X:",arrValX[i])
                    # print("Y:",arrValY[i])
                    # print("Z:",arrayZc[i])
                    sys.exit()
            
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
    #Termino todas las interaciones
    
    print(json.dumps({
        "P":bestProb[len(bestProb)-1],
        "X":arrValX[len(arrValX)-1],
        "Y":arrValY[len(arrValY)-1],
        "Z":arrayZc[len(arrayZc)-1]}))




    




