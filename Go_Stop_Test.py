import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#LEFTENCODERYELLOW = 23
#LEFTENCODERWHITE = 26
#RIGHTENCODERYELLOW = 27
#RIGHTENCODERWHITE = 28

#SENSOR PINS

TRIG = 7
ECHOF = 8
ECHOFL = 10
ECHOFR = 11
ECHOL = 12
ECHOR = 13
ECHOBL = 15
ECHOBR = 19
ECHOB =  21

#SETUP SENSOR ARRAY

sensors = [ECHOBL, ECHOBR, ECHOB, ECHOF, ECHOFL, ECHOFR, ECHOL, ECHOR]
sensors_len = len(sensors)
distances = []

#MOTOR PINS

LEFTENABLE = 33
RIGHTENABLE = 32

LEFTINPUT1 = 31
LEFTINPUT2 = 35
RIGHTINPUT3 = 36
RIGHTINPUT4 = 37

#SENSOR SETUP

GPIO.setup(ECHOF, GPIO.IN)
GPIO.setup(ECHOFL, GPIO.IN)
GPIO.setup(ECHOFR, GPIO.IN)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.setup(ECHOR, GPIO.IN)
GPIO.setup(ECHOBL, GPIO.IN)
GPIO.setup(ECHOBR, GPIO.IN)
GPIO.setup(ECHOB, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)

#MOTOR SETUP
   
#GPIO.setup(LEFTENCODERYELLOW, GPIO.IN)
#GPIO.setup(LEFTENCODERWHITE, GPIO.IN)
#GPIO.setup(RIGHTENCODERYELLOW, GPIO.IN)
#GPIO.setup(RIGHTENCODERWHITE, GPIO.IN)
GPIO.setup(LEFTENABLE, GPIO.OUT)
GPIO.setup(RIGHTENABLE, GPIO.OUT)
GPIO.setup(LEFTINPUT1, GPIO.OUT)
GPIO.setup(LEFTINPUT2, GPIO.OUT)
GPIO.setup(RIGHTINPUT3, GPIO.OUT)
GPIO.setup(RIGHTINPUT4, GPIO.OUT)

#OUTPUT INITIALISE

print("Setting up")
GPIO.output(TRIG, 0)
GPIO.output(LEFTENABLE, 0)
GPIO.output(RIGHTENABLE, 0)
GPIO.output(LEFTINPUT1, 0)
GPIO.output(LEFTINPUT2, 0)
GPIO.output(RIGHTINPUT3, 0)
GPIO.output(RIGHTINPUT4, 0)

#PWM INITIALISE

LPWM = GPIO.PWM(LEFTENABLE, 200)
RPWM = GPIO.PWM(RIGHTENABLE, 200)
LPWM.start(0)
RPWM.start(0)

time.sleep(1)

#DEFINE FUNCTIONS

def FORWARD(speed, duration):
    print("FORWARD at", speed, "power and", duration, "seconds")
    GPIO.output(LEFTINPUT1, 0)
    GPIO.output(LEFTINPUT2, 1)
    GPIO.output(RIGHTINPUT3, 0)
    GPIO.output(RIGHTINPUT4,1)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(i)
        RPWM.ChangeDutyCycle(i)
        time.sleep(0.01)
    time.sleep(duration)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(speed-i)
        RPWM.ChangeDutyCycle(speed-i)
        time.sleep(0.01)
    GPIO.output(LEFTINPUT1, 0)
    GPIO.output(LEFTINPUT2, 0)
    GPIO.output(RIGHTINPUT3, 0)
    GPIO.output(RIGHTINPUT4,0)

    
    
def RIGHT(speed, duration):
    print("Turning RIGHT at", speed, "power and", duration, "seconds")
    GPIO.output(LEFTINPUT1, 0)
    GPIO.output(LEFTINPUT2, 1)
    GPIO.output(RIGHTINPUT3, 1)
    GPIO.output(RIGHTINPUT4,0)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(i)
        RPWM.ChangeDutyCycle(i)
        time.sleep(0.01)
    time.sleep(duration)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(speed-i)
        RPWM.ChangeDutyCycle(speed-i)
        time.sleep(0.01)
    GPIO.output(LEFTINPUT1, 0)
    GPIO.output(LEFTINPUT2, 0)
    GPIO.output(RIGHTINPUT3, 0)
    GPIO.output(RIGHTINPUT4,0)


