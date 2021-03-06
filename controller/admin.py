from flask import Blueprint, redirect, render_template, \
    request, url_for, session, jsonify, json
from model.test import Admin, db, Adminactionlog, Agent, Role
from controller import api
from controller.api import is_login
from config.permission import Permission
import datetime

admin_blueprint = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
log_data = {}


@admin_blueprint.route('/index/')
def index():
    admin_info = Admin.query.filter_by().all()
    user_list = []
    for admin_name in admin_info:
        user_list.append(admin_name.UserName)
    user_list.remove('vipadmin')
    return render_template('Admin_index.html', user_list=user_list)


# 管理员列表
@admin_blueprint.route('/admin_index/', methods=['GET'])
def admin_index():
    page = int(request.args['page'])
    param = []
    temp_dict = {}
    if ('admin_info' in request.args) and (request.args['admin_info']):
        admin_info = request.args['admin_info']
        param.append(Admin.UserName == admin_info)
    admin_all = Admin.query.filter(*param).order_by(Admin.ID.desc()).paginate(page=page, per_page=15)
    pages = admin_all.pages
    admin_all = admin_all.items
    temp = []
    for i in admin_all:
        if i.UserName != 'vipadmin':
            temp.append(i.to_json())
    for admin_list in temp:
        if admin_list['RoleID'] != 0:
            admin_list['RoleID'] = (Role.query.filter_by(RoleID=admin_list['RoleID']).first()).RoleName
        else:
            admin_list['RoleID'] = '超级管理员'
        if admin_list['AgentID'] != 0 | admin_list['AgentID'] != 1:
            admin_list['AgentID'] = (Agent.query.filter_by(AgentID=admin_list['AgentID']).first()).AgentName
        else:
            admin_list['AgentID'] = '平台'

    temp_dict['data'] = temp
    temp_dict['pages'] = pages

    return json.dumps(temp_dict)


