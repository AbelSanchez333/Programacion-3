int estadoLed=0; 

void setup() {
  pinMode(3, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()>0){
    int estadoMonitor = Serial.read();
    if (estadoMonitor == '1'){
      digitalWrite(3, HIGH);  
      digitalWrite(4, HIGH);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      Serial.println("LEDS Rojos encendidos");
      Serial.println("LEDS Verdes apagados");
    }else if (estadoMonitor == '0'){
      digitalWrite(3, LOW);  
      digitalWrite(4, LOW);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      Serial.println("LEDS Verdes encendidos");
      Serial.println("LEDS Rojos apagados");
    }
  }
}