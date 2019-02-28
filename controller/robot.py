from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
robot_blueprint = Blueprint('robot', __name__, template_folder='templates', static_folder='static')
@robot_blueprint.route('/index/')
def index():
    return ''