from collections import deque
import time
def enqueue(cola, elemento):
    cola.append(elemento)

def dequeue(cola):
    return cola.popleft()

def simular_linea_espera(clientes):
    queue = deque(clientes)
    while queue:
        print("Atendiendo a la persona:", dequeue(queue))
        time.sleep(1)

print("IMPLEMENTAR UNA COLA UTILIZANDO UNA LISTA EN PYTHON")
cantidad_datos = int(input("Ingrese la cantidad de personas en la fila: "))

clientes_en_espera = []
print("Ingrese segun el orden en que entraron a la cola: ")
for i in range(cantidad_datos):
    dato = input(f"Ingrese a la persona {i + 1}: ")
    enqueue(clientes_en_espera, dato)  

print("Bienvenido, se le estara atendiendo segun este orden: ")
simular_linea_espera(clientes_en_espera)
print("Todas las personas de la cola han sido atendidas")