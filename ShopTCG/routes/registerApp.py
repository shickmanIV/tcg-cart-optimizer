from flask import Flask, render_template, request
import mysql.connector

#app = Flask(__name__)

# Database connection configuration
try:
    db = mysql.connector.connect(
        host="mtg-db.c8twqwf2vwsx.us-west-2.rds.amazonaws.com",
        user="admin",
       password="password",
        database="mtg-db"
    )
except mysql.connector.Error as err:
    print(f"Database connection error: {err}")

def registerUser(form_data):
    username = form_data['username']
    password = form_data['password']
    first_name = form_data['first_name']
    last_name = form_data['last_name']

    # Insert user data into the database
    cursor = db.cursor()
    sql = "INSERT INTO users (Username, Password, FirstName, LastName) VALUES (%s, %s, %s, %s)"
    val = (username, password, first_name, last_name)
    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    return True


#@app.route('/')
#def register_page():
#    return render_template('register.html')

#@app.route('/register', methods=['POST'])
#def register():
#    if request.method == 'POST':
#        username = request.form['username']
#        password = request.form['password']
#        first_name = request.form['first_name']
#        last_name = request.form['last_name']
#
#        # Insert user data into the database
#        cursor = db.cursor()
#        sql = "INSERT INTO users (Username, Password, FirstName, LastName) VALUES (%s, %s, %s, %s)"
#        val = (username, password, first_name, last_name)
#        cursor.execute(sql, val)
#        db.commit()
#
#        cursor.close()
#        return "User registered successfully!"
#
#if __name__ == '__main__':
#    app.run(debug=True)
