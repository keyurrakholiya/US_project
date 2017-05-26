// || RAM ||

unsigned int left_encoder=4; // INTERRUPT
unsigned int right_encoder=5; // INTERRUPT

unsigned int left_pwm=6;
unsigned int right_pwm=7;

unsigned int left_break=8;
unsigned int right_break=9;

unsigned int left_count=0;
unsigned int right_count=0;


void setup_pin_direction()
{
pinMode(left_encoder,INPUT_PULLUP);
pinMode(right_encoder,INPUT_PULLUP);
pinMode(left_pwm,OUTPUT);
pinMode(right_pwm,OUTPUT);
pinMode(left_break,OUTPUT);
pinMode(right_break,OUTPUT);
}

void setup_interrupts()
{
attachInterrupt(digitalPinToInterrupt(left_encoder),left_encoder_isr,FALLING);
attachInterrupt(digitalPinToInterrupt(right_encoder),right_encoder_isr,FALLING);
}

void left_encoder_isr()
{ left_count++;
}

void right_encoder_isr()
{ right_count++;
}

int main()
{
  printf("hello world");
}


