# # # # # # # # # # # # # # # # # # # # # #
#
#  PiTimer: A Python Cube Timer for the RPi
#    FUNCTIONS Module
#
#

import time
import math
import requests
#import tkinter as tk
import RPi.GPIO as GPIO
import keyboard

# # #  GPIO SETUP  # # #
GPIO.setmode(GPIO.BOARD)

LH = 16
RH = 18

LMenu = 29
Enter = 31
RMenu = 33


# # # # #  ##  # # # # #


class Buttons(self, inputType):
    '''Creates an object that can be used to query button presses'''

    def __init__(self, inputType):
        if (self.inputType == 'GPIO'):
            self.inputType = inputType
            
            GPIO.setup(LH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(RH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

            GPIO.setup(LMenu, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(Enter, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(RMenu, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        else:
            self.inputType = 'kb'

            import keyboard;
    
    def isPressed(self, mode):
        if (mode == 'both'):
            if (inputType == 'GPIO'):
                return GPIO.input(LH) and GPIO.input(RH)
            else:
                return keyboard.isPressed('f+j')
        else:
            if (inputType == 'GPIO'):
                return GPIO.input(LH) or GPIO.input(RH)
            else:
                return keyboard.isPressed('f') or keyboard.isPressed('j')

    def waitUntilRelease(self):
        while (isPressed() == True):
            time.sleep(.01) # fix this with .join()

    def waitForPressAndRelease(self, mode):
        while True:
            if self.isPressed(mode):
                self.waitUntilRelease()
                break


    

class Cube:
    '''Creates a Cube object that contains all solves and times for a cube.'''

    def __init__(self, cubeType):
        self.cubeType = cubeType

        # cubeType should be a TNoodle Short Name:
        '''
        {"shortName":"222","longName":"2x2x2"},
        {"shortName":"333","longName":"3x3x3"},
        {"shortName":"333fm","longName":"3x3x3 Fewest Moves"},
        {"shortName":"333ni","longName":"3x3x3 no inspection"},
        {"shortName":"444","longName":"4x4x4"},
        {"shortName":"444fast","longName":"4x4x4 (fast, unofficial)"},
        {"shortName":"444ni","longName":"4x4x4 no inspection"},
        {"shortName":"555","longName":"5x5x5"},
        {"shortName":"555ni","longName":"5x5x5 no inspection"},
        {"shortName":"666","longName":"6x6x6"},
        {"shortName":"777","longName":"7x7x7"},
        {"shortName":"clock","longName":"Clock"},
        {"shortName":"minx","longName":"Megaminx"},
        {"shortName":"pyram","longName":"Pyraminx"},
        {"shortName":"skewb","longName":"Skewb"},
        {"shortName":"sq1","longName":"Square-1"},
        {"shortName":"sq1fast","longName":"Square-1 (fast, unofficial)"}
        '''

    def scramble(self):

        URLload = {'' : self.cubeType}

        r = requests.get('http://localhost:2014/scramble/.txt', params=URLload)
        rPage = r.text
        scramble = rPage[0:len(rPage)-2]
        return scramble

class Solve:
    '''An object representing a single solve.'''

    DNF = False
    Penalty = False
    
    def __init__(self, inspection, cube, buttons):
        self.inspection = inspection
        self.cube = cube         # should be a cube obj
        self.buttons = buttons   # should be a buttons obj

    def timer(self):
        stopped = False
        startTime = time.time_ns()
        endTime = 0
        mils, secs, mins = 0, 0, 0
        while stopped != True:

            print(" %02d : %02d : %d " % (mins, secs, mils))
            mils += 1
            if mils > 9:
                mils = 0
                secs += 1
            elif secs > 59:
                secs = 0
                mins += 1
            elif buttons.isPressed('both'):
                endTime = time.time_ns()
                stopped = True
                buttons.waitUntilRelease()
                break
            time.sleep(0.1)

        elapsed = (endTime - startTime) / 1000000
        calcMils = elapsed
        calcMins = calcMils / 60
        calcMils %= calcMins
        calcSecs = calcMils / 100
        calcMils %= calcSecs

        finishCalcTimeText = (" %02d : %02d : %d " % (calcMins, calcSecs, (calcMils - 1)))
        finishTimeText = (" %02d : %02d : %d " % (mins, secs, (mils - 1)))
        finishTimeNumb = [mins, secs, mils]

        return finishTimeText, finishTimeNumb

    def solve(self):
        scramble = self.cube.scramble()
        print(scramble)
        timeText = ""
        timeList = []

        GPIO.add_event_detect(RH, GPIO.FALLING, bouncetime=100)
        GPIO.add_event_detect(LH, GPIO.FALLING, bouncetime=100)

        print("Ready.")

        handsDown = False
        buttons.waitForPressAndRelease('both')
        print("Starting")
        
        startTime = time.time_ns()
        currentTime = time.time_ns()
        timeoutTime = startTime + (30 * 1000000000)
        penaltyTime = startTime + self.inspection
        pressedTime = 0
        canStart = False
        while currentTime < timeoutTime:
            if currentTime > penaltyTime:
                Penalty = True
            if GPIO.input(RH) == False and GPIO.input(LH) == False:
                pressedTime += 0.1
                handsDown = True
            if pressedTime > 1:
                print("You can go")
                canStart = True
            if GPIO.input(RH) == True and GPIO.input(LH) == True and handsDown == True and canStart == True:
                handsDown = False
                break
            print(str(penaltyTime - currentTime))
            currentTime = time.time_ns()
            time.sleep(0.1)
   
        timeText, timeList = self.timer()
        return timeText, timeList
        

class Session:
    '''Creates a session of a few solves and then gives stats'''

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
        return str(int(totalTime / len(Session.timeList)))
        #avgTimeList = divmod(int(totalTime / len(Session.timeList)), 60)
        #avgTimeList = str(avgTimeList[1]).split('.')
        #return str(avgTimeList[0]) + str(avgTimeList[1][0]) + str(avgTimeList[1][1])
   
    def printSession(self):
        for i in range(len(Session.timeList)):
            print(Session.scrambList[i] + " : " + str(Session.timeList[i]))
        print("Average : " + Session.getAverage(self))

qiyi = Cube(222)
testSolve = Solve(15, qiyi)
testSolve.solve()
GPIO.cleanup()
#Cube Test

'''
mySession = Session(int(input("How Many Solves?")), int(input("Inspection Time?")), qiyi)
mySession.session()
time.sleep(1)
GPIO.cleanup()
#mySession.printSession()
#Session Tests
'''