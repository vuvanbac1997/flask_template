from flask import Blueprint, render_template

home = Blueprint('Home', __name__)


@home.route('/')
def index():
    return render_template('web/index.html')
