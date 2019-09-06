import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Tulsi@991",database = "searchdb")

mycursor = mydb.cursor()
mycursor.execute("SELECT STOVEPIPE from test")

result = mycursor.fetchall()

for row in result:
	print(row)
