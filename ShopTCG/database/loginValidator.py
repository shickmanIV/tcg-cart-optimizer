from database import aws_connection as db

def validateLogin(form_data):
    print("validateLogin() called")
    print(form_data)
    username = form_data['username']
    password = form_data['password']

    cursor = db.cursor()

    # Check if username and password match in the database
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchone()

    if user_data:
        if password == user_data[0]:
            print("Password accepted")
            cursor.close()
            return True #redirect(url_for('main_page_bp.main_page'))
        else:
            print("Incorrect username or password")
            error = "Incorrect username or password"
            cursor.close()
            return False #render_template('login.html', error=error_message)
    else:
        error = "Incorrect username or password"
        print(error)
        cursor.close()
        return False #render_template('login.html', error=error_message)