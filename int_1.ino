#define spd_right 90
#define spd_left 98
const byte ledPin = 13;
const byte interruptPin_left = 2;
const byte interruptPin_right = 3;
volatile unsigned int count_left = 0;
volatile unsigned int count_right = 0;

int left_pwm = 4;
int right_pwm = 5;

int dir_left = 6;
int dir_right = 7;

int brake_left = 8;
int brake_right = 9;
int y;
int response = 0;
void setup() {

  pinMode(interruptPin_left,INPUT);
  digitalWrite(interruptPin_left,HIGH);
  
  pinMode(interruptPin_right,INPUT);
  digitalWrite(interruptPin_right,HIGH);
   
  attachInterrupt(0, left_ISR,RISING); //left motor int0 pin2
  attachInterrupt(1, right_ISR,RISING); //right motor int1 pin 3
  Serial.begin(9600);

  pinMode(left_pwm,OUTPUT);
  pinMode(right_pwm,OUTPUT);
 // analogWrite(dir_right,255);
 // analogWrite(dir_left,255);
}

void forward()
{
  analogWrite(brake_left,0);
  analogWrite(brake_right,0);
  analogWrite(dir_left,255);
  analogWrite(dir_right,255);
  
}
///

void left()
{
  analogWrite(brake_left,0);
  analogWrite(brake_right,0);
  analogWrite(dir_left,0);
  analogWrite(dir_right,255);
}

void right()
{
  analogWrite(brake_left,0);
  analogWrite(brake_right,0);
  analogWrite(dir_left,255);
  analogWrite(dir_right,0); 
}

void back()
{
 analogWrite(brake_left,0);
  analogWrite(brake_right,0);
  analogWrite(dir_left,0);
  analogWrite(dir_right,0);
  
}

void brake()
{
  
  analogWrite(brake_left,255);
  analogWrite(brake_right,255);
  
}


void linear_distance_mm(unsigned int DistanceInMM ,int masterPower)
{ int slavePower = masterPower -9 ;
  int error = 0;
  int kp = 1;
  unsigned long int totalTicks = 0;
  
  float ReqdShaftCount = 0;
  unsigned long int ReqdShaftCountInt = 0;

  ReqdShaftCount = DistanceInMM / 0.6059649; // division by resolution to get shaft count
  ReqdShaftCountInt = (unsigned long int) ReqdShaftCount;
  
  count_right = 0;
  count_left = 0;
  
  while(totalTicks < ReqdShaftCountInt)
  {
    analogWrite(left_pwm, masterPower);
    analogWrite(right_pwm,slavePower);

    error = count_left - count_right;
    slavePower += error/kp;

    count_left = 0;
    count_right = 0;
    Serial.print("error: "); Serial.print(error);
    Serial.print(" MP :"); Serial.print(masterPower);
    Serial.print(" SP:"); Serial.println(slavePower);
    delay(0.1);
    totalTicks += count_left;
  }
Serial.print(response);   //this is sending response to pi when it goes forward and backward
brake(); //Stop robot
}


void angle_rotate(unsigned int Degrees)
{
  float ReqdShaftCount = 0;
  unsigned long int ReqdShaftCountInt = 0;

  ReqdShaftCount = (float) Degrees/ 0.315789; // division by resolution to get shaft count
  ReqdShaftCountInt = (unsigned int) ReqdShaftCount;
  count_right  = 0;
  count_left = 0;

  while (1)
  {
    if((count_right  >= ReqdShaftCountInt) | (count_left >= ReqdShaftCountInt))
    break;
    
  }
  Serial.print(response);   //this will send 2 for left and 3 for right turn.
  brake(); //Stop robot
}

void forward_mm(unsigned int DistanceInMM, int power)
{
  forward();
  response = "1";   //we are sending 1 back to pi that forward is done
  linear_distance_mm(DistanceInMM, power);
}

void back_mm(unsigned int DistanceInMM)
{
  back();
  
//  linear_distance_mm(DistanceInMM ,int power);
}

void left_degrees(unsigned int Degrees)
{
  // 88 pulses for 360 degrees rotation 4.090 degrees per count
  left(); //Turn left
  response = "2"; 
  angle_rotate(Degrees);
}



void right_degrees(unsigned int Degrees)
{
  // 88 pulses for 360 degrees rotation 4.090 degrees per count
  right(); //Turn right
  response = "3";
  angle_rotate(Degrees);
}
void left_ISR()
{
  count_left++;
}

void right_ISR()
{
  count_right++;
}



//loooooooooooooooooooooooooooooooooooooooooooooooooooooop
void loop()
{
  if(Serial.available())  // data is coming from pi , "pathfind.py" send data to "com.py" and "com.py" send data to arduino
                         // data 1 for forward, 2 for left , 3 for right ,4 for brake , 5 for back
                         // when motion will be completed arduino will send response back to pi and waiting for next command.
                          // arduino will send 1 when forward motion will be done, (see the last line of linear_distance_mm(unsigned int DistanceInMM ,int masterPower))
                          // response value is changed from respective functions like left,right
  {
    y = Serial.read() - '0';
    
    decision(y);    //according to command from  pi motion will take place.
  }
  
  delay(500);
  analogWrite(left_pwm,spd);
  analogWrite(right_pwm,spd);
}

void decision(int n)
{
  if(n == 1)
  {
    forward_mm(40);
  }
  if(n == 2)
  {
    left_degrees(90);
  }
  if(n == 3)
  {
    right_degrees(90);
  }
  if(n == 4)
  {
    brake();
  }
  
  if( n == 5)
  {
    start();  //robot will move forward always
  }
  
}
