import datetime as dT
import time as rDT
import UpdateGameState as uGS

class MainLoop:

    def render(self, p, g):
        pass

    def __init__(self, package):
        previous = dT.datetime.now()
        lag = 0
        Frame60 = 0
        TimeFrame = dT.datetime.now()
        gameState = 0
        while True:
            current = dT.datetime.now()
            elapsed = current - previous
            previous = current
            lag = lag + elapsed.microseconds
            while lag >= 16667: #frameskip
                gameState = uGS.gameSequence(package, gameState)
                lag = lag - 16667
            self.render(package, gameState)
            package.rootWindow.update_idletasks()
            package.rootWindow.update()
            Frame60 = Frame60 + 1


            TimeDiff = dT.datetime.now() - TimeFrame
            if TimeDiff.seconds >= 1:
                TimeFrame = dT.datetime.now()
                print(Frame60)
                Frame60 = 0
            rDT.sleep(1/60 - lag/1000000)