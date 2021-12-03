import RPi.GPIO as GPIO
import threading
import time
import sys

#Pin GPIO Beban 1
DAT1 =7
CLK1 =5

DAT2 =16 #Beban 2
CLK2 =12

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
		berat1=((num1/843.2)-9999.5)
		sigma_berat1=sigma_berat1+berat1
	volume1=(sigma_berat1/(10*0.997))
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
		berat2=((num2/831.1)-9998.5)
		sigma_berat2=sigma_berat2+berat2
	volume2=(sigma_berat2/(10*0.997))
	return volume2

#input volume awal infus
nilai_awal1 = input ("Volume Infus 1: ")
nilai_awal2 = input ("Volume Infus 2: ")

selisih1=Baca_Volume1()-nilai_awal1
selisih2=Baca_Volume2()-nilai_awal2
print "Selisih 1= {:.2f}".format(selisih1),"		Selisih 2= {:.2f}".format(selisih2)

while True:
	volume_infus1=Baca_Volume1()-selisih1
	volume_infus2=Baca_Volume2()-selisih2
	print "Volume 1= {:.2f}".format(volume_infus1),"		Volume 2= {:.2f}".format(volume_infus2),"ml"
	time.sleep(1)
