#!/usr/bin/env python

import sys
import mysql.connector
print("Content-Type: text/html;charset=utf-8")
print "Content-type:text/html\r\n\r\n"

conn = mysql.connector.connect(host='localhost',database='searchdb',user='root',password='Tulsi@991')
cursor = conn.cursor()
if conn.is_connected():
	print('sucessfull...Connected to MySQL database')

cursor.execute(" SELECT * FROM test ")
print ("<html>")
print("<p>")
print("</p>")
print("<body")
print ("<table border='2'>")
print ("<tr><td>")


for row in cursor.fetchall():
        print (row)
print ("</td></tr>")
print  ("</table>")
print ("</body>")
print ("</html>")
