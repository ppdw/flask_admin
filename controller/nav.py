from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
nav_blueprint = Blueprint('nav', __name__, template_folder='templates', static_folder='static')


@nav_blueprint.route('/index/')
def index():
    nav = request.form['nav_url']
    print(str(nav))
    return '1234'