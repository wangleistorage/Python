#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys, os, shutil, re

project = {
           'http://gitlab.ops.xkeshi.so/backend-new-framework/xkeshi-business.git': (['common','openApi','servicebus','statistics','xkeshi-sync']),
           'http://gitlab.ops.xkeshi.so/backend-openplatform/shopplatform.git': ['shopplatform'],
           'http://gitlab.ops.xkeshi.so/backend-openplatform/integralmall.git': ['integralmall'],
           'http://gitlab.ops.xkeshi.so/backend-openplatform/ele.git': ['takeaway'],
           'http://gitlab.ops.xkeshi.so/backend-member-market/xkeshi-member.git': ['member'],
           'http://gitlab.ops.xkeshi.so/framework/x-framework.git': ['xkeshi-framework'],
           'http://gitlab.ops.xkeshi.so/backend-social/wemall.git': ['wemall'],
           'http://gitlab.ops.xkeshi.so/framework/cas-4.1.10.git': ['cas'],
           'http://gitlab.ops.xkeshi.so/backend-shop-item/shop.git': ['shop'],
           'http://gitlab.ops.xkeshi.so/backend-payment/payment.git': ['payment'],
           'http://gitlab.ops.xkeshi.so/backend-payment/ecoupon.git': ['ecoupon'],
}

project_path = "/root/.m2/repository/com/xkeshi/"
project_module = sys.argv[1]

def delete_module(module):
    global project_path
    os.chdir(project_path)
    print module

    for mod in module:
        print '-------------  ' + mod + '  ------------'
        if os.path.exists(mod):
            shutil.rmtree(mod)
            print 'delete %s' % mod
    
        path_lists = os.listdir(project_path)
        path = []
        pattern = "^%s-" % mod
        for i in path_lists:
            if re.search(pattern, i):
                if os.path.isdir(i):
                    path.append(i)

        for i in path:
            shutil.rmtree(i)
            print 'delete ---> %s' % i

try:
    module =  project[project_module]
except KeyError, e:
    print 'Please add a new project address to Jenkins choice'
    sys.exit()
else:
    delete_module(module)
