import gpiozero
import time

class Buttons:
    '''Creates an object that can be used to query button presses'''

    def __init__(self, inputType, pinout):

        self.inputType = inputType
        if (self.inputType == 'kb'):
            import keyboard;
            self.inputType = inputType

        else:
            self.inputType = 'GPIO'
            self.Hands = gpiozero.Button(pinout[0])

            self.LMenu = gpiozero.Button(pinout[1])
            self.CMenu = gpiozero.Button(pinout[2])
            self.RMenu = gpiozero.Button(pinout[3])


    # Are the below methods even necessary at this point?
    # They do nothing other than return gpiozero methods
    # that could just be called in the main script

    def isPressed(self):
        if ('GPIO' in self.inputType):
            return self.Hands.is_pressed
        else:
            return keyboard.isPressed('f+j')

    def isHeld(self):
        if ('GPIO' in self.inputType):
            return self.Hands.is_held
        else:
            return keyboard.isPressed('f+j')

    def waitUntilRelease(self):
        self.Hands.wait_for_release()
