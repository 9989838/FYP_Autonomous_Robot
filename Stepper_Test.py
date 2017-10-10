import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A1 = 36
A3 = 37
B1 = 38
B3 = 40
count = 0

GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A3, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B3, GPIO.OUT)

print("setting up")


GPIO.output(A1, 0) 
GPIO.output(A3, 0)
GPIO.output(B1, 0)
GPIO.output(B3, 0) 

time.sleep(0.5)

print("Rotating to pos 1")
GPIO.output(A1, 1)
time.sleep(0.5)
print("Rotating back")
GPIO.output(A1, 0)

def CW(angle, speed):
    sleep_time = 0.1/speed
    #for loop in range (0, abs(angle/7.5)):
        
