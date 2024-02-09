##Se importa de las collecciones deque
from collections import deque
##Se importa time para poder hacer pausas en el codigo
import time

##Se define la funcion enqueue que ingresa un elemento a la cola
def enqueue(cola, elemento):
    cola.append(elemento)

##Se define la funcion dequeue que elimina el primer elemento de la cola 
def dequeue(cola):
    return cola.popleft()

##Se define la funcion simular linea de espera que simulara el proceso
def simular_linea_espera(clientes):
    queue = deque(clientes)
    ##El ciclo se repetira mientras la cola siga existiendo
    while queue:
        print("Atendiendo a la persona:", dequeue(queue))
        ##Time sirve para hacer una pausa de 1 segundo en la ejecucion del codigo 
        time.sleep(1)

##Se ingresa la cantidad de datos para la cola
print("IMPLEMENTAR UNA COLA UTILIZANDO UNA LISTA EN PYTHON")
cantidad_datos = int(input("Ingrese la cantidad de personas en la fila: "))

##Se defina la lista de clientes en espera
clientes_en_espera = []
print("Ingrese segun el orden en que entraron a la cola: ")

##Se crea un ciclo con la funcion range para que llegue hasta un valor anterior de antidad datos
##En este ciclo se van ingresando los datos de la lista 
for i in range(cantidad_datos):
    dato = input(f"Ingrese a la persona {i + 1}: ")
    enqueue(clientes_en_espera, dato)  

##Aqui se llama a la funcion de simular linea de espera con los datos de la lista de clientes en espera 
print("Bienvenido, se le estara atendiendo segun este orden: ")
simular_linea_espera(clientes_en_espera)
print("Todas las personas de la cola han sido atendidas")