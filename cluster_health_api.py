#!/usr/bin/python
# -*- coding:utf-8 -*-

import cookielib
import urllib2
import urllib
import simplejson
import sys

try:
    if sys.argv[1]:
        pass
except IndexError, e:
    print 'Usage: python %s [status|number_of_nodes|number_of_data_nodes]' % sys.argv[0]
    sys.exit()

url = 'http://es.arch.xxx.xxx/_cluster/health'
username = "xxxx"
password = "xxxx"
value = sys.argv[1]

def cluster_health_api_getinfo():
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()  # 创建密码管理者
    password_mgr.add_password(None, url, username, password)  # 添加用户名和密码
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)      # 创建一个新的handler
    opener = urllib2.build_opener(handler)                    # 创建opener
    opener.open(url)                                          # 使用opener获取一个URL
    urllib2.install_opener(opener)                            # 安装opener
    ret = urllib2.urlopen(url)                                # urllib2.urlopen 使用上面的opener
    info = ret.read()                                         # 读取信息
    info_s = simplejson.loads(info)                           # 将读取的信息转换为json
    return info_s


def cluster_health_api(value):
    try:
        cluster_info = cluster_health_api_getinfo()
    except urllib2.HTTPError, e:
        print 1
    else:
        if value == 'status' or value == 'number_of_nodes' or value == 'number_of_data_nodes':
            for variable in cluster_info:
                if value == 'status':
                    if variable == 'status':
                        if cluster_info[variable] == 'green' or cluster_info[variable] == 'yellow':
                            print 0
                        else:
                            print 1
                if value == 'number_of_nodes': 
                    if variable == 'number_of_nodes':
                        if cluster_info[variable] == 3:
                            print 0
                        else:
                            print 1
                if value == 'number_of_data_nodes':
                    if variable == 'number_of_data_nodes':
                        if cluster_info[variable] == 3:
                            print 0
                        else:
                            print 1
        else:
            print 'Usage: python %s [status|number_of_nodes|number_of_data_nodes]' % sys.argv[0]

cluster_health_api(value)
