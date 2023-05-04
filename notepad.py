from tkinter import *
from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = 'w', defaultextension=".txt")
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetypes = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)

canvas = tk.Tk()
canvas.geometry("500x700")
canvas.title("Notepad")
canvas.config(bg = "#000053")
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = tk.Button(canvas, text="Open", bg = "black", fg="white", command = openFile)
b1.pack(in_ = top, side=RIGHT)

b2 = tk.Button(canvas, text="Save", bg = "black", fg="white", command = saveFile)
b2.pack(in_ = top, side=RIGHT)

b3 = tk.Button(canvas, text="Exit", bg = "black", fg="white", command = exit)
b3.pack(in_ = top, side=RIGHT)

b4 = tk.Button(canvas, text="Clear", bg = "black", fg="white", command = clearFile)
b4.pack(in_ = top, side=RIGHT)


entry = Text(canvas, bg = "darkblue", font = ("arial", 20), fg="white")
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

canvas.mainloop()
