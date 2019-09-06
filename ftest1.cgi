#!/usr/bin/env python

import mysql.connector as mx
import sys
import cgi
import cgitb

cgitb.enable()

def htmltop():
        print("""Content-type: text/html\r\n\r\n<!DOCTYPE html><html><body>""")

def htmltail():
        print("""</body></html>""")

def connectdb():
	mydb = mx.connect(host='localhost',user='root',passwd='Tulsi@991',database='emp')
        cur=mydb.cursor()
        return mydb,cur

def retrievedata(mydb,cur):
	form = cgi.FieldStorage()
	if (form.getvalue('valuetosearch')):
		valuetosearch = "%" + form.getvalue('valuetosearch') + "%"
		query = "SELECT * FROM emptbl WHERE concat_ws(empno,bday,fname,lname,gender,hdate,depname,depno) LIKE '"+valuetosearch+"'";
	 	cur.execute(query)
		result=cur.fetchall()
		return result
#		print("connection established")
	else:
		query = "SELECT * FROM emptbl";
		cur.execute(query)
		result = cur.fetchall()
		return result
		print("Enter to search based on the below table:<br><br>")

def displaytest(result):
	print("<div id = 'bottom' style='text-align:center; font-fammily: Eras Bold ITC; font-size:medium;'>")
	print("<table border = '1' align='center'>")
	print("<tr align='center'>")
	print("<th align='center'>EMPLOYEE NAME</th>")
	print("<th align='center'>BIRTHDAY</th>")
	print("<th align='center'>FIRSTNAME</th>")
	print("<th align='center'>LASTNAME</th>")
	print("<th align='center'>GENDER</th>")
	print("<th align='center'>HIRE DATE</th>")
	print("<th align='center'>DEPARTMENT NAME</th>")
	print("<th align='center'>DEPARTMENT NUMBER</th>")
	print("</tr>")
	for x in result:
		print("<tr align='center'>")
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
	print("</div>")

if __name__ == '__main__':
        try:
		htmltop()
		print("<div id='top'>")
		print("<body style = 'background-color:#FFFFFF'>")
		print("<div id='heading' style='text-align:center; font-fammily: Eras Bold ITC; font-size:medium;'>")
		print("<h1 font='Eras Bold ITC'> WAF Search </h1>")
		print("<p font='Eras Bold ITC'> Enter a word to search </p>")
		print("<form action = '/cgi-bin/ftest1.cgi' method = 'POST'>")
		print('<input type="text" name="valuetosearch" placeholder="Search">')
		print('<input type="submit" name="search" value="Search"><br></br>')
		print('</form>')
		print("</div>")
		print("</body>")
		print("</div>")
		mydb,cur = connectdb()
		result = retrievedata(mydb,cur)
		displaytest(result)
		cur.close()
		htmltail()
        except:
                cgi.print_exception()
