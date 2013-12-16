from random import *
from time import *
import RPi.GPIO as GPIO

button_pin = 8
led_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin , GPIO.IN)
GPIO.setup(led_pin , GPIO.OUT)

reel1 = ["cherry","lemon","bell"]
reel2 = ["cherry","lemon","bell"]
reel3 = ["cherry","lemon","bell"]

while True:
    #sleep(3)
    print ("Press the button to start the game")
    sleep(1)
    if GPIO.input(button_pin)==1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            :
        for i in range(0,3):
            r1 = choice(reel1)
            r2 = choice(reel2)
            r3 = choice(reel3)
            print ("++Playing the game++")
            print (" ")
            print (r1) + " " + (r2) + " " + (r3)
            print (" ")
            sleep(2)

            if (r1) == (r2) and (r1) == (r3):
                print ("=======")
                GPIO.output(led_pin, True)
                sleep(0.5)
                GPIO.output(led_pin, False)
                sleep(0.5)
                print ("Jackpot")
                GPIO.output(led_pin, True)
                sleep(0.5)
                GPIO.output(led_pin, False)
                sleep(0.5)
                print ("=======")
            elif (r2) == (r1) and (r2) == (r3):
                print ("=======")
                GPIO.output(led_pin, True)
                sleep(0.5)
                GPIO.output(led_pin, False)
                sleep(0.5)
                print ("Jackpot")
                GPIO.output(led_pin, True)
                sleep(0.5)
                GPIO.output(led_pin, False)
                sleep(0.5)
                print ("=======")
            elif (r3) == (r1) and (r3) == (r2):
                print ("=======")
                GPIO.output(led_pin, True)
                sleep(0.5)
                GPIO.output(led_pin, False)
                sleep(0.5)
                print ("Jackpot")
                GPIO.output(led_pin, True)
                sleep(0.5)
                GPIO.output(led_pin, False)
                sleep(0.5)
                print ("=======")
    #else:
        #print ("End of game")
        #break
