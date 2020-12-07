import math
import time
import json
import random
import numpy
import matplotlib.pyplot as plt


class ATS:
    number_variables = 0
    restrictions = []
    M_gauss = 0
    option = 0
    NUM_ITER = 0
    NUM_POBL = 0

    def __init__(self, points, num_iter = 500000, num_pobl = 10): # Recibe una lista de tuplas y como opcional el num_iter y num_pobl
                                                                  # Se recomienda que num_iter*num_pobl = 6000000 para obtener un buen resultado
        self.points = points
        self.NUM_ITER = num_iter
        self.NUM_POBL = num_pobl

        self.init_line() # Indica que las evaluaciones, restricciones y variables pertenecen a la función Lineal
        solLine = self.solve()     #Resuelve para las restricciones, variables y evaluaciones de la funcion lineal

        self.init_gauss() # Indica que las evaluaciones, restricciones y variables pertenecen a la función Gaussiana
        solGauss = self.solve()      #Resuelve para las restricciones, variables y evaluaciones de la funcion lineal

        #Grafica 
        xValues = list()
        yValues = list()
        for i in range(len(points)):
            xValues.append(points[i][0])
            yValues.append(points[i][1])
            # Puntos
            plt.scatter(points[i][0],points[i][1], color="r")
                
        # Prepare the data
        x1 = numpy.linspace(numpy.min(xValues)-1, numpy.max(xValues)+1, 100)
        x2 = numpy.linspace(numpy.min(xValues)-1, numpy.max(xValues)+2, 100)

        pend = solLine[0]
        b = solLine[1]
        lineal = pend*(x1)+ b
        indexValMax = xValues.index(numpy.max(yValues))
        m = yValues[indexValMax]
        exp = numpy.exp(-solGauss[0]*pow((x2-m),2))

        # Funciones
        plt.plot(x1, lineal, label='Lineal')
        plt.plot(x2, exp, label='Exponencial')

        # Add a legend
        plt.legend()

        #Limits
        axes = plt.gca()
        axes.set_xlim([numpy.min(xValues)-0.2,numpy.max(xValues)+0.2])
        axes.set_ylim([numpy.min(yValues)-0.2,numpy.max(yValues)+0.2])

        # Show the plot
        plt.show()

    def generateRandom(self, limitL, limitR): #Para generar numeros aleatorios
        return (limitR - limitL)*numpy.random.random_sample() + limitL;


    def evaluate_function_line(self, m, b): #Evalúa un "m" y "b"
        value = 0
        for x,y in self.points:
            value += abs(m*x + b - y)
        return value
        
    def evaluate_restrictions_line(self, m, b): #Revisa que se cumpla las restricciones de "m" y "b"
        return (self.minResM<= m <=self.maxResM) and (self.minResB <= b <= self.maxResB)

    def evaluate_function_gauss(self, k): #Evalúa la función Gaussiana para un "k"
        value = 0
        for x, y in self.points:
            value += abs( (math.exp(-k*((x-self.M_gauss)**2))) - y)
        return value
        
    def evaluate_restrictions_gauss(self, k): #Revisa que se cumpla las restricciones para algún K
        return self.minResK <= k <= self.maxResK
    
    def init_line(self): #Indica al código que se procesará una función lineal con dos variables
        self.option = 0
        self.number_variables = 2
        self.restrictions = [0 for i in range(self.number_variables)]
        self.restrictions[0] = (-100,100)
        aux = (sum(x for x,y in self.points))
        self.restrictions[1] = (-aux,aux)
        return


    def init_gauss(self): #Indica al código que se procesará una función lineal con una variable
        self.option = 1
        self.number_variables = 1
        self.restrictions = [(0,5)]
        max_y = -1
        for x,y in self.points: #Para encontrar el "X" del "Y" Máximo
            if(y > max_y):
                self.M_gauss = x
                max_y = y      
        return

    def evaluate_function(self, variables): #Revisa qué tipo de función se va a evaluar
        if self.option == 0:
            return self.evaluate_function_line(variables[0], variables[1])
        else:
            return self.evaluate_function_gauss(variables[0])

    def evaluate_restrictions(self, x, y = 0): #Revisa qué tipo de restricciones se van a evaluar
        if self.option == 0:
            return self.evaluate_restrictions_line(x, y)
        else:
            return self.evaluate_restrictions_gauss(x)

    def solve(self):
        curr_solutions = [0 for i in range(self.number_variables)]
        best_solutions = [0 for i in range(self.number_variables)]
        
        curr_value = self.evaluate_function(curr_solutions)
        best_value = curr_value
        
        begin = time.time()

        
        T = 0.5*curr_value

        for i in range(self.NUM_ITER):
            
            for j in range(self.NUM_POBL):

                next_solutions = []
                for k in range(self.number_variables): #Genera posibles soluciones
                    limitL, limitR = self.restrictions[k]
                    next_solutions.append(self.generateRandom(limitL, limitR))


                next_value = self.evaluate_function(next_solutions) #Obtiene la función para las posibles soluciones

                diff_values = (curr_value - next_value)
                if diff_values > 0 or (math.exp(diff_values/T) > self.generateRandom(0,1)): #Si el valor es menor o se cumple la desigualdad entonces 
                                                                                            #se aceptan las posibles soluciones
                    curr_solutions = next_solutions[:]
                    curr_value = next_value
                    if curr_value < best_value: #Si la posible solución es la menor globalmente, se guarda en la respuesta
                        best_value = curr_value
                        best_solutions = curr_solutions[:]
                    T = 0.51*T # Se actualiza T
            
            
        print(json.dumps({"S":best_solutions, "Z":best_value}));
        return best_solutions
        # print(time.time() - begin)
        
        

# A = ATS([(1, 0.42), (3, 0.75), (3.5, 1.00), (4, 0.92)])
# A = ATS([(15, 0.3), (25, 0.45), (30, 0.78), (34, 1), (40, 0.85)])
# A = ATS([(0.2, 0.1), (0.5,0.83), (0.9, 0.4)])