import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

BIN1 = 32
BIN2 = 31
MODE = 36

GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(MODE, GPIO.OUT)

print("Setting up")
time.sleep(1)

GPIO.output(MODE, 1)

VAR = 1
count = 0

while count < 2:
    print("Coasting")
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 0)
    time.sleep(1)
    
    print("Forward")
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    time.sleep(1)
    
    print("Coasting")
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 0)
    time.sleep(3)
    
    print("Reverse")
    GPIO.output(BIN1, 1)
    GPIO.output(BIN2, 0)
    time.sleep(1)

    print("BRAKE!!!")
    GPIO.output(BIN1, 1)
    GPIO.output(BIN2, 1)
    time.sleep(1)
    
    count = count + 1

GPIO.output(BIN1, 0)
GPIO.output(BIN2, 0)
time.sleep(1)
