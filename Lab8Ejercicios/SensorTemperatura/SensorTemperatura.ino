// Definir el pin al que está conectado el sensor de temperatura
const int sensorPin = A0;

void setup() {
  // Inicializar comunicación serial a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Leer el valor analógico del sensor de temperatura
  int sensorValue = analogRead(sensorPin);

  // Convertir el valor leído en voltaje
  float voltage = sensorValue * (5.0 / 1023.0);

  // Convertir el voltaje en grados Celsius
  float temperatureC = (voltage - 0.5) * 100.0;

  // Mostrar la temperatura en el monitor serial
  Serial.print("Temperatura: ");
  Serial.print(temperatureC);
  Serial.println(" °C");

  // Esperar un breve periodo de tiempo antes de volver a leer el sensor
  delay(1000);
}
