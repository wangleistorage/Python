#!/usr/bin/python
import os
import commands
import re
import sys
from colorama import init, Fore
init(autoreset=True)


phpKeyword="/usr/local/php7[0]{0,1}"
nginxKeyword="/usr/local/nginx"
mysqlKeyword="/usr/local/mysql"

def getPhpInfo():
    output = commands.getoutput("ps -ef|grep php|grep -v grep")
    return output

def returnPhpCode():
    phpInfo = getPhpInfo()
    phpCount = 0
    for line in phpInfo.splitlines():
      if re.search(phpKeyword, line):
         phpCount = 1
         break
    return phpCount
    
def getNginxInfo():
    output = commands.getoutput("ps -ef|grep nginx|grep -v grep")
    return output

def returnNginxCode():
    nginxInfo = getNginxInfo()
    nginxCount = 0
    for line in nginxInfo.splitlines():
        if re.search(nginxKeyword, line):
            nginxCount = 1
            break
    return nginxCount

def getMySQLInfo():
    output = commands.getoutput("ps -ef|grep mysql|grep -v grep")
    return output

def returnMySQLCode():
    mysqlInfo = getMySQLInfo()
    mysqlCount = 0
    for line in mysqlInfo.splitlines():
        if re.search(mysqlKeyword, line):
            mysqlCount = 1
            break
    return mysqlCount


try:
    if sys.argv[1]:
        pass
except IndexError, e:
    print Fore.GREEN + '#####'
    print './%s [php|nginx|mysql]' % sys.argv[0]
    print Fore.GREEN + '#####'
else:
    if sys.argv[1] == 'php':
        phpCode = returnPhpCode()
        print phpCode
    elif sys.argv[1] == 'nginx':
        nginxCode = returnNginxCode()
        print nginxCode
    elif sys.argv[1] == 'mysql':
        mysqlCount = returnMySQLCode()
        print mysqlCount
    else:
        print Fore.GREEN + '#####'
        print './%s [php|nginx|mysql]' % sys.argv[0]
        print Fore.GREEN + '#####'
