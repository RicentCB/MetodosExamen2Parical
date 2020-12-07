import sys
import matplotlib.pyplot as plt
import numpy as np

from Templado import ATS

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        lenArray = len(sys.argv) - 1
        arrCordsVal = list()
        for i in range(1, int(lenArray/2)):
            arrCordsVal.append((float(sys.argv[(2*i)+1]), float(sys.argv[(2*i)+2])))
        # print(arrCordsVal)
        inter = int(sys.argv[1][1::])
        pob = int(sys.argv[2][1::])
        # A = ATS([(0.2, 0.1), (0.5,0.83), (0.9, 0.4)], inter, pob)
        A = ATS(arrCordsVal, inter, pob)


    else:
        print("Faltan argumentos")