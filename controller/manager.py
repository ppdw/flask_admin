from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify, json
from controller import api
from config.public import Public
from model.test import Admin

manager_blueprint = Blueprint('manager', __name__, template_folder='templates', static_folder='static')


@manager_blueprint.route('/user/')
def user():
    if api.checkpower('manager.user'):
        admin_id = session.get('admin_id')
        admin_info = Admin.query.filter_by(ID=admin_id).first()
        admin_agentid = admin_info.AgentID

        return render_template('Manager_user.html')
    else:
        return redirect(url_for('index.login'))


@manager_blueprint.route('/ajax_online_user/')
def ajax_online_user():

    cgi_url = Public.user_cgi + "?method=accountcgi_get_user_online_pinpai_auto"
    print(cgi_url)
    data = {
        'agentids': 0,
        'agentid': 0,
        'gameid': 0,
        'gameids': '',
        'usertype': 0,
        'sorttype': 0,
        'page': 1,
        'size': 25,
        'pid': 9,
        'time': 1552036733,
        'code': 'aa2ad2acc6247f19e73ba1b64b82307c',
    }
    user_info = api.fpost(cgi_url,data)
    print(user_info)
    temp = []
    print("刷新1")
    return user_info


@manager_blueprint.route('/frozen_list/')
def frozen_list():
    return '1234'


@manager_blueprint.route('/search/')
def search():
    return redirect(url_for('index.login'))


@manager_blueprint.route('/gm_list/')
def gm_list():
    return '1234'

@manager_blueprint.context_processor
def my_context_processor():
    try:
        nav_dict = api.init_nav()
        nav_on = api.last_nav()
        return {'nav_dict': nav_dict, 'nav_on': nav_on}
    except:
        return redirect(url_for('index.login'))