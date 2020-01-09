import pymysql
from sqlalchemy import create_engine

hostname = "aibnbdb.c9v9a7trklsr.us-east-1.rds.amazonaws.com"
username = "aibnb"
password = "cse6242aibnb"
database = "aibnb"
port = 3306
try:
        db = pymysql.connect(host=hostname, port=port, user=username, passwd=password,
                             db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
except:
        print("Error: connection failed!")
