#!/usr/bin/env python3

import MySQLdb
import cgi
import Cookie

# Open database connection
db = MySQLdb.connect("localhost","root","Tulsi@991","emp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
data=cgi.FieldStorage()
a=data.getvalue('e1')
#b=data.getvalue('pl')

# Prepare SQL query to fetch a record into the database.
sql = "select * from emptbl where ='%s'"
try:
# Execute the SQL command
	if(cursor.execute(sql)):
   # Commit your changes in the database
		db.commit()
#   c=Cookie.SimpleCookie()

   # assign a value
#   c['mou']=a

   # set the xpires time
#   c['mou']['expires']=24*60*60

   # print the header, starting with the cookie
#   print c
		print("Content-type: text/html")
		print('''<html><head><title>Hello Word - First CGI Program</title></head><body><h2>successfully login</h2></body></html>''')
	else:
   # Commit your changes in the database
		db.commit()
		print("Content-type: text/html")
		print("<html>")
		print("<body>")
		print("<h2>fail</h2>")
		print("</body>")
		print("</html>")
except:
   # Rollback in case there is any error
	db.rollback()
   # disconnect from server
	db.close()
