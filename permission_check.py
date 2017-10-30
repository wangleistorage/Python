#!/usr/bin/python
# -*- coding:utf-8 -*-

import paramiko
import os
import sys
import time
import datetime
import difflib
import smtplib
from email.mime.text import MIMEText
from email.header import Header


host_lists = {
    'qdapi-app-online1': '1.1.1.1',
    'qdapi-online3': '2.2.2.2',
    'qdapi-online2': '3.3.3.3',
    'qdapi-online1': '4.4.4.4',
    'qdfront-online2': '5.5.5.5',
    'qdfront-online1': '6.6.6.6',
    'qdback-online': '7.7.7.7',
    'data-online': '8.8.8.8',
    'zjbapi-online': '9.9.9.9',
    'zjbback-online': '10.10.10.10',
    'dcback-online': '11.11.11.11',
    'dc-online': '12.12.12.12',
    'qdmsg-online': '13.13.13.13',
    'gray-release': '14.14.14.14',
    'qiandao-offline': '15.15.15.15'
}

host_path = '/home/web'
host_user = 'operations'
host_port = 22
host_file = '/tmp/tmpfile'
diff_path = '/tmp/permission'
today = time.strftime("%Y%m%d")
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-1)
yesterday = yes_time.strftime('%Y%m%d')


def sendmail(text):
    '''  定义邮件信息  '''

    sender = 'from_user_1'
    mailtos = ['to_user_1@163.com', 'to_user_2@qq.com', 'to_user_3@qq.com', 'to_user_4@qq.com', 'to_user_5@qq.com']
    for mailto in mailtos:
        msg = MIMEText(text)                 # 邮件正文
        msg['Subject'] = 'permission change'        # 邮件主题
        msg['To'] = mailto
        msg['From'] = sender
        smtp = smtplib.SMTP('smtp.163.com')
        smtp.login('to_user_1@163.com', 'to_user_1_pass')
        smtp.sendmail(sender, mailto, msg.as_string())
        smtp.quit        

def create_path(ip):
    paths = '%s/%s' % (diff_path, ip)
    if not os.path.isdir(paths):
        os.makedirs(paths)

def ssh_connect(ip, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='%s' % ip, port=host_port, username=host_user)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    return result

def save_to_file(files, values):
    f = open(files,'w')
    f.write(values)
    f.close()

def diff_check(file1, file2):
    f1 = open(file1, 'r')
    f1s = f1.read()
    f1.close()
    f2 = open(file2, 'r')
    f2s = f2.read()
    f2.close()
    if not f1s == f2s:
        dimensions = 'module=%s:%s/%s' % (project_addr, host_path, project)
        line = '%s:%s/%s Permission change, please check... ' % (project_addr, host_path, project)
        sendmail(line)
        
        
if __name__ == '__main__':
    for i in host_lists:
        project_name = i
        project_addr = host_lists[i]
        create_path(project_addr)      # 创建存放diff信息的路径
        command1 = "ls -l %s|grep ^d|awk '{print $NF}'" % host_path
        project_list =  ssh_connect(project_addr, command1).strip('\n').splitlines()
        for project in project_list:
            command2 = "getfacl %s/%s/*" % (host_path, project)
            diff_info = ssh_connect(project_addr, command2)
            today_diff = diff_path + '/' + project_addr + '/' + project + '-' + today + '.diff'
            yesterday_diff = diff_path + '/' + project_addr + '/' + project + '-' + yesterday + '.diff'
            save_to_file(today_diff, diff_info)
            diff_check(today_diff, yesterday_diff)
