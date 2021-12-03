import RPi.GPIO as GPIO
import threading
import time
import sys

DAT =37
CLK =35
#num =0
DAT2 =40
CLK2 =38
#num2 =0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK,GPIO.OUT)
GPIO.setup(CLK2,GPIO.OUT)

#Program Beban 1
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
# 	hasil=num
#	time.sleep(0.01)
	sigma=0
	for wei in range(20):
		wei=((num/830.0)-10000)
		sigma=sigma+wei
		time.sleep(0.01)
	hasil=(sigma/20)

#Program Beban 2
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
#	hasil2=num2
#	time.sleep(0.01)
	sigma2=0
	for wei2 in range(20):
		wei2=((num2/842.6)-10000)
		sigma2=sigma2+wei2
		time.sleep(0.01)
	hasil2=sigma2/20
	print "Beban 1 = %d"%hasil,"g			Beban 2 = %d"%hasil2,"g"
#	print "Beban 1 = %f"%hasil, "g			Beban 2 = %f"%hasil2, "g"
