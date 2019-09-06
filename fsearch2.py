#!/usr/bin/env python

import mysql.connector as mx
import sys
import cgi
import cgitb

cgitb.enable()

def htmltop():
        print("""Content-type: text/html\r\n\r\n; charset=utf-8<!DOCTYPE html><html><head>
		<style type = 'text/css'>
			body {
				font-family: 'Eras Bold ITC';
				color: black;
			}
			#top,#bottom {
				position: fixed;
				left: 0;
				right: 0;
				height: 50%;
			}
			#top {
				top: 0;
				background-color: #000f2b;
			}
			#bottom {
				bottom: 0;
				background-color: white;
				font: 'Eras Bold ITC';
				overflow: auto;
				text-align: center;
			}
			th {
				background-color: #588c7e;
				color: white;
			}
			tr,th,td {
				border: 1px solid black;
			}
			table {
				font-family: Eras Bold ITC;
				text-align: center;
			}
		</style></head>""")

def htmltail():
        print("""</body></html>""")

def connectdb():
	mydb = mx.connect(host='localhost',user='root',passwd='Tulsi@991',database='searchdb')
        cur=mydb.cursor()
        return mydb,cur

def retrievedata(mydb,cur):
	form = cgi.FieldStorage()
	if (form.getvalue('valuetosearch')):
		valuetosearch = "%" + form.getvalue('valuetosearch') + "%"
		query = "SELECT * FROM test WHERE concat_ws(STOVEPIPE,DATACENTER,VSN,FQDN,IP,PORT,POLICY,DEVICE) LIKE '"+valuetosearch+"'";
	 	cur.execute(query)
		result=cur.fetchall()
		return result
#		print("connection established")
	else:
		query = "SELECT * FROM test";
		cur.execute(query)
		result = cur.fetchall()
		return result
		print("Enter to search based on the below table:<br><br>")

def displaytest(result):
	print("<div id = 'bottom' style='text-align:center; font-fammily: Eras Bold ITC; font-size:medium;'>")
	print("<table border = '1' align='center'>")
	print("<tr align='center'>")
	print("<th align='center'>STOVEPIPE</th>")
	print("<th align='center'>DATACENTER</th>")
	print("<th align='center'>VIRTUAL SERVER NAME</th>")
	print("<th align='center'>FQDN</th>")
	print("<th align='center'>IP ADDRESS</th>")
	print("<th align='center'>SERVICE PORT</th>")
	print("<th align='center'>SECURITY POLICY</th>")
	print("<th align='center'>DEVICE NAME</th>")
	print("</tr>")
	for x in result:
		print("<tr align='center'>")
		print("<td> {0} </td>".format(x[0].encode("utf-8")))
		print("<td> {0} </td>".format(x[1].encode("utf-8")))
		print("<td> {0} </td>".format(x[2].encode("utf-8")))
		print("<td> {0} </td>".format(x[3].encode("utf-8")))
		print("<td> {0} </td>".format(x[4].encode("utf-8")))
		print("<td> {0} </td>".format(x[5].encode("utf-8")))
		print("<td> {0} </td>".format(x[6].encode("utf-8")))
		print("<td> {0} </td>".format(x[7].encode("utf-8")))
		print("</tr>")
	print("</table>")
	print("</div>")

if __name__ == '__main__':
        try:
		htmltop()
		print("<div id='top'>")
#		print("<body style = 'background-color:#FFFFFF'>")
		print("<div id='heading' style='text-align:center; font-fammily: Eras Bold ITC; font-size:medium;'>")
		print("<h1 font='Eras Bold ITC'> WAF Search </h1>")
		print("<p font='Eras Bold ITC'> Enter a word to search for example: UTC or fannie or 10.136 etc. </p>")
		print("<form action = '/cgi-bin/fsearch2.py' method = 'POST'>")
		print('<input type="text" name="valuetosearch" placeholder="Search">')
		print('<input type="submit" name="search" value="Search"><br></br>')
		print('</form>')
		print("</div>")
		print("</div>")
		mydb,cur = connectdb()
		result = retrievedata(mydb,cur)
		displaytest(result)
		cur.close()
		htmltail()
        except:
                cgi.print_exception()
