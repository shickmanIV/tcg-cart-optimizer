from flask import Blueprint, request, redirect, url_for, render_template
import routes.registerApp as regApp

bp = Blueprint('register_bp', __name__)

@bp.route('/register', methods=['POST', 'GET'])
def register_page():
    error = None
    if request.method == 'POST':
        if request.form.get('go_to_login'):
            return redirect(url_for('login_bp.login'))
        elif validate_new_user(request.form):
            print("Attempting registration")
            #Upload user info to database
            if register_new_user(request.form):
                #TODO: Go to homepage
                return f"TODO: go to hompage of {request.form['username']}"
            else:
                error = 'User registration failed'
        else:
            error = 'Invalid username/password'
    return render_template('register.html', error=error)

def validate_new_user(form_data):
    # Implement user validation logic here
    return True

def register_new_user(form_data):
    return regApp.registerUser(form_data)