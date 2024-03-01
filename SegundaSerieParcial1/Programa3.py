#VARIANTE A
#3. Escribe un programa que pida al usuario una lista de números y luego
#imprima la suma de los números pares en la lista.

#Se le pide a el usuario los datos que se deben ingresar
cantidad_datos = int(input("Ingrese la cantidad de datos para la lista: "))

#se inicia la lista
lista = []

##Se crea un ciclo con la funcion range para que llegue hasta un valor anterior de cantidad datos
##En este ciclo se van ingresando los datos en la lista 
for i in range(cantidad_datos):
    dato = int(input(f"Ingrese el dato {i + 1}: "))
    #Se utiliza el metodo append para ingresar los datos en la lista 
    lista.append(dato)
suma=0
#Se hace un for que recorrera cada elemento de la lista 
for elemento in lista:
    #Se hace un condicional que solo funcionara si el numero es par
    if (elemento%2 == 0):
        #Se suma el valor solo si es par
        suma = suma + elemento
#Se imprime la suma de los numeros pares
print(f"La suma de los numeros pares de la lista ingresada es: {suma}")








