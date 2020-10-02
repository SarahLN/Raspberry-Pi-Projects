import RPi.GPIO as GPIO
import time

ledPin = 11 # define LED Pin

def setup():
    GPIO.setmode(GPIO.BOARD) # use physical GPIO numbering
    GPIO.setup(ledPin, GPIO.OUT) # set the LED pin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW) # make LED pin output LOW level
    print ('using pin%d'%ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH) # make ledPin output HIGH level to turn on led
        print ('led turned on >>>') # print information on terminal
        time.sleep(2) # Wait for 1 second
        GPIO.output(ledPin, GPIO.LOW) 
        print ('led turned off <<<') # make ledPin output LOW level to turn off led 
        time.sleep(.5) # Wait for 1 second

def destroy():
    GPIO.cleanup() # release all GPIO

if __name__ == '__main__':
    print('Program is starting ... \n') 
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
