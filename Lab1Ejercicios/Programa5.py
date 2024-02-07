print("*** QUE TIPO DE DATO SE INGRESO ***")
entrada_usuario = input("Ingrese un valor: ")
try:
    entrada_num = eval(entrada_usuario)
    tipo = type(entrada_num).__name__
    print("La entrada es de tipo:", tipo)
except:
    tipo = type(entrada_usuario).__name__
    print("La entrada es de tipo:", tipo)

## condicionales
if tipo == "int":
    print("¡La entrada es un número entero!")
elif tipo == "float":
    print("¡La entrada es un número decimal!")
elif tipo == "str":
    print("¡La entrada es una cadena de texto!")
elif tipo == "bool":
    print("¡La entrada es de tipo booleana!")
else:
    print("¡Tipo de dato no identificado!")

