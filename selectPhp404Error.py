#!/usr/bin/python
# -*- coding:utf-8 -*-

import paramiko
import sys
import time
import MySQLdb

sshUser = 'operations'
sshPort = 22
today = time.strftime('%Y-%m-%d')
nowStamp = int(time.time())
agoStamp = nowStamp - 1800
mysql = {'host':'localhost', 'user':'operations', 'port':3306, 'passwd': 'ERcghIRV0nEzUawc', 'db':'operations'}

def getDBValue(sql):
    conn = MySQLdb.connect(host=mysql['host'], user=mysql['user'], port=mysql['port'], passwd=mysql['passwd'], db=mysql['db'])
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close
    return data

def getLogValue(logHost, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='%s' % logHost, port=sshPort, username=sshUser)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    return result

def analysisValue():
    values = getDBValue(sql)
    logHost = values[1]
    logFile = values[2] % today
    command = "cat %s|egrep '\[%s\]'|egrep 'CHttpException.404'|awk -v time1=%s -v time2=%s '{if($3>=time1 && $3<=time2){ print $0} }'" % (logFile, sys.argv[2], agoStamp, nowStamp)
    logInfo = getLogValue(logHost, command)
    if sys.argv[3] == 'log':
        print logInfo.strip('\n')
    if sys.argv[3] == 'line':
        print len(logInfo.strip('\n').splitlines())

try:
    if sys.argv[1] and sys.argv[2] and sys.argv[3]:
        sql = 'select * from phpLogMonitor where name="%s"' % sys.argv[1]
except IndexError:
    print 'Usage: python %s [itemName] [error|warning] [log|line]'
else:
    analysisValue()
