from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('login_logic', __name__)

@bp.route('/login', methods=['POST', 'GET'])
def login_page():
    error = None
    if request.method == 'POST':
        if request.form.get('go_to_registration'):
            return redirect(url_for('register_logic.register_page'))
        elif validate_login(request.form):
            if log_the_user_in(request.form['username']):
                #TODO: Go to homepage
                return f"TODO: log user in, username: {request.form['username']}"
            else:
                error = 'Login failed'
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

def validate_login(form_data):
    return True

def log_the_user_in(username):
    # Implement user login logic here
    pass#return f"TODO: log user in, username: {username}"