#!/usr/bin/python

import urllib2, subprocess, base64

api_url = 'https://docker.wanglei.net/v2/_catalog'
username = 'wanglei'
password = 'wanglei'

socket = urllib2.urlopen(api_url)
content = socket.read()
socket.close()

content = eval(content)

for i in content:
    images_lists = content[i]

for i in images_lists:
    tag_url = 'https://docker.wanglei.net/v2/%s/tags/list' % i
    request = urllib2.Request(tag_url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header('Authorization', 'Basic %s' % base64string)
    result = urllib2.urlopen(request)

    for i in result:
        i = eval(i)
        x = i['tags']
        print 'name: ', i['name']
        print 'tags: '
        for q in x:
            print ' ' * 6, q
        print ''
