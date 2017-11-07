#!/usr/bin/python
# -*- coding:utf-8 -*-

import MySQLdb
import sys
import re
from colorama import init, Fore

def GetmysqlInfo(sql):
    mysql = {'host':'127.0.0.1', 'user':'zabbix', 'port':3306, 'passwd': 'zabbix', 'db':'zabbix'}
    conn = MySQLdb.connect(host=mysql['host'], user=mysql['user'], port=mysql['port'], passwd=mysql['passwd'], db=mysql['db'])
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close
    return data

init(autoreset=True)
sql = 'show status;'
mysqlInfo = GetmysqlInfo(sql)


try:
    if sys.argv[1]:
        pass
except IndexError, e:
    print Fore.GREEN + '#####'
    print 'python %s [Uptime|Com_begin|Com_update|Com_select|Com_rollback|Com_insert|Com_delete|Com_commit|Bytes_sent|Bytes_received|Slow_queries|Questions]' % sys.argv[0]
    print Fore.GREEN + '#####'
else:
    for values in mysqlInfo:
        if values[0] == sys.argv[1]:
            print values[1]
