 #!/usr/bin/env python3

"""Python, MySQL and CGI (Common Gateway Interface) all
in the same demo script.

Note - need to moderate live public boards of this type!
"""

import cgi
import MySQLdb

# Following line is what you would need to create table
# prior to running for the first time
#
# create table comment
#     (info  text, enteredat timestamp,
#     cid int primary key not null auto_increment)

# Connect to MySQL database
db = MySQLdb.connection(host="localhost",user="root",passwd="Tulsi@991",db="searchdb")

# Collect values from form
inputs = cgi.FieldStorage()
fill = {}
for key in inputs:
   fill[key] = inputs[key].value

# If the form was completed, save what was entered on it
"""try:
     said = fill["info"]
     form = 1
     db.query('insert into comment (info) values ("' \
               +said.replace('"',r'\"') \
               +'")')
except:
     form = 0
"""
# Read back 10 latest comments
db.query("SELECT * FROM test WHERE(STOVEPIPE or DATACENTER or VSN or FQDN or IP or PORT or POLICY or DEVICE LIKE ?")
r = db.store_result()

history = ""
for row in r.fetch_row(10):
    history += cgi.escape(row[0]) + "<br>\n"

# Generate the HTML response

#######################################################

print """content-type: text/html

<html>
<head>
<title>MySQL and Python on the Web</title>
</head>
<body bgcolor=#FFCCFF>
<h1>Message Board Report</h1>
This is a message board report demo.<br>
<b>This is what has been going on ... </b><br>
"""

print history

print """
<form method=POST>Please enter your comment: <input name=info><br>
<input type=submit>
</form>
Demonstration from Well House Consultants.<br>
<a href=http://www.wellho.net/>Website</a>
</body></html>
"""
