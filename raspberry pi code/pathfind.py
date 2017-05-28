<<<<<<< HEAD
import numpy as np
import setting
import RPi.GPIO as GPIO
import time
import time
import serial
import com

ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(5)

GPIO.setmode(GPIO.BCM)
trig_front = 23 #front sesnor pin
echo_front = 24

#left sensor
trig_left = 20
echo_left = 21

print "Distance Measurement In Progress"
GPIO.setup(trig_front,GPIO.OUT)
GPIO.setup(echo_front,GPIO.IN)
GPIO.setup(trig_left,GPIO.OUT)
GPIO.setup(echo_left,GPIO.IN)
GPIO.output(trig_front, False)
GPIO.output(trig_left, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

row = 12
col = 12
loop_no= row * col   ##(it should be 20*20 = 400 idealy)


path = np.arange(400).reshape(4,100)
map1 = np.arange(loop_no).reshape(row,col)
map1 =[1,1,1,1,1,1,1,1,1,1,1,1],[1,2,0,0,0,0,0,0,0,1,0,1],[1,0,0,1,0,1,1,0,0,1,0,1],[1,0,0,1,1,1,1,0,0,1,0,1],[1,0,1,0,0,1,1,0,0,1,0,1],[1,1,1,1,0,0,0,0,1,1,1,1],[1,1,1,1,0,0,0,0,0,1,1,1],[1,0,0,0,0,1,1,0,0,1,0,1],[1,0,0,1,0,1,1,0,0,1,0,1],[1,0,0,1,1,1,1,0,0,1,0,1],[1,0,0,0,'R',1,1,0,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1]
'''
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,0,0,0,0,0,0,0,1,0,1],
[1,0,0,1,0,1,1,0,0,1,0,1],
[1,0,0,1,1,1,1,0,0,1,0,1],
[1,0,1,0,0,1,1,0,0,1,0,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,0,1,1,1],
[1,0,0,0,0,1,1,0,0,1,0,1],
[1,0,0,1,0,1,1,0,0,1,0,1],
[1,0,0,1,1,1,1,0,0,1,0,1],
[1,0,0,0,'R',1,1,0,0,1,0,1],
[1,1,1,1,0,0,1,0,1,1,1,1]

'''

cordinate = 0

 
'''
map11 = [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,2,0,0,0,1,1,1,1,1,1,1],
       [1,0,0,1,0,1,1,1,1,1,1,1],
       [1,0,0,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,'R',1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1]




       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,2,0,0,0,1,1,0,0,1,0,1],
       [1,0,0,1,0,1,1,0,0,1,0,1],
       [1,0,0,1,1,1,1,0,0,1,0,1],
       [1,0,0,0,0,1,1,0,0,1,0,1],
       [1,1,1,1,0,0,1,0,1,1,1,1]
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,1,1,0,0,1,0,1],
       [1,0,0,1,0,1,1,0,0,1,0,1],
       [1,0,0,1,1,1,1,0,0,1,0,1],
       [1,0,0,0,'R',1,1,0,0,1,0,1],
       [1,1,1,1,0,0,1,0,1,1,1,1]
'''



changed_r_row4 = 0
changed_r_col4 = 0

changed_r_row1 = 0
changed_r_col1 = 0

changed_r_row2 = 0
changed_r_col2 = 0

changed_r_row3 = 0
changed_r_col3 = 0



changed_left_r_row1 = 0
changed_left_r_col1 = 0

changed_left_r_row2 = 0
changed_left_r_col2 = 0

changed_left_r_row3 = 0
changed_left_r_col3 = 0

changed_left_r_row4 = 0
changed_left_r_col4 = 0

setting.ind1=0
setting.ind2=0
setting.ind3=0
setting.ind4=0;
I=0
J=0

def flush():

    i=0;
    j=0;
    k=0;
    I=0;
    J=0;
    l=0;
    setting.temp1=0;
    setting.temp2=0;
    setting.temp3=0;
    setting.temp4=0;
    setting.sum1=0;
    setting.sum2=0;
    setting.sum3=0;
    setting.sum4=0;
    setting.temp  = 2;
    r1=0;
    r2=0;
    r3=0;
    r4=0;
    c1=0;
    c2=0;c3=0;
    c4=0;
    setting.flag = 1;
    length=0;
    setting.path_num = 0
    setting.r_row = 0
    setting.r_col = 0




def path_find():
    global row
    global col
    global loop_no
    flush();
    for k in range(0,4):
	for l in range(0,100):
            path[k][l] = 0;
	    setting.ind1 = 0;
	    setting.ind2 = 0;
	    setting.ind3 = 0;
	    setting.ind4 = 0;

    for i in range(0,row):
        for j in range(0,col):
            if(map1[i][j] == 2): ##fsetting.ind goal 'G'
		map1[i][j] = 2;
		setting.row_desti = i;
		setting.col_desti = j;
    print "destination location",setting.row_desti,setting.col_desti
	
    while(setting.temp < loop_no):
        ##printf("\n value of setting.temp = %d" ,setting.temp);
        for i in range(0,row):
            for j in range(0,col):
		if(map1[i][j] == setting.temp):				##printf("\n value of k = %d" ,k);
                    if((map1[i][j+1] != 1) & (map1[i][j+1] != 'R') & (map1[i][j+1] < 2)):
                        map1[i][j+1] = setting.temp + 1;
		    if((map1[i][j-1] != 1) & (map1[i][j-1] != 'R') & (map1[i][j-1] < 2)):
			map1[i][j-1] = setting.temp + 1;
                    if((map1[i+1][j] != 1) & (map1[i+1][j] != 'R') & (map1[i+1][j] < 2)):
                        map1[i+1][j] = setting.temp + 1;
                    if((map1[i-1][j] != 1) & (map1[i-1][j] != 'R') & (map1[i-1][j] < 2)):
			map1[i-1][j] = setting.temp + 1;
	setting.temp = setting.temp + 1;
        
    
#fsetting.ind out location of robot
    for I in range(0,row):
        for J in range(0,col):
            if(map1[I][J] == 'R'): 
                i = I
                setting.r_row = I
                j = J
                setting.r_col = J
    print "robot location", i,j


    setting.temp1 = map1[i][j-1]; 
    r1 = i;
    c1 = j-1;    ##column decrement 
    path[0][setting.ind1] = r1;
    path[0][setting.ind1+1] = c1;
    setting.sum1 = setting.temp1;
        
        
    setting.temp2 = map1[i][j+1]; ##columne increment
    r2 = i;
    c2 = j+1;
    path[1][setting.ind2] = r2;
    path[1][setting.ind2+1] = c2;
    setting.sum2 = setting.temp2;
        ##printf("setting.temp2= %d",setting.sum2);

    setting.temp3 = map1[i+1][j]; ##row increment
    r3 = i+1;
    c3 = j;
    path[2][setting.ind3] = r3;
    path[2][setting.ind3+1] = c3;
    setting.sum3 = setting.temp3;
        ##printf("setting.temp3= %d",setting.sum3);

    setting.temp4 = map1[i-1][j]; ##row decrement
    r4 = i-1;
    c4 = j;
    path[3][setting.ind4] = r4;
    path[3][setting.ind4+1] = c4;   
    setting.sum4 = setting.temp4;


    while(setting.flag == 1):
		
	if(setting.temp1 > 2):
	    
            if(map1[r1][c1-1] == map1[r1][c1] - 1):
                setting.sum1 = setting.sum1 + map1[r1][c1-1];
                setting.temp1 = map1[r1][c1-1];
                    
                setting.ind1= setting.ind1 + 2;
                path[0][setting.ind1]= r1;
                path[0][setting.ind1+1] = c1-1;
                                
                if(map1[r1][c1-1] == 2):
                    setting.flag = 0;
                c1 = c1 - 1;
					
            elif(map1[r1][c1+1] == map1[r1][c1] - 1):
            
                setting.sum1 = setting.sum1 + map1[r1][c1+1];
                setting.temp1 = map1[r1][c1+1];
                    
                setting.ind1= setting.ind1 + 2;
                path[0][setting.ind1]= r1;
                path[0][setting.ind1+1] = c1+1;
                    
                if(map1[r1][c1+1] == 2):
                    setting.flag = 0;
                c1 = c1 + 1;
                
            elif(map1[r1+1][c1] == map1[r1][c1] - 1):
                setting.sum1 = setting.sum1 + map1[r1+1][c1];
                setting.temp1 = map1[r1+1][c1];

                setting.ind1 = setting.ind1 + 2;
                path[0][setting.ind1]= r1+1;
                path[0][setting.ind1+1] = c1;

                if(map1[r1+1][c1] == 2):
                    setting.flag = 0;
                r1 = r1 +1;
                    
            elif(map1[r1-1][c1] == map1[r1][c1] -1 ):
                setting.sum1 = setting.sum1 + map1[r1-1][c1];
                setting.temp1 = map1[r1-1][c1];

                setting.ind1 = setting.ind1 + 2;
                path[0][setting.ind1]= r1-1;
                path[0][setting.ind1+1] = c1;                   

                if(map1[r1-1][c1] == 2):
                    setting.flag = 0;
                r1 = r1 -1;
                
			

        if(setting.temp2 > 2 ):
            if(map1[r2][c2+1] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2][c2+1];
                setting.temp2 = map1[r2][c2+1];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2;
                path[1][setting.ind2+1] = c2+1;

                if(map1[r2][c2+1] == 2):
                    setting.flag = 0;
                c2 = c2 + 1;

                
                
            elif(map1[r2][c2-1] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2][c2-1];
                setting.temp2 = map1[r2][c2-1];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2;
                path[1][setting.ind2+1] = c2-1;

                if(map1[r2][c2-1] == 2):
                    setting.flag = 0;
                c2 = c2 - 1;

            elif(map1[r2+1][c2] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2+1][c2];
                setting.temp2 = map1[r2+1][c2];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2 +1;
                path[1][setting.ind2+1] = c2;

                if(map1[r2+1][c2] == 2):
                    setting.flag = 0;     
                r2 = r2 + 1;
                    
            elif(map1[r2-1][c2] == map1[r2][c2] -1 ):
                setting.sum2 = setting.sum2 + map1[r2-1][c2];
                setting.temp2 = map1[r2-1][c2];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2-1;
                path[1][setting.ind2+1] = c2;

                if(map1[r2-1][c2] == 2):
                    setting.flag = 0;
                r2 = r2 - 1;
                
            
        
	
	if(setting.temp3 > 2 ):	##row increment
        
            if(map1[r3][c3+1] == map1[r3][c3] - 1):
                setting.sum3 = setting.sum3 + map1[r3][c3+1];
                setting.temp3 = map1[r3][c3+1];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3;
                path[2][setting.ind3+1] = c3+1;
                if(map1[r3][c3+1] == 2):
                    setting.flag = 0;
                c3 = c3 + 1;
                
            elif(map1[r3+1][c3] == map1[r3][c3] - 1):
                setting.sum3 = setting.sum3 + map1[r3+1][c3];
                setting.temp3 = map1[r3+1][c3];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3+1;
                path[2][setting.ind3+1] = c3;
                        
                if(map1[r3+1][c3] == 2):
                    setting.flag = 0;
                r3 = r3 + 1;
                
            elif(map1[r3-1][c3] == map1[r3][c3] - 1):
                
                    
                setting.sum3 = setting.sum3 + map1[r3-1][c3];
                setting.temp3 = map1[r3-1][c3];
                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3-1;
                path[2][setting.ind3+1] = c3;
                if(map1[r3-1][c3] == 2):
                    setting.flag = 0;
                r3 = r3 - 1;
                
            elif(map1[r3][c3-1] == map1[r3][c3] -1 ):
                setting.sum3 = setting.sum3 + map1[r3][c3-1];
                setting.temp3 = map1[r3][c3-1];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3;
                path[2][setting.ind3+1] = c3-1;
            
                if(map1[r3][c3-1] == 2):
                    setting.flag = 0;
                c3 = c3 -1;
                
                		
        if(setting.temp4 > 2 ):  ##row decrem
            if(map1[r4][c4+1] == map1[r4][c4] - 1): 
                setting.sum4 = setting.sum4 + map1[r4][c4+1];
                setting.temp4 = map1[r4][c4+1];

                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4;
                path[3][setting.ind4+1] = c4+1;

                if(map1[r4][c4+1] == 2):
                    setting.flag = 0;
                c4 = c4 + 1;

                
                
            elif(map1[r4-1][c4] == map1[r4][c4] - 1):
                setting.sum4 = setting.sum4 + map1[r4-1][c4];
                setting.temp4 = map1[r4-1][c4];
                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4-1;
                path[3][setting.ind4+1] = c4;

                if(map1[r4-1][c4] == 2):
                    setting.flag = 0;
                r4 = r4 - 1;
                
            elif(map1[r4+1][c4] == map1[r4][c4] - 1):
                setting.sum4 = setting.sum4 + map1[r4+1][c4];
                setting.temp4 = map1[r4+1][c4];

                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4+1;
                path[3][setting.ind4+1] = c4;

                if(map1[r4+1][c4] == 2):
                    setting.flag = 0;
                r4 = r4 + 1;
                
            elif(map1[r4][c4-1] == map1[r4][c4] -1 ):
                setting.sum4= setting.sum4 + map1[r4][c4-1];
                setting.temp4 = map1[r4][c4-1];
                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4;
                path[3][setting.ind4+1] = c4-1;
                    
                if(map1[r4][c4-1] == 2):
                    setting.flag = 0;
                c4 = c4 - 1;

				
    for k in range(0,4):
        for l in range(0,99):
	    if((path[k][l] == setting.row_desti) & (path[k][l+1] == setting.col_desti)):
                print("final path number is %d ",k);
		setting.path_num = k;
	l = l+ 2;
############################################################################################


def distance(trigger,echo):
        
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    while GPIO.input(echo)==0:
        pulse_start = time.time()
    while GPIO.input(echo)==1:
        pulse_end = time.time()   
    pulse_duration = pulse_end - pulse_start
    dist = pulse_duration * 17150
    dist = round(dist, 2)
    
    return dist
    
def check_obs():
    print "do you want obstacles ..............."
    #time.sleep(2)
    global changed_r_row4
    global changed_r_col4
    
    global changed_r_row1
    global changed_r_col1

    global changed_r_row2
    global changed_r_col2

    global changed_r_row3
    global changed_r_col3


    
    distance_front = distance(trig_front,echo_front)
    print "Distanc_front:",distance_front,"cm"

    if(distance_front < 10):
        if (setting.pos == 0):
            map1[setting.r_row + 1][setting.r_col] = 1
            setting.detect_front1 = 1
            changed_r_row1 = setting.r_row + 1
            changed_r_col1 = setting.r_col
 
             
        elif (setting.pos == 90):
            map1[setting.r_row ][setting.r_col + 1] = 1
            setting.detect_front2 = 1
            changed_r_row2 = setting.r_row
            changed_r_col2 = setting.r_col + 1
 
             
        elif (setting.pos == 180):
            map1[setting.r_row - 1][setting.r_col] = 1
            setting.detect_front3 = 1
            changed_r_row3 = setting.r_row - 1
            changed_r_col3 = setting.r_col

                
             
        elif (setting.pos == 270):
            map1[setting.r_row ][setting.r_col - 1] = 1
            setting.detect_front4 = 1
            changed_r_row4=setting.r_row
            changed_r_col4=setting.r_col - 1

 
            
    else:
        if(setting.detect_front1 == 1):
            map1[changed_r_row1][changed_r_col1] = 0
            setting.detect_front1 = 0
        if(setting.detect_front2 == 1):
            map1[changed_r_row2][changed_r_col2] = 0
            setting.detect_front2 = 0
        if(setting.detect_front3 == 1):
            map1[changed_r_row3][changed_r_col3] = 0
            setting.detect_front3 = 0
        if(setting.detect_front4 == 1):
            map1[changed_r_row4][changed_r_col4] = 0
            setting.detect_front4 = 0
    

    global changed_left_r_row1 
    global changed_left_r_col1 

    global changed_left_r_row2
    global changed_left_r_col2
    
    global changed_left_r_row3 
    global changed_left_r_col3 

    global changed_left_r_row4 
    global changed_left_r_col4 
    
 
    
    

    distance_left = distance(trig_left,echo_left)
    print "Distance_left:",distance_left,"cm"
    
    if(distance_left < 10):
        if(setting.pos == 0):
            map1[setting.r_row ][setting.r_col + 1] = 1;
            setting.detect_left1 = 1
            changed_left_r_row1 = setting.r_row
            changed_left_r_col1 = setting.r_col + 1
                
        elif(setting.pos == 90):
            map1[setting.r_row - 1][setting.r_col] = 1;
            setting.detect_left2 = 1
            changed_left_r_row2 = setting.r_row - 1
            changed_left_r_col2 = setting.r_col
            
        elif(setting.pos == 180):
            map1[setting.r_row ][setting.r_col - 1] = 1;
            setting.detect_left3 = 1
            changed_left_r_row3 = setting.r_row 
            changed_left_r_col3 = setting.r_col-1
            
        elif(setting.pos == 270):
              map1[setting.r_row +1][setting.r_col ] = 1;
              setting.detect_left4 = 1
              changed_left_r_row4 = setting.r_row + 1
              changed_left_r_col4 = setting.r_col
    else:
        if(setting.detect_left1 == 1):
            map1[changed_left_r_row1 ][changed_left_r_col1] = 0
            setting.detect_left1 = 0

        if(setting.detect_left2 == 1):
            map1[changed_left_r_row2][changed_left_r_col2] = 1;
            setting.detect_left2 = 0

        if(setting.detect_left3 == 1):
            map1[changed_left_r_row3][changed_left_r_col3] = 1;
            setting.detect_left3 = 0

        if(setting.detect_left4 == 1):
            map1[changed_left_r_row4 ][changed_left_r_col4] = 1;
            setting.detect_left4 = 0
            
            
               
    for i in range(0,row):
        print map1[i]   
######################################################################       
            
            
            
    
	    
		

def main():
    check_obs()
    path_find();
    while (setting.go):
        for i in range(0,row):
            print map1[i]
        if(path[setting.path_num][cordinate] == setting.r_row + 1):
            ##no need to change head setting.position
            if(setting.pos == 0):
                print("forward \n");
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find();
            
            elif(setting.pos == 90):
                print("right forward \n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find()
                   
            elif(setting.pos == 270):
                print("left forward \n");
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                com.brake()
                com.left()
                com.forward()
                
                setting.pos = 0;
                path_find();
            
            elif(setting.pos == 180):
                print("180 forward \n");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find();

        elif((path[setting.path_num][cordinate]) == setting.r_row - 1):
        
            ##change head 180 upside
            if(setting.pos == 0):
            
                print("180 forward \n");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();

            elif(setting.pos == 90):
                print("left forward \n");
                com.brake()
                com.left()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();

            elif(setting.pos == 270):
                print("right forward \n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();
                
            
            elif(setting.pos == 180):
                print("forward \n");
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
            
                setting.pos = 180;
                path_find();
            
        

        elif(path[setting.path_num][cordinate+1] ==  setting.r_col + 1):  ##left   
            if(setting.pos == 0):
                print("left forward\n");
                com.brake()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
                
            elif(setting.pos == 90):
                print("forward \n");
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
            
            elif(setting.pos == 180):
                print("right forward\n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
                
            elif(setting.pos == 270):
                print("180 forward\n");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();

        elif(path[setting.path_num][cordinate+1] ==  setting.r_col - 1):          
            if(setting.pos == 0):
                print("right forward\n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();
                
            elif(setting.pos == 270 ):
                print("forward\n");
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();
            
            elif(setting.pos == 180):
                print("left forward\n");
                com.brake()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();    
            
            elif(setting.pos == 90):
                print("180 forward\n");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
		path_find();

			
				
	if((path[setting.path_num][cordinate+2]== setting.row_desti) & (path[setting.path_num][cordinate+3] == setting.col_desti)): 
		if(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 0)):
			print("\t left 2time forward");
			com.brake()
			com.left()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0;
			
		elif(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 180)):
			print("\tright 2time forward");
			com.brake()
			com.right()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0;
			
		elif(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 90)):
			print("1time forward");
			com.forward()
			com.brake()
			
			map1[setting.r_row][setting.r_col+1] = 'R'
			map1[setting.r_row][setting.r_col]  = 0
			
			
			
				
			
			##col decre
		elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 0)):
			print("\tright 2 time forward");
			com.brake()
			com.right()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0; 
			
		elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 180)):
			print("\tleft 2 time forward");
			com.brake()
			com.left()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0; 
					
		elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 270)):
			print("1time forward");
			map1[setting.r_row][setting.r_col - 1] = 'R'
			map1[setting.r_row][setting.r_col]  = 0
			com.forward()
			com.brake()
				
			##row incre
		elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 270)):
			print("\tleft 2 time forward");
			com.brake()
			com.left()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0; 
				
		elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 90)):
			print("\tright 2 time forward");
			com.brake()
			com.right()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0; 
				
		elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 0)):
			print("\t1 time forward");
			map1[setting.r_row + 1][setting.r_col] = 'R'
			map1[setting.r_row][setting.r_col]  = 0
                        com.forward()
                        com.brake()
			
			##row decre
		elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos == 90)):
			print("\tleft 2 time forward");
			com.brake()
			com.left()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0; 
			
		elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos ==270)):
			print("\tright 2 time forward");
			com.brake()
			com.right()
			com.forward()
			com.forward()
			com.brake()
			
			setting.go = 0; 
				
		elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos == 180)):
			print("\t1 time forward");
			com.forward()
			com.brake()
			
			map1[setting.r_row - 1][setting.r_col] = 'R'
			map1[setting.r_row][setting.r_col]  = 0
		setting.go = 0
		print "done"

            
        check_obs()
        path_find()