def LEFT(speed, duration):
    print("Turning LEFT at", speed, "power and", duration, "seconds")
    GPIO.output(LEFTINPUT1, 1)
    GPIO.output(LEFTINPUT2, 0)
    GPIO.output(RIGHTINPUT3, 0)
    GPIO.output(RIGHTINPUT4,1)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(i)
        RPWM.ChangeDutyCycle(i)
        time.sleep(0.01)
    time.sleep(duration)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(speed-i)
        RPWM.ChangeDutyCycle(speed-i)
        time.sleep(0.01)
    GPIO.output(LEFTINPUT1, 0)
    GPIO.output(LEFTINPUT2, 0)
    GPIO.output(RIGHTINPUT3, 0)
    GPIO.output(RIGHTINPUT4,0)
  
    
def REVERSE(speed, duration):
    print("REVERSE at", speed, "power and", duration, "seconds")
    GPIO.output(LEFTINPUT1, 1)
    GPIO.output(LEFTINPUT2, 0)
    GPIO.output(RIGHTINPUT3, 1)
    GPIO.output(RIGHTINPUT4,0)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(i)
        RPWM.ChangeDutyCycle(i)
        time.sleep(0.01)
    time.sleep(duration)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(speed-i)
        RPWM.ChangeDutyCycle(speed-i)
        time.sleep(0.01)
    GPIO.output(LEFTINPUT1, 0)
    GPIO.output(LEFTINPUT2, 0)
    GPIO.output(RIGHTINPUT3, 0)
    GPIO.output(RIGHTINPUT4,0)

GPIO.output(LEFTINPUT1, 1)
GPIO.output(LEFTINPUT2, 0)
GPIO.output(RIGHTINPUT3, 1)
GPIO.output(RIGHTINPUT4,0)

for i in range(0,40): #25 for tiles, for carpet
    LPWM.ChangeDutyCycle(i)
    RPWM.ChangeDutyCycle(i)
    time.sleep(0.005)

scount = 1
countB = 0
countBL = 0
countBR = 0
VAR=1

while VAR ==1:

#SEND TRIGGER TO ALL SENSORS
    
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

#LOOP TO FIND DISTANCE FOR BACK SENSOR    

    while GPIO.input(ECHOB)==0:
        STARTB = time.time()

    while GPIO.input(ECHOB)==1:
        ENDB = time.time()

    DURATIONB = ENDB-STARTB
    DISTANCEB = DURATIONB*17150
    DISTANCEB = round(DISTANCEB, 2)
    print("BACK=", DISTANCEB)
    time.sleep(0.05)

#LOOP TO FIND DISTANCE FROM BACK RIGHT SENSOR

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    
    while GPIO.input(ECHOBR)==0:
        STARTBR = time.time()

    while GPIO.input(ECHOBR)==1:
        ENDBR = time.time()

    DURATIONBR = ENDBR-STARTBR
    DISTANCEBR = DURATIONBR*17150
    DISTANCEBR = round(DISTANCEBR, 2)
    print("                 BACK RIGHT=", DISTANCEBR)
    time.sleep(0.05)

#LOOP TO FIND DISTANCE FROM BACK LEFT SENSOR

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    
    while GPIO.input(ECHOBL)==0:
        STARTBL = time.time()

    while GPIO.input(ECHOBL)==1:
        ENDBL = time.time()

    DURATIONBL = ENDBL-STARTBL
    DISTANCEBL = DURATIONBL*17150
    DISTANCEBL = round(DISTANCEBL, 2)
    print("                                               BACK LEFT=", DISTANCEBL)
    time.sleep(0.05)
