# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -09
# @File: test_mysql_connect.py
from deleteSqlApp.utils.HandleSqlMysqlC import HandleSqlMysqlC
from deleteSqlApp.utils.HandleSqlMysqlA import HandleSqlMysqlA
from deleteSqlApp.model.DBPoolSet import DBPoolSet
from deleteSqlApp.model.DbInfo import DbInfo
from deleteSqlApp.utils.YmlUtil import YmlUtil

def test_mysql_connet():
    # 建立a 的连接池
    a_mysql_db = HandleSqlMysqlA()

    # 建立c的连接池
    c_mysql_db = HandleSqlMysqlC()

    # a 执行查询sql
    a_sql = "SELECT * FROM a.client WHERE id = %s"
    param = "1"
    param1 = "2"
    result1 = a_mysql_db.selectone(a_sql, param)
    result2 = a_mysql_db.selectone(a_sql, param1)

    print("a 执行查询sql", result1)
    print("a 执行查询sql", result2)

    # c 执行查询sql
    c_sql = "SELECT * FROM c.act WHERE id = %s"
    param3 = "34"
    param4 = "35"
    result3 = c_mysql_db.selectone(c_sql, param3)
    result4 = c_mysql_db.selectone(c_sql, param4)

    print("result3", result3)
    print("result4", result4)
if __name__ == '__main__':
    test_mysql_connet()
    print("-----------------")
    test_mysql_connet()














