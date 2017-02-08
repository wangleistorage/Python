#!/usr/bin/python

import MySQLdb

mysql = {
         'host': 'localhost',
         'passwd': '3dq2w3y2',
         'port': 3306,
         'user': 'root',
         'unix_socket': '/tmp/mysql.sock',
         'db': 'xuesheng'
}

class operation_db(object):
   def __init__(self, host, passwd, port, user, unix_socket, db):
       self.host = host
       self.passwd = passwd
       self.port = port
       self.user = user
       self.unix_socket = unix_socket
       self.db = db
       self.conn = MySQLdb.connect(host=self.host, passwd=self.passwd, port=self.port, user=self.user, unix_socket=self.unix_socket, db=self.db)
       self.cursor = self.conn.cursor()

   def execute_sql(self,sql):
       self.cursor.execute(sql)
       self.conn.commit()

   def closedb(self):
       self.cursor.close()
       self.conn.close()

to_db = operation_db(mysql['host'], mysql['passwd'], mysql['port'], mysql['user'], mysql['unix_socket'], mysql['db'])
to_db.execute_sql("insert into student values('90', 'hongxue', '1 year 21', '24')")
