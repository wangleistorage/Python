#!/usr/bin/python
# -*- coding:utf-8 -*-

# 定义函数"book_and_milk",并且定义两个参数book_count,milk_count

def book_and_milk(book_count, milk_count):
    print "I have %d books." % book_count
    print "I have %d milk.\n" % milk_count

# 设置变量
book_count = 10
milk_count = 12

book_and_milk(5, 4)
book_and_milk(book_count, milk_count)
book_and_milk(5 * 2, 4 * 2)
book_and_milk(book_count * 10, milk_count * 10)
