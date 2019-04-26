from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
from controller import api
from model.test import Role, db, Admin
from config.permission import Permission

import json

role_blueprint = Blueprint('role', __name__, template_folder='templates', static_folder='static')
log_data = {}


@role_blueprint.route('/index/')
def index():
    return render_template('Role_index.html')


# 加载角色权限列表
@role_blueprint.route('/ajax_role/')
def ajax_role():
    param = []
    temp_dict = {}
    page = int(request.args['page'])
    if ('reserv' in request.args) and (request.args['reserv']):
        reserv = request.args['reserv']
        # 模糊查询
        param.append(Role.RoleName.contains(reserv))
    role_list = Role.query.filter(*param).order_by(Role.RoleID.desc()).paginate(page=page, per_page=15)
    pages = role_list.pages
    role_list = role_list.items
    temp = []
    for x in role_list:
        temp.append(x.to_json())

    temp_dict['data'] = temp
    temp_dict['pages'] = pages
    return json.dumps(temp_dict)


# 删除角色权限
@role_blueprint.route('/delete/', methods=['GET'])
def delete():
    admin_user = session.get('admin_user')
    delete_id = request.args['delete_id']
    admin_role = Admin.query.filter_by(RoleID=delete_id).first()
    print(admin_role)
    if not admin_role:
        try:
            del_id = Role.query.filter_by(RoleID=delete_id).first()
            db.session.delete(del_id)
            db.session.commit()
            log_data['ActionName'] = Permission.ACTION_NAME[6]
            log_data['ActionContent'] = '管理员: ' + str(admin_user) + '删除角色权限: ' + str(del_id.RoleName) + '(ID: ' + str(
                delete_id) + ')'
            api.adminlogs(log_data)
            return jsonify({'error': 0, 'info': '删除角色成功', 'href': '/role/index/'})
        except:
            return jsonify({'error': 1, 'info': '删除角色权限失败', 'href': '/role/index/'})
    return jsonify({'error': 2, 'info': '该角色权限已绑定管理员', 'href': '/role/index/'})


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
