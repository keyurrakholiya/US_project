/********************************************************************************
 Written by: Vinod Desai,Sachitanand Malewar NEX Robotics Pvt. Ltd.
 Edited by: e-Yantra team
 AVR Studio Version 6

 Date: 19th October 2012


 This experiment demonstrates use of position encoders.

 Concepts covered: External Interrupts, Position control
 
 Microcontroller pins used:
 PORTA3 to PORTA0: Robot direction control
 PL3, PL4: Robot velocity control. Currently set to 1 as PWM is not used
 PE4 (INT4): External interrupt for left motor position encoder 
 PE5 (INT5): External interrupt for the right position encoder

 Note: 
 
 1. Make sure that in the configuration options following settings are 
 	done for proper operation of the code

 	Microcontroller: atmega2560
    Frequency: 14745600
 	Optimization: -O0  (For more information read section: Selecting proper optimization 
 					options below figure 2.22 in the Software Manual)

 2.	It is observed that external interrupts does not work with the optimization level -Os

 3. Auxiliary power can supply current up to 1 Ampere while Battery can supply current up to 
 	2 Ampere. When both motors of the robot changes direction suddenly without stopping, 
	it produces large current surge. When robot is powered by Auxiliary power which can supply
	only 1 Ampere of current, sudden direction change in both the motors will cause current 
	surge which can reset the microcontroller because of sudden fall in voltage. 
	It is a good practice to stop the motors for at least 0.5seconds before changing 
	the direction. This will also increase the useable time of the fully charged battery.
	the life of the motor.

*********************************************************************************/

/********************************************************************************

   Copyright (c) 2010, NEX Robotics Pvt. Ltd.                       -*- c -*-
   All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:

   * Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.

   * Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the
     distribution.

   * Neither the name of the copyright holders nor the names of
     contributors may be used to endorse or promote products derived
     from this software without specific prior written permission.

   * Source code can be used for academic purpose. 
	 For commercial use permission form the author needs to be taken.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE. 

  Software released under Creative Commence cc by-nc-sa licence.
  For legal information refer to: 
  http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode

********************************************************************************/
#define F_CPU 14745600
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "robot.h"
#include "lcd.h"

//volatile variable means compiler will load its value from memory everytime when it refers. it's used in ISR ,ADC . because in main loop we don't use some variable so compiler will try to optimize it 
//and changes the value. so we have  to declare it volatile so compiler will not optimize it.

volatile unsigned long int ShaftCountLeft = 0; //to keep track of left position encoder
volatile unsigned long int ShaftCountRight = 0; //to keep track of right position encoder
volatile unsigned int Degrees; //to accept angle in degrees for turning

//Function to configure ports to enable robot's motion
void motion_pin_config (void)
{
	DDRA = DDRA | 0x0F;
	PORTA = PORTA & 0xF0;
	DDRL = DDRL | 0x18;   //Setting PL3 and PL4 pins as output for PWM generation
	PORTL = PORTL | 0x18; //PL3 and PL4 pins are for velocity control using PWM.
}

//Function to configure INT4 (PORTE 4) pin as input for the left position encoder
void left_encoder_pin_config (void)
{
	DDRE  = DDRE & 0xEF;  //Set the direction of the PORTE 4 pin as input
	PORTE = PORTE | 0x10; //Enable internal pull-up for PORTE 4 pin
}

//Function to configure INT5 (PORTE 5) pin as input for the right position encoder
void right_encoder_pin_config (void)
{
	DDRE  = DDRE & 0xDF;  //Set the direction of the PORTE 4 pin as input
	PORTE = PORTE | 0x20; //Enable internal pull-up for PORTE 4 pin
}

//Function to initialize ports
void port_init()
{
	motion_pin_config(); //robot motion pins config
	left_encoder_pin_config(); //left encoder pin config
	right_encoder_pin_config(); //right encoder pin config
	lcd_port_config();
}

void left_position_encoder_interrupt_init (void) //Interrupt 4 enable
{
	cli(); //Clears the global interrupt
	EICRB = EICRB | 0x02; // INT4 is set to trigger with falling edge
	EIMSK = EIMSK | 0x10; // Enable Interrupt INT4 for left position encoder
	sei();   // Enables the global interrupt
}

void right_position_encoder_interrupt_init (void) //Interrupt 5 enable
{
	cli(); //Clears the global interrupt
	EICRB = EICRB | 0x08; // INT5 is set to trigger with falling edge
	EIMSK = EIMSK | 0x20; // Enable Interrupt INT5 for right position encoder
	sei();   // Enables the global interrupt
}

//ISR for right position encoder
ISR(INT5_vect)
{
	ShaftCountRight++;  //increment right shaft position count
}


//ISR for left position encoder
ISR(INT4_vect)
{
	ShaftCountLeft++;  //increment left shaft position count
}


