int latchPin = 5;
int clockPin = 3;
int dataPin = 7;
unsigned long previousMillis = 0;
const long interval = 1000; // interval in milliseconds (1 second)
int totalSeconds = 0;
int userTime = 0;

bool digits[10][8] = {
  {1,1,0,1,1,1,0,1}, // 0
  {0,1,0,1,0,0,0,0}, // 1
  {1,1,0,0,1,1,1,0}, // 2
  {1,1,0,1,1,0,1,0}, // 3
  {0,1,0,1,0,0,1,1}, // 4
  {1,0,0,1,1,0,1,1}, // 5
  {1,0,1,1,1,1,1,1}, // 6
  {1,1,0,1,0,0,0,0}, // 7
  {1,1,0,1,1,1,1,1}, // 8
  {1,1,1,1,1,0,1,1}  // 9
};

void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  digitalWrite(clockPin, LOW);
  Serial.begin(9600);
  
  // Prompt the user for the time in minutes and seconds
  Serial.println("Enter the time in minutes and seconds:");
  while (userTime == 0){
    userTime = Serial.parseInt();
    int minutes = userTime / 100; 
    int seconds = userTime % 100; 
    if (minutes >= 60 and seconds >= 60) {
    	Serial.println("Incorrect number entered!");
      	Serial.println("Enter the time in minutes and seconds:");
    	userTime = 0;
    }
    
  }
}

void show_time(int number) {
  int thousands = number / 1000;
  int hundreds = (number / 100) % 10;
  int tens = (number / 10) % 10;
  int ones = number % 10;

  digitalWrite(latchPin, LOW);

  for (int i = 7; i >= 0; i--) {
    shift_and_set(digits[thousands][i]);
  }
  for (int i = 7; i >= 0; i--) {
    shift_and_set(digits[hundreds][i]);
  }
  for (int i = 7; i >= 0; i--) {
    shift_and_set(digits[tens][i]);
  }
  for (int i = 7; i >= 0; i--) {
    shift_and_set(digits[ones][i]);
  }

  digitalWrite(latchPin, HIGH);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // enough time has passed to update the time
    previousMillis = currentMillis;

    // Update the time
    userTime++;
    int number = userTime % 10000;
    
    show_time(number);
  }
}

void shift_and_set(bool val) {
  digitalWrite(dataPin, val);
  digitalWrite(clockPin, HIGH);
  delay(10);
  digitalWrite(clockPin, LOW);
}
