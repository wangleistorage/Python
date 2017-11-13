#!/usr/bin/python
# -*- coding:utf-8 -*-

import paramiko
import sys
import time

itemPath ='/home/web'
today = time.strftime('%Y-%m-%d')
nowStamp = int(time.time())
agoStamp = nowStamp - 1800

def sshGetValue(ip, command):
    port = 22
    user = 'operations'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='%s' % ip, port=port, username=user)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    return result

def returnValue(ip, logFile):
    command = "cat %s|egrep '\[error\]'|egrep -v 'CHttpException.404|NodeService.php'|awk -v time1=%s -v time2=%s '{if($3>=time1 && $3<=time2){ print $0} }'" % (logFile, agoStamp, nowStamp)
    print command
    data = sshGetValue(ip, command)
    if sys.argv[2] == 'log':
        print data.strip('\n')
    else:
        print len(data.strip('\n').splitlines())

def dataOnline1():
    ip = '10.168.154.241'
    logFile = '%s/data-php/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def dcBackOnline1():
    ip = '10.117.17.211'
    logFile = '%s/online-dc-back/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def dcApiOnline1():
    ip = '10.252.219.140'
    logFile = '%s/online-dc-api/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def zjbApiOnline1():
    ip = '10.117.51.33'
    logFile= '%s/online-zjb-api/storage/logs/lumen-http-all-error-%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def zjbBackOnline1():
    ip = '10.168.61.180'
    logFile = '%s/online-zjb-back/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def zjbBackOnline1V2():
    ip = '10.168.61.180'
    logFile = '%s/online-zjb-back-v2/runtime/logs/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def qdMsgOnline1():
    ip = '10.117.13.155'
    logFile = '%s/online-qd-msg/storage/logs/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def qdFrontOnline1():
    ip = '10.171.200.214'
    logFile = '%s/qdwebfront-php/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)
    
def qdBackOnline1():
    ip = '10.117.13.221'
    logFile = '%s/qdback-php/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def qdApiOnline1():
    ip = '10.51.13.231'
    logFile = '%s/online-qd-api/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def qdApiOnline2():
    ip = '10.132.46.105'
    logFile = '%s/online-qd-api/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def qdApiOnline3():
    ip = '10.175.206.144'
    logFile = '%s/online-qd-api/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def qdAppApiOnline1():
    ip = '10.251.245.254'
    logFile = '%s/online-qd-api/protected/runtime/log/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def loanMarketOnline1():
    ip = '10.171.217.44'
    logFile = '%s/online-loan_market-api/runtime/logs/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

def loanMarketOnline2():
    ip = '10.117.13.155'
    logFile = '%s/online-loan_market-api/runtime/logs/%s.log' % (itemPath, today)
    returnValue(ip, logFile)

try:
    if sys.argv[1]:
        pass
except IndexError:
    print 'Usage: python %s [dataOnline1|dcBackOnline1|dcApiOnline1|zjbApiOnline1|zjbBackOnline1|qdMsgOnline1|qdFrontOnline1|qdBackOnline1|qdApiOnline1|qdApiOnline2|qdApiOnline3|qdAppApiOnline1|loanMarketOnline1|loanMarketOnline2] [log|line]' % sys.argv[0]
else:
    if sys.argv[1] == 'dataOnline1':
        dataOnline1()
    elif sys.argv[1] == 'dcBackOnline1':
        dcBackOnline1()
    elif sys.argv[1] == 'dcApiOnline1':
        dcApiOnline1()
    elif sys.argv[1] == 'zjbApiOnline1':
        zjbApiOnline1()
    elif sys.argv[1] == 'zjbBackOnline1':
        zjbBackOnline1()
    elif sys.argv[1] == 'qdMsgOnline1':
        qdMsgOnline1()
    elif sys.argv[1] == 'qdFrontOnline1':
        qdFrontOnline1()
    elif sys.argv[1] == 'qdBackOnline1':
        qdBackOnline1()
    elif sys.argv[1] == 'qdApiOnline1':
        qdApiOnline1()
    elif sys.argv[1] == 'qdApiOnline2':
        qdApiOnline2()
    elif sys.argv[1] == 'qdApiOnline3':
        qdApiOnline3()
    elif sys.argv[1] == 'qdAppApiOnline1':
        qdAppApiOnline1()
    elif sys.argv[1] == 'loanMarketOnline1':
        loanMarketOnline1()
    elif sys.argv[1] == 'loanMarketOnline2':
        loanMarketOnline2()
    else:
        print 'Usage: python %s [dataOnline1|dcBackOnline1|zjbApiOnline1|zjbBackOnline1|qdMsgOnline1|qdFrontOnline1|qdBackOnline1|qdApiOnline1|qdApiOnline2|qdApiOnline3|loanMarketOnline1|loanMarketOnline2|qdAppApiOnline1] [log|line]' % sys.argv[0]
