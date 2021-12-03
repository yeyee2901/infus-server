import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def  convertToBinaryData(filename):
	#convert data to binary format
	with open(filename, 'rb') as file:
		binaryData = file.read()
	return binaryData

def insertBLOB (bad_id, volume_infus_1, photo):
        print("Inserting BLOB into database")

        try:
                #pi_volume1 = volume_input1()
                #pi_volume2 = volume_input2()
                con = mysql.connector.connect(host = '192.168.137.146',
                                      database = 'testdb',
                                      user = 'pi',
                                      passwd = 'raspberry')

                cursor = con.cursor(prepared=True)
                sql_insert_blob_query = """ REPLACE INTO `Pengukuran`
                                (`id`, `volume_infus_1`, `photo`) VALUES (%s, %s, %s)"""

                #file = convertToBinaryData(volume)
                infusPicture = convertToBinaryData(photo)

                #convert data into tuple format
                insert_blob_tuple = (bad_id, volume_infus_1, infusPicture)

                result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
                con.commit()
                print ("Image and file inserted successfully as a BLOB into pengukuran table", result)

        except mysql.connector.Error as error:
                con.rollback()
                print("Falied inserting BLOB data into MySQL table {}".format(error))

        finally:
                #closing database connection
                if (con.is_connected()):
                        cursor.close()
                        con.close()
                        print("MySQL connection is closed")

def insertdata (bad_id, volume_infus_2):
        try:
                #pi_volume1 = volume_input1()
                #pi_volume2 = volume_input2()
                con = mysql.connector.connect(host = '192.168.137.146',
                                      database = 'testdb',
                                      user = 'pi',
                                      passwd = 'raspberry')

                cursor = con.cursor()
                sql_insert = """ REPLACE INTO `Pengukuran`
                                (`id`,volume_infus_2`) VALUES(%s,%s)"""

                cursor.execute(sql_insert)
                con.commit()
                print ("Image and file inserted successfully as a BLOB into pengukuran table")

        except mysql.connector.Error as error:
                con.rollback()
                print("Falied inserting BLOB data into MySQL table {}".format(error))

        finally:
                #closing database connection
                if (con.is_connected()):
                        cursor.close()
                        con.close()
                        print("MySQL connection is closed")

insertBLOB("Bed 1", "500 mL", "/home/pi/Pictures/Image_Bed1.jpg")
insertdata("Bed 1","50 mL")
