import	RPi.GPIO as GPIO
import	threading 
import	time
DAT = 7
CLK = 15
num = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK,GPIO.OUT)
def weight():
	i=0
	num=0
	GPIO.setup(DAT,GPIO.OUT)
	GPIO.output(DAT,1)
	GPIO.output(CLK,0)
	GPIO.setup(DAT,GPIO.IN)

	while GPIO.input(DAT)==1:
		i=0
	for i in range(24):
		GPIO.output(CLK,1)
		num=num<<1

		GPIO.output(CLK,0)

		if GPIO.input(DAT)==0:
			num=num+1

	GPIO.output(CLK,1)
	num=num^0x800000
	GPIO.output(CLK,0)
	wei=0
#	wei=num
	wei=(num/835)
	print (-(wei-9996)), "g"
#	print wei, "g"
	time.sleep(3)

while (1):
	weight()
