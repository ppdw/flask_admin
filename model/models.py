# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, String, TIMESTAMP, Table, Text
from sqlalchemy.dialects.mysql import BIGINT, BIT, INTEGER, TINYINT, TINYTEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()
metadata = Base.metadata
db = SQLAlchemy()


class Admin(Base):
    __tablename__ = 'admin'

    ID = db.Column(db.INTEGER, primary_key=True)
    UserName = db.Column(db.String(50), nullable=False)
    UserPwd = db.Column(db.String(32), nullable=False)
    Name = db.Column(db.Text)
    Phone = db.Column(db.String(11))
    LoginCount = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    RoleID = db.Column(db.INTEGER, nullable=False, server_default= Text("0"))
    IsSystem = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PwdErrorCount = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PwdErrorDate = db.Column(db.TIMESTAMP)
    RegTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_TIMESTAMP()"))
    LastLoginIP = db.Column(db.String(15))
    LastLoginTM = db.Column(db.TIMESTAMP)
    PrevLoginTM = db.Column(db.TIMESTAMP)
    PartnerID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    AgentID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    ParentID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PowerList = db.Column(db.Text)
    NavList = db.Column(db.String(200))
    LastUpdateTM = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    CheckCode = db.Column(CHAR(32))
    mac = db.Column(db.Text)
    mac_num = db.Column(db.INTEGER, server_default=Text("3"))
    Sign = db.Column(db.String(50), server_default=Text("'3'"))
    IsAllOrder = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Adminactionlog(Base):
    __tablename__ = 'adminactionlogs'

    ID = db.Column(db.INTEGER, primary_key=True)
    ActionName = db.Column(db.TINYdb.Text, nullable=False)
    ActionContent = db.Column(db.Text, nullable=False)
    AdminID = db.Column(db.INTEGER, nullable=False)
    AdminUser = db.Column(db.String(50))
    AdminIP = db.Column(db.String(15))
    UserName = db.Column(db.String(50))
    UserID = db.Column(db.Text)
    InputDate = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP()"))
    PartnerID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    ConAct = db.Column(db.String(50))


class Agent(Base):
    __tablename__ = 'agent'

    AgentID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    ParentID = db.Column(db.INTEGER, nullable=False)
    AgentName = db.Column(db.String(50), nullable=False)
    Level = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    MinPay = db.Column(db.INTEGER, nullable=False)
    InviteCode = db.Column(db.INTEGER, nullable=False)
    ServiceFee = db.Column(db.INTEGER, nullable=False)
    IsAlone = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsTran = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsDelete = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    RegTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    UserID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    UpdateTime = db.Column(DateTime)
    LastLoginTM = db.Column(DateTime)
    payway = db.Column(db.String(200))
    payname = db.Column(db.String(200))
    payuser = db.Column(db.String(200))
    tel = db.Column(db.String(200))
    ShowRate = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PayType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    opennum = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PowerList = db.Column(db.Text)


class Agentbill(Base):
    __tablename__ = 'agentbill'

    BillID = db.Column(db.INTEGER, primary_key=True)
    AgentID = db.Column(db.INTEGER, nullable=False)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    ApplyID = db.Column(db.INTEGER, nullable=False)
    Gamebi = db.Column(db.INTEGER, nullable=False)
    Status = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    AddTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    LastEditer = db.Column(db.String(100), nullable=False)
    LastTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))


class CustomerConfig(Base):
    __tablename__ = 'customer_config'

    ID = db.Column(db.INTEGER, primary_key=True)
    qq = db.Column(db.String(50), nullable=False)
    weixin = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(200), nullable=False)


class Denomlist(Base):
    __tablename__ = 'denomlist'

    denomid = db.Column(db.INTEGER, primary_key=True)
    denomname = db.Column(db.String(200), nullable=False)
    IsDefault = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    addtime = db.Column(db.TIMESTAMP)


