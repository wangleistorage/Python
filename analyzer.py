#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import re
import os

day = time.strftime('%Y-%m-%d')

log_file = '/home/tracker/access.log'
to_logfile = '/home/tracker/logfile'

# 颜色定义
def color_print(msg, color='red', exits=False):
    """
    Print colorful string.
    颜色打印字符或者退出
    """
    color_msg = {'blue': '\033[1;36m%s\033[0m',
                 'green': '\033[1;32m%s\033[0m',
                 'yellow': '\033[1;33m%s\033[0m',
                 'red': '\033[1;31m%s\033[0m',
                 'title': '\033[30;42m%s\033[0m',
                 'info': '\033[32m%s\033[0m'}
    msg = color_msg.get(color) % msg
    if exits:
        time.sleep(2)
        sys.exit()
    return msg


print color_print('------------------- Nginx access.log 日志分析 --------------------')
print 

# 统计总访问次数
def day_total_access_count():
    totalrequests = 0
    f = open(log_file)
    files = f.readlines()
    for i in files:
        totalrequests += 1
    print color_print("昨日请求总量: %s" % totalrequests, "green")
    print
    #f = open(to_logfile, 'w')
    #f.write("total count: %s" % totalrequests)
    #f.close()


# 统计每个小时的访问次数
def hour_total_access_count():
    total_hours = []
    for hour in range(24):
        if hour <= 9:
            hour = '0' + str(hour)
        hours = 'T' + str(hour)
        total_hours.append(hours)
    #print total_hours
     
    f = open(log_file)
    files = f.readlines()
    f.close()

    count = {}
    print color_print("---------------------- 每小时请求数量 ----------------------", "green")
    print color_print("当前时间:\t\t\t\t\t  请求数量:", "green")
    for current_hours in total_hours:
        current_hours_line = 0
        for line in files:
            if re.search(current_hours, line):
                current_hours_line += 1
        #print "当前小时:%s ---> 访问量:%s" % (current_hours, current_hours_line),
        print color_print("  %s  \t\t\t\t\t\t   %s" % (current_hours, current_hours_line))
        count[current_hours] = current_hours_line
    print
     
    
    y = max(count.items(), key=lambda x:x[1])
    print color_print("----------------- 昨日访问高峰时间及数量 -----------------", "green")
    print color_print("高峰时间: %s  \t\t\t\t  请求数量: %s" % (y[0], y[1]))
    print

    total_minute = []
    for times in range(60):
        if times <= 9:
            times = '0' + str(times)
            total_minute.append(str(times))
        else:
            total_minute.append(str(times))
    #print total_minute
    
    f = open(log_file)
    files = f.readlines()
    f.close()
    print color_print("--------------- 昨日访问峰值一小时请求分析 ---------------", "green")
    print color_print("当天峰值最高时间段: \t\t\t\t 请求数量:", "green")
    for current_minute in total_minute:
        times = y[0] + ":" + current_minute
        max_hour_line = 0
        for line in files:
            if re.search(times, line):
                max_hour_line += 1
        print color_print("      %s \t\t\t\t\t %s" % (times, max_hour_line)) 


def minute_total_access_count():
    total_hours = []
    total_minute = []

    for times in range(60):
        if times <= 23:
            if times <= 9:
                times = '0' + str(times)
                total_hours.append(str(times))
            else:
                total_hours.append(str(times))
        if times <= 9:
            total_minute.append('0' + str(times))
        else:
            total_minute.append(str(times))

    count = {}
    f = open(log_file)
    files = f.readlines()
    for current_hours in total_hours:
        for current_minute in total_minute:
            current_times = 'T' +  current_hours + ':' + current_minute
            #print current_times
            current_times_line = 0
            for line in files:
                if re.search(current_times, line):
                    current_times_line += 1 
            print "当前分钟:%s ---> 访问量:%s" % (current_times, current_times_line)
            count[current_times] = current_times_line

    y =  max(count.items(), key=lambda x:x[1])
    print "每分钟中访问高峰于: %s  \n访问的请求数为: %s" % (y[0], y[1])
    

day_total_access_count()
hour_total_access_count()
#minute_total_access_count()

