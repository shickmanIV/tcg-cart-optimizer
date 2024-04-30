from database import db

def registerUser(form_data):
    username = form_data['username']
    password = form_data['password']
    first_name = form_data['first_name']
    last_name = form_data['last_name']

    print("registerUser() called")
    print(form_data)

    # Insert user data into the database
    cursor = db.cursor()
    sql = "INSERT INTO users (Username, Password, FirstName, LastName) VALUES (%s, %s, %s, %s)"
    val = (username, password, first_name, last_name)
    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    print("Registered new user: ", username)
    return True