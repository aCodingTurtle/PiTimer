import requests
import time

class Cube:
    '''Creates a Cube object that contains all solves and times for a cube.'''

    def __init__(self, cubeType):
        self.cubeType = cubeType
        self.timeList = []

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

    def addSolve(self, scramble, time):
        self.timeList.append([scramble, time])
        
    def getAverageTime(self):
        total = 0
        for i in self.timeList:
            total += i[1]
        return total / len(self.timeList)

