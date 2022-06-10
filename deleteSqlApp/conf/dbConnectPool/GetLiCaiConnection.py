# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: GetLiCaiConnection.py

from deleteSqlApp.conf.dbConnectPool.LiCailConnectionPool import LiCaiConnectionPool
from deleteSqlApp.utils.singleton import singleton


@singleton
class GetLiCaiConnection:
    def __init__(self):
        self.conn = LiCaiConnectionPool()


