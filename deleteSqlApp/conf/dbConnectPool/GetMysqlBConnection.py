# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: GetMysqlBConnection.py

from deleteSqlApp.conf.dbConnectPool.MySqlBConnectionPool import MySqlBConnectionPool
from deleteSqlApp.utils.singleton import singleton


@singleton
class GetMySqlBConnection:
    def __init__(self):
        self.conn = MySqlBConnectionPool()


