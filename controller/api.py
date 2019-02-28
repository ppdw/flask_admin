import hashlib, time
from flask import url_for, redirect, session
from functools import wraps
from model.test import Admin, Role,db
from config.permission import Permission
from config.public import Public
from collections import defaultdict
from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify



# 检查权限
def checkpower(power):
    return ''

# 点击记忆
def last_nav():
    nav_on = request.args.get("nav_on")
    return nav_on
# 初始化导航
def init_nav():
    admin_id = session.get('admin_id')
    admin_info = Admin.query.filter_by(ID=admin_id).first()
    powerlist = defaultdict(lambda: defaultdict(lambda: 0))  # 声明一个二维dict
    if admin_info.IsSystem == 1:
        # powerlist = Permission.ADMIN_ACTION
         powerlist = Permission.LEFT_NAV
    else:
        admin_role_id = admin_info.RoleID
        try:
            role_info = Role.query.filter_by(RoleID=admin_role_id).first()
            # all_power = get_all_power()
            if role_info.IsEnable == 1:
                mypower = role_info.PowerList
                for k,v in Permission.LEFT_NAV.items():
                    for k1,v1 in v.items():
                        if k1 in mypower:
                            print('成功')
                            powerlist[k][k1]=v1
                print(powerlist)
            else:
                powerlist = ''
        except:     # 查询不到对应的role_id,返回空列表
            powerlist = ''
    return powerlist

# 取出所有权限
def get_all_power():
    powerall_dict = Permission.ADMIN_ACTION
    powerlist = []
    for k, v in powerall_dict.items():
        for k1 in v.values():
            for k2 in k1.keys():
                powerlist.append(k2)
    return powerlist



# 判断是否登陆
def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        admin_user = session.get('admin_user')
        if admin_user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.login'))

    return check_login


# 创建密码
def create_pwd(pwd, time):
    salt = Public.PWD_KEY
    return md5(md5(pwd) + salt + md5(str(int(time / 2))))


# md5 32位小写
def md5(str):
    return hashlib.md5(str.encode(encoding='utf-8')).hexdigest()


# 转化linux时间戳
def strtotime(date):
    timeArray = time.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