# 管理员信息
@admin_blueprint.route('/info/', methods=['GET'])
@is_login
def info():
    admin_sign = int(request.args['id'])
    print(admin_sign, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    return render_template('Admin_info.html')


# 编辑/添加管理员
@admin_blueprint.route('/edit/', methods=['POST'])
def edit():
    new_password = request.form['reUserPwd']
    print(new_password)
    if new_password == '':
        exit()
    else:
        admin_id = session.get('admin_id')
        admin_info = Admin.query.filter_by(ID=admin_id).first()
        ChangeTime = datetime.datetime.now()
        my_pwd = api.create_pwd(new_password, api.strtotime(ChangeTime))
        admin_info.UserPwd = my_pwd
        admin_info.RegTime = ChangeTime
        db.session.commit()
        log_data['ActionName'] = '管理员类控制器'
        log_data['ActionContent'] = '编辑管理员(' + str(admin_info.UserName) + '),管理员ID为' + str(admin_id)
        api.adminlogs(log_data)
        if not admin_info:
            return
        jumpurl = 'www.baidu.com'
        return render_template('Public_success.html', jumpurl=jumpurl)


# 删除管理员
@admin_blueprint.route('/delete_admin/', methods=['GET'])
def delete_admin():
    admin_user = session.get('admin_user')
    delete_id = request.args['delete_id']
    try:
        del_id = Admin.query.filter_by(ID=delete_id).first()
        if del_id.UserName == 'admin':
            return jsonify({'error': 1, 'msg': '管理员admin不能被删除', 'info': '/admin/admin_index/'})
        del_name = del_id.UserName
        db.session.delete(del_id)
        db.session.commit()
        log_data['ActionName'] = Permission.ACTION_NAME[5]
        log_data['ActionContent'] = '管理员' + str(admin_user) + '删除了管理员:' + str(del_name) + '(ID:' + str(delete_id) + ')'
        api.adminlogs(log_data)
        return jsonify({'error': 0, 'msg': '删除成功', 'info': '/admin/admin_index/'})
    except:
        return jsonify({'error': 1, 'msg': '管理员不存在', 'info': '/admin/admin_index/'})


# 登陆验证
@admin_blueprint.route('/act_admin_login/', methods=['POST'])
def act_admin_login():
    admin_user = request.form['admin_user']
    admin_pwd = request.form['admin_pwd']
    try:
        admin_info = Admin.query.filter_by(UserName=admin_user).first()
        my_pwd = api.create_pwd(admin_pwd, api.strtotime(admin_info.RegTime))
        if my_pwd == admin_info.UserPwd:
            session['admin_id'] = admin_info.ID
            session['admin_user'] = admin_user
            log_data['ActionName'] = Permission.ACTION_NAME[1]
            log_data['ActionContent'] = '管理员：' + str(admin_user) + '登入后台'
            api.adminlogs(log_data)
            admin_info.LastLoginTM = datetime.datetime.now()
            admin_info.LoginCount = int(admin_info.LoginCount) + 1
            admin_info.LastLoginIP = request.remote_addr
            db.session.commit()
            return jsonify({'error': 0, 'info': '登录成功', 'href': '/index/index/'})
        else:
            return jsonify({'error': 1, 'info': '密码错误'})
    except:
        return jsonify({'error': 1, 'info': '用户不存在'})


# 退出登陆
@admin_blueprint.route('/logout/')
def logout():
    session.clear()
    # 跳转到登录页面
    return redirect(url_for('index.login'))


# 管理员日志
@admin_blueprint.route('/log/')
def log():
    admin_user = session.get('admin_user')
    admin_info = Admin.query.filter_by().all()
    user_list = []
    for admin_name in admin_info:
        user_list.append(admin_name.UserName)
    if admin_user != 'vipadmin':
        try:
            user_list.remove('vipadmin')
        except:
            pass
    return render_template('Admin_log.html', user_list=user_list, ACTION_NAME=Permission.ACTION_NAME)


# 管理员日志刷新
@admin_blueprint.route('/ajax_log/', methods=['GET'])
def ajax_log():
    admin_name = session.get('admin_user')
    temp_dict = {}
    page = int(request.args['page'])
    date_picker = request.args['date_time']
    date_arr = date_picker.split('- ')
    starttime = date_arr[0] + ' 00:00:00'
    endtime = date_arr[1] + ' 23:59:59'
    param = []
    if ('admin_info' in request.args) and (request.args['admin_info']):
        admin_info = request.args['admin_info']
        param.append(Adminactionlog.AdminUser == admin_info)
    if ('action_name' in request.args) and (request.args['action_name']):
        action_name = request.args['action_name']
        param.append(Adminactionlog.ActionName == action_name)
    # vipadmin 管理员能看所有日志，包括已删除的日志
    if admin_name != 'vipadmin':
        param.append(Adminactionlog.ConAct == 0)
    param.append(Adminactionlog.InputDate >= starttime)
    param.append(Adminactionlog.InputDate <= endtime)
    log_info = Adminactionlog.query.filter(*param).order_by(Adminactionlog.InputDate.desc()).paginate(page=page,
                                                                                                      per_page=15)
    pages = log_info.pages
    log_info = log_info.items
    temp = []
    for x in log_info:
        temp.append(x.to_json())
    # 将数据存入字典
    temp_dict['data'] = temp
    temp_dict['pages'] = pages

    return json.dumps(temp_dict)


# 删除管理员日志
@admin_blueprint.route('/delete_logs/', methods=['GET'])
def delete_logs():
    if not api.checkpower('admin.delete_logs'):
        return render_template('Public_error.html')
    admin_user = session.get('admin_user')
    delete_id = request.args['delete_id']
    try:
        del_id = Adminactionlog.query.filter_by(ID=delete_id).first()
        if del_id.ConAct == 1:
            return jsonify({'error': 1, 'info': '日志已被删除', 'href': '/admin/log/'})
        # 防止管理员重复删除日志
        if del_id.ActionName != Permission.ACTION_NAME[4]:
            del_id.ConAct = 1
            db.session.add(del_id)
            db.session.commit()
            log_data['ActionName'] = Permission.ACTION_NAME[4]
            log_data['ActionContent'] = '管理员：' + str(admin_user) + '删除了日志 ID: ' + str(delete_id)
            api.adminlogs(log_data)
            return jsonify({'error': 0, 'info': '日志删除成功', 'href': '/admin/log/'})
        return jsonify({'error': 2, 'info': '删除日志失败', 'href': '/admin/log/'})
    except:
        return jsonify({'error': 3, 'info': '日志不存在', 'href': '/admin/log/'})


@admin_blueprint.context_processor
def my_context_processor():
    try:
        admin_user = session.get('admin_user')
        nav_dict = api.init_nav()
        nav_on = api.last_nav()
        return {'nav_dict': nav_dict, 'nav_on': nav_on, 'admin_user': admin_user}
    except:
        return redirect(url_for('index.login'))
