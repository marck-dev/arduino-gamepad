#define X_AXIS A1
#define Y_AXIS A0
#define X_ID X_AXIS
#define Y_ID Y_AXIS

void setup() {
  Serial.begin(115200);
  Serial.print(0xF0F0);
  Serial.print("\n");
  pinMode(X_AXIS, INPUT);
  pinMode(Y_AXIS, INPUT);
}

void loop() {
  unsigned int out = 0;
  int x_axis = analogRead(X_AXIS);
  int y_axis = analogRead(Y_AXIS);
  change2Byte(&x_axis);
  change2Byte(&y_axis);
  Serial.print(X_ID);
  Serial.print("=");
  Serial.print(x_axis);
  Serial.print(";");
  Serial.print(Y_ID);
  Serial.print("=");
  Serial.print(y_axis);
  Serial.print("\n");
}

void change2Byte(int* data){
  *data = (int)(( *data / 1023.0 ) * 255.0);
}