class Funattr(Base):
    __tablename__ = 'funattr'

    FunID = db.Column(db.INTEGER, primary_key=True)
    Content = db.Column(db.String(200))
    Ishow = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Funlist(Base):
    __tablename__ = 'funlist'

    FunID = db.Column(db.INTEGER, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    UiName = db.Column(db.String(200))
    SpriteName = db.Column(db.String(200))
    FunName = db.Column(db.String(200))
    Status = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    Version = db.Column(db.INTEGER)
    SortNum = db.Column(db.INTEGER)
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    ParentID = db.Column(db.INTEGER)
    Type = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Gameattr(Base):
    __tablename__ = 'gameattr'

    AttrID = db.Column(db.INTEGER, primary_key=True)
    Gid = db.Column(db.INTEGER, nullable=False)
    MaxDesk = db.Column(db.INTEGER, nullable=False)
    MaxSeat = db.Column(db.INTEGER, nullable=False)
    MaxNum = db.Column(db.INTEGER, nullable=False)
    DeskNum = db.Column(db.INTEGER)


class Gamebilog(Base):
    __tablename__ = 'gamebilog'

    LogID = db.Column(db.INTEGER, primary_key=True)
    UID = db.Column(db.INTEGER, nullable=False)
    Type = db.Column(db.INTEGER, nullable=False)
    Number = db.Column(BIGINT(20), nullable=False)
    Why = db.Column(db.String(300), nullable=False)
    AddTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))


t_gamelist = Table(
    'gamelist', metadata,
    db.Column('GameID', db.INTEGER, nullable=False),
    db.Column('Gid', db.INTEGER, nullable=False),
    db.Column('CatID', db.INTEGER, nullable=False),
    db.Column('GameName', db.String(20), nullable=False),
    db.Column('Version', db.INTEGER),
    db.Column('PackageName', db.String(50)),
    db.Column('IsEnable', db.INTEGER, nullable=False, server_default=Text("0")),
    db.Column('SortNum', db.INTEGER),
    db.Column('Status', db.INTEGER, nullable=False, server_default=Text("0")),
    db.Column('SeatNum', db.INTEGER),
    db.Column('AlgoType', db.INTEGER)
)


t_news = Table(
    'news', metadata,
    db.Column('ID', db.INTEGER, nullable=False),
    db.Column('Title', db.String(200), nullable=False),
    db.Column('Content', db.Text),
    db.Column('Type', db.INTEGER, server_default=Text("0")),
    db.Column('SendTime', DateTime),
    db.Column('AddTime', DateTime),
    db.Column('IsEnable', db.INTEGER, nullable=False, server_default=Text("0")),
    db.Column('aa', db.INTEGER, nullable=False, server_default=Text("0"))
)


class Partner(Base):
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
    IsWeiXinpay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsAlipay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsCardpay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
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
    RegTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    LastUpdateTM = db.Column(db.TIMESTAMP, server_default=Text("'0000-00-00 00:00:00'"))
    IsFree = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PayType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PreSales = db.Column(db.String(50))
    PreSalesNo = db.Column(db.String(20))
    AfterSales = db.Column(db.String(50))
    AfterSalesNo = db.Column(db.String(20))
    AgentNum = db.Column(db.INTEGER)
    AloneNum = db.Column(db.INTEGER)
    DeskNum = db.Column(db.Text)
    DomainUrl = db.Column(db.String(200))
    DenomRate = db.Column(db.INTEGER)
    Isjbpay = db.Column(db.INTEGER, server_default=Text("0"))
    Isjtpay = db.Column(db.INTEGER, server_default=Text("0"))
    JbpayNo = db.Column(db.String(50))
    RedType = db.Column(db.INTEGER, server_default=Text("0"))
    wxappid = db.Column(db.String(50))
    wxappsecret = db.Column(db.String(50))
    Clientype = db.Column(db.INTEGER, server_default=Text("0"))
    Is_Rate = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Partnerbill(Base):
    __tablename__ = 'partnerbill'

    BillID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    CardpayNum = db.Column(db.INTEGER, nullable=False)
    CardpayMoney = db.Column(DECIMAL(10, 4), nullable=False)
    WeixinpayNum = db.Column(db.INTEGER, nullable=False)
    WeixinPayMoney = db.Column(DECIMAL(10, 4), nullable=False)
    AlipayNum = db.Column(db.INTEGER, nullable=False)
    AlipayMoney = db.Column(DECIMAL(10, 4), nullable=False)
    RenchangNum = db.Column(db.INTEGER, nullable=False)
    RenchangMony = db.Column(DECIMAL(10, 4), nullable=False)
    IsPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    RegTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    LastUpdateTM = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    Note = db.Column(db.String(200), nullable=False)
    LastEditor = db.Column(db.String(100), nullable=False)


