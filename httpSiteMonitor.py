#!/usr/bin/python
# -*- coding:utf-8 -*-

import MySQLdb
import sys
import requests
import time

mysql = {'host':'localhost', 'user':'operations', 'port':3306, 'passwd': 'ERcghIRV0nEzUawc', 'db':'operations'}

# 定义数据库连接地址
def executeSQL(sql):
    conn = MySQLdb.connect(host=mysql['host'], user=mysql['user'], port=mysql['port'], passwd=mysql['passwd'], db=mysql['db'])
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close
    return data

# 定义http请求的响应时间与数量阈值
def getHttpResponseTime(url, times, count):
    counts = 0
    for i in range(count):
        r = requests.head(url, verify=False)
        elapsedTime = r.elapsed.microseconds / 1000.
        if int(elapsedTime) >= times:
            counts += 1
        time.sleep(1)
    if counts == 3:
        print 0
    else:
        print 1
        
# 定义http请求的响应状态与数量阈值
def getHttpResponseStatus(url, status, count):
    counts = 0
    for i in range(count):
        r = requests.head(url, verify=False)
        if int(r.status_code) >= status:
            counts += 1
        time.sleep(1)
    if counts == 3:
        print 0
    else:
        print 1

Usage = 'Usage: python %s [http_url] [time|status]'

try:
    if sys.argv[1] and sys.argv[2]:
        sql = 'select * from httpSiteMonitor where url="%s"' % sys.argv[1]
        urlData = executeSQL(sql)
except IndexError, e:
    print Usage % sys.argv[0]
else:
    if not urlData:
        print Usage % sys.argv[0]
    for value in urlData:
        url = value[0]
        responseTime = value[2]
        responseTimeCount = value[3]
        responseStatus = value[4]
        responseStatusCount = value[5]
        if sys.argv[2] == 'time':
            getHttpResponseTime(url, int(responseTime), int(responseTimeCount))
        if sys.argv[2] == 'status':
            getHttpResponseStatus(url, responseStatus, responseStatusCount)
