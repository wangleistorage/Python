#!/usr/bin/python
# -*- coding:utf-8 -*-

# 定义函数"print_one",包含参数arg1
def print_one(arg1):
    print "arg1:%s" % arg1

# 定义函数"print_rwo",包含匹配参数*arg
def print_two(*arg):
    arg1, arg2 = arg
    print "arg1:%s, arg2:%s" % (arg1, arg2)

# 定义函数"print_two_again",包含参数arg1,arg2
def print_two_again(arg1, arg2):
    print "arg1:%s, arg2:%s" % (arg1, arg2)

# 定义函数"print_none",没有定义参数
def print_none():
    print "none argument"

print_one("hong")
print_two("hong","xue")
print_two_again("hong","xue")
print_none()
