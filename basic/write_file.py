#!/usr/bin/python
# -*- coding:utf-8 -*-

from sys import argv
from os.path import exists
script, files = argv

print "file exists? ", exists(files)
print "file long? ", len(files)

print "get new line"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "open %s" % files
txt = open(files,'w')

print "write new line to %s" % files
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

txt.close()
