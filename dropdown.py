#!/usr/bin/env python3

import MySQLdb
import cgi
import cgitb

def db_dropdown():  # Execute query
	db = MySQLdb.connect(user='root', db='searchdb', passwd='Tulsi@991', host='localhost')  # Your DB details here
	cursor = db.cursor()

	sql = 'SELECT * from test where CONCAT(STOVEPIPE,DATACENTER,VSN,FQDN,IP,PORT,POLICY,DEVICE) LIKE %s'
	cursor.execute(sql)
	list_tested = cursor.fetchall()  # Get query response and store in variable
	list_tested = [i for sub in list_tested for i in sub]  # Convert to list from tuple
	return list_tested

def print_dropdown(data):  # Print the dropdown
	print '<div>'
	print '<select>'
	for i in data:
		print '<option value="%s"selected>%s</option>' % (i, i)

	print '</select>'
	print '</div>'
