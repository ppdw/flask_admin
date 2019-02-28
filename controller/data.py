from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
data_blueprint = Blueprint('data', __name__, template_folder='templates', static_folder='static')

@data_blueprint.route('/index/')
def index():
    return ''
@data_blueprint.route('/user_pay/')
def user_pay():
    return ''

@data_blueprint.route('/user_wealth/')
def user_wealth():
    return ''

@data_blueprint.route('/game_data/')
def game_data():
    return ''

@data_blueprint.route('/user_buy_bill/')
def user_buy_bill():
    return ''

@data_blueprint.route('/pay_rank/')
def pay_rank():
    return ''
@data_blueprint.route('/game_profile/')
def game_profile():
    return ''
@data_blueprint.route('/user_bullet/')
def user_bullet():
    return ''
@data_blueprint.route('/user_client/')
def user_client():
    return ''
@data_blueprint.route('/user_goldmoney/')
def user_goldmoney():
    return ''