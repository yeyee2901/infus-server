import tkinter as tk
import time

top = tk.Tk()

def addText():
    oldText = L.cget("text")
    newText = oldText + '\nfirst change'
    L.configure(text=newText)

    top.update_idletasks()
    time.sleep(2)

    newText += '\nsecond change'
    L.configure(text=newText)

B = tk.Button(top, text = "Change text", command = addText)
L = tk.Label(top,text='original text')

B.pack()
L.pack()
top.mainloop()
