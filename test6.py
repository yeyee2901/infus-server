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
sigma=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK,GPIO.OUT)
GPIO.setup(CLK2,GPIO.OUT)

nilaiawal = input ("Volume infus 1: ")
nilaiawal2 = input ("Volume infus 2: ")
sigma_volume=0
sigma_volume2=0
while True:
#program infus 1
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

	sigma_wei=0
	for wei in range (20):
		wei=((num//843.2)-9999.5) #wei=berat
		sigma_wei=sigma_wei+wei
	volume=(sigma_wei/(20*0.997)) #konversi ke volume
##	print "volume 1= {:.2f}".format(volume)
	sigma_volume=volume-sigma_volume
	if (sigma_volume<=0):
		pengurang=2*sigma_volume
##		print "pengurang 1= {:.2f}".format(pengurang)
		hasil=nilaiawal+pengurang
		print "Infus 1= {:.2f}".format(hasil)
#	hasil=nilaiawal-sigma_volume
#	if(sigma_volume>0):
#		selisih=
#	if (sigma_volume<0)
#	print "Infus 1 {:.2f}".format(volume), "ml"
#	volume=nilaiawal+sigma
#	hasil=wei-sigma
#	print "		hasil %d"%hasil
#	if (sigma<0):
#		hasil=wei-sigma
#		print "hasil %d"%hasil
#		volume=nilaiawal+hasil
#		if (volume<(nilaiawal+5)):
#		volume=nilaiawal+hasil
#			print "		infus 1 %d"%volume
#	time.sleep(0.1)
#Program infus 2
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

	sigma_wei2=0
	for wei2 in range (20):
		wei2=((num2//831.1)-9998.5)
		sigma_wei2=sigma_wei2+wei2
	volume2=(sigma_wei2/(20*0.997))
##	print "				volume 2= {:.2f}".format(volume2)
	sigma_volume2=volume2-sigma_volume2
##	print "				sigma 2 = {:.2f}".format(sigma_volume2)
	if (sigma_volume<=0):
		pengurang2=2*sigma_volume2
##		print "				pengurang 2= {:.2f}".format(pengurang2)
		hasil2=nilaiawal2+pengurang2
		print "				Infus 2= {:.2f}".format(hasil2)
	time.sleep(0.5)
#	volume = hasil
#	print  "				Infus 2 = {:.2f}".format(volume2), "ml"

#	print "infus 1 = {:.2f}".format(sigma_volume), "ml			infus 2 = {:.2f}".format(volume2), "ml"
#	print "						infus 2 = {:.2f}".format(volume2),"ml"
