arreglo = [23,6,4,3,54,54,34]
'''
arreglo = [6,23,4,3,54,54,34]
arreglo = [6,4,23,3,54,54,34]
arreglo = [6,4,3,23,54,54,34]
arreglo = [6,4,3,23,54,34,54]
arreglo = [4,6,3,23,54,34,54]
arreglo = [4,3,6,23,54,34,54]
arreglo = [4,3,6,23,34,54,54]
arreglo = [3,4,6,23,34,54,54]
'''
print("Arreglo no ordenado: ",arreglo)
n = len(arreglo)
contador_de_intercambios = 1

intercambio = True

while (intercambio):
    intercambio = False
    for i in range(1,n):
        if arreglo[i-1]>arreglo[i]:
            arreglo[i-1],arreglo[i] = arreglo[i], arreglo[i-1]
            intercambio = True
            print("Intercambio#",contador_de_intercambios)
            print(arreglo)
            contador_de_intercambios+=1

print("Arreglo ordenado: ",arreglo)
