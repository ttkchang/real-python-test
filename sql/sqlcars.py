# Create an SQLite3 database and table
# 
# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't exist
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQl commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE inventory
			(Make TEXT, Model TEXT, Quantity INT)
			""")

#close the database connection
conn.close()