//Function used for setting motor's direction
void motion_set (unsigned char Direction)
{
	unsigned char PortARestore = 0;

	Direction &= 0x0F; 		// removing upper nibbel for the protection
	PortARestore = PORTA; 		// reading the PORTA original status
	PortARestore &= 0xF0; 		// making lower direction nibbel to 0
	PortARestore |= Direction; // adding lower nibbel for forward command and restoring the PORTA status
	PORTA = PortARestore; 		// executing the command
}

void forward (void) //both wheels forward
{
	motion_set(0x06);
}

void back (void) //both wheels backward
{
	motion_set(0x09);
}

void left (void) //Left wheel backward, Right wheel forward
{
	motion_set(0x05);
}

void right (void) //Left wheel forward, Right wheel backward
{
	motion_set(0x0A);
}

void soft_left (void) //Left wheel stationary, Right wheel forward
{
	motion_set(0x04);
}

void soft_right (void) //Left wheel forward, Right wheel is stationary
{
	motion_set(0x02);
}

void soft_left_2 (void) //Left wheel backward, right wheel stationary
{
	motion_set(0x01);
}

void soft_right_2 (void) //Left wheel stationary, Right wheel backward
{
	motion_set(0x08);
}

void stop (void)
{
	motion_set(0x00);
}


//Function used for turning robot by specified degrees
void angle_rotate(unsigned int Degrees)
{
	float ReqdShaftCount = 0;
	unsigned long int ReqdShaftCountInt = 0;

	ReqdShaftCount = (float) Degrees/ 4.090; // division by resolution to get shaft count
	ReqdShaftCountInt = (unsigned int) ReqdShaftCount;
	ShaftCountRight = 0;
	ShaftCountLeft = 0;

	while (1)
	{
		if((ShaftCountRight >= ReqdShaftCountInt) | (ShaftCountLeft >= ReqdShaftCountInt))
		break;
	}
	stop(); //Stop robot
}

//Function used for moving robot forward by specified distance

void linear_distance_mm(unsigned int DistanceInMM)
{
	float ReqdShaftCount = 0;
	unsigned long int ReqdShaftCountInt = 0;

	ReqdShaftCount = DistanceInMM / 5.338; // division by resolution to get shaft count
	ReqdShaftCountInt = (unsigned long int) ReqdShaftCount;
	
	ShaftCountRight = 0;
	while(1)
	{
		if(ShaftCountRight > ReqdShaftCountInt)
		{
			break;
		}
	}
	stop(); //Stop robot
}

void forward_mm(unsigned int DistanceInMM)
{
	forward();
	linear_distance_mm(DistanceInMM);
}

void back_mm(unsigned int DistanceInMM)
{
	back();
	linear_distance_mm(DistanceInMM);
}

void left_degrees(unsigned int Degrees)
{
	// 88 pulses for 360 degrees rotation 4.090 degrees per count
	left(); //Turn left
	angle_rotate(Degrees);
}



void right_degrees(unsigned int Degrees)
{
	// 88 pulses for 360 degrees rotation 4.090 degrees per count
	right(); //Turn right
	angle_rotate(Degrees);
}


void soft_left_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_left(); //Turn soft left
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}

void soft_right_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_right();  //Turn soft right
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}

void soft_left_2_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_left_2(); //Turn reverse soft left
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}

void soft_right_2_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_right_2();  //Turn reverse soft right
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}

//Function to initialize all the devices
void init_devices()
{
	cli(); //Clears the global interrupt
	port_init();  //Initializes all the ports
	left_position_encoder_interrupt_init();
	right_position_encoder_interrupt_init();
	sei();   // Enables the global interrupt
}


//Main Function




