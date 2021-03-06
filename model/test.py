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

    def __init__(self, UserName, UserPwd, RegTime, ID, IsEnable, LastLoginIP, LastLoginTM, IsSystem, RoleID, AgentID,
                 PowerList):
        self.ID = ID
        self.UserName = UserName
        self.AgentID = AgentID
        self.PowerList = PowerList
        self.UserPwd = UserPwd
        self.RegTime = RegTime
        self.IsEnable = IsEnable
        self.LastLoginIP = LastLoginIP
        self.LastLoginTM = LastLoginTM
        self.IsSystem = IsSystem
        self.RoleID = RoleID

    def to_json(self):
        return {
            'ID': self.ID,
            'UserName': self.UserName,
            'AgentID': self.AgentID,
            'RoleID': self.RoleID,
            'RegTime': self.RegTime.strftime("%Y-%m-%d %H:%M:%S"),
            'LastLoginIP': self.LastLoginIP,
            'LastLoginTM': self.LastLoginTM.strftime("%Y-%m-%d %H:%M:%S"),
        }


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
    ConAct = db.Column(db.Integer)

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

    def __init__(self, AgentName, AgentID, ParentID):
        self.AgentName = AgentName
        self.AgentID = AgentID
        self.ParentID = ParentID


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


class Gamelist(db.Model):
    __tablename__ = 'gamelist'
    GameID = db.Column('GameID', db.INTEGER, nullable=False)
    Gid = db.Column('Gid', db.INTEGER, nullable=False, primary_key=True)
    CatID = db.Column('CatID', db.INTEGER, nullable=False)
    GameName = db.Column('GameName', db.String(20), nullable=False)
    Version = db.Column('Version', db.INTEGER)
    PackageName = db.Column('PackageName', db.String(50))
    IsEnable = db.Column('IsEnable', db.INTEGER, nullable=False, server_default='0')
    SortNum = db.Column('SortNum', db.INTEGER)
    Status = db.Column('Status', db.INTEGER, nullable=False, server_default='0')
    SeatNum = db.Column('SeatNum', db.INTEGER)
    AlgoType = db.Column('AlgoType', db.INTEGER)

    def __init__(self, GameName, Gid, GameID):
        self.Gid = Gid
        self.GameName = GameName
        self.GameID = GameID
class Partner(db.Model):
    __tablename__ = 'partner'

    PartnerID = db.Column(db.INTEGER, primary_key=True)
    PartnerName = db.Column(db.String(100), nullable=False)
    Name = db.Column(db.String(100))
    Mobile = db.Column(CHAR(11))
    Email = db.Column(db.String(50))
    Type = db.Column(db.INTEGER)
    ExcjamgeRate = db.Column(DECIMAL(10, 4), nullable=False)
    ServerIP = db.Column(db.String(100))
    ServerPort = db.Column(db.INTEGER)
    IsWeiXinpay = db.Column(db.INTEGER, nullable=False, server_default="0")
    IsAlipay = db.Column(db.INTEGER, nullable=False, server_default="0")
    IsCardpay = db.Column(db.INTEGER, nullable=False, server_default="0")
    PayUrl = db.Column(db.String(300))
    ExchangeUrl = db.Column(db.String(300))
    DownUrl = db.Column(db.String(200))
    ApkUrl = db.Column(db.String(200))
    AndroidApkUrl = db.Column(db.String(200))
    AndroidUrl = db.Column(db.String(200))
    IosUrl = db.Column(db.String(200))
    IsEnable = db.Column(db.INTEGER, nullable=False)
    Adder = db.Column(db.String(50))
    LastEditor = db.Column(db.String(50))
    RegTime = db.Column(db.TIMESTAMP, nullable=False)
    LastUpdateTM = db.Column(db.TIMESTAMP, server_default='0000-00-00 00:00:00')
    IsFree = db.Column(db.INTEGER, nullable=False, server_default="0")
    PayType = db.Column(db.INTEGER, nullable=False, server_default="0")
    PreSales = db.Column(db.String(50))
    PreSalesNo = db.Column(db.String(20))
    AfterSales = db.Column(db.String(50))
    AfterSalesNo = db.Column(db.String(20))
    AgentNum = db.Column(db.INTEGER)
    AloneNum = db.Column(db.INTEGER)
    DeskNum = db.Column(db.Text)
    DomainUrl = db.Column(db.String(200))
    DenomRate = db.Column(db.INTEGER)
    Isjbpay = db.Column(db.INTEGER, server_default="0")
    Isjtpay = db.Column(db.INTEGER, server_default="0")
    JbpayNo = db.Column(db.String(50))
    RedType = db.Column(db.INTEGER, server_default="0")
    wxappid = db.Column(db.String(50))
    wxappsecret = db.Column(db.String(50))
    Clientype = db.Column(db.INTEGER, server_default="0")
    Is_Rate = db.Column(db.INTEGER, nullable=False, server_default="0")

    def __init__(self, ExcjamgeRate):
        self.ExcjamgeRate = ExcjamgeRate
