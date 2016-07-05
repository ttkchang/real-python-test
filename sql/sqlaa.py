# Create an SQLite3 database and table
# 
# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQl commands
cursor = conn.cursor()

#create a table

# cursor.execute("""CREATE TABLE population
# 			(city TEXT, state TEXT, population INT)
# 			""")

#close the database connection
try:
	#insert data
	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 18200000)")
	cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 1800000)")
	conn.commit()

except sqlite3.OperationalError:
	print "Oops! Something went wrong!"
	print sqlite3.OperationalError

conn.close()
