import time

timeLists = []
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
    timeLists.append(finishTime)

timer(5)
