import tkinter as tk
import serial
import threading

# Inicializar la comunicación serial con Arduino
arduino = serial.Serial('COM3', 9600)  # Reemplaza 'puerto_serial_de_arduino' con el puerto correcto

# Función para procesar los datos recibidos de Arduino
def procesar_datos(datos):
    print("Datos recibidos desde Arduino:", datos.decode().strip())

# Función para enviar comandos a Arduino
def enviar_comando(comando):
    arduino.write(comando.encode())

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Dashboard")

# Estilo botones
estilo_boton = {
    'font': ('Bevan', 12),
    'width': 15,
    'height': 2,
    'bg': '#4BCA5E',  
    'fg': '#005D0E',  
    'activebackground': '#04FF00',  
    'activeforeground': 'black',
    'bd': 0, 
    'highlightthickness': 3,  
}
estilo_boton_circulo = {
    'font': ('Bevan', 12),
    'width': 15,
    'height': 2,
    'bg': '#DA4242',  
    'fg': '#840707',  
    'activebackground': '#FF0000',  
    'activeforeground': 'black',  
    'bd': 0,  
    'highlightthickness': 3,  
}


# Botones
boton_A = tk.Button(ventana, text="Grupo A encendido", command=lambda: enviar_comando('A'), **estilo_boton)
boton_A.pack(pady=5)

boton_B = tk.Button(ventana, text="Grupo B encendido", command=lambda: enviar_comando('B'), **estilo_boton)
boton_B.pack(pady=5)

boton_C = tk.Button(ventana, text="Grupo C encendido", command=lambda: enviar_comando('C'), **estilo_boton)
boton_C.pack(pady=5)

boton_D = tk.Button(ventana, text="Grupo D encendido", command=lambda: enviar_comando('D'),**estilo_boton )
boton_D.pack(pady=5)

boton_A = tk.Button(ventana, text="Todos encendidos", command=lambda: enviar_comando('A''B''C''D'), **estilo_boton)
boton_A.pack(pady=5)

boton_E = tk.Button(ventana, text="Grupo A apagado", command=lambda: enviar_comando('E'), **estilo_boton_circulo )
boton_E.pack(pady=7)

boton_F = tk.Button(ventana, text="Grupo B apagado", command=lambda: enviar_comando('F'), **estilo_boton_circulo)
boton_F.pack(pady=5)

boton_G = tk.Button(ventana, text="Grupo C apagado", command=lambda: enviar_comando('G'), **estilo_boton_circulo)
boton_G.pack(pady=5)

boton_H = tk.Button(ventana, text="Grupo D apagado", command=lambda: enviar_comando('H'),**estilo_boton_circulo)
boton_H.pack(pady=5)

boton_H = tk.Button(ventana, text="Todos apagados", command=lambda: enviar_comando('E''F''G''H'),**estilo_boton_circulo)
boton_H.pack(pady=5)

# Bucle principal para recibir y procesar datos de Arduino
def leer_datos_desde_arduino():
    while True:
        datos = arduino.readline()
        if datos:
            procesar_datos(datos)

# Crear un hilo para leer datos de Arduino en segundo plano
thread_arduino = threading.Thread(target=leer_datos_desde_arduino)
thread_arduino.start()

# Iniciar el bucle de la interfaz de usuario
ventana.mainloop() 