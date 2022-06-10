from dbutils.pooled_db import PooledDB
from deleteSqlApp.model.DBPoolSet import DBPoolSet
from deleteSqlApp.model.DbInfo import DbInfo
import random

from deleteSqlApp.utils.YmlUtil import YmlUtil

"""
@功能：创建数据库连接池
"""


class LiCaiConnectionPool(object):
    __pool = None
    path = "/Users/zhaohui/PycharmProjects/KunYuan/KunYuanJiJin/deleteSqlApp/conf/dbinfo/licai.yml"
    dbInfo = YmlUtil.readDbYml(path)
    dbPoolSet = DBPoolSet()

    # 构造器，传DbInfo、DBPoolSet
    # def __init__(self):
    #     self.conn = self.__getconn()
    #     self.cursor = self.conn.cursor()

    # 创建数据库连接conn和游标cursor
    def __enter__(self):
        self.conn = self.__getconn()
        self.cursor = self.conn.cursor()

    # 创建数据库连接池,私有方法
    def __getconn(self):

        if self.__pool is None:
            self.__pool = PooledDB(
                creator=self.dbPoolSet.DB_CREATOR, # creator : 使用连接数据库的模块
                mincached=self.dbPoolSet.DB_MIN_CACHED, # mincached : 启动时开启的闲置连接数量(缺省值 0 开始时不创建连接)
                maxcached=self.dbPoolSet.DB_MAX_CACHED,
                maxshared=self.dbPoolSet.DB_MAX_SHARED,
                maxconnections=self.dbPoolSet.DB_MAX_CONNECYIONS,
                blocking=self.dbPoolSet.DB_BLOCKING,
                maxusage=self.dbPoolSet.DB_MAX_USAGE,
                setsession=self.dbPoolSet.DB_SET_SESSION,
                host=self.dbInfo.host,
                port=self.dbInfo.port,
                user=self.dbInfo.username,
                passwd=self.dbInfo.password,
                db=self.dbInfo.database,
                use_unicode=False,
                charset=self.dbInfo.charset
            )

        return self.__pool.connection()

    # 释放连接池资源
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    # 关闭连接归还给链接池
    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()

    # 从连接池中取出一个连接
    def getconn(self):
        conn = self.__getconn()
        cursor = conn.cursor()
        return cursor, conn


# # 获取连接池,实例化
# def get_licai_connection() -> LiCaiConnectionPool:
#     return LiCaiConnectionPool()