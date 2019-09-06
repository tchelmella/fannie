#!/usr/bin/env python

import mysql.connector as mx
import sys
import cgi
import cgitb

cgitb.enable()

def htmltop():
	print("""Content-type: text/html\r\n\r\n
	<!DOCTYPE html><html><body>
	<table border='1'>
	<tr><th>STOVEPIPE</th><th>DATACENTER</th><th>VIRTUALSERVERNAME</th><th>FQDN</th><th>IPADDRESS</th><th>SERVICE PORT</th><th>SECURITY POLICY</th>
	<th>DEVICE NAME</th></tr>""")

def htmltail():
	print("""</body></html>""")

def connectdb():
	mydb=mx.connect(host='localhost',user='root',passwd='Tulsi@991',database='searchdb')
	cur=mydb.cursor()
	return mydb,cur

def Blacklist(mydb,cur):
	query="select * from test"
	cur.execute(query)
	result=cur.fetchall()
	return result

def displaytest(result):
	print("<table border='1'>")
	for x in result:
		print("<tr>")
		print("<td> {0} </td>".format(x[0]))
		print("<td> {0} </td>".format(x[1]))
		print("<td> {0} </td>".format(x[2]))
		print("<td> {0} </td>".format(x[3]))
		print("<td> {0} </td>".format(x[4]))
		print("<td> {0} </td>".format(x[5]))
		print("<td> {0} </td>".format(x[6]))
		print("<td> {0} </td>".format(x[7]))
		print("</tr>")
	print("</table>")


if __name__ == '__main__':
	try:
		htmltop()
		"""form = cgi.FieldStorage()
		valsearch = form.getvalue('valsearch')"""
		print "<form action = '/cgi-bin/fsearch.cgi' method = 'post'>"
		print "<textarea name = 'textcontent' cols = '4' rows = '4'></textarea>"
		print "<input type = 'submit' value = 'Search' />"
		print "</form>"
		form = cgi.FieldStorage()
		# Get data from fields
		if form.getvalue('textcontent'):
			text_content = form.getvalue('textcontent')
		else:
			text_content = "Not entered"

		mydb,cur=connectdb()
		result=Blacklist(mydb,cur)
		displaytest(result)
		cur.close()
		htmltail()
	except:
		cgi.print_exception()
