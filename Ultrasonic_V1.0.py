import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

ECHO = 10
TRIG = 8

GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)            

GPIO.output(TRIG, 0)
print("Setting up")
time.sleep(1)


VAR = 1

while VAR ==1:

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    
    while GPIO.input(ECHO)==0:
        start = time.time()

    while GPIO.input(ECHO)==1:
        end = time.time()

    duration = end-start

    distance = duration*17150

    distance = round(distance, 2)
    if distance > 200:
        print("Too far")
    else:
        print(distance)
    time.sleep(0.2)

GPIO.cleanup()




    
    
    
