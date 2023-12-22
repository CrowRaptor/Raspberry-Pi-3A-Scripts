import RPi.GPIO as GPIO     #get gpio lib
from time import sleep      #get sleep func from time module

GPIO.setwarnings(False)     #ignore problems
GPIO.setmode(GPIO.BOARD)       #use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   #set pin 8 as output and set value to off

while True: #run forever
    GPIO.output(8, GPIO.HIGH)   #turn on
    sleep(1)    #1 second eep
    GPIO.output(8, GPIO.LOW)
    sleep(1)
    