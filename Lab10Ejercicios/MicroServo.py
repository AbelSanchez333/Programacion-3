import serial
import tkinter as tk

# Establecer la comunicación serial con Arduino
arduino_port = 'COM3'  # Cambiar al puerto serial correcto
arduino_baud = 9600
ser = serial.Serial(arduino_port, arduino_baud, timeout=1)

# Funciones para enviar comandos al Arduino
def move_left():
    ser.write(b'1')  # Enviar '1' al Arduino

def move_right():
    ser.write(b'2')  # Enviar '2' al Arduino

def set_position():
    position = position_entry.get()  # Obtener la posición ingresada
    try:
        position_int = int(position)
        if 0 <= position_int <= 180:
            ser.write(str(position_int).zfill(3).encode())  # Enviar la posición al Arduino, rellenando con ceros a la izquierda si es necesario
    except ValueError:
        print("Error: La posición debe ser un número entre 0 y 180.")

# Crear la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Control de Micro Servo")

# Configurar el tamaño de los botones
button_width = 25
button_height = 3

# Configurar el color y el estilo de fuente de los botones
button_bg1 = "#4BD440"
button_bg2 = "#405FD4"
button_bg3 = "#D44040"   # Color de fondo en formato hexadecimal
button_fg = "white"    # Color de texto
button_font = ("Comic sans MS", 15, "bold")  # Estilo de fuente

# Crear los botones para mover el servo
left_button = tk.Button(root, text="Mover a la izquierda 180°", command=move_left, width=button_width, height=button_height, bg=button_bg1, fg=button_fg, font=button_font)
left_button.pack(side=tk.LEFT, padx=10, pady=10)  # Alinear a la izquierda y agregar espacio

right_button = tk.Button(root, text="Mover a la derecha 0°", command=move_right, width=button_width, height=button_height, bg=button_bg2, fg=button_fg, font=button_font)
right_button.pack(side=tk.LEFT, pady=10)  # Alinear a la izquierda y agregar espacio

# Crear una entrada para establecer la posición
position_entry_label = tk.Label(root, text="Posición (0-180):", font=("Comic sans MS", 12))
position_entry_label.pack(pady=(20, 5))  # Agregar espacio superior

position_entry = tk.Entry(root, font=("Comic sans MS", 12))
position_entry.pack(pady=5)

position_button = tk.Button(root, text="Establecer Posición", command=set_position, width=button_width, height=button_height, bg=button_bg3, fg=button_fg, font=button_font)
position_button.pack(pady=10)

# Función para cerrar la conexión serial al cerrar la ventana
def on_close():
    ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)  # Asignar la función on_close() al cerrar la ventana
root.mainloop()
