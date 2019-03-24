import pygame as pyGame
import tkinter as tk
import pygame as pyGame
import MainLoop as mL
import WindowWithContents as wWC

def startGame(package):
    package.rootWindow.after(0, mL.MainLoop(package))


def playSound(package):
    #print(package.rootWindow.geometry().split("x")[0])
    #package.frameList.append(tk.Tk.frame(package.rootWindow, width=package.rootWindow.geometry().split("x")[0], height=))
    chillFrame = tk.Frame(package.rootWindow)
    chillFrame.configure(bg="yellow")
    chillFrame.pack(expand=True, fill='both')
    pyGame.mixer.init()
    pyGame.mixer.music.load("stuhlAudio.mp3")
    pyGame.mixer.music.play(-1)
    stopChilling = tk.Button(chillFrame, text="Not Anymore", command=lambda: (pyGame.mixer.music.stop(), chillFrame.destroy())).pack()

def mainMenu():



    WIDTH = 840
    HEIGHT = 600
    #Makes a tk.window containing 3 tk.frames
    FrameRoot = wWC.makeWindowWithXFrames(3, WIDTH, HEIGHT)
    package = wWC.WindowWithContents(FrameRoot[0], FrameRoot[1])

    package.frameList[0].place(x=0, y=0, anchor="nw", width=WIDTH/3 * 2, height=HEIGHT/2)
    package.frameList[0].configure(bg="black")
    package.frameList[1].place(x=0, y=HEIGHT/2, anchor="nw", width=WIDTH/3 * 2, height=HEIGHT/2)
    package.frameList[1].configure(bg="green")
    package.frameList[2].place(x=WIDTH/3 * 2, y=0, anchor="nw", width=WIDTH/3, height=HEIGHT)
    package.frameList[2].configure(bg="red")

    # textBox = tk.Label(package.frameList[2], text="welkom", fg="white", bg="grey")
    # textBox.pack()
    startButton = tk.Button(package.frameList[0], text="Start", command=lambda: (startAndRemove(package)))
    startButton.pack(expand=True, fill='both')
    destroyButton = tk.Button(package.frameList[1], text="Quit", command=package.rootWindow.destroy)
    destroyButton.pack(expand=True, fill='both')
    musicButton = tk.Button(package.frameList[2], text="Stûhl", command=lambda: playSound(package))
    musicButton.pack(expand=True, fill='both')

    def startAndRemove(p):
        startButton.destroy()
        destroyButton.destroy()
        musicButton.destroy()
        mL.MainLoop(package)

    package.rootWindow.mainloop()