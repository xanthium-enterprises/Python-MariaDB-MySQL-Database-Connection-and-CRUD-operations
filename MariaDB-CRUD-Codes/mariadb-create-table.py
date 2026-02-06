# connect to mariadb and create a table inside the MariaDB database using sql commands using Python
# Hard coding our credentials into the source code is not the best practice to follow.
# (c) www.xanthium.in 2026

#sql query to create table called transaction_history

create_table_sql_query = '''

CREATE TABLE IF NOT EXISTS transaction_history(  id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
                                                 cust_name VARCHAR (255),
                                                 cust_age INTEGER ,
                                                 cust_email VARCHAR (255),
                                                 total_bill DECIMAL(10,2),
                                                 time_of_pay TIMESTAMP)
'''

import mariadb #import mariadb connector for Python 
import sys

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
   cursor.execute(create_table_sql_query) #execute the sql query
   conn.commit()
   print("table created succesfully")

except mariadb.Error as e:
   print(f"Error in creating database :{e}")

finally:
   conn.close() #close the connection