#BACK DISTANCE MONITORING
    if DISTANCEB < 100:
        if countB == 0:     
            LPWM.ChangeDutyCycle(40)
            RPWM.ChangeDutyCycle(40)    
            countB += 1
        if countB == 1 and DISTANCEB < 60:   
            LPWM.ChangeDutyCycle(30)
            RPWM.ChangeDutyCycle(30)
            countB += 1
        if countB == 2 and DISTANCEB < 50:
            countB +=1
        if countB== 3:
            print("B Too close, braking")
            GPIO.output(LEFTINPUT1, 0)
            GPIO.output(LEFTINPUT2, 0)
            GPIO.output(RIGHTINPUT3, 0)
            GPIO.output(RIGHTINPUT4,0)
            FORWARD(50, 1)
            if scount%2 == 1:
                RIGHT(50, 1)
            else:
                LEFT(50, 1)
            GPIO.output(LEFTINPUT1, 1)
            GPIO.output(LEFTINPUT2, 0)
            GPIO.output(RIGHTINPUT3, 1)
            GPIO.output(RIGHTINPUT4,0)
            LPWM.ChangeDutyCycle(40)
            RPWM.ChangeDutyCycle(40)
            countB = 0
            countBL = 0
            countBR = 0
    else:
        countB = 0
        LPWM.ChangeDutyCycle(40)
        RPWM.ChangeDutyCycle(40)

#BACK LEFT DISTANCE MONITORING
    if DISTANCEBL < 80:
        if countBL == 0:     
            LPWM.ChangeDutyCycle(40)
            RPWM.ChangeDutyCycle(40)    
            countBL += 1
        if countBL == 1 and DISTANCEBL < 50:   
            LPWM.ChangeDutyCycle(30)
            RPWM.ChangeDutyCycle(30)
            countBL += 1
        if countBL == 2 and DISTANCEBL < 40:
            countBL +=1
        if countBL == 3:
            print("BL Too close, braking")
            GPIO.output(LEFTINPUT1, 0)
            GPIO.output(LEFTINPUT2, 0)
            GPIO.output(RIGHTINPUT3, 0)
            GPIO.output(RIGHTINPUT4,0)
            FORWARD(50, 0.5)
            LEFT(50, 0.5)
            GPIO.output(LEFTINPUT1, 1)
            GPIO.output(LEFTINPUT2, 0)
            GPIO.output(RIGHTINPUT3, 1)
            GPIO.output(RIGHTINPUT4,0)
            LPWM.ChangeDutyCycle(40)
            RPWM.ChangeDutyCycle(40)
            countB = 0
            countBL = 0
            countBR = 0
    
    else:
        countBL = 0
        LPWM.ChangeDutyCycle(40)
        RPWM.ChangeDutyCycle(40)

#BACK RIGHT DISTANCE MONITORING
         
    if DISTANCEBR < 80:
        if countBR == 0:     
            LPWM.ChangeDutyCycle(40)
            RPWM.ChangeDutyCycle(40)    
            countBR += 1
        if countBR == 1 and DISTANCEBR < 50:   
            LPWM.ChangeDutyCycle(30)
            RPWM.ChangeDutyCycle(30)
            countBR += 1
        if countBR == 2 and DISTANCEBR < 40:
            countBR +=1
        if countBR == 3:
            print("BR Too close, braking")
            GPIO.output(LEFTINPUT1, 0)
            GPIO.output(LEFTINPUT2, 0)
            GPIO.output(RIGHTINPUT3, 0)
            GPIO.output(RIGHTINPUT4,0)
            FORWARD(50, 0.5)
            RIGHT(50, 0.5)
            GPIO.output(LEFTINPUT1, 1)
            GPIO.output(LEFTINPUT2, 0)
            GPIO.output(RIGHTINPUT3, 1)
            GPIO.output(RIGHTINPUT4,0)
            LPWM.ChangeDutyCycle(40)
            RPWM.ChangeDutyCycle(40)
            count = 0
            countBL = 0
            countBR = 0
    else:
        countBR = 0
        LPWM.ChangeDutyCycle(40)
        RPWM.ChangeDutyCycle(40)
       
    
    scount += 1
    
LPWM.ChangeDutyCycle(0)
RPWM.ChangeDutyCycle(0)
GPIO.cleanup()




    
