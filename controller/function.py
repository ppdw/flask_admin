from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
function_blueprint = Blueprint('function', __name__, template_folder='templates', static_folder='static')

@function_blueprint.route('/payconfig/')
def payconfig():
    return ''
@function_blueprint.route('/vip/')
def vip():
    return ''
@function_blueprint.route('/register/')
def register():
    return ''
@function_blueprint.route('/customer/')
def customer():
    return ''
@function_blueprint.route('/prop/')
def prop():
    return ''
@function_blueprint.route('/extime/')
def extime():
    return ''
@function_blueprint.route('/gifts/')
def gifts():
    return ''