#!/usr/bin/python

import sys
import os
import shutil
import re

lists = ['account', 'account-api', 'account-business', 'account-dubbo', 'account-scheduler', 'account-web', 'ape-api', 'ape-scheduler', 'common', 'common-api', 'common-business', 'common-web', 'couponplatform', 'couponplatform-api', 'couponplatform-business', 'couponplatform-dubbo', 'couponplatform-web', 'dataCollection', 'dataCollection-api', 'dataCollection-business', 'dataCollection-dubbo', 'dataCollection-web', 'datapush', 'datapush-api', 'datapush-business', 'datapush-dubbo', 'datapush-web', 'delivery', 'delivery-api', 'delivery-business', 'ecoupon', 'ecoupon-api', 'ecoupon-business', 'ecoupon-dubbo', 'gateway', 'gateway-web', 'gather', 'gather-api', 'gather-business', 'integralmall', 'integralmall-api', 'integralmall-business', 'koubei-shop-sdk', 'market-web', 'maven', 'member', 'member-api', 'member-business', 'member-dubbo', 'member-web', 'message', 'message-api', 'message-business', 'message-dubbo', 'message-platform', 'message-sdk', 'message-sender', 'message-web', 'microWeb', 'mybatis', 'openApi', 'openapi-sdk', 'openplatform', 'openplatform-api', 'openplatform-business', 'payment', 'payment-api', 'payment-business', 'payment-dubbo', 'payment-sdk', 'payment-web', 'servicebus', 'shop', 'shop-api', 'shop-business', 'shop-dubbo', 'shopplatform', 'shopplatform-api', 'sign-tools', 'statistics', 'statistics-api', 'statistics-business', 'statistics-dubbo', 'takeaway', 'takeaway-api', 'takeaway-business', 'takeaway-dubbo', 'takeaway-web', 'virtualservice', 'virtualservice-api', 'virtualservice-business', 'virtualserviceplatform', 'weixin', 'weixin-api', 'weixin-business', 'wemall', 'wemall-api', 'wemall-business', 'wemall-web', 'xkeshi', 'xkeshi-business', 'xkeshi-core', 'xkeshi-etl', 'xkeshi-framework', 'xkeshi-framework-core', 'xkeshi-framework-services', 'xkeshi-framework-webkits', 'xkeshi-item', 'xkeshi-koubei', 'xkeshi-market', 'xkeshi-market-api', 'xkeshi-market-business', 'xkeshi-market-platform', 'xkeshi-scheduler', 'xkeshi-spi', 'xkeshi-sync', 'xkeshi-vip']

path = "/root/.m2/repository/com/xkeshi/"
pom = sys.argv[1]

def delete_module(pom):
    pom_module = pom[:-8]
    os.chdir(path)
    shutil.rmtree(pom_module)

    if pom_module in lists:
        pattern = "^%s-" % pom_module
        for i in lists:
            if re.search(pattern, i):
                os.chdir(path)
                shutil.rmtree(i)

delete_module(pom)
