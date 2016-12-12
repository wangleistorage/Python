#!/usr/bin/python

import time, subprocess, os, shutil, pexpect

times = time.strftime('%Y%m%d')
rds1 = ['xkeshi_com', 'xkeshi_shop_new', 'xkeshi_payment', 'xkeshi_sso', 'coupon_platform', 'xkeshi_market', 'wemall']
rds2 = ['xkeshi_ecoupon', 'xkeshi_business', 'xkeshi_common']

rds1_host = 'rds1.mysql.rds.aliyuncs.com'
rds1_port = 3306
rds2_host = 'rds2.mysql.rds.aliyuncs.com'
rds2_port = 3400
rds_path = '/mnt/aliyunrds1bk/tracker/'
rds_today_path = rds_path + times

rds_remote_path = '/home/tracker/rds_backup'
rds_remote_host = '192.168.143.202'

def rds_database_bak(database, host, port):
    if not os.path.exists(rds_today_path):
        os.makedirs(rds_today_path)
    os.chdir(rds_today_path)
    for rds in database:
        name = rds + '_' + times
        retn = subprocess.call("/home/guoqing/mysql/bin/mysqldump --defaults-extra-file=/home/scripts/recon/rds-my.cnf --set-gtid-purged=OFF --default-character-set=utf8 --single-transaction -R -q -h%s -P%s %s > %s.sql" % (host, port, rds, name), shell=True)
        retn = subprocess.call("tar zcf %s.tar.gz %s.sql" % (name, name), shell=True)    
        retn = subprocess.call("rm -f %s.sql" % name, shell=True)
        retn = subprocess.call("find ./ -mtime +30 -name '*.tar.gz' -exec rm -Rf {} \;", shell=True)
        time.sleep(5)

def rds_database_bak_tgz(remote_host, remote_path):
    name = 'rds_backup_' + times
    os.chdir(rds_path)
    retn = subprocess.call("tar zcf %s.tar.gz %s" % (name, times), shell=True)
    cmd = 'scp -r %s.tar.gz %s:%s' % (name, remote_host, remote_path)
    scp = pexpect.spawn(cmd)
    scp.read()

rds_database_bak(rds1, rds1_host, rds1_port)
rds_database_bak(rds2, rds2_host, rds2_port)

rds_database_bak_tgz(rds_remote_host, rds_remote_path)
