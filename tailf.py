#!/usr/bin/python
# -*- coding:utf-8 -*-

import os.path
import time

class file_read:
    def __init__(self, logname):
        self.logname = logname

    def get_time(self, logname):
        if os.path.exists(logname):
            return os.path.getctime(logname)
        else:
            print str(logname) + 'is not exists'
            time.sleep(2)
            self.get_time(logname)

    def file_readlines(self, line):
        print line,

    def file_readline(self):
        if not os.path.exists(self.logname):
            print str(self.logname) + 'is not exists'
            time.sleep(2)
            self.file_readline()
        f = open(self.logname, 'r')
        f.seek(0, 2)

        while True:
            before_ctime = self.get_time(self.logname)
            before_offset = f.tell()
            line = f.readline()
            if not line:
                after_ctime = self.get_time(self.logname)
                after_offset = f.tell()
                if before_offset == after_offset and before_ctime != after_ctime and os.path.exists(self.logname):
                    f.close()
                    f = open(self.logname)
                    line = f.readline()
                    self.file_readlines(line)
            else:
                self.file_readlines(line)
        f.close()

if __name__ == '__main__':
    a = file_read('./file.txt')
    a.file_readline()
