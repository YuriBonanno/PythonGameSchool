import tkinter as tk
from tkinter import *

root = tk.Tk()
frame1 = tk.Frame(root, width=200, height=1000, background="bisque")
frame2 = tk.Frame(root, width=50, height = 50, background="#b22222")

frame1.pack(fill=None, expand=0)
frame2.place(relx=.5, rely=.5, anchor="c")

root.mainloop()