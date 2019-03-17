import datetime as dT
import time as rDT


def update():
    pass

def render():
    pass

previous = dT.datetime.now()
lag = 0
Frame60 = 0
lagtotal = 0
loops = 0
TimeFrame = dT.datetime.now()
while True:
    current = dT.datetime.now()
    elapsed = current - previous
    previous = current
    lag = lag + elapsed.microseconds
    while lag >= 16667: #frameskip
        update()
        lag = lag - 16667

    render()
    Frame60 = Frame60 + 1

    TimeDiff = dT.datetime.now() - TimeFrame
    if TimeDiff.seconds >= 1:
        TimeFrame = dT.datetime.now()
        print(Frame60)
        Frame60 = 0
    rDT.sleep(1/60 - lag/1000000)