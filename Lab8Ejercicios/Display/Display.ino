// Definición de los pines para cada segmento del display
const int segmentos[10][7] = {
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}, // 3
  {0, 1, 1, 0, 0, 1, 1}, // 4
  {1, 0, 1, 1, 0, 1, 1}, // 5
  {1, 0, 1, 1, 1, 1, 1}, // 6
  {1, 1, 1, 0, 0, 0, 0}, // 7
  {1, 1, 1, 1, 1, 1, 1}, // 8
  {1, 1, 1, 1, 0, 1, 1}  // 9
};

// Definición de los pines del display
const int pin_a = 2;
const int pin_b = 3;
const int pin_c = 4;
const int pin_d = 5;
const int pin_e = 6;
const int pin_f = 7;
const int pin_g = 8;

void setup() {
  // Configurar pines como salida
  pinMode(pin_a, OUTPUT);
  pinMode(pin_b, OUTPUT);
  pinMode(pin_c, OUTPUT);
  pinMode(pin_d, OUTPUT);
  pinMode(pin_e, OUTPUT);
  pinMode(pin_f, OUTPUT);
  pinMode(pin_g, OUTPUT);
}

void loop() {
  // Encender números del 1 al 9 en el display
  for (int i = 1; i <= 9; i++) {
    mostrarNumero(i);
    delay(1000); // Mostrar cada número durante 1 segundo
  }
}

void mostrarNumero(int numero) {
  // Apagar todos los segmentos
  apagarSegmentos();
  
  // Encender segmentos correspondientes al número dado
  for (int i = 0; i < 7; i++) {
    if (segmentos[numero][i] == 1) {
      encenderSegmento(i);
    }
  }
}

void apagarSegmentos() {
  digitalWrite(pin_a, LOW);
  digitalWrite(pin_b, LOW);
  digitalWrite(pin_c, LOW);
  digitalWrite(pin_d, LOW);
  digitalWrite(pin_e, LOW);
  digitalWrite(pin_f, LOW);
  digitalWrite(pin_g, LOW);
}

void encenderSegmento(int segmento) {
  switch (segmento) {
    case 0:
      digitalWrite(pin_a, HIGH);
      break;
    case 1:
      digitalWrite(pin_b, HIGH);
      break;
    case 2:
      digitalWrite(pin_c, HIGH);
      break;
    case 3:
      digitalWrite(pin_d, HIGH);
      break;
    case 4:
      digitalWrite(pin_e, HIGH);
      break;
    case 5:
      digitalWrite(pin_f, HIGH);
      break;
    case 6:
      digitalWrite(pin_g, HIGH);
      break;
  }
}
