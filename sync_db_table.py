#!/usr/local/bin/python3.6

import os
import threading
import time

class MyOperation(threading.Thread):
    ''' 该类用于备份mysql数据表及还原 '''

    my_backup_cmd = '/usr/local/mysql-5.6.36/bin/mysqldump'
    my_store_cmd = '/usr/local/mysql-5.6.36/bin/mysql'

    def __init__(self, src_addr,src_user,src_pass,src_db,dest_addr,dest_user,dest_pass,dest_db,tab):
        super(MyOperation, self).__init__()
        self.src_addr = src_addr
        self.src_user = src_user
        self.src_pass = src_pass
        self.src_db = src_db
        self.dest_addr = dest_addr
        self.dest_user = dest_user
        self.dest_pass = dest_pass
        self.dest_db = dest_db
        self.tab = tab

    def run(self):
        os.system('%s -h%s -u%s -p%s --set-gtid-purged=off %s %s > /tmp/%s.sql' % (self.my_backup_cmd,self.src_addr,self.src_user,self.src_pass, 
                                                                                   self.src_db,self.tab, self.tab))
        os.system('%s -h%s -u%s -p%s %s < /tmp/%s.sql' % (self.my_store_cmd,self.dest_addr,self.dest_user,self.dest_pass,self.dest_db,self.tab))
        

# 多线程调用备份和还原任务
tab_list = ['productcate', 'collarsize', 'productbrand', 'productdescription', 'productcolor']
tab_objs = []
for tab in tab_list:
    m = MyOperation('db1_host', 'backups', 'db1_pass', 'operation', 'db2_host', 'backups', 'db2_pass', 'sync_db', tab)
    m.start()
    tab_objs.append(m)

# 等待多线程执行结束
for m in tab_objs:
    m.join()

time.sleep(5)

# 删除备份的sql
for tab in tab_list:
    del_f = '/tmp/' + tab + '.sql'
    if os.path.isfile(del_f):
        os.remove(del_f)
        print(del_f)

print('ok')
