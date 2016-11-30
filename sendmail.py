# -*- coding:utf-8 -*-

import urllib2
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://front2.ngx.xxxxx.net/status'
content = urllib2.urlopen(url).readlines()

def sendmail(text):
    '''  定义邮件信息  '''

    sender = 'wanglei_storage@163.com'
    mailto = '846317702@qq.com'
    msg = MIMEText(text)                 # 邮件正文
    msg['Subject'] = 'Jetty down'        # 邮件主题
    msg['To'] = mailto
    msg['From'] = sender
    smtp = smtplib.SMTP('smtp.163.com')
    smtp.login('wanglei_storage@163.com', 'xxxxxx')
    smtp.sendmail(sender, mailto, msg.as_string())
    smtp.quit        

for line in content:
    if re.search(' down$', line):
        print line,
        sendmail(line) 
