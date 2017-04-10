#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import os
import sys
import datetime
import time

def get_delete_day(day_num):
    today = datetime.date.today()
    day = datetime.timedelta(days=day_num)
    return today - day

def arch_delete_by_query():
    day_num = int(sys.argv[2])
    times = str(get_delete_day(day_num)) + 'T' + time.strftime('%H:%M:%S') + '+' + '08:00'
    es_logs = ['xkeshi_log-accesslog', 'xkeshi_log-errorlog']
    es_user = "es_admin1:tz9aAD9L"
    es_addr = "101.37.38.127:9200"
    data ='{"query": {"range": {"createTime":{"from": null,"to": "%s"}}}}' % times
    for index_name in es_logs:
        cmd="curl --user %s -XDELETE '%s/%s/_query?pretty' -H 'Content-Type: application/json' -d '%s'" % (es_user, es_addr, index_name, data)
        os.system(cmd)

def arch_delete_index():
    day_num = int(sys.argv[2])
    times = str(get_delete_day(day_num))
    es_logs = ['xkeshi_log-']
    es_addr = 'http://101.37.38.127:9200/'
    es_user = "es_admin1:tz9aAD9L"
    for log in es_logs:
        delete_url = es_addr + log + str(times)
        cmd = "curl -u %s -XDELETE %s" % (es_user, delete_url)
        os.system(cmd)

def data_delete_index():
    day_num = int(sys.argv[2])
    times = str(get_delete_day(day_num))
    es_logs = ['xkeshi_log_', 'xkeshi_nginx_log_']
    es_addr = 'http://120.55.99.43:9200/'
    es_user = "xkeshi_admin3:FQxZWKm2"
    for log in es_logs:
        delete_url = es_addr + log + str(times)
        cmd = "curl -u %s -XDELETE %s" % (es_user, delete_url)
        os.system(cmd)

try:
    if sys.argv[1] and sys.argv[2]:
         pass
except:
    print 'Usage: %s  execute_function_name  delete_log_days' % sys.argv[0]
else:
    if sys.argv[1] == "arch_delete_by_query" and sys.argv[2].isdigit():
        arch_delete_by_query()
    if sys.argv[1] == "arch_delete_index" and sys.argv[2].isdigit():
        arch_delete_index()
    if sys.argv[1] == "data_delete_index" and sys.argv[2].isdigit():
        data_delete_index()
