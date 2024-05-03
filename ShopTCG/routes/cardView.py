from flask import Blueprint, request, render_template

bp = Blueprint('card_view_bp', __name__)

@bp.route('/cardview')
def cardView():
    query = request.args.get('query', '')
    return render_template('cardviewpage.html', query=query)