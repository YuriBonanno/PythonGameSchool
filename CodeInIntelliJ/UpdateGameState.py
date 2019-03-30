import MainMenu as mainMenu
import tkinter as tk

def makeAGameState(gamestate):
    chosen = False
    pass

def generateGameState(package, gameState):
    gameState = makeAGameState(gameState)
    returnButton = tk.Button(package.frameList[0],
                             text="Return",
                             command=lambda: (returnButton.destroy(),
                                              mainMenu.menuScreen(package)))
    returnButton.pack()
    return gameState

def gameSequence(p, g):
    if g == 0:
        generateGameState(p, g)