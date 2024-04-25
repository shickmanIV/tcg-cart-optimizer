from flask import Blueprint, render_template

bp = Blueprint('testroutes_1', __name__)

@bp.route('/route1')
def route1_method():
    error = None
    return render_template('testpage1.html', error=error)