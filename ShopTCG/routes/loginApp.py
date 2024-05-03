from flask import render_template, request, redirect, url_for, Blueprint
from database import aws_connection as db

bp = Blueprint('loginApp_bp', __name__)

# Define route for login page
@bp.route('/loginY', methods=['GET', 'POST'])
def login():
    cursor = db.cursor()
    if request.method == 'POST':
        if request.form.get('go_to_registration'):
            print("Redirecting to registration")
            cursor.close()
            return redirect(url_for('register_bp.register_page'))
        else:
            print("Attempting login")
            print(request.form)
            username = request.form['username']
            password = request.form['password']

            # Check if username and password match in the database
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            user_data = cursor.fetchone()

            if user_data:
                if password == user_data[0]:
                    # Redirect to main page if login is successful
                    cursor.close()
                    return redirect(url_for('main_page_bp.main_page'))
                else:
                    error_message = "Incorrect username or password"
                    cursor.close()
                    return render_template('login.html', error=error_message)
            else:
                error_message = "Incorrect username or password"
                cursor.close()
                return render_template('login.html', error=error_message)
    cursor.close()
    return render_template('login.html')