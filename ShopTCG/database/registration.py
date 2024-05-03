from database import aws_connection as db

def registerUser(form_data):
    username = form_data['username']
    password = form_data['password']
    first_name = form_data['first_name']
    last_name = form_data['last_name']
    account_type = form_data['accountType']

    buyer = 1 if account_type == 'Buyer' else 0
    seller = 1 if account_type == 'Seller' else 0

    print("registerUser() called")
    print(form_data)

    # Insert user data into the database
    cursor = db.cursor()
    sql = "INSERT INTO users (Username, Password, FirstName, LastName, Buyer, Seller) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (username, password, first_name, last_name, buyer, seller)
    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    print("Registered new user: ", username)
    return True
