from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify,json
from model.test import Admin, db,Adminactionlog
from controller import api
from controller.api import is_login
from config.permission import Permission
import datetime, time


admin_blueprint = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@admin_blueprint.route('/index/')
def index():
    nav_dict = api.init_nav()
    nav_on = api.last_nav()
    return render_template('Admin_index.html', nav_dict=nav_dict, nav_on=nav_on)


@admin_blueprint.route('/info/')
@is_login
def info():
    nav_dict = api.init_nav()
    return render_template('Admin_info.html', nav_dict=nav_dict)


# 登陆页面
@admin_blueprint.route('/')
def login():
    return render_template('Admin_login.html')


# 登陆验证
@admin_blueprint.route('/act_admin_login/', methods=['POST'])
def act_admin_login():
    admin_user = request.form['admin_user']
    admin_pwd = request.form['admin_pwd']
    print(admin_pwd)
    try:
        admin_info = Admin.query.filter_by(UserName=admin_user).first()
        my_pwd = api.create_pwd(admin_pwd, api.strtotime(admin_info.RegTime))
        if my_pwd == admin_info.UserPwd:
            session['admin_id'] = admin_info.ID
            session['admin_user'] = admin_user
            return jsonify({'error': 0, 'info': '登录成功', 'href': '/index'})
        else:
            return jsonify({'error': 1, 'info': '密码错误'})

    except:
        return jsonify({'error': 1, 'info': '用户不存在'})


# 退出登陆
@admin_blueprint.route('/logout/')
def logout():
    session.clear()
    # 跳转到登录页面
    return redirect(url_for('admin.login'))


# 管理员日志
@admin_blueprint.route('/log/')
def log():
    nav_dict = api.init_nav()
    nav_on = api.last_nav()
    keyword = request.args.get("keyword")
    if keyword == None:
        keyword = ''
    starttime = (datetime.datetime.now()-datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    endtime = datetime.datetime.now().strftime('%Y-%m-%d')
    return render_template('Admin_log.html', nav_dict=nav_dict, nav_on=nav_on, starttime=starttime, endtime=endtime,
                           keyword=keyword)


# 管理员日志刷新
@admin_blueprint.route('/ajax_log/')
def ajax_log():
    page = int(request.args.get("p"))
    keyword = request.args.get("keyword")
    date_picker = request.args.get("date_picker")
    date_arr = date_picker.split('- ')
    starttime = date_arr[0]
    endtime = date_arr[1]
    log_info = Adminactionlog.query.order_by(Adminactionlog.InputDate.desc()).paginate(page=page,per_page=15).items
    # log_info = Adminactionlog.query.all()
    # for a in log_info:
    #     print(a.ActionContent)
    temp = []
    for x in log_info:
        temp.append(x.to_json())
    return json.dumps(temp)

