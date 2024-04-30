import mysql.connector

config = {
    'host': 'mtg-db.c8twqwf2vwsx.us-west-2.rds.amazonaws.com',
    'user': 'admin',
    'password': 'password',
    'database': 'mtg'
}

db = mysql.connector.connect(**config)
