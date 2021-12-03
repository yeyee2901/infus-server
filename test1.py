from tkinter import *                           #panggil semua library GUI tkinter
from tkinter import messagebox                  #kasus khusus messagebox harus dipanggil tersendiri 
from picamera import PiCamera                   #panggil library raspberry kamera
from mysql.connector import Error               #library mengetahui error pada mysql
from mysql.connector import errorcode           #library koreksi error
import mysql.connector                          #library mysql untuk koneksi ke server
import sys                                      #library sistem raspberry pi
import subprocess 
import RPi.GPIO as GPIO                         #library untuk python dapat akses pin GPIO rasperry pi 
from time import sleep                          #library untuk akses waktu: jam dan delay

DAT1= 37                                        #Pin GPIO Beban 1: 37 pin data, 35 pin clock
CLK1= 35

DAT2= 40                                        #Pin GPIO Beban 2: 40 pin data, 38 pin clock
CLK2= 38

RELAY1= 32                                      #Pin GPIO Relay: 32 infus 1 31 infus 2
RELAY2= 31

########## KALIBRASI ##########
SPAN1 = 830.0                                   #untuk kalibrasi nilai span load cell 1
SPAN2 = 842.0                                   #ni                                                                                                                            lai span load cell 2
ZERO1 = 10000                                   #nilai zero load cell 1
ZERO2 = 10000                                   #nilai zero load cell 2
MASAJENIS_INFUS = 0.997                         #masa jenis cairan

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)                        #set pin GPIO berdasarkan no pada board
GPIO.setup(CLK1,GPIO.OUT)                       #set pin CLK1 sebagai output
GPIO.setup(CLK2,GPIO.OUT)                       #set pin CLK2 sebagai output
GPIO.setup(RELAY1,GPIO.OUT)                     #set pin RELAY1 sebagai output
GPIO.setup(RELAY2,GPIO.OUT)                     #set pin RELAY2 sebagai output
GPIO.output(RELAY1,1)                           #niali awal RELAY1 agar saat pertama kali dihidupkan relay off
GPIO.output(RELAY2,1)                           #nilai awal RELAY2

