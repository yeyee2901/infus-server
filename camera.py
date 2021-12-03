#from tkinter import *
#from tkinter import messagebox
from picamera import PiCamera
#from datetime import datetime
from time import sleep, gmtime, strftime

#gui = Tk()
camera = PiCamera()
#output = ""#strftime("/home/pi/Pictures/image-%y-%d-%m %H:%M:%S.png", gmtime())
camera.start_preview(alpha=150)
#def take():
#global output
sleep(2)
output = strftime("/home/pi/Pictures/image-%y-%d-%m %H:%M:%S.jpg", gmtime())
camera.capture(output)
camera.stop_preview()
camera.close()
    
#photobutton = Button (gui, text = 'take photo', command=take)
#photobutton.place(x=10, y=10)
#########################################################################

#camera = PiCamera()
#camera.start_preview(alpha=190)
#for i in range (2):
#    sleep(3)
#    camera.capture('/home/pi/Pictures/Image%s.jpg' % i)
#camera.stop_preview()

#########################################################################

#camera = PiCamera()
#gui = Tk()
#now = datetime.now()

#filename = ''

#def photo():
#    global filename
#    filename = now.year,now.month,now.day,now.hour,now.minute,now.second #"{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.jpg"
#    camera.start_preview(alpha=190)
    #for i in range (5):
#    sleep(3)
#    camera.capture("/home/pi/Pictures/{0}.jpg".format(filename))
    #camera.stop_preview()

#def exitprogram():
 #   mExit = messagebox.askokcancel(title="Quit", message = "Are You Sure")
  #  if mExit > 0:
        #myGui.destroy()
   #     gui.quit()
        #camera.destroy()
    #    return

#photobutton = Button (gui, text = 'take photo', command=photo)
#photobutton.place(x=10, y=10)

#exitbutton = Button (gui, text = 'exit', command=exitprogram)
#exitbutton.place(x=10, y=40)
