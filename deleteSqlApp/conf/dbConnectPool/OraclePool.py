# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: OraclePool.py

# 基于cx_Oracle自带SessionPool连接池, 线程中使用, 则配置threaded=True
# 官方文档摘要:
# Oracle Real-World Performance Group的建议是使用固定大小的连接池。min和max的值应相同（且增量等于零）。
# 该防火墙，资源管理器 或用户配置文件IDLE_TIME 不应该过期空闲会话。这避免了会降低吞吐量的连接风暴。请参阅《防止连接风暴的指南：使用静态池》，其中包含有关池大小调整的详细信息。
# https://blog.csdn.net/maixiaochai/article/details/82986517

import cx_Oracle as Oracle

from contextlib import contextmanager
import os,sys

from deleteSqlApp.model.DbInfo import DbInfo


class OraclePool:
    """
        1) 这里封装了一些有关oracle连接池的功能;
        2) sid和service_name，程序会自动判断哪个有值，
            若两个都有值，则默认使用service_name；
        3) 关于config的设置，注意只有 port 的值的类型是 int，以下是config样例:
            config = {
                'username':     'maixiaochai',
                'password':     'maixiaochai',
                'host':         '192.168.158.1',
                'port':         1521,
                'sid':          'maixiaochai',
                'service_name': 'maixiaochai'
            }
        """
    __pool = None

    # def __init__(self, username, password, host, port, sid=None, service_name=None):
    def __init__(self,dbInfo:DbInfo):
        self.__pool = self.__get_pool(dbInfo)

    @staticmethod
    # def __get_pool(username, password, host, port, sid=None, service_name=None, pool_size=5):
    def __get_pool(dbInfo:DbInfo, pool_size=5):
        """
        ---------------------------------------------
        以下设置，根据需要进行配置
        max                 最大连接数
        min                 初始化时，连接池中至少创建的空闲连接。0表示不创建
        increment           每次增加的连接数量
        pool_size           连接池大小，这里为了避免连接风暴造成的资源浪费，设置了 max = min = pool_size
        """
        dsn = Oracle.makedsn(dbInfo.host, dbInfo.port, service_name=dbInfo.database)
        # dsn = None
        # if service_name:
        #     dsn = Oracle.makedsn(host, port, service_name=service_name)
        # elif sid:
        #     dsn = Oracle.makedsn(host, port, sid=sid)

        return Oracle.SessionPool(user=dbInfo.username, password=dbInfo.password, dsn=dsn, min=pool_size, max=pool_size, increment=0,
                                  encoding='UTF-8')


    @property
    @contextmanager
    def pool(self):
        _conn = None
        _cursor = None
        try:
            _conn = self.__pool.acquire()
            _cursor = _conn.cursor()
            yield _cursor
        finally:
            _conn.commit()
            self.__pool.release(_conn)


    def execute(self, sql: str, *args, **kwargs):
        """
        执行sql语句
        :param sql:     str     sql语句
        :param args:    list    sql语句参数列表
        :return:        conn, cursor
        """
        with self.pool as cursor:
            cursor.execute(sql, *args, **kwargs)

    def executemany(self, sql, *args, **kwargs):
        """
        批量执行。
        :param sql:     str     sql语句
        :param args:    list    sql语句参数
        :return:        tuple   fetch结果
        """
        with self.pool as cursor:
            cursor.executemany(sql, *args, **kwargs)

    def fetchone(self, sql, *args, **kwargs) -> tuple:
        """
        获取全部结果
        :param sql:     str     sql语句
        :param args:    list    sql语句参数
        :return:        tuple   fetch结果
        """
        with self.pool as cursor:
            cursor.execute(sql, *args, **kwargs)
            return cursor.fetchone()

    def fetchall(self, sql, *args, **kwargs):
        """
        获取全部结果
        :param sql:     str     sql语句
        :param args:    list    sql语句参数
        :return:        tuple   fetch结果
        """
        with self.pool as cursor:
            cursor.execute(sql, *args, **kwargs)
            return cursor.fetchall()

    def __del__(self):
        """
        关闭连接池。
        """
        self.__pool.close()