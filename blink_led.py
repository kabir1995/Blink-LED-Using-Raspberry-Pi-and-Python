import RPi.GPIO as GPIO
import time
ledpin=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin, GPIO.OUT)
while 1:
    GPIO.output(ledpin,True)
    time.sleep(1)
    GPIO.output(ledpin,False)
    time.sleep(1)
#for counter in range(0,10000):
#    GPIO.output(3,True)
#    time.sleep(1)
#    GPIO.output(3,False)
#    time.sleep(1)
#GPIO.output(ledpin,False)
