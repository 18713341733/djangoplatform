# -*- coding: utf-8 -*- 

import sys
from sys import argv
from datetime import datetime, timedelta
import logging
import MySQLdb
import os 
import logging
import time
import subprocess
import io



#------Main--------------------------------------------------------
script, tomcatDir = argv
logging.basicConfig(filename='PostUpgrade.py' + datetime.now().strftime("%Y-%m-%d") + '.log', level=logging.INFO)

logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "开始执行删除文件脚本...........................................................")

    
logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "开始执行sql脚本...........................................................")
arg_host = "192.168.56.1"
arg_port = 3307
arg_user = "root"
arg_passwd = "root"
arg_db = "veems"


try:
    # Start 初始化Mysql
    conn = MySQLdb.connect(host=arg_host,
                           port=int(arg_port),
                           user=arg_user,
                           passwd=arg_passwd,
                           db=arg_db
                           , use_unicode=True, charset='utf8')

except Exception as  e:
    logging.error(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '192.168.56.1连接失败，正在连接127.0.0.1...............')
    conn = MySQLdb.connect(host="127.0.0.1",
                           port=int(arg_port),
                           user=arg_user,
                           passwd=arg_passwd,
                           db=arg_db
                           , use_unicode=True, charset='utf8')
    logging.error(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + 'release505连接数据库127.0.0.1成功...................')
    logging.error(e)
else:
    logging.error(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '数据库连接失败')

#########################################################################################################
# 执行SQL脚本
def runSQLCmd(sqlFile):
    try:
        with io.open(sqlFile,mode='r',encoding='utf-8') as f:
            # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
            sqls = f.read()
            sql_list = sqls.split(';')[:-1]

            for x in sql_list:
                # 判断包含空行的
                if '\n' in x:
                    # 替换空行为1个空格
                    x = x.replace('\n', ' ')

                # 判断多个空格时
                if '    ' in x:
                    # 替换为空
                    x = x.replace('    ', '')

                # sql语句添加分号结尾
                sql_item = x + ';'
                sql_item = sql_item.replace("&&",";")

                # if sql_item in "CALL":
                #     cur.callproc('pro_AddColumn', args=())
                # else:
                try:
                    cur.execute(sql_item)
                    #print(u"执行成功sql: %s" % sql_item)
                except Exception as e:
                    logging.info(u"错误提示sql:%s", sql_item)
                    logging.error(u"错误提示:%s", e)
    except Exception as e:
        logging.error(u"错误提示:%s",  e)
    finally:
        conn.commit();

#执行cmd命令
def runCmd(cmd):
    res = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    sout, serr = res.communicate()  # 该方法和子进程交互，返回一个包含 输出和错误的元组，如果对应参数没有设置的，则无法返回
    return res,res.returncode, sout, serr, res.pid  # 可获得返回码、输出、错误、进程号；

try:
    cur = conn.cursor()    
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    cur.execute('SET FOREIGN_KEY_CHECKS=0;')
    sqlFile = sys.path[0] + '/upgrade.sql';
    runSQLCmd(sqlFile);

    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "数据库升级成功...........................................................")
except Exception as  e:
    logging.error(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '数据库升级失败:')
    logging.error(e)
    #########################################################################################################