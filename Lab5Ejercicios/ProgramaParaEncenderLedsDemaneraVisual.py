import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *

estadoLed = 0
puerto = None

def setup():
    global puerto
    try:
        puerto = serial.Serial(comports()[0].device, 9600)
        sleep(2)  # Espera a que se establezca la conexión
    except Exception as e:
        print("Error al establecer la conexión serial:", e)

def draw():
    global estadoLed
    if estadoLed == 0:
        canvas.create_oval(width/2 - 25, height/2 - 25, width/2 + 25, height/2 + 25, fill="#FF0000")
    elif estadoLed == 1:
        canvas.create_oval(width/2 - 22.5, height/2 - 22.5, width/2 + 22.5, height/2 + 22.5, fill="#F4FFA5")

def mousePressed(event):
    global estadoLed
    if estadoLed == 0:
        estadoLed = 1
        if puerto:
            puerto.write(b'1')
    else:
        estadoLed = 0
        if puerto:
            puerto.write(b'0')

# Configuración de la ventana
root = Tk()
width = 200
height = 200
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()

setup()

canvas.bind("<Button-1>", mousePressed)

root.mainloop()  # Mantén la aplicación en funcionamiento

