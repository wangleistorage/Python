#!/usr/bin/python
# coding: utf-8 

import MySQLdb

# 方法用于创建数据库的连接,里面可以指定参数:主机,端口,用户,密码,Socket等信息,这只是连接到了数据库,想要操作数据库需要创建游标.
conn = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="yunjee0515ueopro1234",unix_socket="/tmp/mysql.sock",db="mysql")

# 通过获取到的数据库连接conn()下的curl()方法来创建游标
cur = conn.cursor()

# 通过游标cur操作execute()方法可以写入纯sql语句.通过execute()方法中写入sql语句来对数据库进行操作
cur.execute("select host,user,password from mysql.user")
cur.execute("grant all privileges on *.* to 'hongxue'@'localhost' identified by '123456';")
cur.execute("create database hongxue")

# 关闭游标
cur.close()

# 关闭数据库连接
conn.close()
