#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import sys

url = 'http://localhost/php_status'
r = requests.get(url)
phpStatus = str(r.text.strip('\n')).splitlines()

#data = str(r.text.strip('\n'))
#phpStatus = data.splitlines()

def acceptedConn():
    # 当前池子接受的请求数
    print phpStatus[4].split()[2]

def listenQueue():
    # 请求等待队列,如果这个值不为0,那么要增加FPM的进程数量
    print phpStatus[5].split()[2]

def maxListenQueue():
    # 请求等待队列最高的数量
    print phpStatus[6].split()[3]

def listenQueueLen():
    # socket等待队列长度
    print phpStatus[7].split()[3]

def idleProcesses():
    # 空闲进程数量
    print phpStatus[8].split()[2]

def activeProcesses():
    # 活跃进程数量
    print phpStatus[9].split()[2]

def totalProcesses():
    # 总进程数量
    print phpStatus[10].split()[2]

def maxActiveProcesses():
    # 最大的活跃进程数量(FPM启动开始算)
    print phpStatus[11].split()[3]

def maxChildrenReached():
    # 进程最大数量限制的次数,如果这个数量不为0,那说明你的最大进程数量太小了,请改大一点
    print phpStatus[12].split()[3]

try:
    if sys.argv[1]:
        pass
except IndexError, e:
    print "Usage: %s [acceptedConn|listenQueue|maxListenQueue|listenQueueLen|idleProcesses|activeProcesses|totalProcesses|maxActiveProcesses|maxChildrenReached]" % sys.argv[0]
else:
    if sys.argv[1] == 'acceptedConn':
        acceptedConn()
    elif sys.argv[1] == 'listenQueue':
        listenQueue()
    elif sys.argv[1] == 'maxListenQueue':
        maxListenQueue()
    elif sys.argv[1] == 'listenQueueLen':
        listenQueueLen()
    elif sys.argv[1] == 'idleProcesses':
        idleProcesses()
    elif sys.argv[1] == 'activeProcesses':
        activeProcesses()
    elif sys.argv[1] == 'totalProcesses':
        totalProcesses()
    elif sys.argv[1] == 'maxActiveProcesses':
        maxActiveProcesses()
    elif sys.argv[1] == 'maxChildrenReached':
        maxChildrenReached()
    else:
        print "Usage: %s [acceptedConn|listenQueue|maxListenQueue|listenQueueLen|idleProcesses|activeProcesses|totalProcesses|maxActiveProcesses|maxChildrenReached]" % sys.argv[0]
