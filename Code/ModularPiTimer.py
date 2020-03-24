from Modules import Buttons, Cube, Timer

b = Buttons.Buttons('GPIO', [23, 5, 6, 13])
c = Cube.Cube('333')
s = 0 #screen object placeholder
timer = Timer.Timer(b, s, c)
for i in range(5):
    timer.solve(30, True)
print(timer.cube.timeList)
print(timer.cube.getAverageTime())