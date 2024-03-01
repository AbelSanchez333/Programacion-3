'''
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
'''
from collections import deque
pila = [1,2,3,4,5,6]

pila.append(7)
pila.append(8)
pila.append(9)

pila1 = deque(pila)
cola = deque()
print(pila)

cola.append(pila1.popleft())
cola.append(pila.pop(-1))

print(pila)
print(cola)








