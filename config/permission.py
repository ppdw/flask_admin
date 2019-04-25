class Permission:
    # .. 项目所有权限(命名重构)
    ADMIN_ACTION = {
        '日常运营管理': {
            '游戏监控管理': {
                'manager.user': {'name': '用户在线状态', 'interface': 'ajax_online_user'},
                'manager.index': {'name': '在线人数', 'interface': 'ajax_total,agent_child_list'},
                'user.info': {'name': '查看用户信息', },
                'manager.warning': {'name': '游戏监控在线预警', 'interface': 'ajax_warning'},
                'user.gm': {
                    'name': '名单管理',
                    'interface': 'gm_user,get_gm_info,set_gm_user_analysis,get_gm_user_analysis,get_strategy_list,delete_gm_user_info_analysis'}
            },
            '充值流水': {
                'data.user_pay': {'name': '充值成功统计', 'interface': 'ajax_user_pay,'},
                'data.user_pay_error': {'name': '充值异常统计', 'interface': 'pay_error_order,'},
                'data.user_nopay': {'name': '充值失败统计', 'interface': 'pay_no_order,'}
            },
            '财富日志': {
                'data.user_buy_bill': {'name': '个人消费账单', },
                'data.fir_pay': {'name': '首冲查询', },
                'data.user_wealth': {'name': '财富日志', 'interface': 'user_money_log'},
                'data.user_agent_log': {'name': '代理日志',
                                        'interface': 'agent_money_log,agent_money_log_total'}
            },
            '游戏流水': {
                'data.game_data': {'name': '游戏流水', 'interface': 'get_game_bill_list,game_data2,......'}
            },
            '游戏管理': {
                'game.index': {'name': '房间列表', 'interface': 'ajax_all_room'},
                'game.del_g_desk': {'name': '减少房间桌子', 'interface': 'delete_game_deskid'},
                'game.delete_room': {'name': '房间删除', },
                'game.info': {'name': '房间详情 ➤', },
                'game.room_add': {'name': '➥ 添加', 'interface': 'edit_room'},
                'game.room_save': {'name': '➥ 编辑', 'interface': 'edit_room'},
                'game.fenpei': {'name': '房间分配', 'interface': 'fenpei_act'},
                'game.game_config': {'name': '游戏配置', },
                'game.desk': {'name': '桌子列表', 'interface': 'ajax_desk,'},
                'game.deskinfo': {'name': '桌子详情', },
                'game.edit_desk': {'name': '桌子配置', },
                'game.algorithm': {'name': '算法配置', 'interface': 'ajax_algorithm,ajax_algorithm_yafen'},
                'game.server': {'name': '游戏服务', },
                'game.clear_bill': {'name': '清除流水', },
                'game.start_stop': {'name': '游戏启动.停止', 'interface': 'start_game,stop_game,restart_all'},
                'game.level': {'name': '房间等级列表', 'interface': 'ajax_level,ajax_level_list'},
                'game.level_info': {'name': '房间等级详情 ➤', },
                'game.level_save': {'name': '➥ 编辑', 'interface': 'insert_level'},
                'game.level_add': {'name': '➥ 添加', 'interface': 'insert_level'},
                'game.delete_level': {'name': '删除', }
            },
            '彩金管理': {
                'user.luckstar_list': {'name': '彩金列表', 'interface': 'lottery_manage_get'},
                'user.luckstar_info': {'name': '彩金编辑', 'interface': 'lottery_manage_edit'}
            },
            '运维管理': {
                'user.operation': {'name': '运维配置', 'interface': 'get_running_mode,set_running_mode'}
            },
            '机器人管理': {
                'robot.index': {'name': '机器人管理', 'interface': 'ajax_robot,clear_nickname,delete'},
                'robot.clear_robot': {'name': '删除机器人', },
                'robot.add': {'name': '添加机器人',
                              'interface': 'add_robot,fen_robot,game_room,room_robot_info'},
                'robot.info': {'name': '添加房间机器人', 'interface': 'fen_robot,game_room,room_robot_info'},
                'robot.del_room_robot': {'name': '删除房间机器人', },
                'robot.add_nickname': {'name': '昵称', 'interface': 'clear_nickname'},
                'robot.room': {'name': '房间机器人配置',
                               'interface': 'ajax_room,fen_robot,game_room,room_robot_info'}
            },
            '内容管理': {
                'sysmsg.index': {'name': '系统公告', 'interface': 'ajax_note'},
                'sysmsg.info': {'name': '公告详情 ➤', },
                'sysmsg.save': {'name': '➥ 编辑', 'interface': 'insert_msg'},
                'sysmsg.add': {'name': '➥ 公告', 'interface': 'insert_msg'},
                'sysmsg.delete_msg': {'name': '删除', },
                'sysmsg.email': {'name': '系统邮件', 'interface': 'ajax_email,'},
                'sysmsg.email_info': {'name': '邮件详情 ➤', },
                'sysmsg.email_save': {'name': '➥ 编辑', 'interface': 'insert_email'},
                'sysmsg.email_add': {'name': '➥ 添加', 'interface': 'insert_email'},
                'sysmsg.delete_email': {'name': '删除', },
                'sysmsg.login': {'name': '登录提示', 'interface': 'ajax_login'},
                'sysmsg.login_info': {'name': '登录提示详情 ➤', 'interface': 'login_next,upload,strcut'},
                'sysmsg.login_save': {'name': '➥ 编辑', 'interface': 'insert_login'},
                'sysmsg.login_add': {'name': '➥ 添加', 'interface': 'insert_login'},
                'sysmsg.delete_login': {'name': '删除', }
            }
        },
        '用户管理': {
            '用户列表': {
                'user.index': {'name': '用户列表', 'interface': 'ajax_user,agent_child_list'},
                'user.downline': {'name': '强制下线', },
                'user.delete_mac': {'name': '清除mac', },
                'user.edit_info': {'name': '编辑', },
                'user.add_user': {'name': '添加', },
                'user.delete': {'name': '删除', 'interface': 'delete_data'},
                'user.gamebi': {'name': '游戏币详情 ➤', 'interface': 'gamebi_info'},
                'user.add_gamebi': {'name': '➥ 加币', 'interface': 'change_gamebi'},
                'user.del_gamebi': {'name': '➥ 减币', 'interface': 'change_gamebi'},
                'user.cardpay': {'name': '点卡充值', 'interface': 'web_cardpay'},
                'user.log': {'name': '用户日志', 'interface': 'ajax_log'},
                'user.edit_log': {'name': '编辑日志', 'interface': 'ajax_edit_log'},
                'user.game_log': {'name': '游戏记录', },
                'user.luckstar': {'name': '辛运之星',
                                  'interface': 'luck_star_send_lottery,luck_star_get_send_lottery_record'}
            },
            '冻结用户': {
                'manager.search_frozen': {'name': '批量冻结', 'interface': 'ajax_search_frozen'},
                'manager.frozen': {'name': '冻结用户', 'interface': 'user.edit_status'},
                'manager.frozen_list': {'name': '冻结列表', 'interface': 'ajax_frozen_user'}
            },
            '用户搜索': {
                'manager.search': {'name': '搜索(条件)', },
                'manager.search_list': {'name': '搜索(列表).查询mac用户', 'interface': 'ajax_list'}
            },
            '名单管理': {
                'manager.gm': {'name': '名单管理', 'interface': 'gm_user'},
                'manager.search_gm': {'name': '名单管理(批量)', 'interface': 'ajax_search_gm'},
                'manager.gm_list': {'name': '名单管理(列表)', 'interface': 'ajax_gm_list'}
            }
        },
        '配置管理': {
            '支付配置': {
                'function.payconfig': {
                    'name': '平台列表',
                    'interface': 'info,update_info,ajax_denomination,ajax_denomination2'},
                'function.update_config': {'name': '支付配置'}
            },
            '点卡配置': {
                'card.index': {'name': '列表管理', 'interface': 'ajax_card_list,delete_data,show_card'},
                'card.del_card': {'name': '删除', },
                'card.frozen_card': {'name': '解锁', },
                'card.create': {'name': '生成', 'interface': 'create_card,create_pay_card'},
                'card.download': {'name': '下载', 'interface': 'down_card,down_card2,excedata'}
            },
            'VIp配置': {
                'function.vip': {'name': 'VIp配置', 'interface': 'set_vip'}
            },
            '注册限制': {
                'function.register': {'name': '注册限制', 'interface': 'set_reg'}
            },
            '客服配置': {
                'function.customer': {'name': '客服配置', 'interface': 'set_cus'}
            },
            '弹头配置': {
                'function.prop': {'name': '弹头配置', 'interface': 'set_prop'}
            },
            '功能配置': {
                'function.info': {'name': '功能信息(列表必选)', },
                'function.update_info': {'name': '功能配置(编辑前提)', },
                'function.index': {'name': '功能管理', },
                'function.close': {'name': '功能开启关闭', },
                'function.extime': {'name': '体验场', },
                'function.agent': {'name': '代理互通', },
                'function.agentshare': {'name': '代理分享', },
                'function.rank': {'name': '排行榜', },
                'function.price': {'name': '大转盘', },
                'function.sms': {'name': '短信配置', },
                'function.rate': {'name': '多倍率', }
            },
            '礼包配置': {
                'function.gifts': {'name': '大礼包.配置', 'interface': 'complete_info_send_money_set'}
            }
        },
        '代销管理': {
            '代销列表': {
                'sale.index': {'name': '代销列表', 'interface': 'ajax_sale,delete'},
                'sale.client_statis': {
                    'name': '日.周.月业绩',
                    'interface': 'ajax_client_daystatis,client_weekstatis,ajax_client_weekstatis,client_monthstatis,ajax_client_monthstatis'},
                'sale.info': {'name': '代销详情 ➤', },
                'sale.save': {'name': '➥ 编辑', 'interface': 'add_sale'},
                'sale.add': {'name': '➥ 添加', 'interface': 'add_sale'},
                'sale.delete': {'name': '删除', }
            },
            '代销面额': {
                'sale.denom': {'name': '面额列表', },
                'sale.saledenom': {'name': '面额编辑', 'interface': 'set_denom'},
                'sale.denoms': {'name': '模板列表', },
                'sale.denominfo': {'name': '模板详情 ➤'},
                'sale.deno_add': {'name': '➥ 新增', 'interface': 'add_denom'},
                'sale.deno_save': {'name': '➥ 编辑', 'interface': 'add_denom'}
            },
            '代销排行': {
                'sale.rank': {'name': '代销排行', }
            }
        },
        '数据中心管理': {
            '用户信息统计': {
                'data.index': {'name': '用户信息统计',
                               'interface': 'no_user_profile_data,no_user_profile_contrast,'},
                'data.user_profile_trend': {
                    'name': '整体趋势',
                    'interface': 'no_user_profile_activeiser,now_user_profile_retention,now_user_profile_oncetime,now_user_profile_daytime'},
                'data.user_analysis': {
                    'name': '用户分析',
                    'interface': 'user_analysis_day_active,user_analysis_week_active,user_analysis_month_newusers,'},
                'data.user_consist': {
                    'name': '用户构成',
                    'interface': 'get_user_consist,get_user_retention,user_retention,day_user_retention,user_retention_week,week_user_retention, ......'},
                'data.user_channel': {'name': '渠道分析',
                                      'interface': 'user_channel_lists,user_channel_lists ......'},
                'data.user_join': {
                    'name': '用户参与度',
                    'interface': 'user_join_rate,user_retention_once_long,user_retention_rate,user_retention_rate_contrast,......'},
                'data.user_terminal': {'name': '终端分析', 'interface': 'user_terminal_list,......'},
                'data.user_error': {'name': '错误分析', 'interface': ',......'},
                'data.user_agent': {
                    'name': '代理分析',
                    'interface': 'get_user_agent,user_agent_list_all,user_agent_list,get_user_list_active......'},
                'data.user_retention': {'name': '用户留存分析', 'interface': 'get_user_consist, ......'}
            },
            '充值数据统计': {
                'data.pay_rank': {'name': '充值排行榜', 'interface': 'get_pay_rank,'},
                'data.pay_trend': {'name': '充值趋势', 'interface': 'get_pay_trend,'},
                'data.pay_translate': {'name': '充值转化',
                                       'interface': 'new_pay_translate,pay_translate2,......'},
                'data.pay_permeate': {'name': '充值渗透',
                                      'interface': 'get_pay_permeate_day,pay_permeate2,......'},
                'data.pay_custom': {'name': '充值习惯', 'interface': '......'},
                'data.pay_space': {'name': '充值间隔', 'interface': 'get_pay_space,'}
            },
            '游戏数据统计': {
                'data.game_profile': {
                    'name': '概况实时统计',
                    'interface': 'now_game_profile_data,now_game_profile_contrast,......'},
                'data.game_analysis': {'name': '用户分析', 'interface': 'game_analysis_day_newuser,......'},
                'data.game_join': {'name': '用户参与度', 'interface': 'game_retention_once_long, ......'},
                'data.game_consist': {'name': '用户构成', 'interface': 'get_game_consist, ......'},
                'data.game_retention': {'name': '用户留存分析', 'interface': 'day_game_retention, ......'}
            },
            '弹头数据统计': {
                'data.user_bullet': {'name': '弹头统计', 'interface': 'user_send_bullet_record'}
            },
            '代销数据统计': {
                'data.user_client': {'name': '代销统计', 'interface': 'user_client_log'}
            },
            '加币数据统计': {
                'data.user_goldmoney': {'name': '金币统计', 'interface': 'user_goldmoney_log'}
            }
        },
        '平台管理': {
            '平台列表': {
                'partner.apk': {'name': '平台apK推广',
                                'interface': 'set_web,downapk,uploadfiy,create_html,repot_down'},
                'partner.index': {'name': '合作商列表', 'interface': 'ajax_partner_list'},
                'partner.info': {'name': '合作商信息', 'interface': 'ajax_partner_list,ajax_gn,ajax_style'},
                'partner.server': {'name': '外网服务器配置', 'interface': 'add_ser'},
                'partner.insert_partner': {'name': '基本信息编辑', },
                'partner.update_config': {'name': '平台信息编辑', }
            },
            '智能结算': {
                'partner.bill': {'name': '智能账单', 'interface': 'ajax_bill'},
                'partner.bill_info': {'name': '账单明细', 'interface': 'ajax_bill_info'},
                'partner.bill_pay': {'name': '账单结算', 'interface': 'update_bill'}
            }
        },
        '代理管理': {
            '代理列表': {
                'agent.index': {'name': '代理列表', 'interface': 'ajax_agent'},
                'agent.delete': {'name': '删除代理', },
                'agent.close': {'name': '开启.禁止代理', },
                'agent.apk': {'name': 'apK推广', 'interface': 'uploadfiy'},
                'agent.set_web': {'name': '生成推广页', 'interface': 'creat_html,set_web'},
                'agent.power': {'name': '代理权限', 'interface': 'uploadfiy,set_power'},
                'agent.total': {'name': '消耗汇总', 'interface': 'get_invite_code_list'},
                'agent.apply_agent_pay': {'name': '申请结算', },
                'agent.info': {'name': '代理详情 ➤', },
                'agent.save': {'name': '➥ 编辑', 'interface': 'add_agent,'},
                'agent.add': {'name': '➥ 添加', 'interface': 'add_agent,'}
            },
            '智能结算': {
                'agent.bill': {'name': '代理结算记录', 'interface': 'ajax_bill'},
                'agent.pay_status': {'name': '设为已结算', }
            },
            '运营报表': {
                'agent.daystatis': {'name': '运营报表', 'interface': 'ajax_daystatis'},
                'agent.agentdaystatis': {'name': '代理详情', 'interface': 'agent_day_pay_statis'}
            }
        },
        '系统设置': {
            '管理员列表': {
                'admin.info': {'name': '管理员详情 ➤', 'interface': 'all_agent,'},
                'admin.add': {'name': '➥ 新增', 'interface': 'insert,'},
                'admin.save': {'name': '➥ 编辑', 'interface': 'insert,'},
                'admin.delete_admin': {'name': '删除'},
                'admin.index': {'name': '管理员列表', 'interface': 'ajax_admin'},
                'admin.handle': {'name': '操作汇总',
                                 'interface': 'mac,clear_mac,change_mac,get_admin_money_data'},
                'admin.nav': {'name': '设置快捷导航', 'interface': 'set_nav'},
                'admin.power': {'name': '自定义权限', 'interface': 'power,insert_power'}
            },
            '管理员日志': {
                'admin.log': {'name': '日志列表', 'interface': 'ajax_log,'},
                'admin.log_delete': {'name': '删除', }
            },
            '角色列表': {
                'role.index': {'name': '角色列表', 'interface': 'ajax_role'},
                'role.power': {'name': '权限编辑', 'interface': 'update_power'},
                'role.info': {'name': '角色详情 ➤', },
                'role.save': {'name': '➥ 编辑', 'interface': 'insert'},
                'role.add': {'name': '➥ 添加', 'interface': 'insert'},
                'role.delete': {'name': '删除', }
            }
        }
        # '其他权限': {
        #     '后台新闻': {
        #         'news.index': {'name': '新闻管理', 'interface': 'ajax_news'},
        #         'news.info': {'name': '详情 ➤', },
        #         'news.save': {'name': '➥ 编辑', 'interface': 'insert_news'},
        #         'news.add': {'name': '➥ 新增', 'interface': 'insert_news'},
        #         'news.delete': {'name': '删除', },
        #     },
        #     '游戏算法': {
        #         'algo.index': {'name': '游戏算法', 'interface': 'ajax_algo'},
        #         'algo.info': {'name': '算法机制配置 ➤', },
        #         'algo.add': {'name': '➥ 添加', 'interface': 'algorithm,'},
        #         'algo.save': {'name': '➥ 配置', 'interface': 'algorithm,'},
        #         'algo.delete': {'name': '删除', },
        #     },
        # .. '注释...' :{
        #                .. 'client.index' :{'name' : '代销后台'},
        # .. 'Home.index' :{'name' : '代理后台'},
        # .. 'apI.index' :{
        #     'name' : 'apI接口', 'interface' : 'check_real_ip,inital_data,inital_admin,vip_admin,update_sys_data,report_ui_data,report_bill_data,report_month_bill,report_total_bill,colse_website,open_website'},
        # .. 'public.main' :{'name' : '公共方法', 'interface' : ''},
        # .. 'pay.index' :{
        #     'name' : '支付接口', 'interface' : 'request_denomination,log_error,error_pay,check_agent_price,get_real_ip,h5pay'},
        # .. 'Ysdk.' :{'name' : '应用宝登录支付', 'interface' : 'test_login,check_login_token,get_balance_m,poy_m,present_m'},
        # .. 'Index.index' :{'name' : '首页.游戏', 'interface' : 'ajax_news,show,home,agent'},
        # .. 'createTool.index' :{
        #     'name' : '工具类', 'interface' : 'ajax_style,ajax_gn,create_game_ui_xml,create_game_xml,create_config_xml,create_zip_file'},
        # ..		},
        # }
    }

    TEST_ACTION = {
        '日常运营管理': {
            '游戏监控管理': {
                'manager.user': {'name': '用户在线状态', 'interface': 'ajax_online_user'},
                'manager.index': {'name': '在线人数', 'interface': 'ajax_total,agent_child_list'},
                'user.info': {'name': '查看用户信息', },
                'manager.warning': {'name': '游戏监控在线预警', 'interface': 'ajax_warning'},
                'user.gm': {
                    'name': '名单管理',
                    'interface': 'gm_user,get_gm_info,set_gm_user_analysis,get_gm_user_analysis,get_strategy_list,delete_gm_user_info_analysis'}
            }
        }
    }

    LEFT_NAV = {
        '日常运营管理': {
            'manager.user': '游戏监控管理', 'data.user_pay': '充值流水', 'data.user_wealth': '财富日志',
            'data.game_data': '游戏流水', 'game.level': '游戏管理', 'user.luckstar_list': '彩金管理',
            'robot.index': '机器人管理', 'sysmsg.index': '内容管理',
        },
        '用户管理': {
            'user.index': '用户列表', 'data.user_buy_bill': '用户消费账单', 'manager.frozen_list': '冻结用户',
            'manager.search': '用户搜索', 'manager.gm_list': '名单管理',
        },
        '配置管理': {
            'function.payconfig': '支付配置', 'card.index': '点卡配置', 'function.vip': 'VIp配置',
            'function.register': '注册限制', 'function.customer': '客服配置', 'function.prop': '弹头配置',
            'function.extime': '功能配置', 'function.gifts': '礼包配置',
        },
        '代销管理': {
            'sale.index': '代销列表', 'sale.denom': '代销面额', 'sale.rank': '代销排行',
        },
        '数据中心管理': {
            'data.index': '用户信息统计', 'data.pay_rank': '充值数据统计', 'data.game_profile': '游戏数据统计',
            'data.user_bullet': '弹头数据统计', 'data.user_client': '代销数据统计', 'data.user_goldmoney': '加币数据统计',
        },
        '平台管理': {
            'partner.index': '平台列表', 'partner.bill': '智能结算',
        },
        '代理管理': {
            'agent.index': '代理列表', 'agent.bill': '智能结算', 'agent.daystatis': '运营报表',
        },
        '系统设置': {
            'admin.index': '管理员列表', 'admin.log': '管理员日志', 'role.index': '角色列表',
        }
    }

    # 日志类型
    ACTION_NAME = {
        1: '管理员登入',
        2: '编辑管理员',
        3: '添加管理员',
        4: '删除日志',
        5: '删除管理员',
    }
