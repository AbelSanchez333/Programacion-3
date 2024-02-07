print("*** FORMULA CUADRATICA ***")
print("ax^2 + bx + c = 0")
print("Ingrese los valores de los coeficientes a, b, c de su")
print("ecuacion cuadratica para encontrar las soluciones")
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
c = input("Ingrese el valor de c: ")

a = float(a)
b = float(b)
c = float(c)

x1 = ((-(b)+(((b**2)-4*a*c)**0.5))/(2*a))
x1 = float(x1)
x2 = ((-(b)-(((b**2)-4*a*c)**0.5))/(2*a))
x2 = float(x2)

print("Las soluciones de la ecuacion cuadratica son: ")
print("x1 =",x1)
print("x2 =",x2)












