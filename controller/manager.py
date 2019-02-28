from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
manager_blueprint = Blueprint('manager', __name__, template_folder='templates', static_folder='static')


@manager_blueprint.route('/user/')
def user():
    return '1234'

@manager_blueprint.route('/frozen_list/')
def frozen_list():
    return '1234'

@manager_blueprint.route('/search/')
def search():
    return '1234'

@manager_blueprint.route('/gm_list/')
def gm_list():
    return '1234'