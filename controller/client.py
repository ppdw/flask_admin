from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
from controller import api
from config.public import Public
from model.test import Partner
client_blueprint = Blueprint('client', __name__, template_folder='templates', static_folder='static')

@client_blueprint.route('/request_denomination/')
def request_denomination():
    pid = request.form.get('areaid',default=0)
    agentid = request.form.get('agentid',default=0)
    uid = request.form.get('uid',default=0)
    time = request.form.get('itime',default=0)
    code = request.form.get('code',default='')
    # if uid==0 or time==0:
    #     return jsonify({'retcode': 2, 'msg': '用户id或时间不能为空'})
    # checkcode = api.md5(uid+"|"+time+"|"+ Public.CLIENT_KEY)
    # if code != checkcode:
    #     return jsonify({'retcode': 1, 'msg': '校验码错误'})
    # if agentid>0:
    #     pass #(这里可以填充独立充值，目前无视)

    partner_info = Partner.query.filter_by().first()
    rate = partner_info.ExcjamgeRate
    print(rate)
    pass