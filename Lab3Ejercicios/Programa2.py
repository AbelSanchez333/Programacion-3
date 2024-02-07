print("**CONDICIONALES Y OPERADORES RELACIONALES**")
try:
    numero = float(input("Ingrese un numero: "))
    if numero < 0:
        print("El numero que ingreso es negativo")
    elif numero > 0:
        print("El numero que ingreso es positivo")
    else:
        print("El numero que ingreso es cero")
except ValueError:
    print("EL valor ingresado no es valido")


