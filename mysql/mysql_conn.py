#!/usr/bin/python

import MySQLdb

mysql = {
         'host': 'localhost',
         'user': 'root',
         'port': 3306,
         'sock': '/tmp/mysql.sock',
         'passwd': '3dq2w3y2',
         'db': 'xuesheng'
         } 
             
conn = MySQLdb.connect(host=mysql['host'], port=mysql['port'], user=mysql['user'], passwd=mysql['passwd'], db=mysql['db'], unix_socket=mysql['sock'])

cur = conn.cursor()

cur.execute("create table student(id int, name varchar(20), class varchar(30), age varchar(10))")
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
cur.execute("update student set class='3 year 1 class' where name='Tom'")
cur.execute("delete from student where age='15'")

cur.close()
conn.commit()
conn.close()

'''
1)建立连接
  conn = MySQLdb.connect(host=mysql['host'], port=mysql['port'], user=mysql['user'], passwd=mysql['passwd'], db=mysql['db'], unix_socket=mysql['sock'])
2)创建游标
  cur = conn.cursor()
3)执行语句
  cur.execute("insert into student values('3', 'huhuhu', '1- year class', '12')")
4)关闭游标
  cur.close()
5)提交事务,在向数据库插入一条数据时必须要有这个方法,否则数据不会被真正的插入
  conn.commit()
6)关闭数据库连接
  conn.close()
'''
