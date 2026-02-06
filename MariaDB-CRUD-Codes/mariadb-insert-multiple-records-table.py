# Insert Multiple Records /Rows of data into the mariadb database Table.
# Hard coding our credentials into the source code is not the best practice to follow.
# (c) www.xanthium.in 2026



import mariadb #import mariadb connector for Python 
import sys
import datetime

# data to be inserted into transaction_history table
# make sure that table exists in the first place

# Data formatted for cur.executemany(sql, customers)
customers = [
    ("Liam Henderson", 28, "liam.h@example.com", 145.50, "2026-02-06 09:15:22"),
    ("Sophia Martinez", 34, "smartinez89@testmail.com", 82.25, "2026-02-06 10:05:45"),
    ("Marcus Chen", 42, "mchen_dev@provider.net", 310.00, "2026-02-06 10:45:10"),
    ("Elena Rodriguez", 23, "elena.rod@example.org", 12.99, "2026-02-06 11:02:33"),
    ("Julian Vane", 56, "jvane56@webmail.com", 540.75, "2026-02-06 11:15:00"),
    ("Aaliyah Smith", 31, "aaliyah.s@example.com", 67.40, "2026-02-06 11:20:12"),
    ("Oliver Quinn", 29, "ollie.q@fastmail.com", 125.00, "2026-02-06 11:23:35"),
    ("Isabella Ross", 45, "i.ross@corporate.com", 215.10, "2026-02-06 11:35:50"),
    ("Ethan Wright", 38, "wright.ethan@test.io", 45.00, "2026-02-06 11:45:18"),
    ("Chloe Tanaka", 27, "ctanaka@example.jp", 189.95, "2026-02-06 11:58:05")
]


#column names should be exactly similar to db coloumn names, inside the SQL query
sql_query_insert_data = '''

INSERT INTO transaction_history (cust_name,
	                             cust_age,
	                             cust_email,
	                             total_bill,
	                             time_of_pay)
VALUES (?,?,?,?,?)
'''


#Connect with the Server
try:
   conn = mariadb.connect(
                           user="rahul",
                           password="EY4u^?%<_VB2tfY2",
                           host="localhost",
                           port=3306,
                           database="mariadb_testdb"
                         )
   
except mariadb.Error as e:
   print(f"Error connecting to MariaDB: {e}")
   sys.exit(1) # telling the system program ended in an error



cursor = conn.cursor() #create a cursor object

try:
	
	cursor.executemany(sql_query_insert_data,customers) #executemany() returns a none 

	print(f"Rows Changed = {cursor.rowcount}")                #to get the number of rows changed, use cursor.rowcount
	print(f"ID of the last inserted row {cursor.lastrowid}")  #ID of the last inserted row 
	
	conn.commit() #commit the changes to the db
   

except mariadb.Error as e:
   print(f"Error in inserting data to the database :{e}")

finally:
	conn.close() #close the connection


