#!/usr/bin/python

import time, subprocess, os, shutil

times = time.strftime('%Y%m%d')
rds1 = ['xkeshi_com', 'xkeshi_shop_new', 'xkeshi_payment', 'xkeshi_sso', 'coupon_platform', 'xkeshi_market', 'wemall']
rds2 = ['xkeshi_ecoupon', 'xkeshi_business', 'xkeshi_common']

rds1_host = 'rds1.mysql.rds.aliyuncs.com'
rds1_port = 3306
rds2_host = 'rds2.mysql.rds.aliyuncs.com'
rds2_port = 3400
rds_home = '/mnt/aliyunrds1bk/tracker/' + times

def rds_database_bak(database, host, port):
    if not os.path.exists(rds_home):
        os.makedirs(rds_home)
    os.chdir(rds_home)
    for rds in database:
        name = rds + '_' + times
        retn = subprocess.call("/home/guoqing/mysql/bin/mysqldump --defaults-extra-file=/home/scripts/recon/rds-my.cnf --set-gtid-purged=OFF --default-character-set=utf8 --single-transaction -R -q -h%s -P%s %s > %s.sql" % (host, port, rds, name), shell=True)
        retn = subprocess.call("tar zcf %s.tar.gz %s.sql" % (name, name), shell=True)    
        retn = subprocess.call("rm -f %s.sql" % name, shell=True)
        retn = subprocess.call("find ./ -mtime +30 -name '*.tar.gz' -exec rm -Rf {} \;", shell=True)
        time.sleep(5)

rds_database_bak(rds1, rds1_host, rds1_port)
rds_database_bak(rds2, rds2_host, rds2_port)
