import RPi.GPIO as GPIO
from time import sleep

servo_pin = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)     #ignore problems
GPIO.setmode(GPIO.BOARD)       #use physical pin numbering
GPIO.setup(8, 11, GPIO.OUT, initial=GPIO.LOW)   #set pin 8 as output and set value to off

def movemotor():
    ## add your servo BOARD PIN number ##

    pwm=GPIO.PWM(servo_pin, 50)
    pwm.start(0)

    ## edit these duty cycle % values ##
    right = 2.5
    neutral = 7.5
    left = 12
    #### that's all folks ####
    while True:
        print("begin loop")

        print("duty cycle", right,"% at left -90 deg")
        pwm.ChangeDutyCycle(2.5)
        sleep(1)

        print("duty cycle", neutral,"% at 0 deg")
        pwm.ChangeDutyCycle(neutral)
        sleep(1)

        print("duty cycle",left, "% at right +90 deg")
        pwm.ChangeDutyCycle(left)
        sleep(1)

        print("went through motor func")


def blinkLED():

    while True: #run forever
        GPIO.output(8, GPIO.HIGH)   #turn on
        sleep(1)    #1 second eep
        GPIO.output(8, GPIO.LOW)
        sleep(1)
        
        print("went though led func")

movemotor()
blinkLED()



