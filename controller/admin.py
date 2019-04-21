from flask import Blueprint, redirect, render_template, \
    request, url_for, session, jsonify, json
from model.test import Admin, db, Adminactionlog, Agent
from controller import api
from controller.api import is_login
import datetime

admin_blueprint = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
log_data = {}


@admin_blueprint.route('/index/')
def index():
    return render_template('Admin_index.html')


# 管理员信息
@admin_blueprint.route('/info/', methods=['POST', 'GET'])
@is_login
def info():
    if request.method == 'GET':
        admin_id = session.get('admin_id')
        if admin_id:
            admin_info = Admin.query.filter_by(ID=admin_id).first()
        return render_template('Admin_info.html', admin_info=admin_info)
    if request.method == 'POST':
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
            # log_data['ConAct'] = 0
            api.adminlogs(log_data)
            if not admin_info:
                return
            jumpurl = 'www.baidu.com'
            return render_template('Public_success.html', jumpurl=jumpurl)


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
    keyword = request.args.get("keyword")
    if keyword == None:
        keyword = ''
    starttime = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    endtime = datetime.datetime.now().strftime('%Y-%m-%d')
    admin_info = Admin.query.filter_by().all()
    user_list = []
    for admin_name in admin_info:
        user_list.append(admin_name.UserName)
    return render_template('Admin_log.html', starttime=starttime, endtime=endtime,
                           keyword=keyword, user_list=user_list)


# 管理员日志刷新
@admin_blueprint.route('/ajax_log/', methods=['POST'])
def ajax_log():
    # page = request.form['page']
    keyword = request.form['keyword']
    date_picker = request.form['date_time']
    date_arr = date_picker.split('- ')
    starttime = date_arr[0]
    endtime = date_arr[1]
    log_info = Adminactionlog.query.order_by(Adminactionlog.InputDate.desc()).paginate(page=1, per_page=15).items
    # log_info = Adminactionlog.query.all()
    # for a in log_info:
    #     print(a.ActionContent)
    ##
    temp = []
    for x in log_info:
        temp.append(x.to_json())
    return json.dumps(temp)


#
@admin_blueprint.context_processor
def my_context_processor():
    try:
        nav_dict = api.init_nav()
        nav_on = api.last_nav()
        return {'nav_dict': nav_dict, 'nav_on': nav_on}
    except:
        return redirect(url_for('index.login'))