class Partnerconfig(Base):
    __tablename__ = 'partnerconfig'

    ConfigID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    AgentID = db.Column(db.INTEGER, nullable=False)
    Cooperation = db.Column(db.INTEGER, nullable=False)
    UItypeID = db.Column(db.INTEGER, nullable=False)
    Language = db.Column(db.String(50), nullable=False)
    BuyLg = db.Column(db.String(50))
    LoginType = db.Column(db.String(200))
    BuyLn = db.Column(db.String(200))
    GongNeng = db.Column(db.String(300))
    BuyGn = db.Column(db.Text)
    BuyGame = db.Column(db.Text)
    Game = db.Column(db.Text)
    OtherGm = db.Column(db.String(200))
    BuyOtherGm = db.Column(db.String(200))
    Adder = db.Column(db.String(100))
    LastEditor = db.Column(db.String(100))
    RegTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    LastUpdateTM = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    IsDefault = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Partnerconfigattr(Base):
    __tablename__ = 'partnerconfigattr'

    ID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    ValID = db.Column(db.INTEGER, nullable=False)
    Content = db.Column(db.String(500), nullable=False)


class Partnerdenomination(Base):
    __tablename__ = 'partnerdenomination'

    mid = db.Column(db.INTEGER, primary_key=True)
    PayType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PartnerID = db.Column(db.INTEGER, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    money = db.Column(db.INTEGER, nullable=False)
    number = db.Column(db.INTEGER, nullable=False)
    getnum = db.Column(db.INTEGER, nullable=False)
    type = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    sort = db.Column(db.INTEGER, nullable=False)
    proid = db.Column(db.String(100))
    qq = db.Column(db.String(100))
    weixin = db.Column(db.String(100))
    AgentID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Partnerpayconfig(Base):
    __tablename__ = 'partnerpayconfig'

    configid = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER)
    partner_no = db.Column(db.String(100))
    partner_key = db.Column(db.Text)
    partner_user = db.Column(db.String(100))
    appid = db.Column(db.String(100))
    appsecret = db.Column(db.String(100))
    paysignkey = db.Column(db.Text)
    qq_appid = db.Column(db.String(100))
    qq_appkey = db.Column(db.String(100))
    wx_appid = db.Column(db.String(100))
    wx_appkey = db.Column(db.String(100))
    type = db.Column(db.String(20), nullable=False)
    agent_no = db.Column(db.String(100))
    agent_key = db.Column(db.Text)
    AgentID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IswxPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsaliPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    payid = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsqqPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsjdPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IswyPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    Iswxh5Pay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    Isalih5Pay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    isfloatprice = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    payname = db.Column(CHAR(50), nullable=False, server_default=Text("''"))


class Paydenomination(Base):
    __tablename__ = 'paydenomination'

    mid = db.Column(db.INTEGER, primary_key=True)
    PayType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    title = db.Column(db.String(200), nullable=False)
    money = db.Column(db.INTEGER, nullable=False)
    number = db.Column(db.INTEGER, nullable=False)
    getnum = db.Column(db.INTEGER, nullable=False)
    type = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    sort = db.Column(db.INTEGER, nullable=False)
    proid = db.Column(db.String(200))
    IsDefault = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    denomid = db.Column(db.INTEGER, nullable=False)


class Paylist(Base):
    __tablename__ = 'paylist'

    ID = db.Column(db.INTEGER, primary_key=True)
    paytype = db.Column(db.String(50), nullable=False)
    status = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    payid = db.Column(db.INTEGER, nullable=False)
    wxpay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    alipay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Paytype(Base):
    __tablename__ = 'paytype'

    TypeID = db.Column(db.INTEGER, primary_key=True)
    PayName = db.Column(db.String(50), nullable=False)
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Rechargecard(Base):
    __tablename__ = 'rechargecard'

    CardID = db.Column(db.INTEGER, primary_key=True)
    CardNo = db.Column(db.String(100), nullable=False)
    CardPwd = db.Column(db.String(100), nullable=False)
    Money = db.Column(db.INTEGER, nullable=False)
    IsUse = db.Column(db.INTEGER, nullable=False, server_default=Text("1"))
    Type = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    CreateTime = db.Column(DateTime, nullable=False)
    UseTime = db.Column(DateTime)
    Error = db.Column(db.INTEGER, server_default=Text("000"))


