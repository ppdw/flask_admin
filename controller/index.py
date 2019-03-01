from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
from controller import api
from controller.api import is_login
from model.test import Admin, Role, Agent

index_blueprint = Blueprint('index', __name__, template_folder='templates', static_folder='static')


@index_blueprint.route('/index/')
@is_login
def index():
    admin_id = session.get('admin_id')
    admin_info = Admin.query.filter_by(ID=admin_id).first()
    user_ip = request.remote_addr
    if admin_info.RoleID == 0 and admin_info.IsSystem == 1:
        role_name = '超级管理员'
        agent_name = '总代理'
    else:
        if admin_info.AgentID == 0 or admin_info.AgentID == 1:
            agent_name = '顶级代理'
            role_info = Role.query.filter_by(RoleID=admin_info.RoleID).first()
            role_name = role_info.RoleName
        else:
            role_info = Role.query.filter_by(RoleID=admin_info.RoleID).first()
            role_name = role_info.RoleName
            agent_info = Agent.query.filter_by(AgentID=admin_info.AgentID).first()
            agent_name = agent_info.AgentName
    nav_dict = api.init_nav()
    return render_template('Index_index.html', admin_info=admin_info, role_name=role_name, user_ip=user_ip,
                           agent_name=agent_name, nav_dict=nav_dict)


#进入登录页面
@index_blueprint.route('/')
def login():
    return render_template('Admin_login.html')
