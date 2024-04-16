import psycopg2

hostname = 'locahost'
database = 'test'
username = 'postgres'
pwd = 'password'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='password'")
    
    cur = conn.cursor()

    cur.execute('SELECT cardID FROM cardIndex')
    for record in cur.fetchall():
        print(record[0])


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


# CREATE TABLE cardIndex (
#     listingID INT PRIMARY KEY,
#     cardID INT, 
#     sellerID INT,
#     price int,
#     wear VARCHAR(50),
#     name VARCHAR(100),
#     set VARCHAR(100),
#     setNum int,
#     art VARCHAR(100),
#     effect VARCHAR(100)

# );

