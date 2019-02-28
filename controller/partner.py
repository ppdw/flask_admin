from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
partner_blueprint = Blueprint('partner', __name__, template_folder='templates', static_folder='static')

@partner_blueprint.route('/index/')
def index():
    return ''
@partner_blueprint.route('/bill/')
def bill():
    return ''