def Baca_Volume1():                                     #ambil data load cell nomor 1
	#baca port GPIO HX711 1
	i=0
	num1=0
	GPIO.setup(DAT1,GPIO.OUT)                       #set port clock data output
	GPIO.output(DAT1,1)
	GPIO.output(CLK1,0)
	GPIO.setup(DAT1,GPIO.IN)                        #kembalikan ke input untuk baca data

	#Konversi ADC Load Cell 1
	while GPIO.input(DAT1) == 1:                    #tunggu data
		i=0
	for i in range(24):                             #ambil data ADC 24 bit
		GPIO.output(CLK1,1)
		num1=num1<<1

		GPIO.output(CLK1,0)
		if GPIO.input(DAT1) == 0:
			num1=num1+1                     #akhir pengambilan data

	GPIO.output(CLK1,1)
	num1=num1^0x800000                              #masking data
	GPIO.output(CLK1,0)                             #berhentikan data
	sigma_berat1=0                                  #nilai awal rata-rata
	for berat1 in range (10):                       #10 data di rata-rata
		berat1=((num1/SPAN1)-ZERO1)
		sigma_berat1=sigma_berat1+berat1
	volume1=(sigma_berat1//(10*MASAJENIS_INFUS))    #berat jadi volume dengan berat jenis
	return volume1

def Baca_Volume2():                                     #ambil data load cell nomor 2
	#baca port GPIO HX711 2
	j=0
	num2=0
	GPIO.setup(DAT2,GPIO.OUT)                       #set port clock data output
	GPIO.output(DAT2,1)
	GPIO.output(CLK2,0)
	GPIO.setup(DAT2,GPIO.IN)                        #kembalikan ke input untuk baca data

	#Konversi ADC Load Cell 2
	while GPIO.input(DAT2) == 1:                    #tunggu data
		j=0
	for i in range (24):                            #ambil data ADC 24 bit
		GPIO.output(CLK2,1)
		num2=num2<<1

		GPIO.output(CLK2,0)
		if GPIO.input(DAT2) == 0:
			num2=num2+1                     #akhir pengambilan data

	GPIO.output(CLK2,1)
	num2=num2^0x800000                              #masking data
	GPIO.output(CLK2,0)                             #berhentikan data
	sigma_berat2=0                                  #nilai awal rata-rata
	for berat2 in range (10):                       #10 data di rata-rata
		berat2=((num2/SPAN2)-ZERO2)
		sigma_berat2=sigma_berat2+berat2
	volume2=(sigma_berat2//(10*MASAJENIS_INFUS))    #berat jadi volume dengan berat jenis
	return volume2

def second_window():
        new_window = Toplevel(myGui)
        new_window.geometry ('480x320')
        new_window.title('Monitoring Infus Digital')
        a = var1.get()                                  #mengambil nilai awal 1
        b = var2.get()                                  #mengambil nilai awal 2
        selisih1=Baca_Volume1()-a                       #mendapatkan berat botol 1
        selisih2=Baca_Volume2()-b                       #mendapatkan berat botol 2
        print ("Selisih 1= {:.2f}".format(selisih1),"		Selisih 2= {:.2f}".format(selisih2))
        def show(vol1, vol2, out1, out2, jam1, jam2, menit1, menit2):
                def hitung():
                        volume_infus1= int (Baca_Volume1()-selisih1)    #volume yang terbaca infus 1
                        vol1.configure(text=volume_infus1)              #agar volume infus 1 terbaca lagi

                        volume_infus2= int (Baca_Volume2()-selisih2)    #volume yang terbaca infus 2
                        vol2.configure(text=volume_infus2)              #agar volume infus 2 terbaca lagi

                        volume_keluar1= int (a-volume_infus1)           #volume infus 1 yang keluar
                        out1.configure(text=volume_keluar1)             #volume infus 1 ditampilkan kembali

                        volume_keluar2= int (b-volume_infus2)           #volume infus 2 yang keluar
                        out2.configure(text=volume_keluar2)             #volume infus 2 ditampilkan kembali

                        jam_infus1 = int (volume_infus1//60)            #perhitungan lama infus 1 habis dalam jam
                        jam1.configure(text=jam_infus1)                 #menapilkan perubahan jam infus 1

                        jam_infus2 = int (volume_infus2//60)            #perhitungan lama infus 2 habis dalam jam
                        jam2.configure(text=jam_infus2)                 #menapilkan perubahan jam infus 2

                        menit_infus1 = int (volume_infus1 % 60)         #perhitungan lama infus 1 habis dalam menit
                        menit1.configure(text=menit_infus1)             #menampilkan perubahan jam infus 1
                        
                        menit_infus2 = int (volume_infus2 % 60)         #perhitungan lama infus 2 habis dalam menit
                        menit2.configure(text=menit_infus2)             #menampilkan perubahan jam infus 2

                        if volume_infus1 % 50 == 0:
                                subprocess.call(['/home/pi/my_python/capture.sh'])

                        if volume_infus1 < 15 and volume_infus1 > 4:
                                GPIO.output(RELAY1,0)
                                subprocess.call(['/home/pi/my_python/capture.sh'])
                        #else:
                        #        GPIO.output(RELAY1,1)

                        if volume_infus2 < 15 and volume_infus2 > 4:
                                GPIO.output(RELAY2,0)
                                subprocess.call(['/home/pi/my_python/capture.sh'])
                        #else:
                         #       GPIO.output(RELAY2,1)

                        volume_infus_1 = str (volume_infus1)            #ubah variabe volume 1 ke string sebelum dikiram 
                        volume_infus_2 = str (volume_infus2)            #ubah variabe volume 1 ke string sebelum dikiram 
                        insertBLOB("1",volume_infus_1, volume_infus_2, "/home/pi/Pictures/Image_Bed1.jpg") #insert niali pengukuran ke data base

                        vol1.after(1000, hitung)                        #delay looping data
                hitung()                                                #panggil program

        def exitprogram():
                mExit = messagebox.askokcancel(title="Quit", message = "Are You Sure") #messagebox sebelum menghentikan program
                if mExit > 0:
                        GPIO.cleanup()                                  #nilai semua pin GPIO kembali ke nilai awal
                        new_window.destroy()                            #mematikan window/tampilan ke dua
                        myGui.destroy()                                 #mematikan window/tampilan pertama
                        exit()                                          #menonaktifkan pytho shel
                        return

        infus1_label = Label(new_window, text='Infus 1',font=('arial',12)).place(x = 70, y = 0)                 #label infus 1 pada window kedua 
        infus2_label = Label(new_window, text='Infus 2',font=('arial',12)).place(x = 320, y = 0)                #label infus 2 pada window kedua 
        sisa_label = Label(new_window, text ='Sisa Volume:', font=('arial',12)).place(x = 10, y = 20)           #label volume infus yang tersisa pada window kedua
        volume_keluar = Label(new_window, text='Volume Keluar:', font=('arial',12)).place(x = 10, y = 90)       #label volume yang telah keluar pada window pertama
        waktu_habis = Label(new_window, text='Habis dalam waktu:', font=('arial',12)).place(x = 10, y = 160)    #label waktu habis
        jam1_label = Label(new_window, text='jam', font=('arial',14,'bold')).place(x = 47, y = 195)             #label jam pada infus 1
        jam2_label = Label(new_window, text='jam', font=('arial',14,'bold')).place(x = 332, y = 195)            #label jam pada infus 2
        menit1_label = Label(new_window, text='menit', font=('arial',14,'bold')).place(x = 135, y = 195)        #label menit pada infus 1
        menit2_label = Label(new_window, text='menit', font=('arial',14,'bold')).place(x = 420, y = 195)        #label menit pada infus 2

        lvol1 = Label(new_window, font=('aral',36,'bold'))                      #menampilkan nilai volume terukur pada infus 1
        lvol1.place(x=70,y=37)
        
        lvol2 = Label(new_window, font=('aral',36,'bold'))                      #menampilkan nilai volume terukur pada infus 2
        lvol2.place(x=320,y=37)
        
        lout1 = Label(new_window, font=('aral',36,'bold'))                      #menampilkan nilai volume keluar pada infus 1
        lout1.place(x=70,y=107)
        
        lout2 = Label(new_window, font=('aral',36,'bold'))                      #menampilkan nilai volume keluar pada infus 2
        lout2.place(x=320,y=107)
        
        ljam1 = Label(new_window, font=('aral',26,'bold'))                      #menampilkan lama cairan infus 1 akan habis dalam jam 
        ljam1.place(x=20,y=180)

        ljam2 = Label(new_window, font=('aral',26,'bold'))                      #menampilkan lama cairan infus 2 akan habis dalam jam
        ljam2.place(x=305,y=180)
        
        lmenit1 = Label(new_window, font=('aral',26,'bold'))                    #menampilkan lama cairan infus 1 akan habis dalam menit
        lmenit1.place(x=85,y=180)

        lmenit2 = Label(new_window, font=('aral',26,'bold'))                    #menampilkan lama cairan infus 2 akan habis dalam menit
        lmenit2.place(x=370,y=180)
 
        show(lvol1, lvol2, lout1, lout2, ljam1, ljam2, lmenit1, lmenit2)        #panggil fungsi show dan meletakkan hasilnya dalam label
        
        exitbutton = Button (new_window, text = 'Stop', command = exitprogram, bg='Red').place(x = 210, y = 220)        #tombol exit: menjalankan fungsi exitprogram()
        new_window.mainloop()

def convertToBinaryData(filename):
	with open(filename, 'rb') as file:                                                      #koversi data ke data biner 
		binaryData = file.read()
	return binaryData

def insertBLOB (bad_id, volume_infus_1, volume_infus_2, photo):
        print("Inserting BLOB into database")
        try:
                con = mysql.connector.connect(host = '192.168.1.8',                             #hostname server
                                      database = 'testdb',                                      #nama tabel database
                                      user = 'pi',
                                      passwd = 'raspberry')

                cursor = con.cursor(prepared=True)
                sql_insert_blob_query = """ REPLACE INTO `Pengukuran`
                                (`id`, `volume_infus_1`, `volume_infus_2`, `photo`) VALUES (%s, %s, %s, %s)"""

                infusPicture = convertToBinaryData(photo)                                       #file = convertToBinaryData(volume)
                insert_blob_tuple = (bad_id, volume_infus_1, volume_infus_2, infusPicture)      #convert data into tuple format

                result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
                con.commit()
                print ("Image and file inserted successfully as a BLOB into pengukuran table", result)

        except mysql.connector.Error as error:                                                  #cek error pengiriman data
                con.rollback()
                print("Falied inserting BLOB data into MySQL table {}".format(error))

        finally:
                if (con.is_connected()):                                                        #tutup koneksi ke database
                        cursor.close()
                        con.close()
                        print("MySQL connection is closed")

myGui = Tk()                            #nama GUI window 1
var1 = IntVar()                         #ubah value pada label input menjadi variabel integer 'infus 1'
var2 = IntVar()                         #ubah value pada label input menjadi variabel integer 'infus 2'

myGui.geometry('480x320')               #ukuran window pertama
myGui.title('Monitoring infus Digital') #title window pertama
 
infus1_label = Label(myGui, text='Infus 1',font=('arial',16,'bold')).place(x = 50, y = 10)      #label infus 1 pada window pertama 
infus2_label = Label(myGui, text='Infus 2',font=('arial',16,'bold')).place(x = 300, y = 10)     #label onfus 2 pada window kedua

volume1_0 = Radiobutton (myGui, text = "0 mL", value=0, variable = var1,font=('arial',22,'bold')).place(x=30, y=40)             #radio button in 0 mL infus 1
volume1_100 = Radiobutton (myGui, text = "100 mL", value=100, variable = var1,font= ('arial',22,'bold')).place(x=30, y=80)      #radio button in 100 mL infus 1
volume1_500 = Radiobutton (myGui, text = "500 mL", value=500, variable = var1,font= ('arial',22,'bold')).place(x=30, y=120)      #radio button in 500 mL infus 1
volume1_540 = Radiobutton (myGui, text = "540 mL", value=540, variable = var1,font= ('arial',22,'bold')).place(x=30, y=160)      #radio button in 540 mL infus 1
volume2_0 = Radiobutton (myGui, text = "0 mL", value=0, variable = var2,font=('arial',22,'bold')).place(x=280, y=40)            #radio button in 0 mL infus 2
volume2_100 = Radiobutton (myGui, text = "100 mL", value=100, variable = var2,font=('arial',22,'bold')).place(x=280, y=80)      #radio button in 100 mL infus 2
volume2_500 = Radiobutton (myGui, text = "500 mL", value=500, variable = var2,font=('arial',22,'bold')).place(x=280, y=120)      #radio button in 500 mL infus 2
volume2_540 = Radiobutton (myGui, text = "540 mL", value=540,variable = var2,font=('arial',22,'bold')).place(x=280, y=160)       #radio button in 540 mL infus 2

okbutton = Button (myGui, text = 'OK', command=second_window, bg='powder blue').place(x = 210, y = 220)           #ok button memanggil fungsi second_window

if __name__ =='__main__':
        mainloop()
