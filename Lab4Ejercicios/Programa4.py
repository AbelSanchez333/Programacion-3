##Se define la clase ColaConPilas
class ColaConPilas:
    def __init__(self):
        self.pila_entrada = []
        self.pila_salida = []

    def enqueue(self, elemento):
        # Operación enqueue: Añadir elemento a la pila de entrada
        self.pila_entrada.append(elemento)

    def dequeue(self):
        # Operación dequeue: Obtener elemento de la cola (si existe)
        if not self.pila_salida:
            # Si la pila de salida está vacía, transferir elementos de la pila de entrada
            # invirtiendo el orden para simular el comportamiento de una cola.
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())

        if self.pila_salida:
            # Devolver el elemento más antiguo (el primero en entrar) de la pila de salida.
            return self.pila_salida.pop()
        else:
            # Si ambas pilas están vacías, la cola está vacía.
            return None

# Crear una instancia de ColaConPilas
cola = ColaConPilas()

# Solicitar al usuario la cantidad de datos
print("IMPLEMENTACION DE UNA COLA CON DOS PILAS")
cantidad_datos = int(input("Ingrese la cantidad de datos: "))

# Llenar la cola con datos ingresados por el usuario
for i in range(cantidad_datos):
    dato = input(f"Ingrese el dato {i + 1}: ")
    cola.enqueue(dato)

# Realizar operaciones de dequeue y mostrar los elementos obtenidos
print("Elementos obtenidos de la cola:")
for i in range(cantidad_datos):
    elemento = cola.dequeue()
    if elemento is not None:
        print(elemento)
    else:
        print("La cola está vacía.")





