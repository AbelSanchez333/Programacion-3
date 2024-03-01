arreglo = [2,4,9,8,45,5,10]
n = len(arreglo)
print("Arreglo desordenado: ", arreglo)

contador = 1
intercambio = True

while(intercambio):
    intercambio = False 
    for i in range(1,n):
        if arreglo[i-1]>arreglo[i]:
            arreglo[i-1],arreglo[i]=arreglo[i],arreglo[i-1]
            intercambio = True
            contador += 1

print("Arreglo ordenado: ", arreglo)











