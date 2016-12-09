#!/usr/bin/python
# -*- coding:utf-8 -*-

import pexpect
import os
import os.path

path_dict = {'/tmp/': '/tmp1/', '/opt/': '/opt1/', '/data/': '/data1/'}
dest_host = "192.168.143.201"

def src_to_dest(path_dict, dest_host):
    '''  该脚本用于将主机 /tmp,/opt,/data 下的所有文件同步至远程主机 /tmp1,/data1,/opt1  '''
    
    for path in path_dict:
        file_list = os.listdir(path)
        dest_path = "ssh %s '[ -d %s ] || mkdir -p %s'" % (dest_host, path_dict[path], path_dict[path])
        os.system(dest_path)
        for files in file_list:
            src_file = path + files
            print src_file + ' ---> ' +  dest_host + ':' + path_dict[path] + files
            cmd = 'scp -r %s %s:%s' % (src_file, dest_host, path_dict[path])
            scp = pexpect.spawn(cmd)
            scp.read()

src_to_dest(path_dict, dest_host)


