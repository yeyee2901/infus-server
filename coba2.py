from tkinter import font
import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.LOW)
GPIO.setwarnings(False)

win = tk.Tk()

myFont = font.Font(family = 'Helvetica',size = 16, weight = 'bold')
font.families()

def ledON():
        print ("LED button pressed")
        if GPIO.input(40):
                GPIO.output(40,GPIO.LOW)
                ledButton["text"] = "LED ON"
        else:
                GPIO.output(40,GPIO.HIGH)
                ledButton["text"] = "LED OFF"

def exitProgram():
        print("Exit Button pressed")
        GPIO.cleanup()
        win.quit()
        
win.title("First GUI")
win.geometry('640x480')

exitButton = tk.Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = tk.BOTTOM)

ledButton = tk.Button(win, text = "LED ON", font = myFont, command = ledON, heigh = 2,width = 8)
ledButton.pack()

tk.mainloop()
