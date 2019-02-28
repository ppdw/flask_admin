from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
card_blueprint = Blueprint('card', __name__, template_folder='templates', static_folder='static')

@card_blueprint.route('/index/')
def index():
    return ''