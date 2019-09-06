#!/usr/bin/env python

import cgi
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

#form = cgi.FieldStorage()
#print(form)

def filtertable(query):
	try:
		connection = mysql.connector.connect(host='localhost', database='searchdb', user='root', password='Tulsi@991')
		cursor = connection.cursor(prepared=True)
		result  = cursor.execute(query)
		return result
	except mysql.connector.Error as error :
		connection.rollback()
		print("Failed to select from  MySQL table {}".format(error))
	finally:
        	#closing database connection.
        	if(connection.is_connected()):
            		cursor.close()
            		connection.close()
            		print("MySQL connection is closed")

print "Content-type: text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
print '<title>F5 Search</title>'
print '</head>'
print '</body>'
print '<h2>Search from mysql</h2>'
print '</body>'
print '</html>'





