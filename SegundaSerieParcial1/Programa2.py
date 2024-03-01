#VARIANTE A
#2. Define una función llamada "inverso_palabra" que reciba una cadena
#como parámetro y devuelva l cadena invertida. Por ejemplo, si la entrada es "python", la salida
#debería ser "nohtyp".

#Se define la funcion 
def inverso_palabra (cadena):
    #se invierte la cadena utilizando slicing
    cadena_invertida = cadena[::-1]
    #Se imprime la cadena invertida
    print("Cadena invertida:", cadena_invertida)
#Se ingresa la cadena a invertir
cadena_ingresada = input("Ingrese una cadena de texto: ")
#Se llama a la funcion con la cadena ingresada
inverso_palabra(cadena_ingresada)