#Insert Command
#import sqlite3 library
import sqlite3
import csv

# create the connection object
# conn = sqlite3.connect("new.db")

with sqlite3.connect("new.db") as connection:

#get a cursor object used to execute SQL commands
#cursor = conn.cursor()
	cursor = connection.cursor()
#insert data
#
	employees = csv.reader(open("employees.csv","rU"))
	#cursor.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
	cursor.executemany("INSERT INTO employees(firstname, lastname) values(?, ?)", employees)