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
    es_logs = ['elasticsearch_log-accesslog', 'elasticsearch_log-errorlog']
    es_user = "user:pass"
    es_addr = "0.0.0.0:9200"
    data ='{"query": {"range": {"createTime":{"from": null,"to": "%s"}}}}' % times
    for index_name in es_logs:
        cmd="curl --user %s -XDELETE '%s/%s/_query?pretty' -H 'Content-Type: application/json' -d '%s'" % (es_user, es_addr, index_name, data)
        os.system(cmd)

def arch_delete_index():
    day_num = int(sys.argv[2])
    times = str(get_delete_day(day_num))
    es_logs = ['elasitcsearch_log-']
    es_addr = 'http://0.0.0.0:9200/'
    es_user = "user:pass"
    for log in es_logs:
        delete_url = es_addr + log + str(times)
        cmd = "curl -u %s -XDELETE %s" % (es_user, delete_url)
        os.system(cmd)

def data_delete_index():
    day_num = int(sys.argv[2])
    times = str(get_delete_day(day_num))
    es_logs = ['elasticsearch_log_', 'elasticsearch_nginx_log_']
    es_addr = 'http://0.0.0.0:9200/'
    es_user = "user:pass"
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
