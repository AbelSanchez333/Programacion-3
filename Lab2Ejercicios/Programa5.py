print("PROGRAMA QUE CALCULA LA PAGA CORRESPONDIENTE")
horasTrabajadas = input("¿Cuantas horas ha trabajado? ")
costoHora = input("¿Cunto es el coste por hora? ")
valor1 = float(horasTrabajadas)
valor2 = float(costoHora)

result = valor1 * valor2

result = float(result)

print("Horas trabajadas:",valor1)
print("Costo por hora trabajada:",valor2)
print("Total a pagar: Q",result)

