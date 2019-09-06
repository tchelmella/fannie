import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Tulsi@991",
  database="searchdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from test")

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 
