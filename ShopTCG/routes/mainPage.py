#This is a placehoder for the main page logic.

from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('main_page_bp', __name__)

@bp.route('/main_page', methods=['POST', 'GET'])
def main_page():
    return render_template('homepage.html')