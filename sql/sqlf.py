# UPDATE and DELETE
# 
import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# carinventory =[
	# 		('Ford','F190', 45),
	# 		('Ford','Escort', 5),
	# 		('Honda','Civic', 19),
	# 		('Honda','Accord', 29),
	# 		('Honda','CRV', 20)
	# 		]

	# # insert data into table
	# c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', carinventory)

	c.execute("SELECT * FROM inventory WHERE make='Ford'")
	rows = c.fetchall()
	for r in rows:
		print r[0], r[1], r[2]