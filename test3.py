import sys
import RPi.GPIO as GPIO
import threading
from time import sleep, gmtime, strftime

DAT2 =40 #Beban 2
CLK2 =38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK2,GPIO.OUT)

nilai_awal2 = input ("Volume Infus 2: ")
def volume():
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
                print ("        sigma = {:.2f}".format(sigma_berat2))
                sleep(0.5)
        volume2=(sigma_berat2//(10*0.997))
        return volume2

selisih2=volume()-nilai_awal2
while True:
        print ("selisih = {:.2f}".format(selisih2))
        volume_infus2=volume()-selisih2
        print ("Volume 1= {:.2f}".format(volume_infus2))

