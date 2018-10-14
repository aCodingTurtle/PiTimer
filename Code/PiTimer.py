# # # # # # # # # # # # # # # # # # # # # #
#
#  PiTimer: A Python Cube Timer for the RPi
#
#

import random
import time
import cubeTurns

class Scramble:
    'Creates a Scramble for 3x3 or 2x2'

    def __init__(self, cube):
      if 1 < cube < 4:
        self.cube = cube

    def generateScramble(self):

      #Set Scramble Length
      if self.cube == 2:
        scrambleSize = 10
      elif self.cube == 3:
        scrambleSize = 15
        
      lastMove = "B"

      for m in range(scrambleSize):
        move = random.choice(cubeTurns.x2)
        mod = random.choice(cubeTurns.modifiers)

        #Check for Repeat  
        if move == lastMove:
          move = random.choice(cubeTurns.x2)
        
        if mod == lastMod:
          mod = random.choice(cubeTurns.modifiers)

        #Print Move
        print(move, end=mod)
        
        lastMove = move
        lastMod = mod

scramble2 = Scramble(2)
scramble2.generateScramble()
