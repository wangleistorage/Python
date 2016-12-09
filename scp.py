#!/usr/bin/python
# -*- coding:utf-8 -*-

import pexpect
import os
import os.path

src_path = ['/tmp/', '/opt/', '/root/']
dest_host = "192.168.143.201"
dest_path = "/tmp" 

for path in src_path:
    file_list = os.listdir(path)
    for files in file_list:
        f = path + files
        cmd = 'scp -r %s %s:%s' % (f, dest_host, dest_path)
        scp = pexpect.spawn(cmd)
        scp.read()
