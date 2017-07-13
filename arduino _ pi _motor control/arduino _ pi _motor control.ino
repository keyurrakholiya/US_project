#define spd 50

const int ledpin= 12;
int y;
int left_pwm = 2;
int right_pwm = 3;
int dir_left = 8;
int dir_right = 9;

int brake_left = 10;
int brake_right = 11;

int left_encoder = 12;
int right_encode = 13;

unsigned int left_count = 0;
unsigned int right_count = 0;


void setup()
{
  pinMode(ledpin,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available())
  {
    y = Serial.read() - '0';
    
    light(y);
  }
  
  delay(500);
  analogWrite(left_pwm,spd);
  analogWrite(right_pwm,spd);
}

void light(int n)
{
  if(n == 1)
  {
    digitalWrite(ledpin,HIGH);
    forward();
  }
  if(n == 2)
  {
    left();
  }
  if(n == 3)
  {
    right();
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

void start()
{
  digitalWrite(dir_left,LOW);
  digitalWrite(dir_right,LOW);
}
  
void forward()
{
  digitalWrite(dir_left,LOW);
  digitalWrite(dir_right,LOW);
  
  left_count = 0;
 /* while(1)
  {
    if(left_count > 500)
      break;
  }*/
  
  delay(2000);
  Serial.print("1");
 
}

void brake()
{
  digitalWrite(brake_left,HIGH);
  digitalWrite(brake_right,HIGH);
  
}

void left()  //90 degree left
{
  digitalWrite(dir_left,HIGH);
  digitalWrite(dir_right,LOW);
  left_count = 0;
  /*while(1)
  {
    if(left_count > 100)
    break;
  }*/
  delay(2000);
  Serial.print("2");
}

void right()  //90 degree right
{
  digitalWrite(dir_left,LOW);
  digitalWrite(dir_right,HIGH);
  left_count = 0;
  /*while(1)
  {
    if(left_count > 100)
    break;
  }*/
  delay(2000);
  Serial.print("3");
}
