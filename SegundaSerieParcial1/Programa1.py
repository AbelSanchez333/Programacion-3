##VARIANTE A
#1. Escribe una función en Python que reciba una lista como parámetro y
#devuelva la suma de todos los
#elementos de la lista.

#Se define la funcion 
def suma_lista(lista):
    suma = 0
    #for que recorrera los elementos de la lista 
    for elemento in lista:
        #en suma se guardan los elementos de la lista 
        suma += elemento
    print(f"La sumatoria de la lista es: {suma}")
#Se da una lita como parametro
lista = [1,2,3]
#Se llama a la funcion con la lista 
suma_lista(lista)