import tkinter as tk
from tkinter import *

root = tk.Tk()
root.minsize(300, 400)
root.maxsize(300, 400)

frame1 = tk.Frame(root, width=200, height=200, background="black")
frame1.configure(height=frame1["height"],width=frame1["width"])
frame1.grid_propagate(0)
frame2 = tk.Frame(root, width=50, height=100, background="grey")

#frame1.pack(fill=None, expand=0)
#frame2.pack(fill=None, expand=0)
textBox = Label(frame1, text="big dick is in town", fg="white", bg="black")
frame1.grid(column=0, row=0)
frame2.grid(column=1, row=0)
textBox.grid()

print("something")

root.mainloop()

