from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify, json
from controller import api
from config.public import Public
from model.test import Admin,Agent

manager_blueprint = Blueprint('manager', __name__, template_folder='templates', static_folder='static')


@manager_blueprint.route('/user/')
def user():
    if not api.checkpower('manager.user'):
        return render_template('Public_error.html')
    admin_id = session.get('admin_id')
    admin_info = Admin.query.filter_by(ID=admin_id).first()
    admin_agentid = admin_info.AgentID
    agent_info = Agent.query.filter_by(AgentID=admin_agentid).first()
    agentid = request.form.get("agentid")
    keyword = request.form.get("keyword",'')
    roomid = request.form.get("roomid")
    return render_template('Manager_user.html',page=1)


@manager_blueprint.route('/ajax_online_user/', methods=['POST'])
def ajax_online_user():
    cgi_url = Public.user_cgi + "?method=accountcgi_get_user_online_pinpai_auto"
    gameid = request.form.get("gameid")
    gameids = request.form.get("gameids")
    agentid = request.form.get("agentid")
    p = request.form.get("p")
    usertype = request.form.get("usertype")
    sorttype = request.form.get("sorttype")
    userid = request.form.get("userid")
    refreshtype = request.form.get("refreshtype")
    roomid = request.form.get("roomid")
    gameid2 = request.form.get("gameid2")
    print("gameid", gameid)
    print("gameids", gameids)
    print("agentid", agentid)
    print("p", p)
    print("usertype", usertype)
    print("sorttype", sorttype)
    print("userid", userid)
    print("refreshtype", refreshtype)
    print("roomid", roomid)
    print("gameid2", gameid2)
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
    user_info = api.fpost(cgi_url, data)
    temp = []
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
