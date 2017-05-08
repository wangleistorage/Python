#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import json
import simplejson
import sys

try:
    if sys.argv[1]:
        pass
except IndexError, e:
    print 'Usage: python %s [master_node|nodes]' % sys.argv[0]
    sys.exit()


url = 'http://es.arch.xxx.xxx/_cluster/state/nodes,master_node'
username = 'xxxx'
password = 'xxxx'
value = sys.argv[1]
master_node = 'VPhl17-eTj6Gdr1jjoPhAw'
nodes_node_1 = ['06Rxc3qFTmOllzN50YVAeQ', 'WsRb7mkzTjGmOc86A_3VLw', 'VPhl17-eTj6Gdr1jjoPhAw']
nodes_node_2 = []


def cluster_status_api_getinfo():
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
 
def cluster_status_api(value):
    try:
        cluster_info = cluster_status_api_getinfo()
    except urllib2.HTTPError, e:
        print 1
    else:
        if value == 'master_node' or value == 'nodes':
            for variable in cluster_info:
                if variable == 'master_node' and value == 'master_node':
                    if master_node == cluster_info[variable]:
                        print 0
                    else:
                        print 1
                if variable == 'nodes' and value == 'nodes':
                    for node in cluster_info[variable]:
                        nodes_node_2.append(node)
                    if nodes_node_1 == nodes_node_2:
                        print 0
                    else:
                        print 1
        else:
            print 'Usage: python %s [master_node|nodes]' % sys.argv[0]

cluster_status_api(value)
