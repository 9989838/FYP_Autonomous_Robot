import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


TRIG = 7
ECHOF = 8
ECHOFL = 10
ECHOFR = 11
ECHOL = 12
ECHOR = 13
ECHOBL = 15
ECHOBR = 19
ECHOB =  21
sensors = [ECHOFL, ECHOFR, ECHOL, ECHOR, ECHOBL, ECHOBR, ECHOB, ECHOF]
sensors_len = len(sensors)
distances = []

GPIO.setup(ECHOF, GPIO.IN)
GPIO.setup(ECHOFL, GPIO.IN)
GPIO.setup(ECHOFR, GPIO.IN)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.setup(ECHOR, GPIO.IN)
GPIO.setup(ECHOBL, GPIO.IN)
GPIO.setup(ECHOBR, GPIO.IN)
GPIO.setup(ECHOB, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)            

GPIO.output(TRIG, 0)
print("Setting up")
time.sleep(0.8)
print("| F Left   |  |   FRight   |  |    Left    | |    Right    |  |    BLeft    | |    B Right  | |    Back   | Front  ")
print("_________________________________________________________________________________________________________")

    


time.sleep(0.8)

VAR = 1

while VAR ==1:

    for i in range(0, 7):
        
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
        
        while GPIO.input(sensors[i])== 0:
            START = time.time()

        while GPIO.input(sensors[i])==1:
            END = time.time()

        DURATION = END-START
        DISTANCE = DURATION*17150
        DISTANCE = round(DISTANCE, 2)
        DISTANCE = format(DISTANCE, '07')
        distances.append(DISTANCE)
        distances.append(' ')
        


    print(distances)
    distances = []
    time.sleep(0.3)
    
GPIO.cleanup()

    
    
    
