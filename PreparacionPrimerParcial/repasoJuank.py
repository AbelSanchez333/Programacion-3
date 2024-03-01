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
'''

'''
arreglo_original = [1,2,3,4,5,6,7,8,9]
print(arreglo_original)
arreglo = []
for elemento in arreglo_original:
    arreglo.append(elemento)
    
arreglo_invertido = []
while(arreglo):
    arreglo_invertido.append(arreglo.pop())

print(arreglo_invertido)
'''
from collections import deque
import time
arreglo_original = [1,2,3,4,5,6,7,8,9]

arreglo_manejable = deque(arreglo_original)

while(arreglo_manejable):
    print(arreglo_manejable.popleft())
    time.sleep(1)


    




