import serial
import tkinter as tk
import threading

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM3', 9600)

# Función para leer datos del puerto serie en un hilo separado
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)

# Función para encender un círculo
def turn_on_circle(circle, color):
    canvas.itemconfig(circle, fill=color)

# Función para apagar un círculo
def turn_off_circle(circle):
    canvas.itemconfig(circle, fill="white")

# Función para manejar los datos recibidos del puerto serie
def handle_code(code):
    try:
        digit = int(code)
        print("Código recibido:", digit)
        # Apagar todos los círculos primero
        for circle in circles:
            turn_off_circle(circle)

        # Encender el círculo correspondiente al código recibido
        if digit == 2:
            turn_on_circle(circles[0], "green")
        elif digit == 1:
            turn_on_circle(circles[1], "red")
        elif digit == 3:
            turn_on_circle(circles[2], "green")
        
        if digit == 4:
            square1 = canvas.create_rectangle(15, 15, 60, 60, fill="blue", width=2)
            canvas.move(square1, 350, 140)
        elif digit == 5:
            square1 = canvas.create_rectangle(15, 15, 60, 60, fill="blue", width=2)
            canvas.move(square1, 420, 140)
        elif digit == 6:
            square1 = canvas.create_rectangle(15, 15, 60, 60, fill="blue", width=2)
            canvas.move(square1, 490, 140)
        elif digit == 10:
            square1 = canvas.create_rectangle(15, 15, 60, 60, fill="white", width=2)
            canvas.move(square1, 350, 140)
            square1 = canvas.create_rectangle(15, 15, 60, 60, fill="white", width=2)
            canvas.move(square1, 420, 140)
            square1 = canvas.create_rectangle(15, 15, 60, 60, fill="white", width=2)
            canvas.move(square1, 490, 140)
        # Actualizar el valor de la barra de potenciómetro
        update_bar_graph(digit)
        # Actualizar el valor del potenciómetro
        update_pot_value(digit)
    except ValueError:
        print("Mensaje desde Arduino:", code)

# Función para actualizar la barra de potenciómetro
def update_bar_graph(value):
    # Normalizar el valor para que esté en el rango de 0 a 1 (Tkinter no acepta valores fuera de este rango)
    normalized_value = value / 1023
    # Calcular las coordenadas de la barra
    x0 = 50
    y0 = 350
    x1 = 60 + normalized_value * 500  # El valor máximo es 1023, por lo que 500 corresponde a aproximadamente la mitad del rango horizontal
    y1 = 400
    # Calcular el color en función del valor del potenciómetro
    color = '#%02x%02x%02x' % (int(192 - (normalized_value * 192)), int(192 - (normalized_value * 192)), int(192 - (normalized_value * 192)))

    # Actualizar las coordenadas y el color de la barra
    canvas.coords(bar, x0, y0, x1, y1)
    canvas.itemconfig(bar, fill=color)

# Función para actualizar el valor del potenciómetro
def update_pot_value(value):
    pot_text.config(text=f"Valor Potenciómetro: {value}")

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Botón Controlador")
root.geometry("800x600")

# Configuración de la gráfica de barras
canvas = tk.Canvas(root, width=600, height=500, bg='white')
canvas.pack()
bar = canvas.create_rectangle(50, 350, 60, 400, fill='#c0c0c0', width=2)  # Rectángulo que representa la barra de potenciómetro

# Crear círculos
circles = []
for i in range(3):
    circle = canvas.create_oval(50 + i * 70, 150, 100 + i * 70, 200, outline="black", width=2)
    canvas.create_text(75 + i * 70, 175, font=("Arial", 12))
    circles.append(circle)

square1 = canvas.create_rectangle(15, 15, 60, 60, fill="white", width=2)
canvas.move(square1, 350, 140)

square2 = canvas.create_rectangle(15, 15, 60, 60, fill="white", width=2)
canvas.move(square2, 420, 140)

square3 = canvas.create_rectangle(15, 15, 60, 60, fill="white", width=2)
canvas.move(square3, 490, 140)

# Texto "Botones" encima del botón
root.option_add("*Font", "Georgia")
button_text = tk.Label(root, text="Laboratorio #7")
button_text.place(x=340, y=30)
button_text = tk.Label(root, text="Arbol")
button_text.place(x=215, y=100)
button_text = tk.Label(root, text="NodoI")
button_text.place(x=150, y=225)
button_text = tk.Label(root, text="Raiz")
button_text.place(x=225, y=225)
button_text = tk.Label(root, text="NodoD")
button_text.place(x=290, y=225)
button_text = tk.Label(root, text="Preorden")
button_text.place(x=445, y=225)
button_text = tk.Label(root, text="Inorden")
button_text.place(x=525, y=225)
button_text = tk.Label(root, text="Postorden")
button_text.place(x=590, y=225)
button_text = tk.Label(root, text="Ordenes")
button_text.place(x=525, y=100)

# Texto "Potenciómetro" encima de la barra
pot_text = tk.Label(root, text="Potenciómetro")
pot_text.place(x=350, y=300)
pot_text = tk.Label(root, text="Valor Potenciómetro: ")
pot_text.place(x=310, y=425)

# Crear y ejecutar el hilo para leer datos del puerto serie
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Ejecutar la aplicación Tkinter
root.mainloop()
