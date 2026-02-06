# create a simple connection to a  mariadb database 

# Please note that we are hard coding our credentials into the source code which is not the best practice to follow.
# This is just a tutorial and the credentials are just for a throw away database 

import mariadb
import sys

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
