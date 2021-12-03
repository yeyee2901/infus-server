import pymysql

db = pymysqlconnect(
	host = "192.168.137.75",user = "pi",passwd = "", database)

if db.is_connected():
	print ("Berhasil terhubung ke database")
