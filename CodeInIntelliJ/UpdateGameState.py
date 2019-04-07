import MainMenu as mainMenu
import tkinter as tk
import Student as Student
import GameState as gSC

def makeAGameState(package, gamestate):
    gamestate = gSC.GameState()
    pressed = False
    def pressedTrue():
        pressed = True
    package.frameList.append(tk.Frame(package.rootWindow, bg="blue").pack(expand=True, fill='both'))
    student1Checked = tk.IntVar()
    student2Checked = tk.IntVar()
    student3Checked = tk.IntVar()
    student3Checked = 1
    student1 = Student.Student()
    student2 = Student.Student()
    student3 = Student.Student()
    tk.Checkbutton(package.frameList[3], text=student1.fullName, variable=student1Checked).pack()
    tk.Checkbutton(package.frameList[3], text=student2.fullName, variable=student2Checked).pack()
    tk.Checkbutton(package.frameList[3], text=student3.fullName, variable=student3Checked).pack()
    tempButton = tk.Button(package.frameList[3], text="finish", command=lambda: pressedTrue())
    tempButton.pack()
    # while pressed == False:
    #     tempButton(command=lambda: pressedTrue())
    # package.rootWindow.update_idletasks()
    # package.rootWindow.update()
    # if (student1Checked == 1):
    #     gamestate.studentList.append(student1)
    # else:
    #     gamestate.notYourStudentsList.append(student1)
    # if (student2Checked == 1):
    #     gamestate.studentList.append(student2)
    # else:
    #     gamestate.notYourStudentsList.append(student2)
    # if (student3Checked == 1):
    #     gamestate.studentList.append(student3)
    # else:
    #     gamestate.notYourStudentsList.append(student3)
    gamestate.started = True
    return package, gamestate

def generateGameState(package, gameState):
    gameState = makeAGameState(package, gameState)
    returnButton = tk.Button(package.frameList[0],
                             text="Return",
                             command=lambda: (returnButton.destroy(),
                                              mainMenu.menuScreen(package)))
    returnButton.pack()
    return package, gameState

def gameSequence(p, g):
    if g == 0:
       p, g = generateGameState(p, g)

    print(g.studentList)