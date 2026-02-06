# Insert data to mariadb database Table.
# Hard coding our credentials into the source code is not the best practice to follow.
# (c) www.xanthium.in 2026



import mariadb #import mariadb connector for Python 
import sys
import datetime

# data to be inserted into transaction_history table
# make sure that table exists in the first place

customer_name  = "Steve Harrington"
customer_age   = 28
customer_email = "steveharrington@mail.com"
customer_bill  = 1289.56


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
	timestamp = datetime.datetime.now()
	print(timestamp)
	cursor.execute(sql_query_insert_data,
		           (customer_name,
		           	customer_age,
		           	customer_email,
		           	customer_bill,
		           	timestamp
		           	)
		           )
	conn.commit() #commit the changes to the db
   

except mariadb.Error as e:
   print(f"Error in inserting data to the database :{e}")

finally:
	conn.close() #close the connection


