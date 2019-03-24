import tkinter as tk
class WindowWithContents:

    def __init__(self, r, f):
        self.rootWindow = r
        self.frameList = f

#Makes window with frames
def makeWindowWithXFrames(amountOfFrames, width, height):
    newRoot = tk.Tk()
    newRoot.minsize(width, height)
    newRoot.maxsize(width, height)
    frameList = []
    for i in range(amountOfFrames):
        frameList.append(tk.Frame(newRoot))
    return (newRoot, frameList)