from flask import Blueprint, request, redirect, url_for, render_template
import database.loginValidator as lv

bp = Blueprint('login_bp', __name__)

@bp.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('go_to_registration'):
            return redirect(url_for('register_bp.register_page'))
        elif lv.validateLogin(request.form):
            return redirect(url_for('main_page_bp.main_page'))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)
