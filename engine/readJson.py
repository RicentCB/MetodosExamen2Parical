import sys
from Templado import ATS

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        lenArray = len(sys.argv) - 1
        arrCordsVal = list()
        for i in range(0, int(lenArray/2)):
            arrCordsVal.append((float(sys.argv[(2*i)+1]), float(sys.argv[(2*i)+2])))
        # print(arrCordsVal)
        # A = ATS([(0.2, 0.1), (0.5,0.83), (0.9, 0.4)])
        A = ATS(arrCordsVal)

    else:
        print("Faltan argumentos")