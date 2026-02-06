# Read the data from the entire table 
# (c) www.xanthium.in 2026

import mariadb #import mariadb connector for Python 
import sys



sql_query_read_all = "SELECT * FROM transaction_history"

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
    cursor.execute(sql_query_read_all) #execute SELECT * FROM transaction_history
    entire_table = cursor.fetchall()   #read the entire table
    
    
    for row in entire_table:
      print(row)
 
except mariadb.Error as e:
  print(f"Error in inserting data to the database :{e}")
finally:
    conn.close() #close the connection


