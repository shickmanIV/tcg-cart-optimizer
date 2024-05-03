from flask import Blueprint, request, redirect, url_for, render_template
import database.registration as reg

bp = Blueprint('register_bp', __name__)

@bp.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        if request.form.get('go_to_login'):
            return redirect(url_for('login_bp.login'))
        elif validate_new_user(request.form):
            print("Attempting registration")
            #Upload user info to database
            if reg.registerUser(request.form):
                return redirect(url_for('home_bp.home'))
            else:
                error = 'Registration failed'
        else:
            error = 'Invalid username/password'
    return render_template('register.html', error=error)

def validate_new_user(form_data):
    # Implement user validation logic here
    return True
