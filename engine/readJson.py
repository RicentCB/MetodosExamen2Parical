import sys

if(len(sys.argv) > 1):
    lenArray = len(sys.argv) - 1
    arrCordsVal = list()
    for i in range(0, int(lenArray/2)):
        arrCordsVal.append((sys.argv[(2*i)+1], sys.argv[(2*i)+2]))
    print(arrCordsVal)

else:
    print("Falta arugmetnos")