##Se importa de las collecciones deque
from collections import deque

##Se crea la funcion "peek" para mostrar el primer elemento de cualquier lista
def peek(pila):
    elemento_superior = pila[-1]
    print("El elemento superior de la pila es: ", elemento_superior)

##Se crea la funcion "push" para agregar un elemento a la pila
def push(pila, elemento):
    pila.append(elemento)

##Se crea la funcion "pop" para eliminar un elemento de la pila
def pop(pila):
    return pila.pop()

##Se crea la funcion "revertir lista" para revertir la lista ingresada
def revertir_lista(lista):
    pila = []
    for elemento in lista:
        ##Se ingresan los datos de la lista original en una nueva pila
        push(pila, elemento)
    ##Se crea una nueva pila llamada lista revertida    
    lista_revertida = []
    while pila:
        ##Se ingresan en la lista los lementos que se van eliminando para que queden al revez
        push(lista_revertida, pop(pila))
    return lista_revertida

print("IMPLEMENTAR UNA PILA UTILIZANDO UNA LISTA EN PYTHON")
##Se le pide al usuario que ingrese cuantos datos tendra la pila 
cantidad_datos = int(input("Ingrese la cantidad de datos: "))

##Se inicia la lista original
lista_original = []

##Se crea un ciclo con la funcion range para que llegue hasta un valor anterior de antidad datos
##En este ciclo se van ingresando los datos de la lista 
for i in range(cantidad_datos):
    dato = input(f"Ingrese el dato {i + 1}: ")
    push(lista_original, dato)

##Se crea la variable lista revertida la cual llama la funcion revertir lista con los datos de la lista original
lista_revertida = revertir_lista(lista_original)

##Se muestra la lista original y la lista invertida 
print("Lista original: ", lista_original)
print("Lista revertida: ", lista_revertida)
