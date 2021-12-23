import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buttonPin = 12
greenLed = 11
redLed = 13

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)

def blinkRedLed():
    GPIO.output(redLed, True)
    time.sleep(1)
    GPIO.output(redLed, False)
    GPIO.cleanup()

def blinkGreenLed():
    GPIO.output(greenLed, True)
    time.sleep(1)
    GPIO.output(greenLed, False)
    GPIO.cleanup()


while 1 == 1:
    buttonState = GPIO.input(buttonPin)
    
    if buttonState == False:
        blinkRedLed()


        


