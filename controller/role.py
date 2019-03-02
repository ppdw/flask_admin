from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
from controller import api
from model.test import Role, db

import json

role_blueprint = Blueprint('role', __name__, template_folder='templates', static_folder='static')


@role_blueprint.route('/index/')
def index():
    return render_template('Role_index.html')


# 加载角色权限列表
@role_blueprint.route('/ajax_role/')
def ajax_role():
    rolelist = Role.query.all()
    temp = []
    for x in rolelist:
        temp.append(x.to_json())
    return json.dumps(temp)


# 角色权限
@role_blueprint.route('/info/', methods=['GET', 'POST'])
def info():
    role_info = ''
    id = request.args.get("id")
    return render_template('Role_info.html', role_info=role_info, id=id)


@role_blueprint.route('/insert/', methods=['POST'])
def insert():
    id = request.form['id']
    RoleName = request.form['RoleName']
    RoleDesc = request.form['RoleDesc']
    IsEnable = request.form['IsEnable']
    ParentID = session.get('admin_id')
    print(id)
    return ''
@role_blueprint.context_processor
def my_context_processor():
    try:
        nav_dict = api.init_nav()
        nav_on = api.last_nav()
        return {'nav_dict': nav_dict, 'nav_on': nav_on}
    except:
        return redirect(url_for('index.login'))