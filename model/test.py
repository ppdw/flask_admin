from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, String, TIMESTAMP, Table, Text
from sqlalchemy.dialects.mysql import BIGINT, BIT, INTEGER, TINYINT, TINYTEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
metadata = Base.metadata
db = SQLAlchemy()


class Admin(db.Model):
    __tablename__ = 'admin'

    ID = db.Column(db.INTEGER, primary_key=True)
    UserName = db.Column(db.String(50), nullable=False)
    UserPwd = db.Column(db.String(32), nullable=False)
    Name = db.Column(db.Text)
    Phone = db.Column(db.String(11))
    LoginCount = db.Column(db.INTEGER, nullable=False, server_default='0')
    RoleID = db.Column(db.INTEGER, nullable=False, server_default='0')
    IsSystem = db.Column(db.INTEGER, nullable=False, server_default='0')
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default='0')
    PwdErrorCount = db.Column(db.INTEGER, nullable=False, server_default='0')
    PwdErrorDate = db.Column(db.TIMESTAMP)
    RegTime = db.Column(db.TIMESTAMP, nullable=False)
    LastLoginIP = db.Column(db.String(15))
    LastLoginTM = db.Column(db.TIMESTAMP)
    PrevLoginTM = db.Column(db.TIMESTAMP)
    PartnerID = db.Column(db.INTEGER, nullable=False, server_default='0')
    AgentID = db.Column(db.INTEGER, nullable=False, server_default='0')
    ParentID = db.Column(db.INTEGER, nullable=False, server_default='0')
    PowerList = db.Column(db.Text)
    NavList = db.Column(db.String(200))
    LastUpdateTM = db.Column(db.TIMESTAMP, nullable=False)
    CheckCode = db.Column(CHAR(32))
    mac = db.Column(db.Text)
    mac_num = db.Column(db.INTEGER, server_default='3')
    Sign = db.Column(db.String(50), server_default='3')
    IsAllOrder = db.Column(db.INTEGER, nullable=False, server_default='0')

    def __init__(self, UserName, UserPwd, RegTime, ID, IsEnable, LastLoginIP, LastLoginTM, IsSystem, RoleID, AgentID):
        self.ID = ID
        self.UserName = UserName
        self.UserPwd = UserPwd
        self.RegTime = RegTime
        self.IsEnable = IsEnable
        self.LastLoginIP = LastLoginIP
        self.LastLoginTM = LastLoginTM
        self.IsSystem = IsSystem
        self.RoleID = RoleID
        self.AgentID = AgentID


class Adminactionlog(db.Model):
    __tablename__ = 'adminactionlogs'

    ID = db.Column(db.INTEGER, primary_key=True)
    ActionName = db.Column(db.Text, nullable=False)
    ActionContent = db.Column(db.Text, nullable=False)
    AdminID = db.Column(db.INTEGER, nullable=False)
    AdminUser = db.Column(db.String(50))
    AdminIP = db.Column(db.String(15))
    UserName = db.Column(db.String(50))
    UserID = db.Column(db.Text)
    InputDate = db.Column(db.TIMESTAMP, nullable=False)
    PartnerID = db.Column(db.INTEGER, nullable=False, server_default='0')
    ConAct = db.Column(db.String(50))

    def __init__(self, ID, ActionName, ActionContent, AdminID, AdminUser, AdminIP, UserName, UserID, InputDate,
                 PartnerID, ConAct):
        self.ID = ID
        self.ActionName = ActionName
        self.ActionContent = ActionContent
        self.AdminID = AdminID
        self.AdminUser = AdminUser
        self.AdminIP = AdminIP
        self.UserName = UserName
        self.UserID = UserID
        self.InputDate = InputDate
        self.PartnerID = PartnerID
        self.ConAct = ConAct

    def to_json(self):
        return {
            'ID': self.ID,
            'ActionName': self.ActionName,
            'ActionContent': self.ActionContent,
            'AdminID': self.AdminID,
            'AdminUser': self.AdminUser,
            'AdminIP': self.AdminIP,
            'UserName': self.UserName,
            'UserID': self.UserID,
            'InputDate': self.InputDate.strftime("%Y-%m-%d %H:%M:%S"),
            'PartnerID': self.PartnerID,
            'ConAct': self.ConAct,

        }


class Agent(db.Model):
    __tablename__ = 'agent'

    AgentID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    ParentID = db.Column(db.INTEGER, nullable=False)
    AgentName = db.Column(db.String(50), nullable=False)
    Level = db.Column(db.INTEGER, nullable=False, server_default='0')
    MinPay = db.Column(db.INTEGER, nullable=False)
    InviteCode = db.Column(db.INTEGER, nullable=False)
    ServiceFee = db.Column(db.INTEGER, nullable=False)
    IsAlone = db.Column(db.INTEGER, nullable=False, server_default='0')
    IsTran = db.Column(db.INTEGER, nullable=False, server_default='0')
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default='0')
    IsDelete = db.Column(db.INTEGER, nullable=False, server_default='0')
    RegTime = db.Column(db.TIMESTAMP, nullable=False)
    UserID = db.Column(db.INTEGER, nullable=False, server_default='0')
    UpdateTime = db.Column(DateTime)
    LastLoginTM = db.Column(DateTime)
    payway = db.Column(db.String(200))
    payname = db.Column(db.String(200))
    payuser = db.Column(db.String(200))
    tel = db.Column(db.String(200))
    ShowRate = db.Column(db.INTEGER, nullable=False, server_default='0')
    PayType = db.Column(db.INTEGER, nullable=False, server_default='0')
    opennum = db.Column(db.INTEGER, nullable=False, server_default='0')
    PowerList = db.Column(db.Text)

    def __init__(self, AgentName):
        self.AgentName = AgentName


class Role(db.Model):
    __tablename__ = 'role'
    RoleID = db.Column(db.INTEGER, primary_key=True)
    RoleName = db.Column(db.String(30), nullable=False)
    RoleDesc = db.Column(db.String(100))
    PowerList = db.Column(db.Text)
    IsEnable = db.Column(db.INTEGER, server_default='0')
    PartnerID = db.Column(db.INTEGER, nullable=False)
    ParentID = db.Column(db.INTEGER, nullable=False)

    def __init__(self, RoleID, RoleName, RoleDesc, PowerList, IsEnable):
        self.RoleID = RoleID
        self.RoleName = RoleName
        self.RoleDesc = RoleDesc
        self.PowerList = PowerList
        self.IsEnable = IsEnable

    def to_json(self):
        return {
            'RoleID': self.RoleID,
            'RoleName': self.RoleName,
            'RoleDesc': self.RoleDesc,
            'PowerList': self.PowerList,
            'IsEnable': self.IsEnable,
        }
