#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import sys
from colorama import init, Fore

init(autoreset=True)
url = "http://localhost/nginx_status"
r = requests.get(url)
nginxStatus = r.text.strip('\n').splitlines()

def active():
    # 当前活跃的连接数
    print nginxStatus[0].strip()[-1]

def reading():
    # 读取到客户端Header的信息数
    print nginxStatus[3].split()[1]

def writing():
    # 响应给客户端的Header的信息数
    print nginxStatus[3].split()[3]

def waiting():
    # nginx已经处理完正在等候下一次请求的驻留连接，在开启keep-alive的情况下,这个值等于active-(reading + writing)
    print nginxStatus[3].split()[5]

def accepts():
    # 总共处理的连接数
    print nginxStatus[2].split()[0]

def handled():
    # 总共创建的握手数
    print nginxStatus[2].split()[1]

def requests():
    # 总共处理的请求数
    print nginxStatus[2].split()[2]


try:
    if sys.argv[1]:
        pass
except IndexError, e:
    print Fore.GREEN + '#####'
    print './%s [active|reading|writing|waiting|accepts|requests]' % sys.argv[0]
    print Fore.GREEN + '#####'
else:
    if sys.argv[1] in 'active':
        active()
    elif sys.argv[1] in 'reading':
        reading()
    elif sys.argv[1] in 'writing':
        writing()
    elif sys.argv[1] in 'waiting':
        waiting()
    elif sys.argv[1] in 'accepts':
        accepts()
    elif sys.argv[1] in 'handled':
        handled()
    elif sys.argv[1] in 'requests':
        requests()
    else:
        print './%s [active|reading|writing|waiting|accepts|requests]' % sys.argv[0]
