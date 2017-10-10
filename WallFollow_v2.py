import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

##SENSOR SETUP
    #PINS
TRIG = 7
ECHOF = 8
ECHOFL = 10
ECHOFR = 11
ECHOL = 12
ECHOR = 13
ECHOBL = 15
ECHOBR = 19
ECHOB =  21

    #SENSOR ARRAY
sensors = [ECHOFL, ECHOL, ECHOBL, ECHOB, ECHOBR, ECHOF, ECHOFR, ECHOR]
sensors_len = len(sensors)
distances = []

distancesAVG1 = []
distancesAVG2 = []
distancesAVG3 = []

    #GPIOs
GPIO.setup(ECHOF, GPIO.IN)
GPIO.setup(ECHOFL, GPIO.IN)
GPIO.setup(ECHOFR, GPIO.IN)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.setup(ECHOR, GPIO.IN)
GPIO.setup(ECHOBL, GPIO.IN)
GPIO.setup(ECHOBR, GPIO.IN)
GPIO.setup(ECHOB, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)

##MOTOR SETUP
    #PINS
LEFTENABLE = 33
RIGHTENABLE = 32
LEFTINPUT1 = 31
LEFTINPUT2 = 35
RIGHTINPUT3 = 36
RIGHTINPUT4 = 37

    #GPIOs
GPIO.setup(LEFTENABLE, GPIO.OUT)
GPIO.setup(RIGHTENABLE, GPIO.OUT)
GPIO.setup(LEFTINPUT1, GPIO.OUT)
GPIO.setup(LEFTINPUT2, GPIO.OUT)
GPIO.setup(RIGHTINPUT3, GPIO.OUT)
GPIO.setup(RIGHTINPUT4, GPIO.OUT)

    #PWM
LPWM = GPIO.PWM(LEFTENABLE, 200)
RPWM = GPIO.PWM(RIGHTENABLE, 200)
LPWM.start(0)
RPWM.start(0)

time.sleep(0.5)

##GLOBAL VARIABLES
    #SENSORS
    #FRONT LEFT
global STARTFL
global ENDFL
global DISTANCEFL
    #LEFT
global STARTL
global ENDL
global DISTANCEL
    #BACK LEFT
global STARTBL
global ENDBL
global DISTANCEBL

##DEFINE FUNCTIONS
##def FORWARD():
##
##def TURNLEFT():
##
##def TURNRIGHT():

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
            STARTFL = time.time()
        
        while GPIO.input(ECHOFL)==1:           
            ENDFL = time.time()

        DURATIONFL = ENDFL-STARTFL        
        DISTANCEFL = DURATIONFL*17150
        time.sleep(0.05)
        if DISTANCEFL < 400:
            print("FRONT LEFT =", DISTANCEFL)
            DISTANCEFLtemp = round(DISTANCEFL, 2)
        else:
            print("inaccurate measurement front left")
            DISTANCEFLtemp = 0
        checkFL = 1

    #LOOP TO FIND DISTANCE FOR LEFT SENSOR
    while checkL==0:
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
        while GPIO.input(ECHOL)==0:
            STARTL = time.time()
        
        while GPIO.input(ECHOL)==1:           
            ENDL = time.time()

        DURATIONL = ENDL-STARTL        
        DISTANCEL = DURATIONL*17150
        time.sleep(0.05)
        if DISTANCEL < 400:
            print("LEFT =", DISTANCEL)
            DISTANCELtemp = round(DISTANCEL, 2)
        else:
            print("inaccurate measurement left")
            DISTANCELtemp = 0
        checkL = 1
        
    #LOOP TO FIND DISTANCE FOR BACK LEFT SENSOR
    while checkBL==0:
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
        while GPIO.input(ECHOL)==0:
            STARTBL = time.time()
        
        while GPIO.input(ECHOL)==1:           
            ENDBL = time.time()

        DURATIONBL = ENDBL-STARTBL        
        DISTANCEBL = DURATIONBL*17150
        time.sleep(0.05)
        if DISTANCEBL < 400:
            print("BACK LEFT =", DISTANCEBL)
            DISTANCEBLtemp = round(DISTANCEBL, 2)
        else:
            print("inaccurate measurement back left")
            DISTANCEBLtemp = 0
        checkBL = 1



        
    return DISTANCEFLtemp, DISTANCELtemp, DISTANCEBLtemp
##MAIN()
#using try/except to enable clean exit of program
try:
    #this is where main code goes here
    var = 1
    i = 0
    while var ==1:
        for count in range(0,3):
            if i == 0:
                distancesAVG1.append(CHECKSENSORS())
                print(distancesAVG1)
            elif i ==1:
                distancesAVG2.append(CHECKSENSORS())
                print(distancesAVG2)
            elif i ==2:
                distancesAVG3.append(CHECKSENSORS())
                print(distancesAVG3)
            count +=1
            i +=1
        if count == 3:
            AverageFL = (distancesAVG1[0]+distancesAVG2[0]+distancesAVG3[0])
            AverageL = (distancesAVG1[1]+distancesAVG2[1]+distancesAVG3[1])
            AverageBL = (distancesAVG1[2]+distancesAVG2[2]+distancesAVG3[2])
            i = 0

            print("FL average", AverageFL, "L average", AverageL, "BL average", AverageBL)
            
        #distances = CHECKSENSORS()

 
        time.sleep(1)
    
##except KeyboardInterrupt:
##    #this happens when you press CTRL+c to end the program
##    print("Keyboard interrupt")
##    print("Shutting down program and cleaning GPIOs")
##except:
##    #this occurs if something unexpected happens and an error is generated
##    print("Something broke")
finally:
    #clean up
    print("clear GPIOs")
    GPIO.cleanup()
    print("shutting down")
