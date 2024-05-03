import mysql.connector
config = {
    'host': 'mtg-db.c8twqwf2vwsx.us-west-2.rds.amazonaws.com',
    'user': 'admin',
    'password': 'password',
    'database': 'mtg'
}

try:
    aws_connection = mysql.connector.connect(**config)
    print("mysql connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
