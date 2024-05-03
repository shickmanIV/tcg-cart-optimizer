from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('home_bp', __name__)

@bp.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('homepage.html')