def check_obs()
    while(1):
      GPIO.output(TRIG, True)
      time.sleep(0.00001)
      GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()   
    pulse_duration = pulse_end - pulse_start
    distance_front = pulse_duration * 17150
    distance_front = round(distance, 2)
    print "Distance:",distance_front,"cm"
    time.sleep(0.05)

    if(distance_front < 10):
        if(pos == 0):
            map1[setting.r_row + 1][setting.r_col] = 1
             
        elif(pos == 90):
            map1[setting.r_row ][setting.r_col + 1] = 1
             
        elif(pos == 180):
            map1[setting.r_row - 1][setting.r_col] = 1
             
        elif(pos == 270):
            map1[setting.r_row ][setting.r_col - 1] = 1
             
    else
        if(pos == 0):
            map1[setting.r_row + 1][setting.r_col] = 0
             
        elif(pos == 90):
            map1[setting.r_row ][setting.r_col + 1] = 0
             
        elif(pos == 180):
            map1[setting.r_row - 1][setting.r_col] = 0
             
        elif(pos == 270):
            map1[setting.r_row ][setting.r_col - 1] = 0
        
        
            
            
            
