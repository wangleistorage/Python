#!/usr/bin/python
#coding:utf-8

try: import httplib
except ImportError:
    import http.client as httplib
import sys, random, string
import urllib, urllib2, time, json, itertools, mimetypes
import base64, hmac, uuid
from hashlib import sha1

# import mail 
import urllib2, os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

print "周一重置邮件密码:"
print "python modify_rds_readonly_user.py"
print ""
print "周五根据分组设置邮件密码:"
print "python modify_rds_readonly_user.py webapi_readonly user1@666.com,user2@666.com"
print "python modify_rds_readonly_user.py take_readonly user1@666.com,user2@666.com"
print "python modify_rds_readonly_user.py imiaoj_readonly user1@666.com,user2@666.com"
print ""

class AliyunMonitor:
    def __init__(self,url):
        self.access_id = '阿里云AccessKey ID'
        self.access_secret = '阿里云AccessKey Secret'
        self.url = url

    ## 发送邮件
    def sendmail(self, text, mailto):
        sender = 'opsalerts@666.com'
        msg = MIMEText(text)
        msg['Subject'] = '周末值班人员RDS临时只读账户信息'
        msg['To'] = mailto
        msg['From'] = sender
        smtp = smtplib.SMTP('smtp.exmail.qq.com')
        smtp.login('opsalerts@666.com', 'password')
        smtp.sendmail(sender, mailto, msg.as_string())
        smtp.quit

    ## 随机密码
    def make_passwd(self):
        strings = string.letters + string.digits
        passwd = ''
        for i in range(16):
            passwd += random.choice(strings)
        return passwd

    ##签名
    def sign(self,accessKeySecret, parameters):
        sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
        canonicalizedQueryString = ''
        for (k,v) in sortedParameters:
            canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)

        stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:]) #使用get请求方法

        h = hmac.new(accessKeySecret + "&", stringToSign, sha1)
        signature = base64.encodestring(h.digest()).strip()
        return signature

    def percent_encode(self,encodeStr):
        encodeStr = str(encodeStr)
        res = urllib.quote(encodeStr.decode(sys.stdin.encoding).encode('utf8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

    def make_url(self,params):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        parameters = {
            'Format' : 'JSON',
            'Version' : '2014-08-15',
            'AccessKeyId' : self.access_id,
            'SignatureVersion' : '1.0',
            'SignatureMethod' : 'HMAC-SHA1',
            'SignatureNonce' : str(uuid.uuid1()),
            'TimeStamp' : timestamp,
        }
        for key in params.keys():
            parameters[key] = params[key]

        signature = self.sign(self.access_secret,parameters)
        parameters['Signature'] = signature
        url = self.url + "/?" + urllib.urlencode(parameters)
        return url

    def do_request(self,params):
        url = self.make_url(params)
        print(url)
        print
        request = urllib2.Request(url)
        try:
            conn = urllib2.urlopen(request)
            response = conn.read()
        except urllib2.HTTPError, e:
            print(e.read().strip())
            raise SystemExit(e)
        try:
            obj = json.loads(response)
        except ValueError, e:
            raise SystemExit(e)
        print obj


if __name__ == "__main__":
    T = AliyunMonitor("https://rds.aliyuncs.com")
    AccountName = ['webapi_readonly', 'take_readonly', 'imiaoj_readonly']
    message = """数据库：rds1\n账户：%s\n密码：%s\n注：收到账户请测试连接及权限问题，有问题及时跟运维联系"""
    try:
        if sys.argv[1] and sys.argv[2]:
            pass
    except IndexError,e:
        for account in AccountName:
            passwd = T.make_passwd()
            T.do_request({"Action":"ResetAccountPassword","DBInstanceId":"数据库实例ID","AccountName":account,"AccountPassword":passwd})
    else:
        for account in AccountName:
            passwd = T.make_passwd() 
            messages = message % (account, passwd)
            mails = sys.argv[2].split(',')
            if account == "webapi_readonly" and sys.argv[1] == "webapi_readonly":
                for mailto in mails:
                    T.sendmail(messages, mailto)
                T.do_request({"Action":"ResetAccountPassword","DBInstanceId":"数据库实例ID","AccountName":account,"AccountPassword":passwd})
            if account == "take_readonly" and sys.argv[1] == "take_readonly":
                for mailto in mails:
                    T.sendmail(messages, mailto)
                T.do_request({"Action":"ResetAccountPassword","DBInstanceId":"数据库实例ID","AccountName":account,"AccountPassword":passwd})
            if account == "imiaoj_readonly" and sys.argv[1] == "imiaoj_readonly":
                for mailto in mails:
                    T.sendmail(messages, mailto)
                T.do_request({"Action":"ResetAccountPassword","DBInstanceId":"数据库实例ID","AccountName":account,"AccountPassword":passwd})
