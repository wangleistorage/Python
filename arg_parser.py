#!/usr/bin/python
# -*- coding:utf-8 -*-

import argparse
parser = argparse.ArgumentParser(description="input para")
parser.add_argument('-s', dest="server_name", help="set server name")
parser.add_argument('-n', action="store_true", dest="name", help="your name")
parser.add_argument('-a', action="store_true", dest="age", help="your age")
parser.add_argument('-b', action="store_true", dest="height", help="your height")
args = parser.parse_args()

dicts = {}
if args.server_name:
    dicts['server_name'] = args.server_name
if args.name:
    dicts['name'] = "wanglei"
if args.age:
    dicts['age'] = '25'
if args.height:
    dicts['height'] = '170'

if dicts:
    print dicts

# parser.add_argument()
# 1.参数中加与action="store_true"的区别
# 如果有加action="store_true"
# 那么在脚本运行的时候会判断是否有带入这个参数(该项只能带前面指定的参数,不可以带入值),如果代入(则返回True),如果没有代入(则返回False)
# 如果没有加action="store_true"
# 那么在脚本运行的时候会判断是否有带入这个参数和值(如果带参数,则必须要带入值),如果代入(则返回代入的值),如果没有带入参数和值(则返回None)

# 2.参数中的dest
# 将用户传入的参数值用dest指定的名称进行赋值,可进行之后的判断和调用

# 3.参数中的help
# 参数的帮助信息

# 4.示例
# [root@centos-210 ~]# ./argssss.py -s appserver
# {'server_name': 'appserver'}
# [root@centos-210 ~]# ./argssss.py -s appserver -a
# {'age': '25', 'server_name': 'appserver'}
# [root@centos-210 ~]# ./argssss.py -s appserver -a -b
# {'age': '25', 'server_name': 'appserver', 'height': '170'}
# [root@centos-210 ~]# ./argssss.py -s appserver -a -b -n
# {'age': '25', 'name': 'wanglei', 'server_name': 'appserver', 'height': '170'}

