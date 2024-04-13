const int pbuttonPre = 8;
const int pbuttonIn = 9;
const int pbuttonPos = 10; 

const int ledPadre = 4;
const int ledHijoI = 3;
const int ledHijoD = 5;

bool leerPotenciometro = true;

void setup() {
  pinMode(ledPadre, OUTPUT);
  pinMode(ledHijoI, OUTPUT);
  pinMode(ledHijoD, OUTPUT);
  pinMode(pbuttonPre, INPUT_PULLUP);
  pinMode(pbuttonIn, INPUT_PULLUP);
  pinMode(pbuttonPos, INPUT_PULLUP);  
  Serial.begin(9600);
}

void loop() {
  if (leerPotenciometro) {
    int pot = analogRead(A0);
    Serial.println(pot);
    delay(10);
  }
  int button1 = digitalRead(pbuttonPre);
  int button2 = digitalRead(pbuttonIn);
  int button3 = digitalRead(pbuttonPos);
  
  if (button1 == LOW) {
    Serial.println("Preorden Iniciado");
    Serial.println(4);
    digitalWrite(ledPadre, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPadre, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledHijoI, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledHijoI, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledHijoD, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledHijoD, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println(10);
    Serial.println("Preorden Finalizado");
  }
  if(button2 == LOW){
    Serial.println("Inorden Iniciado");
    Serial.println(5);
    digitalWrite(ledHijoI, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledHijoI, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPadre, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPadre, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledHijoD, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledHijoD, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println(10);
    Serial.println("Inorden Finalizado");
  }
  if(button3 == LOW){
    Serial.println("Postorden Iniciado");
    Serial.println(6);
    digitalWrite(ledHijoI, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledHijoI, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledHijoD, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledHijoD, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPadre, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPadre, LOW);
    Serial.println(0);
    Serial.println(10);
    Serial.println("Postorden Finalizado");
  }

}



