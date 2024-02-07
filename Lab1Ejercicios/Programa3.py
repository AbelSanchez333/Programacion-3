print("*** CALCULAR DIVISAS EXTRANGERAS ***")
print("-1: Quetzal")
print("-2 Dolar")
print("-3: Euro")
print("-4: Yen")
opcion = input("Ingrese el numero de la moneda que desea convertir a otra: ")
opcion = int(opcion)

if opcion == 1:
    quetzales = input("Ingrese la cantidad de quetzales a convertir: Q")
    quetzales = float(quetzales)

    dolar = 0.128 * quetzales
    dolar = float(dolar)

    euro = 0.117 * quetzales
    euro = float(euro)

    yen = 0.052 * quetzales
    yen = float(yen)

    print("-Q",quetzales,"es igual a: ")
    print("-",dolar,"dolares")
    print("-",euro,"euros")
    print("-",yen,"yenes")

##este es un comentario
if opcion == 2:
    dolar = input("Ingrese la cantidad de dolares a convertir: $")
    dolar = float(dolar)

    quetzal = 7.81 * dolar
    quetzal = float(quetzal)

    euro = 0.92 * dolar
    euro = float(euro)

    yen = 148.35 * dolar
    yen = float(yen)

    print("-$",dolar,"es igual a: ")
    print("-",quetzal,"quetzales")
    print("-",euro,"euros")
    print("-",yen,"yenes")

if opcion == 3:
    euro = input("Ingrese la cantidad de euros a convertir: $")
    euro = float(euro)

    quetzal = 8.47 * euro
    quetzal = float(quetzal)

    dolar = 1.08 * euro
    dolar = float(dolar)

    yen = 161.02 * euro
    yen = float(yen)

    print("-€",euro,"es igual a: ")
    print("-",quetzal,"quetzales")
    print("-",dolar,"dolares")
    print("-",yen,"yenes")

if opcion == 4:
    yen = input("Ingrese la cantidad de yenes a convertir: ¥")
    yen = float(yen)

    quetzal = 0.05 * yen
    quetzal = float(quetzal)

    dolar = 0.0067 * yen
    dolar = float(dolar)

    euro = 0.0062 * yen
    euro = float(euro)

    print("-¥",yen,"es igual a: ")
    print("-",quetzal,"quetzales")
    print("-",dolar,"dolares")
    print("-",euro,"euros")

if opcion < 0 or opcion > 4:
    print("Numero invalido, vuelve a intentarlo")
















