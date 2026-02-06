# Read a single row from the database
# (c) www.xanthium.in 2026

import mariadb #import mariadb connector for Python 
import sys



sql_query_read_one = '''SELECT * FROM transaction_history 

                        WHERE id = 5 '''

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
    cursor.execute(sql_query_read_one) #execute SELECT * FROM transaction_history WHERE id =5 
    just_single_row = cursor.fetchone()   #read the entire table
    print()
    print(just_single_row)
    print()
    print(f"Id   -> {just_single_row[0]}")
    print(f"Name -> {just_single_row[1]}")
    print(f"Age  -> {just_single_row[2]}")
    print(f"Time -> {just_single_row[5]}")


     
except mariadb.Error as e:
  print(f"Error in inserting data to the database :{e}")
finally:
    conn.close() #close the connection


