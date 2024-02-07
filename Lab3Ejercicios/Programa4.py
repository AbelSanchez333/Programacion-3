print("**FUNCIONES Y CONDICIONALES**")

def suma_es_par(num1, num2):
    suma = num1 + num2
    return suma % 2 == 0


numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
resultado = suma_es_par(numero1, numero2)

if resultado:
    print (f"La suma de ambos numeros es par: {resultado}")
else:
    print (f"La suma de ambos numeros es impar: {resultado}")









