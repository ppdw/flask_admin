from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
user_blueprint = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_blueprint.route('/index/')
def index():
    return ''

@user_blueprint.route('/luckstar_list/')
def luckstar_list():
    return ''
