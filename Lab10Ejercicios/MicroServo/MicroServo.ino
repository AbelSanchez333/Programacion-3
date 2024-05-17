#include <Servo.h>

Servo myServo;  // Crear un objeto de tipo Servo
int position = 90; // Posición inicial

void setup() {
  Serial.begin(9600);  // Iniciar la comunicación serial a 9600 baudios
  myServo.attach(9);   // Adjuntar el servo al pin 9
}

void loop() {
  if (Serial.available() > 0) {  // Si hay datos disponibles en el puerto serial
    int command = Serial.parseInt();  // Leer el comando como un entero

    // Realizar acciones basadas en el comando recibido
    if (command == 1) {
      position = 180; // Mover a la derecha
    } else if (command == 2) {
      position = 0; // Mover a la izquierda
    } else if (command >= 0 && command <= 180) {
      // Ajustar la posición del servo
      position = command;
    }

    // Aplicar la velocidad y la posición al servo
    myServo.write(position);
    delay(15); // Pequeña pausa para permitir que el servo se mueva
  }
}
