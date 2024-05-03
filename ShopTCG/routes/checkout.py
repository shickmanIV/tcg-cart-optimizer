from flask import Blueprint, request, render_template

bp = Blueprint('checkout_bp', __name__)

@bp.route('/checkout')
def checkout():
    return render_template('checkout.html')