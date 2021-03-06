import hashlib, time, requests
import datetime
import random
from urllib import parse
import http.client
import json
from flask import url_for, redirect, session
from functools import wraps
from model.test import Admin, Role, db, Adminactionlog, Agent
from config.permission import Permission
from config.public import Public
from collections import defaultdict
from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify


# 检查权限
def checkpower(power):
    admin_id = session.get('admin_id')
    admin_info = Admin.query.filter_by(ID=admin_id).first()
    if admin_info.IsSystem == 1:
        return True
    else:
        admin_role_id = admin_info.RoleID
        try:
            role_info = Role.query.filter_by(RoleID=admin_role_id).first()
            if role_info.IsEnable == 1:
                mypower = role_info.PowerList
                if str(power) in str(mypower):
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False


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
        powerlist = Permission.LEFT_NAV
    else:
        admin_role_id = admin_info.RoleID
        try:
            role_info = Role.query.filter_by(RoleID=admin_role_id).first()
            if role_info.IsEnable == 1:
                mypower = role_info.PowerList
                for k, v in Permission.LEFT_NAV.items():
                    for k1, v1 in v.items():
                        if k1 in mypower:
                            powerlist[k][k1] = v1
            else:
                powerlist = ''
        except:  # 查询不到对应的role_id,返回空列表
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


# 获取当前管理员/代理所有下级代理 递归
def get_child_agent(agent_id):
    all_agent_list = defaultdict(lambda: defaultdict(lambda: 0))
    lev = 0
    if agent_id <= 1:
        all_agent_list['html'][0] = '所有代理'
        all_agent_list['html'][1] = '平台'
        all_agent_list[0] = {'Level': 0, 'AgentID': 0, 'AgentName': '所有代理', 'ParentID': None}
        all_agent_list[1] = {'Level': 0, 'AgentID': 1, 'AgentName': '平台', 'ParentID': None}
    else:
        info = Agent.query.filter_by().all
    pass


# 判断是否登陆
def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        admin_user = session.get('admin_user')
        if admin_user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('index.login'))

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
    date = date.strftime('%Y-%m-%d %H:%M:%S')
    timeArray = time.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


# post提交
def fpost(url, data):
    re = requests.post(url, data=data)
    return re.text


# 日志写入
def adminlogs(log_data):
    # 普通管理员记录值为 0
    log_data['ConAct'] = 0
    if "UserID" not in log_data:
        log_data['UserID'] = None
    if "UserName" not in log_data:
        log_data['UserName'] = None
    admin_id = session.get('admin_id')
    admin_info = Admin.query.filter_by(ID=admin_id).first()
    # vipadmin记录值为2
    if str(admin_info.UserName) == 'vipadmin':
        log_data['ConAct'] = 2
    logs = Adminactionlog(ID=0, ActionName=log_data['ActionName'], ActionContent=log_data['ActionContent'],
                          AdminID=admin_id, AdminUser=admin_info.UserName, AdminIP=admin_info.LastLoginIP,
                          UserName=log_data['UserName'], UserID=log_data['UserID'], InputDate=datetime.datetime.now(),
                          PartnerID=admin_info.PartnerID, ConAct=log_data['ConAct'])
    db.session.add(logs)
    db.session.commit()


# 发送短信
def send_sms(appid, key, mob):
    url = "106.ihuyi.com"
    send_url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"
    num_code = _random(4)
    content = ''.join(['您的验证码是：', num_code, '。请不要把验证码泄露给其他人。'])
    # print(content)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    body = parse.urlencode(
        {'account': appid, 'password': key, 'content': content, 'mobile': mob, 'format': 'json'})
    conn = http.client.HTTPConnection(url)
    conn.request(method='POST', url=send_url, headers=headers, body=body)
    response = conn.getresponse()
    # print(response.status)
    response_str = response.read()
    print(response_str)
    json.loads(response_str)  # 将response_str的json格式转换为python格式的字符串
    conn.close()
    return response_str


# 随机数
def _random(nums):
    nums = nums
    code = ''.join(str(i) for i in random.sample(range(0, 9), nums))
    return code
