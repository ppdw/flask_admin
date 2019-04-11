from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify, json
from controller import api
from config.public import Public
from model.test import Admin, Agent, Gamelist, db
import time
import datetime

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
    keyword = request.form.get("keyword", '')
    roomid = request.form.get("roomid")
    return render_template('Manager_user.html', page=1, admin_agentid=admin_agentid)


@manager_blueprint.route('/ajax_online_user/', methods=['POST'])
def ajax_online_user():
    admin_id = session.get('admin_id')
    admin_info = Admin.query.filter_by(ID=admin_id).first()
    admin_agentid = admin_info.AgentID
    pid = admin_info.PartnerID
    currtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间
    format_currtime = time.strptime(currtime, "%Y-%m-%d %H:%M:%S")  # 格式化时间
    unix_currtime = int(time.mktime(format_currtime))  # 转换成unix时间戳

    cgi_url = Public.user_cgi + "?method=accountcgi_get_user_online_pinpai_auto"
    data = {
        'agentids': 0,
        'agentid': admin_agentid,
        'gameid': 0,
        'gameids': '',
        'usertype': 0,
        'sorttype': 0,
        'page': 1,
        'size': 25,
        'pid': pid,
        'time': unix_currtime,
        'code': api.md5(str(int(unix_currtime / 2))),
    }
    user_info_json = api.fpost(cgi_url, data)
    user_info_dict = json.loads(user_info_json)
    for temp in user_info_dict['data']:
        agentid = temp['agentid']
        temp['registertime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(temp['registertime']))
        if agentid == 1 or agentid == 0:
            temp['agentname'] = '平台'
        else:
            try:
                agent_info = Agent.query.filter_by(AgentID=agentid).first()
                temp['agentname'] = agent_info.AgentName
            except:
                temp['agentname'] = '未知代理'
        if temp['gameid'] == 0:
            temp['gamename'] = '游戏大厅'
        else:
            try:
                gamelist = Gamelist.query.filter_by(Gid=temp['gameid']).first()
                temp['gamename'] = gamelist.GameName
            except:
                temp['gamename'] = '未知游戏'

    user_info_json = json.dumps(user_info_dict)

    return user_info_json


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
