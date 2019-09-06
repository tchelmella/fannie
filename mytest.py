#!/usr/bin/env python3

import MySQLdb

user_input = raw_input("Please enter search and press Enter button: ")

db = MySQLdb.connect(passwd="Tulsi@991",db="searchdb")
mycursor = db.cursor()
mycursor.execute("""SELECT * FROM test WHERE STOVEPIPE = %10s""", (user_input,))

# calls fetchone until None is returned (no more rows)
for row in iter(mycursor.fetchone, None):
    print row
