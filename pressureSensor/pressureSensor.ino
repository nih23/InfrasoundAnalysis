void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float IN = analogRead(A0);
  /*delay(10);
  float IN2 = analogRead(A0);
  delay(10);
  float IN3 = analogRead(A0);
  delay(10);
  float IN4 = analogRead(A0);
  float IN = (IN1+IN2+IN3+IN4) / 4.; */
  
  float pressure = ((IN/1023.0 - .2) / .2); //transfer function from manufacturer
  byte * b = (byte *) &pressure;
  
  Serial.print(pressure,5);
  Serial.println();
  //delay(100);
}
