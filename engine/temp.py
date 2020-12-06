import numpy
from scipy.stats import norm

#Algoritmo de templado simulado

def generateRandom():
    return abs(numpy.random.normal(0.5,1.0)*numpy.random.rand(1))

randomnum = generateRandom()
invrand = norm.ppf(randomnum)

print(randomnum)
print(invrand)



