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
'''
	cursor.execute("INSERT INTO population VALUES('New York City2', \
		'NY', 8200000)")
	cursor.execute("INSERT INTO population VALUES('San Francisco2', \
		'CA', 800000)")
'''

cities = [
		('Boston','MA', 60000 ),
		('Chicago','IL', 2700000 ),
		('Houston', 'TX', 2100000),
		('Phoenix', 'AZ', 1500000)
		]
#commit changes
#conn.commit()

#close the database connection
#conn.close()