setting.init()
main()
          
for I in range(0,row):
    for J in range(0,col):
        if(map1[I][J] == 'R'): 
            i = I
            setting.r_row = I
            j = J
            setting.r_col = J
            
print "robot location", i,j
if((setting.pos == 0) & (setting.r_row == setting.row_desti) & (setting.r_col + 1 == setting.col_desti)):
    print ("right forward done")
    com.brake()
    com.right()
    com.forward()
    com.brake()
    
    map1[setting.r_row ][setting.r_col + 1] = 'R'
    map1[setting.r_row][setting.r_col]  = 0

if((setting.pos == 180) & (setting.r_row == setting.row_desti) & (setting.r_col - 1 == setting.col_desti)):
    print ("left forward done")
    com.brake()
    com.left()
    com.forward()
    com.brake()
    
    map1[setting.r_row ][setting.r_col - 1] = 'R'
    map1[setting.r_row][setting.r_col]  = 0

if((setting.pos == 90) & (setting.r_row-1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
    print ("left forward done")
    com.brake()
    com.left()
    com.forward()
    com.brake()
    
    map1[setting.r_row - 1][setting.r_col] = 'R'
    map1[setting.r_row][setting.r_col]  = 0

if((setting.pos == 270) & (setting.r_row+1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
    print ("right forward done")
    com.brake()
    com.right()
    com.forward()
    com.brake()
    
    map1[setting.r_row + 1][setting.r_col] = 'R'
    map1[setting.r_row][setting.r_col]  = 0

    
    
for i in range(0,row):
    print map1[i]

'''
path_find()
cordinate = 0
for i in range(0,row):
    print map1[i]
print path
print setting.path_num
if(path[setting.path_num][cordinate] == setting.r_row+1):
    print "ok"

'''
=======
import numpy as np
import setting
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
TRIG = 23 #front sesnor pin
ECHO = 24

#left sensor
trig_left = 20
echo_left = 21

print "Distance Measurement In Progress"
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(trig_left,GPIO.OUT)
GPIO.setup(echo_left,GPIO.IN)
GPIO.output(TRIG, False)
GPIO.output(trig_left, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

row = 12
col = 12
loop_no= row * col   ##(it should be 20*20 = 400 idealy)


path = np.arange(400).reshape(4,100)
map1 = np.arange(loop_no).reshape(row,col)
map1 =[1,1,1,1,1,1,1,1,1,1,1,1],[1,2,0,0,0,1,1,0,0,1,0,1],[1,0,0,1,0,1,1,0,0,1,0,1],[1,0,0,1,1,1,1,0,0,1,0,1],[1,0,0,0,0,1,1,0,0,1,0,1],[1,1,1,1,0,0,0,0,1,1,1,1],[1,1,1,1,0,0,0,0,0,1,1,1],[1,0,0,0,0,1,1,0,0,1,0,1],[1,0,0,1,0,1,1,0,0,1,0,1],[1,0,0,1,1,1,1,0,0,1,0,1],[1,0,0,0,'R',1,1,0,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1]
'''
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,0,0,0,1,1,0,0,1,0,1],
[1,0,0,1,0,1,1,0,0,1,0,1],
[1,0,0,1,1,1,1,0,0,1,0,1],
[1,0,0,0,0,1,1,0,0,1,0,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,0,1,1,1],
[1,0,0,0,0,1,1,0,0,1,0,1],
[1,0,0,1,0,1,1,0,0,1,0,1],
[1,0,0,1,1,1,1,0,0,1,0,1],
[1,0,0,0,'R',1,1,0,0,1,0,1],
[1,1,1,1,0,0,1,0,1,1,1,1]

'''

cordinate = 0

 
'''
map11 = [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,2,0,0,0,1,1,1,1,1,1,1],
       [1,0,0,1,0,1,1,1,1,1,1,1],
       [1,0,0,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,'R',1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1]




       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,2,0,0,0,1,1,0,0,1,0,1],
       [1,0,0,1,0,1,1,0,0,1,0,1],
       [1,0,0,1,1,1,1,0,0,1,0,1],
       [1,0,0,0,0,1,1,0,0,1,0,1],
       [1,1,1,1,0,0,1,0,1,1,1,1]
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,1,1,0,0,1,0,1],
       [1,0,0,1,0,1,1,0,0,1,0,1],
       [1,0,0,1,1,1,1,0,0,1,0,1],
       [1,0,0,0,'R',1,1,0,0,1,0,1],
       [1,1,1,1,0,0,1,0,1,1,1,1]
'''



changed_r_row4 = 0
changed_r_col4 = 0

changed_r_row1 = 0
changed_r_col1 = 0

changed_r_row2 = 0
changed_r_col2 = 0

changed_r_row3 = 0
changed_r_col3 = 0



changed_left_r_row1 = 0
changed_left_r_col1 = 0

changed_left_r_row2 = 0
changed_left_r_col2 = 0

changed_left_r_row3 = 0
changed_left_r_col3 = 0

changed_left_r_row4 = 0
changed_left_r_col4 = 0

setting.ind1=0
setting.ind2=0
setting.ind3=0
setting.ind4=0;
I=0
J=0

def flush():

    i=0;
    j=0;
    k=0;
    I=0;
    J=0;
    l=0;
    setting.temp1=0;
    setting.temp2=0;
    setting.temp3=0;
    setting.temp4=0;
    setting.sum1=0;
    setting.sum2=0;
    setting.sum3=0;
    setting.sum4=0;
    setting.temp  = 2;
    r1=0;
    r2=0;
    r3=0;
    r4=0;
    c1=0;
    c2=0;c3=0;
    c4=0;
    setting.flag = 1;
    length=0;
    setting.path_num = 0
    setting.r_row = 0
    setting.r_col = 0




def path_find():
    global row
    global col
    global loop_no
    flush();
    for k in range(0,4):
	for l in range(0,100):
            path[k][l] = 0;
	    setting.ind1 = 0;
	    setting.ind2 = 0;
	    setting.ind3 = 0;
	    setting.ind4 = 0;

    for i in range(0,row):
        for j in range(0,col):
            if(map1[i][j] == 2): ##fsetting.ind goal 'G'
		map1[i][j] = 2;
		setting.row_desti = i;
		setting.col_desti = j;
    print "destination location",setting.row_desti,setting.col_desti
	
    while(setting.temp < loop_no):
        ##printf("\n value of setting.temp = %d" ,setting.temp);
        for i in range(0,row):
            for j in range(0,col):
		if(map1[i][j] == setting.temp):				##printf("\n value of k = %d" ,k);
                    if((map1[i][j+1] != 1) & (map1[i][j+1] != 'R') & (map1[i][j+1] < 2)):
                        map1[i][j+1] = setting.temp + 1;
		    if((map1[i][j-1] != 1) & (map1[i][j-1] != 'R') & (map1[i][j-1] < 2)):
			map1[i][j-1] = setting.temp + 1;
                    if((map1[i+1][j] != 1) & (map1[i+1][j] != 'R') & (map1[i+1][j] < 2)):
                        map1[i+1][j] = setting.temp + 1;
                    if((map1[i-1][j] != 1) & (map1[i-1][j] != 'R') & (map1[i-1][j] < 2)):
			map1[i-1][j] = setting.temp + 1;
	setting.temp = setting.temp + 1;
        
    
#fsetting.ind out location of robot
    for I in range(0,row):
        for J in range(0,col):
            if(map1[I][J] == 'R'): 
                i = I
                setting.r_row = I
                j = J
                setting.r_col = J
    print "robot location", i,j


    setting.temp1 = map1[i][j-1]; 
    r1 = i;
    c1 = j-1;    ##column decrement 
    path[0][setting.ind1] = r1;
    path[0][setting.ind1+1] = c1;
    setting.sum1 = setting.temp1;
        
        
    setting.temp2 = map1[i][j+1]; ##columne increment
    r2 = i;
    c2 = j+1;
    path[1][setting.ind2] = r2;
    path[1][setting.ind2+1] = c2;
    setting.sum2 = setting.temp2;
        ##printf("setting.temp2= %d",setting.sum2);

    setting.temp3 = map1[i+1][j]; ##row increment
    r3 = i+1;
    c3 = j;
    path[2][setting.ind3] = r3;
    path[2][setting.ind3+1] = c3;
    setting.sum3 = setting.temp3;
        ##printf("setting.temp3= %d",setting.sum3);

    setting.temp4 = map1[i-1][j]; ##row decrement
    r4 = i-1;
    c4 = j;
    path[3][setting.ind4] = r4;
    path[3][setting.ind4+1] = c4;   
    setting.sum4 = setting.temp4;


    while(setting.flag == 1):
		
	if(setting.temp1 > 2):
	    
            if(map1[r1][c1-1] == map1[r1][c1] - 1):
                setting.sum1 = setting.sum1 + map1[r1][c1-1];
                setting.temp1 = map1[r1][c1-1];
                    
                setting.ind1= setting.ind1 + 2;
                path[0][setting.ind1]= r1;
                path[0][setting.ind1+1] = c1-1;
                                
                if(map1[r1][c1-1] == 2):
                    setting.flag = 0;
                c1 = c1 - 1;
					
            elif(map1[r1][c1+1] == map1[r1][c1] - 1):
            
                setting.sum1 = setting.sum1 + map1[r1][c1+1];
                setting.temp1 = map1[r1][c1+1];
                    
                setting.ind1= setting.ind1 + 2;
                path[0][setting.ind1]= r1;
                path[0][setting.ind1+1] = c1+1;
                    
                if(map1[r1][c1+1] == 2):
                    setting.flag = 0;
                c1 = c1 + 1;
                
            elif(map1[r1+1][c1] == map1[r1][c1] - 1):
                setting.sum1 = setting.sum1 + map1[r1+1][c1];
                setting.temp1 = map1[r1+1][c1];

                setting.ind1 = setting.ind1 + 2;
                path[0][setting.ind1]= r1+1;
                path[0][setting.ind1+1] = c1;

                if(map1[r1+1][c1] == 2):
                    setting.flag = 0;
                r1 = r1 +1;
                    
            elif(map1[r1-1][c1] == map1[r1][c1] -1 ):
                setting.sum1 = setting.sum1 + map1[r1-1][c1];
                setting.temp1 = map1[r1-1][c1];

                setting.ind1 = setting.ind1 + 2;
                path[0][setting.ind1]= r1-1;
                path[0][setting.ind1+1] = c1;                   

                if(map1[r1-1][c1] == 2):
                    setting.flag = 0;
                r1 = r1 -1;
                
			

        if(setting.temp2 > 2 ):
            if(map1[r2][c2+1] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2][c2+1];
                setting.temp2 = map1[r2][c2+1];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2;
                path[1][setting.ind2+1] = c2+1;

                if(map1[r2][c2+1] == 2):
                    setting.flag = 0;
                c2 = c2 + 1;

                
                
            elif(map1[r2][c2-1] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2][c2-1];
                setting.temp2 = map1[r2][c2-1];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2;
                path[1][setting.ind2+1] = c2-1;

                if(map1[r2][c2-1] == 2):
                    setting.flag = 0;
                c2 = c2 - 1;

            elif(map1[r2+1][c2] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2+1][c2];
                setting.temp2 = map1[r2+1][c2];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2 +1;
                path[1][setting.ind2+1] = c2;

                if(map1[r2+1][c2] == 2):
                    setting.flag = 0;     
                r2 = r2 + 1;
                    
            elif(map1[r2-1][c2] == map1[r2][c2] -1 ):
                setting.sum2 = setting.sum2 + map1[r2-1][c2];
                setting.temp2 = map1[r2-1][c2];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2-1;
                path[1][setting.ind2+1] = c2;

                if(map1[r2-1][c2] == 2):
                    setting.flag = 0;
                r2 = r2 - 1;
                
            
        
	
	if(setting.temp3 > 2 ):	##row increment
        
            if(map1[r3][c3+1] == map1[r3][c3] - 1):
                setting.sum3 = setting.sum3 + map1[r3][c3+1];
                setting.temp3 = map1[r3][c3+1];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3;
                path[2][setting.ind3+1] = c3+1;
                if(map1[r3][c3+1] == 2):
                    setting.flag = 0;
                c3 = c3 + 1;
                
            elif(map1[r3+1][c3] == map1[r3][c3] - 1):
                setting.sum3 = setting.sum3 + map1[r3+1][c3];
                setting.temp3 = map1[r3+1][c3];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3+1;
                path[2][setting.ind3+1] = c3;
                        
                if(map1[r3+1][c3] == 2):
                    setting.flag = 0;
                r3 = r3 + 1;
                
            elif(map1[r3-1][c3] == map1[r3][c3] - 1):
                
                    
                setting.sum3 = setting.sum3 + map1[r3-1][c3];
                setting.temp3 = map1[r3-1][c3];
                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3-1;
                path[2][setting.ind3+1] = c3;
                if(map1[r3-1][c3] == 2):
                    setting.flag = 0;
                r3 = r3 - 1;
                
            elif(map1[r3][c3-1] == map1[r3][c3] -1 ):
                setting.sum3 = setting.sum3 + map1[r3][c3-1];
                setting.temp3 = map1[r3][c3-1];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3;
                path[2][setting.ind3+1] = c3-1;
            
                if(map1[r3][c3-1] == 2):
                    setting.flag = 0;
                c3 = c3 -1;
                
                		
        if(setting.temp4 > 2 ):  ##row decrem
            if(map1[r4][c4+1] == map1[r4][c4] - 1): 
                setting.sum4 = setting.sum4 + map1[r4][c4+1];
                setting.temp4 = map1[r4][c4+1];

                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4;
                path[3][setting.ind4+1] = c4+1;

                if(map1[r4][c4+1] == 2):
                    setting.flag = 0;
                c4 = c4 + 1;

                
                
            elif(map1[r4-1][c4] == map1[r4][c4] - 1):
                setting.sum4 = setting.sum4 + map1[r4-1][c4];
                setting.temp4 = map1[r4-1][c4];
                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4-1;
                path[3][setting.ind4+1] = c4;

                if(map1[r4-1][c4] == 2):
                    setting.flag = 0;
                r4 = r4 - 1;
                
            elif(map1[r4+1][c4] == map1[r4][c4] - 1):
                setting.sum4 = setting.sum4 + map1[r4+1][c4];
                setting.temp4 = map1[r4+1][c4];

                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4+1;
                path[3][setting.ind4+1] = c4;

                if(map1[r4+1][c4] == 2):
                    setting.flag = 0;
                r4 = r4 + 1;
                
            elif(map1[r4][c4-1] == map1[r4][c4] -1 ):
                setting.sum4= setting.sum4 + map1[r4][c4-1];
                setting.temp4 = map1[r4][c4-1];
                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4;
                path[3][setting.ind4+1] = c4-1;
                    
                if(map1[r4][c4-1] == 2):
                    setting.flag = 0;
                c4 = c4 - 1;

				
    for k in range(0,4):
        for l in range(0,99):
	    if((path[k][l] == setting.row_desti) & (path[k][l+1] == setting.col_desti)):
                print("final path number is %d ",k);
		setting.path_num = k;
	l = l+ 2;
############################################################################################
def check_obs():
    print "do you want obstacles ..............."
    time.sleep(2)
    global changed_r_row4
    global changed_r_col4
    
    global changed_r_row1
    global changed_r_col1

    global changed_r_row2
    global changed_r_col2

    global changed_r_row3
    global changed_r_col3


    
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()   
    pulse_duration = pulse_end - pulse_start
    distance_front = pulse_duration * 17150
    distance_front = round(distance_front, 2)
    print "Distance:",distance_front,"cm"
    #time.sleep(0.05)

    if(distance_front < 10):
        if (setting.pos == 0):
            map1[setting.r_row + 1][setting.r_col] = 1
            setting.detect_front1 = 1
            changed_r_row1 = setting.r_row + 1
            changed_r_col1 = setting.r_col
 
             
        elif (setting.pos == 90):
            map1[setting.r_row ][setting.r_col + 1] = 1
            setting.detect_front2 = 1
            changed_r_row2 = setting.r_row
            changed_r_col2 = setting.r_col + 1
 
             
        elif (setting.pos == 180):
            map1[setting.r_row - 1][setting.r_col] = 1
            setting.detect_front3 = 1
            changed_r_row3 = setting.r_row - 1
            changed_r_col3 = setting.r_col

                
             
        elif (setting.pos == 270):
            map1[setting.r_row ][setting.r_col - 1] = 1
            setting.detect_front4 = 1
            changed_r_row4=setting.r_row
            changed_r_col4=setting.r_col - 1

 
            
    else:
        if(setting.detect_front1 == 1):
            map1[changed_r_row1][changed_r_col1] = 0
            setting.detect_front1 = 0
        if(setting.detect_front2 == 1):
            map1[changed_r_row2][changed_r_col2] = 0
            setting.detect_front2 = 0
        if(setting.detect_front3 == 1):
            map1[changed_r_row3][changed_r_col3] = 0
            setting.detect_front3 = 0
        if(setting.detect_front4 == 1):
            map1[changed_r_row4][changed_r_col4] = 0
            setting.detect_front4 = 0
    print "inside detect"

    global changed_left_r_row1 
    global changed_left_r_col1 

    global changed_left_r_row2
    global changed_left_r_col2
    
    global changed_left_r_row3 
    global changed_left_r_col3 

    global changed_left_r_row4 
    global changed_left_r_col4 
    
    GPIO.output(trig_left, True)
    time.sleep(0.00001)
    GPIO.output(trig_left, False)
    while GPIO.input(echo_left)==0:
        pulse_start = time.time()
    while GPIO.input(echo_left)==1:
        pulse_end = time.time()   
    pulse_duration = pulse_end - pulse_start
    distance_left = pulse_duration * 17150
    distance_left = round(distance_left, 2)
    print "Distance_left:",distance_left,"cm"
    #time.sleep(0.05)
    
    if(distance_left < 10):
        if(setting.pos == 0):
            map1[setting.r_row ][setting.r_col + 1] = 1;
            setting.detect_left1 = 1
            changed_left_r_row1 = setting.r_row
            changed_left_r_col1 = setting.r_col + 1
                
        elif(setting.pos == 90):
            map1[setting.r_row - 1][setting.r_col] = 1;
            setting.detect_left2 = 1
            changed_left_r_row2 = setting.r_row - 1
            changed_left_r_col2 = setting.r_col
            
        elif(setting.pos == 180):
            map1[setting.r_row ][setting.r_col - 1] = 1;
            setting.detect_left3 = 1
            changed_left_r_row3 = setting.r_row 
            changed_left_r_col3 = setting.r_col-1
            
        elif(setting.pos == 270):
              map1[setting.r_row +1][setting.r_col ] = 1;
              setting.detect_left4 = 1
              changed_left_r_row4 = setting.r_row + 1
              changed_left_r_col4 = setting.r_col
    else:
        if(setting.detect_left1 == 1):
            map1[changed_left_r_row1 ][changed_left_r_col1] = 0
            setting.detect_left1 = 0

        if(setting.detect_left2 == 1):
            map1[changed_left_r_row2][changed_left_r_col2] = 1;
            setting.detect_left2 = 0

        if(setting.detect_left3 == 1):
            map1[changed_left_r_row3][changed_left_r_col3] = 1;
            setting.detect_left3 = 0

        if(setting.detect_left4 == 1):
            map1[changed_left_r_row4 ][changed_left_r_col4] = 1;
            setting.detect_left4 = 0
            
            
               
    for i in range(0,row):
        print map1[i]   
######################################################################       
            
            
            
    
	    
		

def main():
    check_obs()
    path_find();
    while (setting.go):
        for i in range(0,row):
            print map1[i]
        if(path[setting.path_num][cordinate] == setting.r_row + 1):
            ##no need to change head setting.position
            if(setting.pos == 0):
                print("forward \n");
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find();
            
            elif(setting.pos == 90):
                print("right forward \n");
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find();
                   
            elif(setting.pos == 270):
                print("left forward \n");
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                
                setting.pos = 0;
                path_find();
            
            elif(setting.pos == 180):
                print("180 forward \n");
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find();

        elif((path[setting.path_num][cordinate]) == setting.r_row - 1):
        
            ##change head 180 upside
            if(setting.pos == 0):
            
                print("180 forward \n");
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();

            elif(setting.pos == 90):
                print("left forward \n");
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();

            elif(setting.pos == 270):
                print("right forward \n");
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();
                
            
            elif(setting.pos == 180):
                print("forward \n");
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
            
                setting.pos = 180;
                path_find();
            
        

        elif(path[setting.path_num][cordinate+1] ==  setting.r_col + 1):  ##left   
            if(setting.pos == 0):
                print("left forward\n");
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
                
            elif(setting.pos == 90):
                print("forward \n");
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
            
            elif(setting.pos == 180):
                print("right forward\n");
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
                
            elif(setting.pos == 270):
                print("180 forward\n");
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();

        elif(path[setting.path_num][cordinate+1] ==  setting.r_col - 1):          
            if(setting.pos == 0):
                print("right forward\n");
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();
                
            elif(setting.pos == 270 ):
                print("forward\n");
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();
            
            elif(setting.pos == 180):
                print("left forward\n");
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();    
            
            elif(setting.pos == 90):
                print("180 forward\n");
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
		path_find();

			
				
	if((path[setting.path_num][cordinate+2]== setting.row_desti) & (path[setting.path_num][cordinate+3] == setting.col_desti)): 
		if(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 0)):
			print("\t left 2time forward");
				
		elif(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 180)):
			print("\tright 2time forward");
				
		elif(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 90)):
			print("\t2 time forward");
				
			
			##col decre
		elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 0)):
			print("\tright 2 time forward");
			
		elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 180)):
			print("\tleft 2 time forward");
					
		elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 270)):
			print("\t2 time forward");
				
			##row incre
		elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 270)):
			print("\tleft 2 time forward");
				
		elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 90)):
			print("\tright 2 time forward");
				
		elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 0)):
			print("\t2 time forward");
				
			##row decre
		elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos == 90)):
			print("\tleft 2 time forward");
			
		elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos ==270)):
			print("\tright 2 time forward");
				
		elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos == 180)):
			print("\t2 time forward");
				
		setting.go = 0; 
                print("done");
        check_obs()
        path_find()

setting.init()
main()


		
		
		

'''
path_find()
cordinate = 0
for i in range(0,row):
    print map1[i]
print path
print setting.path_num
if(path[setting.path_num][cordinate] == setting.r_row+1):
    print "ok"

'''
>>>>>>> 9b00e39f0656831aced7eccb42269285f696dbb7
