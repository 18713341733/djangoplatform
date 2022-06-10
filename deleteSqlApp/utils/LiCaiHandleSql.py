# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -09
# @File: LiCaiHandleSql.py
from deleteSqlApp.conf.dbConnectPool.GetLiCaiConnection import GetLiCaiConnection

from deleteSqlApp.model.DBPoolSet import DBPoolSet
from deleteSqlApp.model.DbInfo import DbInfo
from deleteSqlApp.model.DBPoolSet import DBPoolSet
from deleteSqlApp.utils.YmlUtil import YmlUtil
import os

"""
执行语句查询有结果返回结果没有返回0；
增/删/改返回变更数据条数，没有返回0
"""

class LiCaiHandleSql:
    __instance = None


    def __init__(self):
        self.db = GetLiCaiConnection().conn

    # 封装执行命令
    def execute(self, sql, param=None, autoclose=False):
        """
        【主要判断是否有参数和是否执行完就释放连接】
        :param sql: 字符串类型，sql语句
        :param param: sql语句中要替换的参数"select %s from tab where id=%s" 其中的%s就是参数
        :param autoclose: 是否关闭连接
        :return: 返回连接conn和游标cursor
        """
        cursor, conn = self.db.getconn()  # 从连接池获取连接
        count = 0
        try:
            # count : 为改变的数据条数
            if param:
                count = cursor.execute(sql, param)
            else:
                count = cursor.execute(sql)
            conn.commit()
            if autoclose:
                self.close(cursor, conn)
        except Exception as e:
            pass
        return cursor, conn, count

    # 释放连接
    def close(self, cursor, conn):
        """释放连接归还给连接池"""
        cursor.close()
        conn.close()

    # 查询所有
    def selectall(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(e)
            self.close(cursor, conn)
            return count

    # 查询单条
    def selectone(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            res = cursor.fetchone()
            self.close(cursor, conn)
            return res
        except Exception as e:
            print("error_msg:", e.args)
            self.close(cursor, conn)
            return count

    # 增加
    def insertone(self, sql, param):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            # _id = cursor.lastrowid()  # 获取当前插入数据的主键id，该id应该为自动生成为好
            conn.commit()
            self.close(cursor, conn)
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 增加多行
    def insertmany(self, sql, param):
        """
        :param sql:
        :param param: 必须是元组或列表[(),()]或（（），（））
        :return:
        """
        cursor, conn, count = self.db.getconn()
        try:
            cursor.executemany(sql, param)
            conn.commit()
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 删除
    def delete(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            self.close(cursor, conn)
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count

    # 更新
    def update(self, sql, param=None):
        cursor = None
        conn = None
        count = None
        try:
            cursor, conn, count = self.execute(sql, param)
            conn.commit()
            self.close(cursor, conn)
            return count
        except Exception as e:
            print(e)
            conn.rollback()
            self.close(cursor, conn)
            return count

# TODO 查询单条
# sql1 = 'select * from userinfo where name=%s'
# args = 'python'
# ret = db.selectone(sql=sql1, param=args)
# print(ret)  # (None, b'python', b'123456', b'0')

# TODO 增加单条
# sql2 = 'insert into hotel_urls(cname,hname,cid,hid,url) values(%s,%s,%s,%s,%s)'
# ret = db.insertone(sql2, ('1', '2', '1', '2', '2'))
# print(ret)

# TODO 增加多条
# sql3 = 'insert into userinfo (name,password) VALUES (%s,%s)'
# li = li = [
#     ('分省', '123'),
#     ('到达','456')
# ]
# ret = db.insertmany(sql3,li)
# print(ret)

# TODO 删除
# sql4 = 'delete from  userinfo WHERE name=%s'
# args = 'xxxx'
# ret = db.delete(sql4, args)
# print(ret)

# TODO 更新
# sql5 = r'update userinfo set password=%s WHERE name LIKE %s'
# args = ('993333993', '%old%')
# ret = db.update(sql5, args)
# print(ret)


