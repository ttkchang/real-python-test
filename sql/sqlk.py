import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# c.execute("""CREATE TABLE orders
	# 	(make TEXT, model TEXT, order_date TEXT)
	# 	""")

	orderstuple =[
			('Ford','F190','1995-04-01'),
			('Ford','F190','1996-04-02'),
			('Ford','F190','1997-04-03'),
			('Honda','Civic','1997-04-03'),
			('Honda','Civic','1997-04-04'),
			('Honda','Civic','1997-04-05'),
			('Honda','Civic','1997-04-06'),
			('Honda','Accord','2000-04-03'),
			('Honda','Accord','2000-04-04'),
			('Honda','Accord','2000-04-06'),
			('Honda','Accord','2000-04-06')
			]

	#c.executemany("INSERT INTO orders VALUES(?,?,?)", orderstuple)
	# c.execute("SELECT * from orders")

	# rows = c.fetchall()
	# for r in rows:
	# 	print r[0],r[1],r[2]

	c.execute("""SELECT DISTINCT inventory.make, inventory.model, orders.order_date FROM inventory, orders
			WHERE inventory.make = orders.make ORDER by inventory.make ASC
			""")
	rows = c.fetchall()
	for r in rows:
		print "Make: "	+ r[0]
		print "Model: " + r[1]
		print "Order_date: " + r[2]