from collections import deque

def push(pila, elemento):
    pila.append(elemento)


def pop(pila):
    return pila.pop()


def revertir_lista(lista):
    pila = deque()
    for elemento in lista:
        push(pila, elemento)
        print(elemento)
    lista_revertida = []
    while pila:
        push(lista_revertida, pop(pila))
    return lista_revertida

print("IMPLEMENTAR UNA PILA UTILIZANDO UNA LISTA EN PYTHON")
cantidad_datos = int(input("Ingrese la cantidad de datos: "))

lista_original = []

for i in range(cantidad_datos):
    dato = input(f"Ingrese el dato {i + 1}: ")
    push(lista_original, dato)

lista_revertida = revertir_lista(lista_original)

print("Lista original: ", lista_original)
print("Lista revertida: ", lista_revertida)