import tkinter as tk
class WindowWithContents:

    rootWindow = 0

    def __init__(self, r, f):
        print("2")
        self.rootWindow = r
        self.frameList = f

    def getRoot(self):
        return (self.rootWindow)


def makeWindowWithXFrames(amountOfFrames, width, height):
    newRoot = tk.Tk()
    newRoot.minsize(width, height)
    newRoot.maxsize(width, height)
    frameList = []
    for i in range(amountOfFrames):
        frameList.append(tk.Frame(newRoot))
    return (newRoot, frameList)