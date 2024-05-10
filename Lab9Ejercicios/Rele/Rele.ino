int relayPin = 3;  // Pin para controlar el relé
int ledPin = 8;   // Pin para el LED adicional

void setup() {
  pinMode(relayPin, OUTPUT);  // Configura el pin del relé como salida
  pinMode(ledPin, OUTPUT);    // Configura el pin del LED como salida
}

void loop() {
  // Encender el relé y esperar 4 segundos
  digitalWrite(relayPin, HIGH);  // Activa el relé
  delay(4000);

  // Apagar el relé y encender el LED por dos segundos
  digitalWrite(relayPin, LOW);  // Desactiva el relé
  digitalWrite(ledPin, HIGH);    // Enciende el LED
  delay(2000);  // Espera dos segundos
  digitalWrite(ledPin, LOW);     // Apaga el LED

  // Esperar 3 segundos antes de repetir el ciclo
  delay(3000);
}
