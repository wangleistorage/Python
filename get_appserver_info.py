#!/usr/bin/python

import argparse
import MySQLdb

def mysql_info(sql):
    mysql = {'host':'0.0.0.0', 'user':'wanglei', 'port':3306, 'passwd': 'passwd', 'db':'wanglei'}
    conn = MySQLdb.connect(host=mysql['host'], user=mysql['user'], port=mysql['port'], passwd=mysql['passwd'], db=mysql['db'])
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close
    return data

def get_para():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-name", dest="server_name", help="set server name")
    parser.add_argument("--server-type", dest="server_type", action='store_true', help="get server type")
    parser.add_argument("--server-env", dest="server_env", action='store_true', help="get server environment")
    parser.add_argument("--server-deploy-ip", dest="server_deploy_ip", action='store_true', help="get server deplpy ip address")
    parser.add_argument("--server-deploy-port", dest="server_deploy_port", action='store_true', help="get server deploy path")
    parser.add_argument("--server-deploy-path", dest="server_deploy_path", action='store_true', help="get server deploy path")
    parser.add_argument("--server-logs-path", dest="server_logs_path", action='store_true', help="get server logs path")
    parser.add_argument("--all-server-info", dest="all_server_info", action='store_true', help="get server all info")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_para()
    server_info = {}
    sql = "select * from wanglei.ops_app_server where server_name='%s'" % args.server_name

    if args.server_type or args.all_server_info:
        value = mysql_info(sql)
        server_info["server_type"] = value[3]

    if args.server_env or args.all_server_info:
        value = mysql_info(sql)
        server_info["server_env"] = value[5]

    if args.server_deploy_ip or args.all_server_info:
        value = mysql_info(sql)
        server_info["server_deploy_ip"] = value[6]

    if args.server_deploy_port or args.all_server_info:
        value = mysql_info(sql)
        server_info["server_deploy_port"] = value[7]

    if args.server_deploy_path or args.all_server_info:
        value = mysql_info(sql)
        server_info["server_deploy_path"] = value[8]

    if args.server_logs_path or args.all_server_info:
        value = mysql_info(sql)
        server_info["server_logs_path"] = value[13]
 
    if server_info:
        print server_info