class Role(Base):
    __tablename__ = 'role'

    RoleID = db.Column(db.INTEGER, primary_key=True)
    RoleName = db.Column(db.String(30), nullable=False)
    RoleDesc = db.Column(db.String(100))
    PowerList = db.Column(db.Text)
    IsEnable = db.Column(db.INTEGER, server_default=Text("0"))
    PartnerID = db.Column(db.INTEGER, nullable=False)
    ParentID = db.Column(db.INTEGER, nullable=False)


class Sale(Base):
    __tablename__ = 'sale'

    SaleID = db.Column(db.INTEGER, primary_key=True)
    SaleName = db.Column(db.String(100), nullable=False)
    UserID = db.Column(BIGINT(20), nullable=False)
    Phone = db.Column(db.String(50))
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    AddTime = db.Column(DateTime, server_default=Text("'0000-00-00 00:00:00'"))
    UpdateTime = db.Column(DateTime, server_default=Text("'0000-00-00 00:00:00'"))
    LastLoginTM = db.Column(DateTime, server_default=Text("'0000-00-00 00:00:00'"))


class SaleDenom(Base):
    __tablename__ = 'sale_denom'

    denomid = db.Column(db.INTEGER, nullable=False)
    SaleID = db.Column(db.INTEGER, primary_key=True)


class ServerList(Base):
    __tablename__ = 'server_list'

    SerID = db.Column(db.INTEGER, primary_key=True)
    ServerIP = db.Column(db.String(100), nullable=False)
    ServerAccount = db.Column(db.String(100), nullable=False)
    ServerPwd = db.Column(db.String(100), nullable=False)
    Teleport = db.Column(db.String(100), nullable=False)


class ShareConfig(Base):
    __tablename__ = 'share_config'

    ID = db.Column(db.INTEGER, primary_key=True)
    AgentCode = db.Column(db.String(100))
    DownLink = db.Column(db.String(200))
    Content = db.Column(db.String(100))


class Syscategory(Base):
    __tablename__ = 'syscategory'

    SysCatID = db.Column(db.INTEGER, primary_key=True)
    SysCatName = db.Column(VARCHAR(30), nullable=False)
    SysCode = db.Column(VARCHAR(30))
    SysCatPic = db.Column(VARCHAR(200))
    SortNum = db.Column(db.INTEGER)
    SysDesc = db.Column(VARCHAR(200))
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("1"))
    CatType = db.Column(db.INTEGER, server_default=Text("0"))
    ParentID = db.Column(db.INTEGER)


