from tkinter import *
from tkinter import messagebox
from picamera import PiCamera
#from datetime import datetime
import sys
import RPi.GPIO as GPIO
import threading
from time import sleep, gmtime, strftime

#Pin GPIO Beban 1
DAT1 =37
CLK1 =35

DAT2 =40 #Beban 2
CLK2 =38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK1,GPIO.OUT)
GPIO.setup(CLK2,GPIO.OUT)

def Baca_Volume1():
	#baca port GPIO HX711 1
	i=0
	num1=0
	GPIO.setup(DAT1,GPIO.OUT)
	GPIO.output(DAT1,1)
	GPIO.output(CLK1,0)
	GPIO.setup(DAT1,GPIO.IN)

	#Konversi ADC Load Cell 1
	while GPIO.input(DAT1) == 1:
		i=0
	for i in range(24):
		GPIO.output(CLK1,1)
		num1=num1<<1

		GPIO.output(CLK1,0)
		if GPIO.input(DAT1) == 0:
			num1=num1+1

	GPIO.output(CLK1,1)
	num1=num1^0x800000
	GPIO.output(CLK1,0)
	sigma_berat1=0
	for berat1 in range (10):
		berat1=((num1/830.5)-10000)
		sigma_berat1=sigma_berat1+berat1
	volume1=(sigma_berat1//(10*0.997))
	return volume1

def Baca_Volume2():
	#baca port GPIO HX711 2
	j=0
	num2=0
	GPIO.setup(DAT2,GPIO.OUT)
	GPIO.output(DAT2,1)
	GPIO.output(CLK2,0)
	GPIO.setup(DAT2,GPIO.IN)

	#Konversi ADC Load Cell 2
	while GPIO.input(DAT2) == 1:
		j=0
	for i in range (24):
		GPIO.output(CLK2,1)
		num2=num2<<1

		GPIO.output(CLK2,0)
		if GPIO.input(DAT2) == 0:
			num2=num2+1

	GPIO.output(CLK2,1)
	num2=num2^0x800000
	GPIO.output(CLK2,0)
	sigma_berat2=0
	for berat2 in range (10):
		berat2=((num2/842.6)-10000)
		sigma_berat2=sigma_berat2+berat2
	volume2=(sigma_berat2//(10*0.997))
	return volume2

def selisih():
        a = var1.get() #mendapatkan nilai awal
        b = var2.get()
        selisih1=Baca_Volume1()-a #mendapatkan berat botol
        selisih2=Baca_Volume2()-b
        print ("Selisih 1= {:.2f}".format(selisih1),"		Selisih 2= {:.2f}".format(selisih2))


        def volume_input1():
                volume_infus1=Baca_Volume1()-selisih1
                if volume_infus1==450 or volume_infus1==400 or volume_infus1==350 or volume_infus1==300 or volume_infus1==250 or volume_infus1==200 or volume_infus1==150 or volume_infus1== 100 or volume_infus1==50:
                        print ("kamera bekerja %d" %volume_infus1)
                        camera = PiCamera()
                        camera.start_preview(alpha=190)
                        output = strftime("/home/pi/Pictures/image-%y-%d-%m %H:%M:%S.jpg", gmtime())
                        sleep (2)
                        camera.capture(output)
                        camera.stop_preview()
                        camera.close()
                if volume_infus1==10:
                        print ("kamera bekerja %d " %volume_infus1, "dan pinch valve bekerja")
                        camera = PiCamera()
                        camera.start_preview(alpha=190)
                        output = strftime("/home/pi/Pictures/image-%y-%d-%m %H:%M:%S.jpg", gmtime())
                        sleep (2)
                        camera.capture(output)
                        camera.stop_preview()
                        camera.close()
                hasil1.configure(text=volume_infus1)
                #hasil1.after(1000, volume_input1)
                return volume_infus1
                
        def volume_input2():
                volume_infus2=Baca_Volume2()-selisih2
                hasil2.configure(text=volume_infus2)
                #hasil2.after(1000, volume_input2)
                return volume_infus2

        hasil1 = Label(myGui, font=('arial',36,'bold'))
        hasil1.place(x=50, y=150)
        volume_input1()
        
        hasil2 = Label(myGui, font=('arial',36,'bold'))
        hasil2.place(x=250, y=150)
        volume_input2()

def exitprogram():
    mExit = messagebox.askokcancel(title="Quit", message = "Are You Sure")
    if mExit > 0:
        myGui.destroy()
        exit()
        return

myGui = Tk()
var1 = IntVar()
var2 = IntVar()

myGui.geometry('400x300')
myGui.title('Timbangan infus Digital')
 
infus1_label = Label(myGui, text='Infus 1').place(x = 50, y = 10) #bisa tambah warna font(fg) dan background(bg)
infus2_label = Label(myGui, text='Infus 2').place(x = 250, y = 10)

volume1_0 = Radiobutton (myGui, text = "0 mL", value=0, variable = var1).place(x=50, y=30)
volume1_100 = Radiobutton (myGui, text = "100 mL", value=100, variable = var1).place(x=50, y=50)
volume1_500 = Radiobutton (myGui, text = "500 mL", value=500, variable = var1).place(x=50, y=70)
volume1_1000 = Radiobutton (myGui, text = "1000 mL", value=1000, variable = var1).place(x=50, y=90)
volume2_0 = Radiobutton (myGui, text = "0 mL", value=0, variable = var2).place(x=250, y=30)
volume2_100 = Radiobutton (myGui, text = "100 mL", value=100, variable = var2).place(x=250, y=50)
volume2_500 = Radiobutton (myGui, text = "500 mL", value=500, variable = var2).place(x=250, y=70)
volume2_1000 = Radiobutton (myGui, text = "1000 mL", value=1000,variable = var2).place(x=250, y=90)

okbutton = Button (myGui, text = 'OK', command=selisih).place(x = 170, y = 110)

exitbutton = Button (myGui, text = 'Stop', command = exitprogram, bg='powder blue').place(x = 170, y = 250)

if __name__ =='__main__':
        mainloop()
