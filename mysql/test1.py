#!/usr/bin/python

import MySQLdb

mysql = {
         'host': 'localhost',
         'user': 'root',
         'port': 3306,
         'passwd': '3dq2w3y2',
         'unix_socket': '/tmp/mysql.sock',
         'db': 'xuesheng'
}

class do_db(object):
    def __init__(self, host, user, port, passwd, unix_socket, db):
        self.host = host
        self.user = user
        self.port = port
        self.passwd = passwd
        self.unix_socket = unix_socket
        self.db = db
        self.conn = MySQLdb.connect(host=self.host, user=self.user, port=self.port, passwd=self.passwd, unix_socket=self.unix_socket, db=self.db) 
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    def closedb(self):
        self.cursor.close()
        self.conn.close()

to_db = do_db(mysql['host'], mysql['user'], mysql['port'], mysql['passwd'], mysql['unix_socket'], mysql['db'])

value = to_db.execute_sql("select name from student")
for i in value:
    print 'name: ' ,i['name']

to_db.closedb()
