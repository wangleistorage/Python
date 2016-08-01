#!/usr/bin/python
# -*- coding:utf-8 -*-

from sys import argv
script, files = argv
prompt = "> "

print "script name --> %s" % script
print "files name --> %s" % files


print "open %s ..." % files
print "print %s ..." % files
print "-" * 30

txt = open(files)
content = txt.read()

print content
