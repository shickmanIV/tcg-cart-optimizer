from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('register_page'))

@app.route('/register', methods=['POST', 'GET'])
def register_page():
    error = None
    if request.method == 'POST':
        if request.form.get('go_to_login'):
            # Redirect to the login page if requested
            return redirect(url_for('login_page'))
        elif validate_new_user(request.form):  # Validate the new user
            #Upload user info to database
            if register_new_user(request.form):
                #TODO: Go to homepage
                return f"TODO: go to hompage of {request.form['username']}"
            else:
                error = 'User registration failed'
        else:
            error = 'Invalid username/password'
    return render_template('register.html', error=error)

@app.route('/login', methods=['POST', 'GET'])
def login_page():
    error = None
    if request.method == 'POST':
        if request.form.get('go_to_registration'):
            # Redirect to the registration page if requested
            return redirect(url_for('register_page'))
        elif validate_login(request.form):
            if log_the_user_in(request.form['username']):
                #TODO: Go to homepage
                return f"TODO: log user in, username: {request.form['username']}"
            else:
                error = 'Login failed'
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

def validate_new_user(form_data):
    # Implement user validation logic here
    return True

def register_new_user(form_data):
    # Implement user registration logic here
    return True

def validate_login(form_data):
    return True

def log_the_user_in(username):
    # Implement user login logic here
    pass#return f"TODO: log user in, username: {username}"

if __name__ == "__main__":
    app.run(debug=True)