import RPi.GPIO as GPIO
import threading
import time
import sys

DAT =13
CLK =8
#num =0
DAT2 =7
CLK2 =15
#num2 =0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK,GPIO.OUT)
GPIO.setup(CLK2,GPIO.OUT)

#Program Beban 1
#def weight():
while True:
	i=0
	num=0
	GPIO.setup(DAT,GPIO.OUT)
	GPIO.output(DAT,1)
	GPIO.output(CLK,0)
	GPIO.setup(DAT,GPIO.IN)

	while GPIO.input(DAT) == 1:
 		i=0
	for i in range(24):
		GPIO.output(CLK,1)
		num=num<<1

		GPIO.output(CLK,0)

		if GPIO.input(DAT) == 0:
			num=num+1

	GPIO.output(CLK,1)
	num=num^0x800000
	GPIO.output(CLK,0)
 	wei=0
	sigma=0
#	selisih=0
	for wei in range(20):
		wei=((num/837.658)-9997.8)
		sigma=sigma+wei
		time.sleep(0.01)
	hasil=(sigma/20)
#	print "Beban 1 = %d"%hasil,"g"

#Program Beban 2
#def weight2():
#	while True:
	j=0
	num2=0
	GPIO.setup(DAT2,GPIO.OUT)
       	GPIO.output(DAT2,1)
	GPIO.output(CLK2,0)
	GPIO.setup(DAT2,GPIO.IN)

	while GPIO.input(DAT2) == 1:
		j=0
	for j in range(24):
		GPIO.output(CLK2,1)
		num2=num2<<1

		GPIO.output(CLK2,0)
		if GPIO.input(DAT2)==0:
			num2=num2+1
	GPIO.output(CLK2,1)
	num2=num2^0x800000
	GPIO.output(CLK2,0)
	wei2=0
	sigma2=0
	for wei2 in range(20):
		wei2=((num2//849.12)-10008.8)
		sigma2=sigma2+wei2
		time.sleep(0.01)
	hasil2=sigma2/20
#	volume = hasil
#	print  "				Beban 2 = %d"%hasil2,"g"

	print "infus 1 = %d"%hasil,"g"		"infus 2 = %d"%hasil2, "g"
