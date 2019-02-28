from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
game_blueprint = Blueprint('game', __name__, template_folder='templates', static_folder='static')

@game_blueprint.route('/level/')
def level():
    return ''