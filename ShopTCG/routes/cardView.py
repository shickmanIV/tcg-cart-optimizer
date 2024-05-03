from flask import Blueprint, request, render_template

bp = Blueprint('card_page_bp', __name__)

@bp.route('/cardPage')
def cardPage():
    query = request.args.get('query', '')
    return render_template('cardPage.html', query=query)