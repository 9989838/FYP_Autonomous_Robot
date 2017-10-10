import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


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
#GPIO.setup(ECHOFL, GPIO.IN)
##GPIO.setup(ECHOFR, GPIO.IN)
##GPIO.setup(ECHOR, GPIO.IN)
##GPIO.setup(ECHOBL, GPIO.IN)
##GPIO.setup(ECHOBR, GPIO.IN)
##GPIO.setup(ECHOB, GPIO.IN)
##GPIO.setup(TRIG, GPIO.OUT)

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
##GPIO.output(TRIG, 0)
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
        time.sleep(0.005)
    time.sleep(duration)
    for i in range(0, speed):
        LPWM.ChangeDutyCycle(speed-i)
        RPWM.ChangeDutyCycle(speed-i)
        time.sleep(0.005)
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

    
    
count = 0

while count <1:
    FORWARD(0, 1)
    FORWARD(20, 2)
    REVERSE(40, 2)
    FORWARD(60, 2)
    REVERSE(80, 1.5)
    FORWARD(100, 1.5)
    

    
    
    
    count = count+1
    print(count)

GPIO.cleanup()

    #Read Encoder outputs
  #  if GPIO.input(ENCODERA)==0:
   #     #print('low')
    #    if GPIO.input(ENCODERA)==1:
     #       #print('high')
      #      count = count + 1
       #     print(count)
    

    #Calculate frequency of rising edges, 16 counts per rev


    
