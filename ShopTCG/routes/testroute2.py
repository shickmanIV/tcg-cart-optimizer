from flask import Blueprint, render_template

bp = Blueprint('testroutes_2', __name__)

@bp.route('/route2')
def route2_method():
    error = None
    return render_template('testpage2.html', error=error)