int main()
{
	init_devices();
	path_find();
	lcd_set_4bit();
	lcd_init();
	lcd_cursor(1,3);
	lcd_string("FIRE BIRD 5");
	lcd_cursor(2,1);
	lcd_string("NEX ROBOTICS IND");
	lcd_wr_command(0x01); //lcd clear
	
	while(go)

	{	
		
		if((path[path_num][cordinate]) == r_row + 1)
		{
			//no need to change head position
			if(pos == 0)
			{
				//printf("forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("forward1");
				forward_mm(400);
				
			
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				pos = 0;
				path_find();
			}
			else if(pos == 90)
			{
				//printf("right forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("right forward1");
				
				right_degrees(90);
				forward_mm(400);
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				pos = 0;
				path_find();
				
			}	
			else if(pos == 270)
			{
				//printf("left forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("left forward1");
				
				left_degrees(90);
				forward_mm(400);
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				
				pos = 0;
				path_find();
			}
			else if(pos == 180)
			{
				//printf("180 forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("l80 forward1");
				
				right_degrees(180);
				forward_mm(400);
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				pos = 0;
				path_find();
			}	
			
	
		}

		else if((path[path_num][cordinate]) == r_row - 1)
		{
			//change head 180 upside
			if(pos == 0)
			{
				//printf("180 forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("l80 forward2");
				
				right_degrees(180);
				forward_mm(400);
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
				pos = 180;
				path_find();
			}
			else if(pos == 90)
			{
				//printf("left forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("left forward2");
				
				left_degrees(90);
				forward_mm(400);
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
				pos = 180;
				path_find();
			}
			else if(pos == 270)
			{
				//printf("right forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("right forward2");
				
				right_degrees(90);
				forward_mm(400);
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
				pos = 180;
				path_find();
				
			}
			else if(pos == 180)
			{
				//printf("forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string(" forward2");
				
				forward_mm(400);
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
			
				pos = 180;
				path_find();
			}
		}

		else if(path[path_num][cordinate+1] ==  r_col + 1) 
		{	
			//left
			
			
			

			if(pos == 0)
			{
				//printf("left forward\n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("left forward3");
				
				left_degrees(90);
				forward_mm(400);
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();
				
			}
			else if(pos == 90)
			{
				//printf("forward \n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string(" forward3");
				
				forward_mm(400);
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();
			}
			
			else if(pos == 180)
			{
				//printf("right forward\n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("right forward3");
				
				right_degrees(90);
				forward_mm(400);
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();	
			}
			else if(pos == 270)
			{
				//printf("180 forward\n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("l80 forward3");
				
				right_degrees(180);
				forward_mm(400);
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();
			}	
			
		}

		else if(path[path_num][cordinate+1] ==  r_col - 1)
		{	
			
						
			if(pos == 0)
			{
				//printf("right forward\n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("right forward4");
				
				right_degrees(90);
				forward_mm(400);
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();
				
			}
			else if(pos == 270 )
			{
				//printf("forward\n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("forward4");
				
				forward_mm(400);
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();
			}
			
			else if(pos == 180)
			{
				//printf("left forward\n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("left forward4");
				
				left_degrees(90);
				forward_mm(400);
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();	
			}
			else if(pos == 90)
			{
				//printf("180 forward\n");
				lcd_wr_command(0x01);
				lcd_cursor(1,1);
				lcd_string("l80 forward4");
				
				right_degrees(180);
				forward_mm(400);
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();
			}
			
				
		}
	if((path[path_num][cordinate+2]== row_desti) && (path[path_num][cordinate+3] == col_desti)) 
		{
			lcd_wr_command(0x01);
			lcd_cursor(1,1);
			lcd_string("reached at goal");
			//col incre
			if(((r_col + 1) == path[path_num][cordinate+1] )&&( pos == 0))
				{
					//printf("\t left 2time forward");
					left_degrees(90);
					forward_mm(400);
				}
			else if(((r_col + 1) == path[path_num][cordinate+1] )&&( pos == 180))
				{
					//printf("\tright 2time forward");
					right_degrees(90);
					forward_mm(400);
				}
			else if(((r_col + 1) == path[path_num][cordinate+1] )&&( pos == 90))
				{
					//printf("\t2 time forward");
					forward_mm(400);
				}
			
			//col decre
			else if(((r_col - 1) == path[path_num][cordinate+1] )&&( pos == 0))
				{
					//printf("\tright 2 time forward");
					right_degrees(90);
					forward_mm(400);
				}
			else if(((r_col - 1) == path[path_num][cordinate+1] )&&( pos == 180))
				{
					//printf("\tleft 2 time forward");
					left_degrees(90);
					forward_mm(400);
				}
			else if(((r_col - 1) == path[path_num][cordinate+1] )&&( pos == 270))
				{
					//printf("\t2 time forward");
					forward_mm(400);
				}
			//row incre
			else if(((r_row + 1) == path[path_num][cordinate] )&&( pos == 270))
				{
					//printf("\tleft 2 time forward");
					left_degrees(90);
					forward_mm(400);
				}
			else if(((r_row + 1) == path[path_num][cordinate] )&&( pos == 90))
				{
					//printf("\tright 2 time forward");
					right_degrees(90);
					forward_mm(400);
				}
			else if(((r_row + 1) == path[path_num][cordinate] )&&( pos == 0))
				{
					//printf("\t2 time forward");
					forward_mm(400);
				}
			//row decre
			else if(((r_row - 1) == path[path_num][cordinate] )&&( pos == 90))
				{
					//printf("\tleft 2 time forward");
					left_degrees(90);
					forward_mm(400);
				}
			else if(((r_row - 1) == path[path_num][cordinate] )&&( pos ==270))
				{
					//printf("\tright 2 time forward");
					right_degrees(90);
					forward_mm(400);
				}
			else if(((r_row - 1) == path[path_num][cordinate] )&&( pos == 180))
				{
					//printf("\t2 time forward");
					forward_mm(400);
				}
			 go = 0; 
			//printf("done"); 
		}
	//printf("coooooooont %d",count);
	
	}


		
}


