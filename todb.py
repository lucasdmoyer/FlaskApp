import psycopg2
 
import sys
 
db_con = None
 
try:
 
#Create a database session
 
	db_con = psycopg2.connect(database='yourdbname', user='yourusername', password='yourpassword')
	 
	#Create a client cursor to execute commands
	 
	cursor = db_con.cursor()
	 
	cursor.execute("CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR age INTEGER);")
	 
	#The variables placeholder must always be a %s, psycop2 will automatically convert the values to SQL literal
	 
	cursor.execute("INSERT INTO customers ( name, AGE) VALUES (%s, %s)",("leo", 26))
	 
	db_con.commit()
	 
	cursor.execute("SELECT * FROM customers")

	print(cursor.fetchone())
 
except psycopg2.DatabaseError as e: 
 
	print ('Error %s' % e    )
	 
	sys.exit(1)
 
finally:
 
	if db_con:
	 
		db_con.close()