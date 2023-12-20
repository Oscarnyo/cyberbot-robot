from cyberbot import *

def forward():
    bot(18).servo_speed(75)
    bot(19).servo_speed(-75)

def backwards():
    bot(18).servo_speed(-75)
    bot(19).servo_speed(75)
    sleep(250)

def right():
    bot(18).servo_speed(75)
    bot(19).servo_speed(75)
    sleep(250)

def left():
    bot(18).servo_speed(-75)
    bot(19).servo_speed(-75)
    sleep(250)


while True:

    #LIGHT sensor
    bot(9).write_digital(1)
    qt_left = bot(9).rc_time(1)
    bot(8).write_digital(1)
    qt_right = bot(8).rc_time(1)
    
    
    
    # infrared sensor
    irL = bot(14, 13).ir_detect(37500)
    irR = bot(1, 2).ir_detect(37500)
    
    
    
    if irL == 1 and irR == 1:
        bot(20).write_digital(0)
        #Check the light intensity and set motor speeds
        if qt_left > 0 and qt_right == 0:  # Light is on the left
            left_speed = -50  # Turn left
            right_speed = -50
        elif qt_right > 0 and qt_left == 0:  # Light is on the right
            left_speed = 50  # Turn right
            right_speed = 50
        elif qt_left > 0 and qt_right > 0:  # Light is centered
            left_speed = 50  # Move straight
            right_speed = -50
        elif qt_left == 0 and qt_right == 0:  # No significant light detected
            left_speed = 0  # Stop
            right_speed = 0
        else:
            # If none of the conditions above are met, stop the robot
            # This is a fallback in case the readings are not within expected ranges
            left_speed = 0
            right_speed = 0

        # Apply the speeds to the servos
        bot(18).servo_speed(left_speed)
        bot(19).servo_speed(right_speed)
        
    elif irL == 0 and irR == 0:     
        backwards()                                 
        right()
        bot(20).write_digital(1)
    elif irL == 1 and irR == 0:   
        backwards()                                  
        left()
    elif irL == 0 and irR == 1:  
        backwards()                                   
        right()

    # Debugging: print the sensor values 
    print('QT_Left:',qt_left, ' QT_Right: ',qt_right)