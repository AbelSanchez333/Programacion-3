##Se importa de las collecciones deque
from collections import deque

##Se define la funcion revertir mitad de la cola 
def revertir_mita_cola(cola):
    if not isinstance(cola, deque):
        raise ValueError("Se esperaba una cola (deque) como entrada")

    ##Obtener la longitud de la cola
    longitud_cola = len(cola)

    ##Verificar si la longitud es par o impar
    es_longitud_impar = longitud_cola % 2 != 0

    if es_longitud_impar:
        print("La longitud de la cola debe ser par")
        return None

    ##Calcular la mitad de la longitud
    mitad_longitud = longitud_cola // 2

    ##Crear una pila para revertir la segunda mitad
    pila_revertir = []

    ##Dividir la cola original en dos partes
    cola_parte1 = deque()
    cola_parte2 = deque()

    ##Se crean ciclos para ir creando las colas y revertirlas 
    for _ in range(mitad_longitud):
        cola_parte1.append(cola.popleft())

    while cola:
        pila_revertir.append(cola.popleft())

    while pila_revertir:
        cola_parte2.append(pila_revertir.pop())

    ##Unir las colas en una sola
    cola_unida = cola_parte1 + cola_parte2
    cola_final = list(cola_unida)
    return cola_unida

##Solicitar al usuario la cantidad de datos
print("REVERTIR LA MITAD DE UNA COLA")
cantidad_datos = int(input("Ingrese la cantidad de datos para la cola: "))

##Llenar la cola con datos ingresados por el usuario
mi_cola = deque()
for i in range(cantidad_datos):
    dato = input(f"Ingrese el dato {i + 1}: ")
    mi_cola.append(dato)

cola_original = list(mi_cola)
print("Cola original:", cola_original)

##Se llama a la funcion revertir mitad de la cola con la cola ingresada anteriormente
cola_resultante = revertir_mita_cola(mi_cola)

##Se muestra el resultado con el condicional por si la cola no es par
if cola_resultante is not None:
    print("Cola con la segunda mitad revertida:",cola_resultante)

