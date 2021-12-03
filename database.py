import pymysql

mydb = pymysql.connect(
	host = '192.168.137.192',
	#port = 3306,
	user = 'pi',
	passwd = 'raspberry',
	database = 'testdb')
#	database="test")

cursor = mydb.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

print ("Database Version : %s " % data)

mydb.close()

#if db.is_connected():
#	print ("Berhasil terhubung ke database")
