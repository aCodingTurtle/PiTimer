# # # # # # # # # # # # # # # # # # # # # #
#
#  PiTimer: A Python Cube Timer for the RPi
#
#

import random
import time
import tkinter as tk
import cubeTurns

class Scramble:
    'Creates a Scramble and Solve Time for 3x3 or 2x2'

    def __init__(self, cube):
      if 1 < cube < 4:
        self.cube = cube

    def generateScramble(self):

      scramble = ""

      #Set Scramble Length
      if self.cube == 2:
        scrambleSize = 10
      elif self.cube == 3:
        scrambleSize = 15

      lastMove = "B"
      lastMod = "'"

      for m in range(scrambleSize):
        move = random.choice(cubeTurns.x2)
        mod = random.choice(cubeTurns.modifiers)

        #Check for Repeat
        if move == lastMove:
          move = random.choice(cubeTurns.x2)
          if mod == lastMod:
            mod = random.choice(cubeTurns.modifiers)

        #Print Move
        scramble = scramble + str(move) + str(mod) + " "

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


class Session:
    'Creates a session of a few solves and then gives stats'

    def __init__(self, solveNums):
      self.solveNums = solveNums
      #Gets the number of solves in session

    #def newSolve():
      #New solve class

    #def printSession():




#generates a test scramble and prints
scramble2 = Scramble(3)
scramble2.generateScramble()

# -- Tk Program Starts Here -- #
BOXX = 1200
BOXY = 700
BOXGEO = str(BOXX) + 'x' + str(BOXY)

window = tk.Tk()
window.geometry('1200x700')

titleBar = tk.Label(window, text="PiTimer", fg="orange", bg="white", font = "Courier 14")
titleBar.grid(column=3, row=2)

#  Menu Bar  #
menu = tk.Menu(window)

scrambleMenu = tk.Menu(menu)
scrambleMenu.add_command(label="New Scramble")
menu.add_cascade(label="Scramble", menu=scrambleMenu)

sessionMenu = tk.Menu(menu)
sessionMenu.add_command(label="New Session")
menu.add_cascade(label="Session", menu=sessionMenu)

window.config(menu=menu)

#  Scramble Bar  #
scrambleDisp = tk.Label(window,
                        text=scramble2.generateScramble(),
                        fg="orange",
                        bg="white",
                        font="Courier 16 bold")
scrambleDisp.grid(column=0, columnspan=3, pady=5, row=0)

#  Timer  #
timer = tk.Message(window,
                   text="00 : 00 : 0",
                   fg="black",
                   bg="white",
                   font = "Courier 48")
timer.grid(column=0, columnspan=3, row=1)

#  Stats Bar  #
stats = tk.Message(window,
                   text="Stats for a sesson will appear here.",
                   fg="grey",
                   bg="white",
                   font="Courier 16 italic",
                   relief="sunken")
stats.grid(column=0, columnspan=2, row=2)

window.mainloop()
