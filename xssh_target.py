#!/usr/bin/python

import os, sys, re

host_list = "/etc/hosts"
host_target = "192.168.143.202"

def ssh_list():
    files = open(host_list)
    hostlist = files.readlines()
    for i in hostlist:
        print i,

def ssh_conn():
    ip = "^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}([1]?\d\d?|2[0-4]\d|25[0-5])$"
    pattern = re.compile(ip)
    if pattern.match(sys.argv[1]):
        print "ssh %s -t -t 'ssh %s'" % (host_target, sys.argv[1])
        os.system("ssh %s -t -t 'ssh %s'" % (host_target, sys.argv[1]))
    else:
        print "please input remote ip addr"

try:
    if sys.argv[1]:
        pass
except:
    ssh_list()
else:
    ssh_conn()
    

