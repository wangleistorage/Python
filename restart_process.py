#!/usr/bin/python

import os
import datetime
import subprocess
import commands

path = '/data/test/'

def execute_cmd(script_path):
    retn = subprocess.call('%s/bin/restart.sh' % script_path, shell=True)

def monitor_directory():
    code, output = commands.getstatusoutput('find /data/test/ -maxdepth 1 -mmin -1')
    output = output.split("\n")
    for i in output:
        if not i == path:
            execute_cmd(i)

monitor_directory()
