from flask import Blueprint, render_template

main_bp = Blueprint('user', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/services')
def servicos():
    return render_template('services.html')

@main_bp.route('/register')
def servicos():
    return render_template('register.html')