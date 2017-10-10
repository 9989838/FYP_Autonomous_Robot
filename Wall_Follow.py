import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

count=0

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
sensors = [ECHOFL, ECHOL, ECHOBL, ECHOB, ECHOBR, ECHOF, ECHOFR, ECHOR]
sensors_len = len(sensors)
distances = []

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

#MOTOR PINS
LEFTENABLE = 33
RIGHTENABLE = 32

LEFTINPUT1 = 31
LEFTINPUT2 = 35
RIGHTINPUT3 = 36
RIGHTINPUT4 = 37

#MOTOR SETUP
GPIO.setup(LEFTENABLE, GPIO.OUT)
GPIO.setup(RIGHTENABLE, GPIO.OUT)
GPIO.setup(LEFTINPUT1, GPIO.OUT)
GPIO.setup(LEFTINPUT2, GPIO.OUT)
GPIO.setup(RIGHTINPUT3, GPIO.OUT)
GPIO.setup(RIGHTINPUT4, GPIO.OUT)

#PWM INITIALISE
LPWM = GPIO.PWM(LEFTENABLE, 200)
RPWM = GPIO.PWM(RIGHTENABLE, 200)
LPWM.start(0)
RPWM.start(0)

time.sleep(0.5)

#DEFINE FUNCTION
def FORWARD(LEFT, RIGHT):
    print("Left motor: ", LEFT, "Right motor: ", RIGHT)
    GPIO.output(LEFTINPUT1, 0)
    GPIO.output(LEFTINPUT2, 1)
    GPIO.output(RIGHTINPUT3, 0)
    GPIO.output(RIGHTINPUT4,1)
    LPWM.ChangeDutyCycle(LEFT)
    RPWM.ChangeDutyCycle(RIGHT)

def CHECKSENSORS():
    checkL= 0
    checkFL = 0
    checkBL = 0
    #LOOP TO FIND DISTANCE FOR FRONT LEFT SENSOR
    while checkFL==0:
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
        while GPIO.input(ECHOFL)==0:
            global STARTFL
            STARTFL = time.time()
        
        while GPIO.input(ECHOFL)==1:
            global ENDFL
            ENDFL = time.time()

        DURATIONFL = ENDFL-STARTFL
        global DISTANCEFL
        DISTANCEFL = DURATIONFL*17150
        DISTANCEFL = round(DISTANCEFL, 2)
        time.sleep(0.05)
        if DISTANCEFL < 400:
            print("FRONT LEFT =", DISTANCEFL)
            checkFL = 1

#LOOP TO FIND DISTANCE FROM LEFT SENSOR
    while checkL == 0:
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
    
        while GPIO.input(ECHOL)==0:
            global STARTL
            STARTL = time.time()

        while GPIO.input(ECHOL)==1:
            global ENDL
            ENDL = time.time()

        DURATIONL = ENDL-STARTL
        global DISTANCEL
        DISTANCEL = DURATIONL*17150
        DISTANCEL = round(DISTANCEL, 2)
        time.sleep(0.05)
        if DISTANCEL < 400:
            print("                       LEFT =", DISTANCEL)
            checkL = 1

#LOOP TO FIND DISTANCE FROM BACK LEFT SENSOR
    while checkBL==0:
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
    
        while GPIO.input(ECHOBL)==0:
            global STARTBL
            STARTBL = time.time()

        while GPIO.input(ECHOBL)==1:
            global ENDBL
            ENDBL = time.time()

        DURATIONBL = ENDBL-STARTBL
        global DISTANCEBL
        DISTANCEBL = DURATIONBL*17150
        DISTANCEBL = round(DISTANCEBL, 2)
        time.sleep(0.05)
        if DISTANCEBL < 400:
            print("                                           BACK LEFT=", DISTANCEBL)
            checkBL = 1
        return DISTANCEFL, DISTANCEL, DISTANCEBL


#START MOTOR
for i in range(9,27): 
    LPWM.ChangeDutyCycle(i-9)
    RPWM.ChangeDutyCycle(i)
    time.sleep(0.005)
    
global LSPEED
LSPEED = 18
global RSPEED
RSPEED = 27

#SENSOR DETECTION LOOP
var = 1
while var ==1:
    distances = CHECKSENSORS()
    print(distances)

    while distances[0] - distances[1] > 20:
        print("Straightening LEFT")
        LSPEED = 18 - count
        RSPEED = 27 + count
        FORWARD(LSPEED, RSPEED)
        count = count + 1
        distances = CHECKSENSORS()
        print(round(distances[0]-distances[2], 2))
        time.sleep(0.1)
    LSPEED = 18
    RSPEED = 27
    count = 0
    while distances[2] - distances[1] > 20:
        print("Straighten Right")
        LSPEED = 18 + count
        RSPEED = 27 - count
        FORWARD(LSPEED, RSPEED)
        count = count + 1
        distances = CHECKSENSORS()
        print(round(distances[2]-distances[0], 2))
        time.sleep(0.1)
    LSPEED = 18
    RSPEED = 27
    count = 0
    if distances[1] > 35:
        print("Finding Wall")
        FORWARD(20, 39)
    if distances[1] < 25:
        print("Too close")
        FORWARD(39, 20)

    count=0
        
GPIO.cleanup()

