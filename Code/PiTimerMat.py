# # # # # # # # # # # # # # # # # # # # # #
#
#  PiTimer: A Python Cube Timer for the RPi
#    FUNCTIONS Module
#
#

import random
import time
import tkinter as tk
import cubeTurns
import RPi.GPIO as GPIO

# # #  GPIO SETUP  # # #
GPIO.setmode(GPIO.BOARD)

#RedL = 11
#BluL = 13
#GreL = 15

LH = 29
RH = 31

GPIO.setup(LH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# # #              # # #

class Cube:
    'Creates a Cube object that contains all solves and times for a cube.'

    def __init__(self, cubeType):
        self.cubeType = cubeType

    def scramble(self):

        scrambleText = ""
        
        #Scramble Length
        if self.cubeType == 2:
            scrambleSize = 10
        elif self.cubeType == 3:
            scrambleSize = 15

        lastMoveSet = "FB"
        lastMove = "B"
        lastMod = "'"

        for m in range(scrambleSize):
            moveSet = random.choice(list(cubeTurns.Moves))
            move = random.choice(list(moveSet))
            mod = random.choice(list(cubeTurns.Modifiers))

            #Check for Repeat
            if moveSet == lastMoveSet:
                while move == lastMove:
                    move = random.choice(list(moveSet))
                while mod == lastMod:
                    mod = random.choice(list(cubeTurns.Modifiers))

            #Print Move
            scrambleText = scrambleText + str(move) + str(mod) + " "

            lastMoveSet = moveSet
            lastMove = move
            lastMod = mod

        print(scrambleText)
        return scrambleText

    def timer(self, inspect):

        stopped = False

        mils = 0
        secs = 0
        mins = 0

        print("Get Ready")
        time.sleep(inspect)
        print("Go!")

        while stopped != True:

            print(" %02d : %02d : %d " % (mins, secs, mils))
            mils += 1
            if mils > 9:
                mils = 0
                secs += 1
            elif secs > 59:
                secs = 0
                mins += 1
            elif GPIO.input(LH) == 1 and GPIO.input(RH):
                stopped = True
                GPIO.wait_for_edge(LH, GPIO.RISING) or GPIO.wait_for_edge(RH, GPIO.Rising)
                break
            time.sleep(0.1)

        finishTimeText = (" %02d : %02d : %d " % (mins, secs, (mils - 1)))
        finishTimeNumb = [mins, secs, mils]

        return finishTimeText, finishTimeNumb


class Session:
    'Creates a session of a few solves and then gives stats'

    timeList = []    #lists for storing stats
    scrambList = []

    def __init__(self, solves, inspection, cube):
        self.solves = solves
        self.inspection = inspection
        self.cube = cube
        #Gets the number of solves in session
        #Sets inspection time for each solve

    def session(self):
        print("Starting a Session of %d" % self.solves)
        for i in range(int(self.solves)):
            Session.scrambList.append(self.cube.scramble())
            input("Ready!")
            Session.timeList.append(self.cube.timer(self.inspection)[1])
            
    def getAverage(self):
        totalTime = 0
        for i in range(len(Session.timeList)):
            totalTime += Session.timeList[i][0] * 60  #
            totalTime += Session.timeList[i][1]       # Lists -> Total Seconds
            totalTime += Session.timeList[i][2] * 0.1 #
        avgTimeList = divmod(int(totalTime / len(Session.timeList)), 60)
        avgTimeList = str(avgTimeList[1]).split('.')
        return str(avgTimeList[0]) + str(avgTimeList[1][0]) + str(avgTimeList[1][1])

    def printSession(self):
        for i in range(len(Session.timeList)):
            print(Session.scrambList[i] + " : " + str(Session.timeList[i]))
        print("Average : " + Session.getAverage(self))

qiyi = Cube(2)
qiyi.scramble()
#Cube Test

mySession = Session(int(input("How Many Solves?")), 10, qiyi)
mySession.session()
time.sleep(1)
GPIO.cleanup()
#mySession.printSession()
#Session Tests

