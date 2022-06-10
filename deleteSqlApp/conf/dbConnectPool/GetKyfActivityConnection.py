# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: GetKyfActivityConnection.py
from deleteSqlApp.conf.dbConnectPool.KyfActivityConnectionPool import KyfActivityConnectionPool
from deleteSqlApp.utils.singleton import singleton


@singleton
class GetKyfActivityConnection:
    def __init__(self):
        self.conn = KyfActivityConnectionPool()