class Syscatvalue(Base):
    __tablename__ = 'syscatvalue'

    ValID = db.Column(db.INTEGER, primary_key=True)
    ValName = db.Column(db.String(50), nullable=False)
    ValCode = db.Column(db.String(50))
    SortNum = db.Column(db.INTEGER, nullable=False)
    SysCatID = db.Column(db.INTEGER, nullable=False)
    IsEnable = db.Column(db.INTEGER, server_default=Text("0"))
    Status = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Sysemail(Base):
    __tablename__ = 'sysemail'

    EmailID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    Title = db.Column(db.String(100), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    Editer = db.Column(db.String(30), nullable=False)
    SendTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    Sendto = db.Column(db.String(50), nullable=False)
    RegTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    LastUpdateTM = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Syslogin(Base):
    __tablename__ = 'syslogin'

    LoginID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    Title = db.Column(db.String(100), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    Editer = db.Column(db.String(30), nullable=False)
    StartTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    EndTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    Condition = db.Column(db.String(50), nullable=False)
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Sysmsg(Base):
    __tablename__ = 'sysmsg'

    MsgID = db.Column(db.INTEGER, primary_key=True)
    PartnerID = db.Column(db.INTEGER, nullable=False)
    Title = db.Column(db.String(100), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    Editer = db.Column(db.String(30), nullable=False)
    StartTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP() ON UPDATE current_db.TIMESTAMP()"))
    EndTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    DelayTime = db.Column(db.INTEGER, nullable=False)
    RepeaTM = db.Column(db.String(50), nullable=False)
    RegTime = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    LastUpdateTM = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("'0000-00-00 00:00:00'"))
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Torder(Base):
    __tablename__ = 'torders'

    ID = db.Column(db.INTEGER, primary_key=True)
    SendType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    SendUID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    OrderNo = db.Column(db.INTEGER, nullable=False)
    TOrderNo = db.Column(db.String(50))
    CheckNo = db.Column(db.INTEGER, nullable=False)
    UserID = db.Column(BIGINT(20), nullable=False)
    UserName = db.Column(db.String(50), nullable=False)
    PayMoney = db.Column(db.INTEGER, nullable=False)
    GiftType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    GiveReason = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    GiftID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    GiveAmount = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PayType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    BuyType = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsPrev = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsDone = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsNote = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsFalse = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsError = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsFirstPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    Remarks = db.Column(db.Text)
    InputDate = db.Column(db.TIMESTAMP, nullable=False, server_default=Text("current_db.TIMESTAMP()"))
    DoneDate = db.Column(db.TIMESTAMP)
    AgentID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PartnerID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    CardID = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Tpayconfig(Base):
    __tablename__ = 'tpayconfig'

    ID = db.Column(db.INTEGER, nullable=False)
    PayTyoe = db.Column(db.INTEGER, nullable=False)
    PayName = db.Column(db.Text, nullable=False)
    PayDes = db.Column(db.Text)
    Logo = db.Column(db.String(50))
    SideLogo = db.Column(db.String(50))
    PayWebSiteUrl = db.Column(db.String(50))
    PayID = db.Column(db.String(100))
    PayUser = db.Column(db.String(100))
    PayKey = db.Column(db.String(100))
    PaySubmitUrl = db.Column(db.String(200), nullable=False)
    SortNum = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    PartnerID = db.Column(db.INTEGER, primary_key=True)


class Tpaymoney(Base):
    __tablename__ = 'tpaymoney'

    ID = db.Column(db.INTEGER, nullable=False)
    PayType = db.Column(db.INTEGER, nullable=False)
    PayMoney = db.Column(db.INTEGER, nullable=False)
    PayGameMoney = db.Column(db.INTEGER, nullable=False)
    SortNum = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IsEnable = db.Column(BIT(1), nullable=False)
    PartnerID = db.Column(db.INTEGER, primary_key=True)


class Uilist(Base):
    __tablename__ = 'uilist'

    UIID = db.Column(db.INTEGER, primary_key=True)
    UIType = db.Column(db.INTEGER)
    UIName = db.Column(db.String(200))
    Picurl = db.Column(db.String(250))
    SortNum = db.Column(db.INTEGER)
    IsEnable = db.Column(db.INTEGER, nullable=False, server_default=Text("1"))
    Status = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))


class Website(Base):
    __tablename__ = 'website'

    AgentID = db.Column(db.INTEGER, primary_key=True)
    TopBanner = db.Column(db.String(200), nullable=False)
    Logo = db.Column(db.String(200), nullable=False)
    Game1 = db.Column(db.String(200), nullable=False)
    Game2 = db.Column(db.String(200), nullable=False)
    Game3 = db.Column(db.String(200), nullable=False)
    Game4 = db.Column(db.String(200), nullable=False)
    Game5 = db.Column(db.String(200), nullable=False)
    Wechat = db.Column(db.String(200), nullable=False)
    Title = db.Column(db.String(200))
    Desc = db.Column(db.String(200))
    Keyword = db.Column(db.String(200))
    Copyright = db.Column(db.String(250))
    ServerCode = db.Column(db.Text)
    IosNum = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    AndroidNum = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    IpadNum = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    DomainUrl = db.Column(db.String(250))
    IosDownUrl = db.Column(db.String(250))
    AdDownUrl = db.Column(db.String(250))
    IosDownUrl2 = db.Column(db.String(250))
    AdDownUrl2 = db.Column(db.String(250))


class YsdkOrder(Base):
    __tablename__ = 'ysdk_order'

    CheckNo = db.Column(db.INTEGER, primary_key=True)
    UserID = db.Column(db.INTEGER, nullable=False)
    openid = db.Column(db.String(100), nullable=False)
    openkey = db.Column(db.String(300), nullable=False)
    offerid = db.Column(db.String(100), nullable=False)
    pf = db.Column(db.String(100), nullable=False)
    pfkey = db.Column(db.String(100), nullable=False)
    zoneid = db.Column(db.String(100), nullable=False)
    AddTime = db.Column(db.INTEGER, nullable=False)
    IsDone = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    login_type = db.Column(db.String(100))
    balance = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    gen_balance = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    OverTime = db.Column(db.INTEGER, server_default=Text("0"))
    IsPay = db.Column(db.INTEGER, nullable=False, server_default=Text("0"))
    why = db.Column(db.String(200))
