import mysql.connector as mx
import sys
import cgi
import cgitb

def htmltop():
	print("""Content-type: text/html\r\n\r\n
	<!DOCTYPE html><html><body>Output:""")

def htmltail():
	print("""</body></html>""")

def connectdb():
	mydb=mx.connect(host='localhost',user='root',passwd='Tulsi@991',database='searchdb')
	cur=mydb.cursor()
	return mydb,cur

def Blacklist(mydb,cur,valsearch):
	query="select * from test where valsearch=" + valsearch
	cur.execute(query)
	result=cur.fetchall()
	return result

def displaytest(result):
	print("<table border='5'>")
	print("<tr>")
	print("<th> STOVEPIPE </th>")
	print("<th> DATACENTER </th>")
	print("<th> VIRTUALSERVERNAME </th>")
	print("<th> FQDN </th>")
	print("<th> IPADDRESS </th>")
	print("<th> SERVICE PORT </th>")
	print("<th> SECURITY POLICY </th>")
	print("<th> DEVICE NAME </th>")	
	print("</tr>")
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
		form = cgi.FieldStorage()
		mydb,cur=connectdb()
		result=Blacklist(mydb,cur,form["valsearch"])
		displaytest(result)
		cur.close()
		htmltail()
	except:
		cgi.print_exception()
