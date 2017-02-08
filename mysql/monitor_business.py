# -*- coding:utf8 -*-

import MySQLdb

shopdbinfo={'host':'x.x.x.x','user':'root','port’:11111,’passwd’:’xxxxxxxxxx’,’db':'shop'}
tradedbinfo={'host':'x.x.x.x','user':'root','port’:11111,’passwd':'xxxxxxxxxx','db':'trade'}


class do_db(object):
    def __init__(self,_host,_port,_user,_passwd,_db):
        self.host=_host
        self.port=_port
        self.passwd=_passwd
        self.dbf=_db
        self.user=_user
        self.db=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,port=self.port,db=self.dbf)
        self.cursor=self.db.cursor(MySQLdb.cursors.DictCursor)

    def execsql(self,_sql):
        self.cursor.execute(_sql)
        self.db.commit()
        return self.cursor.fetchall()
    
    def closedb(self):
        self.cursor.close()
        self.db.close()


class business():
    @staticmethod
    def monitor_parent(_userid):
        check_zero='zero'
        sql='SELECT ID,PARENT_ID,PAY_ORDER_ID FROM shop.shop where USER_ID='+str(_userid)
        todo=do_db(shopdbinfo['host'],shopdbinfo['port'],shopdbinfo['user'],shopdbinfo['passwd'],shopdbinfo['db'])
        shop_parent=todo.execsql(sql)
        if shop_parent != None:
            for i in shop_parent:
                if str(i['PARENT_ID']) == '0' and str(i['PAY_ORDER_ID']) != '-1':
                    todo.closedb()
                    return check_zero
                elif str(i['ID']) == str(i['PARENT_ID']):
                    todo.closedb()
                    return check_zero
                else:
                    todo.closedb()
                    return '!zero'
        else:
            todo.closedb()
            return check_zero
                
    @staticmethod
    def monitor_commission(_ordernumber):
        check_result = 'order_fail'
        sql='select count(*) monitor_pay_shop from shop.shop_commission_order_r where order_number='+str(_ordernumber)
        todo=do_db(shopdbinfo['host'],shopdbinfo['port'],shopdbinfo['user'],shopdbinfo['passwd'],shopdbinfo['db'])
        order_commission = todo.execsql(sql)
        if order_commission != None:
            for i in order_commission:
                if i['monitor_pay_shop'] == 0:
                    todo.closedb()
                    return check_result
                else:
                    todo.closedb()
                    return 'order_ok'
                '''if i['monitor_pay_shop'] < 5:#查询收益发放小于5个的订单
                    sql = 'select * from shop.shop where id in (select shop_id from shop.shop_commission where ID in (select shop_commission_id from shop.shop_commission_order_r where order_number='+str(_ordernumber)+'))'
                    #小于5个有可能是免费开店导致的
                    sql_result=todo.execsql(sql)
                    for n in sql_result:
                        if str(n['PARENT_ID']) == '0' and str(n['PAY_ORDER_ID']) == '-1':#免费开店的特征
                            check_result = 'order_ok'
                            todo.closedb()
                            return check_result#如果有一个免费开店的方法结束，返回正确状态    
                    if check_result == 'order_fail': #跑完一个收益流程还没有找到免费开店的人，表示这个订单不正常。
                        todo.closedb()
                        return check_result 
                else:
                    return 'order_ok'
                    '''
        else:
            todo.closedb()
            return 'order_fail'
    @staticmethod
    def monitor_pay_shop(_userid):
        sql='select count(user_id) paid_times from shop.shop_order where user_id = '+str(_userid)+' and paid_time is not Null group by user_id HAVING count(user_id) > 1'
        todo=do_db(shopdbinfo['host'],shopdbinfo['port'],shopdbinfo['user'],shopdbinfo['passwd'],shopdbinfo['db'])
        paid_times = todo.execsql(sql)
        if paid_times:
            for m in paid_times:
                if m['paid_times'] != 1:
                    todo.closedb()
                    return 'repeated_paied'
                else:
                    todo.closedb()
                    return 'onece_paied'
        else:
            return 'onece_paied'
    @staticmethod
    def monitor_proceeds(_ordernumber):
        pass
    
