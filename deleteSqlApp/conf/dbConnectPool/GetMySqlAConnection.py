# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: GetMySqlAConnection.py
from deleteSqlApp.conf.dbConnectPool.MySqlAConnectionPool import MySqlAConnectionPool
from deleteSqlApp.utils.singleton import singleton


@singleton
class GetMySqlAConnection:
    def __init__(self):
        self.conn = MySqlAConnectionPool()

