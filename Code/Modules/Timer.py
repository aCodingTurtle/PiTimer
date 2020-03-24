import time

class Timer:

    def __init__(self, buttons, screen, cube):
        self.buttons = buttons
        self.screen = screen
        self.cube = cube

    def setCube(self, cube):
        self.cube = cube

    def getScramble(self):
        return self.cube.scramble()

    def inspection(self, duration):
        startTime = time.time()
        currentTime = startTime
        endTime = startTime + duration
        
        penalty = False
        ready = False
        
        print("Inspection Started")
        
        while currentTime < endTime:
            if self.buttons.isPressed():
                if self.buttons.isHeld():
                  ready = True
                  print("Ready!")
            
            if self.buttons.isPressed() and ready:
                print("You can go!")
                self.buttons.waitUntilRelease()  # BUG: Infinite inspection due to blocking
                break
            
            if currentTime > endTime:
                penalty = True
            
            currentTime = time.time()
            print(endTime - currentTime)
            time.sleep(.1)
        else:
            print("Inspection timed out")
            self.buttons.waitUntilRelease()
    
    def timeSolve(self):
        startTime = time.time()
        stopTime = 0
        stopped = False
        
        while stopped == False:
            print(time.time() - startTime)
            
            if self.buttons.isPressed():
                stopTime = time.time()
                stopped = True
                self.buttons.waitUntilRelease()
            
            time.sleep(.1)
            
        return stopTime - startTime
    
    def solve(self, insp, save):
        scramble = self.getScramble()
        print(scramble)
        self.buttons.CMenu.wait_for_press()
        self.inspection(insp)
        time = self.timeSolve()
        
        if save:
            self.cube.addSolve(scramble, time)
    
