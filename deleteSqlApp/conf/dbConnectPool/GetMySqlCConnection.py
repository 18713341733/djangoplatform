# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: GetMySqlCConnection.py
from deleteSqlApp.conf.dbConnectPool.MySqlCConnectionPool import MySqlCConnectionPool
from deleteSqlApp.utils.singleton import singleton
@singleton
class GetKytzDevConnection:
    def __init__(self):
        self.conn = MySqlCConnectionPool()

