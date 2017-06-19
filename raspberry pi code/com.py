
#def get_serial_port():
#    return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()
import time
import serial
ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(5)
print "connected"
##forward
def forward():
	ser.write("1")
	while (1):
		y = ser.read()
		if (y == '1'):
                        print "forward done"
                        break	

##left
def left():
	ser.write("2")
	while(1):
		y = ser.read()
		if (y == '2'):
                        print "left done"
                        break

#right
def right():

	ser.write("3")
	while(1):
		y =ser.read()
		if( y == '3'):
                        print "right done"
                        break

##brake
def brake():
	ser.write("4")


##start we are not using it for now

def start():
	ser.write("5")
	
	
## we will add code for back later
