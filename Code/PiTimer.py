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

class Cube:
    'Creates a Cube object that contains all solves and times for a cube.'

    def __init__(self, cubeType):
        self.cubeType = cubeType

    def scramble():

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
            moveSet = random.choice(cubeTurns.Moves)
            move = random.choice(moveSet)
            mod = random.choice(cubeTurns.Modifiers)

            #Check for Repeat
            if moveSet == lastMoveSet:
                while move == lastMove:
                    move = random.choice(moveSet)
                while mod == lastMod:
                    mod = random.choice(cubeTurns.Modifiers)

            #Print Move
            scramble = scramble + str(move) + str(mod) + " "

            lastMoveSet = moveSet
            lastMove = move
            lastMod = mod

        print(scramble)
        return scramble

    def timer(inspect):

        mils = 0
        secs = 0
        mins = 0

        stopped = False

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
            elif secs == 20:
                stopped = True
                break
            time.sleep(0.1)
        finishTime = (" %02d : %02d : %d " % (mins, secs, (mils - 1)))
        return finishTime
    

##class Scramble:
##    'Creates a Scramble and Solve Time for 3x3 or 2x2'
##
##    def __init__(self, cube):
##      if 1 < cube < 4:
##        self.cube = cube
##
##    def generateScramble(self):
##
##      scramble = ""
##
##      #Set Scramble Length
##      if self.cube == 2:
##        scrambleSize = 10
##      elif self.cube == 3:
##        scrambleSize = 15
##
##      lastMove = "B"
##      lastMod = "'"
##
##      for m in range(scrambleSize):
##        move = random.choice(cubeTurns.x2)
##        mod = random.choice(cubeTurns.modifiers)
##
##        #Check for Repeat
##        if move == lastMove:
##          move = random.choice(cubeTurns.x2)
##          if mod == lastMod:
##            mod = random.choice(cubeTurns.modifiers)
##
##        #Print Move
##        scramble = scramble + str(move) + str(mod) + " "
##
##        lastMove = move
##        lastMod = mod
##
##      print(scramble)
##      return scramble


class Session:
    'Creates a session of a few solves and then gives stats'

    def __init__(self, solveNums, inspection, cube):
        self.solveNums = solveNums
        self.inspection = inspection
        self.cube = cube
        #Gets the number of solves in session
        #Sets inspection time for each solve

        timeList = []    #lists for storing stats
        scrambList = []  #

    def session():
        print("Starting a Session of %d" % solveNums)
        for i in range(int(solveNums)):
            scrambList.append(cube.scramble())
            input("Ready!")
            timeList.append(cube.timer(inspection))
            
    def getAverage():
        totalTime = 0
        for i in range(len(timeList)):
            totalTime += timeList[i]
        return int(totalTime / len(timeList))

    def printSession():
        for i in range(len(timeList)):
            print(scrambList[i] + " : " + timeList[i])
        print("Average : " + getAverage())

