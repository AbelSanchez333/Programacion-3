##Se define a la funcion parentesis balanceados 
def paréntesis_balanceados(cadena):

    ##Se define la pila 
    pila = []
    ##Se ingresan los diferentes diccionarios con los parentesis corchetes y llaves
    paréntesis_abiertos = {'(', '[', '{'}
    paréntesis_cerrados = {')', ']', '}'}
    paréntesis_correspondientes = {')': '(', ']': '[', '}': '{'}

    ##Se crea un for donde se evaluara cada caracacter de la cadena 
    for caracter in cadena:
        if caracter in paréntesis_abiertos:
            pila.append(caracter)
        elif caracter in paréntesis_cerrados:
            if not pila or pila.pop() != paréntesis_correspondientes[caracter]:
                return False
    
    # La cadena está balanceada si la pila está vacía al final
    return not pila

##Se ingresa una cadena de texto con parentesis 
print("VERIFICACION DE PARENTESIS BALANCEADOS")
cadena_ejemplo = input("Ingrese una cadena de paréntesis: ")

##Se pone en la condicional a la funcion parentesis balanceados con el valor de la cadena ingresada
##En caso de que retorne un valor bool falso no estan balanceados
if paréntesis_balanceados(cadena_ejemplo):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")