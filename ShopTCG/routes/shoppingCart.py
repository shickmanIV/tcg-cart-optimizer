from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('shopping_cart_bp', __name__)

# Define route for shopping cart page
@bp.route('/shoppingcart', methods=['GET', 'POST'])
def shoppingCart():
    return render_template('shoppingCart.html')