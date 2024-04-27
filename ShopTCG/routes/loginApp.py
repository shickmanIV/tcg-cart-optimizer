from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL database connection
db = mysql.connector.connect(
    host="mtg-db.c8twqwf2vwsx.us-west-2.rds.amazonaws.com",
    user="admin",
    password="password",
    database="mtg-db"
)

cursor = db.cursor()

# Define route for login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password match in the database
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()

        if user_data:
            if password == user_data[0]:
                # Redirect to main page if login is successful
                return redirect(url_for('main_page'))
            else:
                error_message = "Incorrect username or password"
                return render_template('login.html', error=error_message)
        else:
            error_message = "Incorrect username or password"
            return render_template('login.html', error=error_message)
    
    return render_template('login.html')

# Define route for main page (redirected after successful login)
@app.route('/main_page')
def main_page():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)