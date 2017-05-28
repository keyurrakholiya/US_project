
#def get_serial_port():
#    return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()


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


##start

def start():
	ser.write("5")
