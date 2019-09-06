import mysql.connector
from mysql.connector import errorcode
def getDeveloperDetails(valsearch):
	try:
		mySQLConnection = mysql.connector.connect(host='localhost',database='searchdb',user='root',password='Tulsi@991')
		cursor = mySQLConnection.cursor(prepared=True)
		sql_select_query ="""SELECT * from test where CONCAT (STOVEPIPE,DATACENTER,VSN,FQDN,IP,PORT,POLICY,DEVICE) LIKE '%s'"""
		cursor.execute(sql_select_query,(valsearch, ))
		record = cursor.fetchall()
		for row in record:
			print("STOVEPIPE = ", row[0], )
			print("DATACENTER = ", row[1])
			print("VSN = ", row[2])
			print("FQDN = ", row[3])
			print("IP = ", row[4])
			print("PORT = ", row[5])
			print("POLICY = ", row[6])
			print("DEVICE  = ", row[7], "\n")
	except mysql.connector.Error as error:
		print("Failed to get record from database: {}".format(error))
	finally:
        # closing database connection.
		if (mySQLConnection.is_connected()):
			cursor.close()
			mySQLConnection.close()
			print("connection is closed")

val = '10'
getDeveloperDetails(val)

