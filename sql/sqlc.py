#Insert Command
#import sqlite3 library
import sqlite3

# create the connection object
# conn = sqlite3.connect("new.db")

with sqlite3.connect("new.db") as connection:

#get a cursor object used to execute SQL commands
#cursor = conn.cursor()
	cursor = connection.cursor()
#insert data
#

	cities = [
			('Boston','MA', 60000 ),
			('Chicago','IL', 2700000 ),
			('Houston', 'TX', 2100000),
			('Phoenix', 'AZ', 1500000)
			]
	cursor.executemany('INSERT INTO population VALUES(?,?,?)', cities)

#commit changes
#conn.commit()

#close the database connection
#conn.close()