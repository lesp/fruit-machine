from random import *
from time import *

reel1 = ["cherry","lemon","bell"]
reel2 = ["cherry","lemon","bell"]
reel3 = ["cherry","lemon","bell"]

while True:
    if raw_input() == "p":
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
                print ("Jackpot")
                print ("=======")
            elif (r2) == (r1) and (r2) == (r3):
                print ("=======")
                print ("Jackpot")
                print ("=======")
            elif (r3) == (r1) and (r3) == (r2):
                print ("=======")
                print ("Jackpot")
                print ("=======")
    else:
        print ("End of game")
        break
