import os
import redis

from datetime import timedelta
from flask import Flask
from model.test import db
from flask_session import Session

from controller.admin import admin_blueprint
from controller.index import index_blueprint
from controller.agent import agent_blueprint
from controller.card import card_blueprint
from controller.data import data_blueprint
from controller.function import function_blueprint
from controller.game import game_blueprint
from controller.manager import manager_blueprint
from controller.partner import partner_blueprint
from controller.robot import robot_blueprint
from controller.role import role_blueprint
from controller.sale import sale_blueprint
from controller.sysmsg import sysmsg_blueprint
from controller.user import user_blueprint
from controller.nav import nav_blueprint


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')
    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)
    app.register_blueprint(blueprint=admin_blueprint, url_prefix='/admin')
    app.register_blueprint(blueprint=index_blueprint, url_prefix='/index')
    app.register_blueprint(blueprint=agent_blueprint, url_prefix='/agent')
    app.register_blueprint(blueprint=card_blueprint, url_prefix='/card')
    app.register_blueprint(blueprint=data_blueprint, url_prefix='/data')
    app.register_blueprint(blueprint=function_blueprint, url_prefix='/function')
    app.register_blueprint(blueprint=game_blueprint, url_prefix='/game')
    app.register_blueprint(blueprint=manager_blueprint, url_prefix='/manager')
    app.register_blueprint(blueprint=partner_blueprint, url_prefix='/partner')
    app.register_blueprint(blueprint=robot_blueprint, url_prefix='/robot')
    app.register_blueprint(blueprint=role_blueprint, url_prefix='/role')
    app.register_blueprint(blueprint=sale_blueprint, url_prefix='/sale')
    app.register_blueprint(blueprint=sysmsg_blueprint, url_prefix='/sysmsg')
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=nav_blueprint, url_prefix='/nav')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@47.92.247.134:3306/WebDB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 设置session密钥
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
    # 设置连接的redis数据库 默认连接到本地6379
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
    app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)  # 设置session过期时间
    # 设置远程
    app.config['SESSION_REDIS'] = redis.Redis(host='47.92.247.134', port=5001, password='')
    Session(app)

    db.init_app(app=app)
    with app.app_context():
        db.create_all()
        
    return app
