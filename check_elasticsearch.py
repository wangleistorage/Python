#!/usr/bin/python
# -*- coding:utf-8 -*-

import os.path
import time
import re
import subprocess

elastic_path = '/home/deploy/elasticsearch-1.7.1/'
elastic_log = elastic_path + 'logs/elasticsearch_xkeshi.log'
elastic_bin = elastic_path + 'bin/service/elasticsearch'

class file_read:
    def __init__(self,logfilename):
        self._logfilename=logfilename
    def get_time(self,_logfilename):
        if os.path.exists(_logfilename):
            return time.ctime(os.path.getctime(_logfilename))
        else:
            print str(self._logfilename)+'is not exist,after 1s system will check again'
            time.sleep(1)
            self.get_time(_logfilename)   
    def file_readlines(self,line):
        pattern = "java.lang.OutOfMemoryError: Java heap space"
        if re.search(pattern, line):
            print 'restart elasticsearch'
            retn = subprocess.call("%s restart" % elastic_bin , shell=True)
            time.sleep(20)
           
    def file_readline(self):
        if os.path.exists(self._logfilename):
            f=open(self._logfilename,'r')
        else:
            print str(self._logfilename)+'is not exist,after 1s system will check again'
            time.sleep(1)
            self.file_readline()
              
        f.seek(0,2)
        before_ctime=self.get_time(self._logfilename)
        while True:             
            offset=f.tell()
            line=f.readline()
            if not line:
                after_ctime=self.get_time(self._logfilename)
                after_offset=f.tell()
                if offset == after_offset and before_ctime != after_ctime and os.path.exists(self._logfilename):
                    f.close()
                    f=open(self._logfilename,'r')
                    line=f.readline()
                    self.file_readlines(line)
                    before_ctime=self.get_time(self._logfilename)
                    continue
                time.sleep(0.1)
            else:
                self.file_readlines(line) 
                before_ctime=self.get_time(self._logfilename)
            
        f.close()

if __name__ == '__main__':
    a=file_read(elastic_log)
    a.file_readline()
