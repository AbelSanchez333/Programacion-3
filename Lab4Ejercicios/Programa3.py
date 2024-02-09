def paréntesis_balanceados(cadena):
    pila = []
    paréntesis_abiertos = {'(', '[', '{'}
    paréntesis_cerrados = {')', ']', '}'}
    paréntesis_correspondientes = {')': '(', ']': '[', '}': '{'}

    for carácter in cadena:
        if carácter in paréntesis_abiertos:
            pila.append(carácter)
        elif carácter in paréntesis_cerrados:
            if not pila or pila.pop() != paréntesis_correspondientes[carácter]:
                return False

    # La cadena está balanceada si la pila está vacía al final
    return not pila

# Ejemplo de uso
cadena_ejemplo = input("Ingrese una cadena de paréntesis: ")
if paréntesis_balanceados(cadena_ejemplo):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")