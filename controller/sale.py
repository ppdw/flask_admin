from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
sale_blueprint = Blueprint('sale', __name__, template_folder='templates', static_folder='static')

@sale_blueprint.route('/index/')
def index():
    return ''
@sale_blueprint.route('/denom/')
def denom():
    return ''
@sale_blueprint.route('/rank/')
def rank():
    return ''