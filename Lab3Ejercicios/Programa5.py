print("**CLASES Y METODOS**")

class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        return self.calificacion >= 60

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
edad_estudiante = int(input("Ingrese la edad del estudiante: "))
calificacion_estudiante = int(input("Ingrese la calificación del estudiante: "))

estudiante = Estudiante(nombre_estudiante, edad_estudiante, calificacion_estudiante)

if estudiante.verificar_aprobacion():
    print(f"El estudiante {estudiante.nombre} de {estudiante.edad} años ha aprobado.")
else:
    print(f"El estudiante {estudiante.nombre} de {estudiante.edad} años no ha aprobado.")