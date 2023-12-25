#define sensor_pin A0
#define test_pin A1
#define led_pin 2

bool streaming = false;
bool send_one_value = false;
long previous_send_time = 0;
long send_count = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(test_pin, INPUT);
  pinMode(led_pin, OUTPUT);
}

void loop() {
  int a = analogRead(test_pin);
  Serial.println(a);
  if(a < 600){
     digitalWrite(led_pin, HIGH); 
  }else{
     digitalWrite(led_pin, LOW); 
  }
}

void send_photo_data() {
  int val = analogRead(sensor_pin);
  Serial.print("Sensor value:");
  Serial.println(val);  
}

void data_reading() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'p') { // p for Photo sensor
      streaming = true;
    } else if (command == 's') { // s for Single value
      streaming = false;
      send_one_value = true;
    }
    else {
      streaming = false;
    }
  }
}
