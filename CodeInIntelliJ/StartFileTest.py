import tkinter as tk
import MainLoop as mL





if __name__ == '__main__':
    root = tk.Tk()
    WIDTH = 840
    HEIGHT = 600
    root.minsize(WIDTH, HEIGHT)
    root.maxsize(WIDTH, HEIGHT)
    frame1 = tk.Frame(root, width=round(WIDTH/3 * 2), height=round(HEIGHT/2), background="black")
    frame1.configure(height=frame1["height"], width=frame1["width"])
    frame1.grid_propagate(0)
    frame2 = tk.Frame(root, width= round(WIDTH/3), height=HEIGHT, background="grey")
    frame2.configure(height=frame1["height"], width=frame1["width"])
    frame2.grid_propagate(0)
    frame3 = tk.Frame(root, width=round(WIDTH/3 * 2), height=round(HEIGHT/2), background="grey")
    frame3.configure(height=frame1["height"], width=frame1["width"])
    frame3.grid_propagate(0)

    textBox = tk.Label(frame1, text="big dick is in town", fg="white", bg="black")

    frame1.grid(column=0, row=0)
    frame2.grid(column=1, row=0)
    frame3.grid(column=0, row=1)
    textBox.grid()

    startButton = tk.Button(frame2, text="start", command=mL.main)
    startButton.pack()
    print("something")

    root.mainloop()

