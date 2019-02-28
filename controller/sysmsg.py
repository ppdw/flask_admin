from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
sysmsg_blueprint = Blueprint('sysmsg', __name__, template_folder='templates', static_folder='static')

@sysmsg_blueprint.route('/index/')
def index():
    return ''