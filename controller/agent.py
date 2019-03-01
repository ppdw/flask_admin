from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify

agent_blueprint = Blueprint('agent', __name__, template_folder='templates', static_folder='static')


@agent_blueprint.route('/index/')
def index():
    return '123'


@agent_blueprint.route('/bill/')
def bill():
    return ''


@agent_blueprint.route('/daystatis/')
def daystatis():
    return ''
