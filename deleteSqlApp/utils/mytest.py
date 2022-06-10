# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -09
# @File: mytest.py
from deleteSqlApp.utils.LiCaiHandleSql import LiCaiHandleSql
from deleteSqlApp.utils.KyfActivityHandleSql import KyfActivityHandleSql
from deleteSqlApp.model.DBPoolSet import DBPoolSet
from deleteSqlApp.model.DbInfo import DbInfo
from deleteSqlApp.utils.YmlUtil import YmlUtil

def test_my_connet():
    # 建立kyf_activity 的连接池
    kyf_activity_db = KyfActivityHandleSql()

    # 建立licai的连接池
    licai_dbInfo_db = LiCaiHandleSql()

    # licai 执行查询sql
    licai_sql = "SELECT * FROM licai.client_registration_info WHERE id = %s"
    param = "1"
    param1 = "2"
    result1 = licai_dbInfo_db.selectone(licai_sql, param)
    result2 = licai_dbInfo_db.selectone(licai_sql, param1)

    print("licai 执行查询sql", result1)
    print("licai 执行查询sql", result2)

    # kyf_activity 执行查询sql
    kyf_activity_sql = "SELECT * FROM kyf_activity.activity_invite_relation WHERE id = %s"
    param3 = "34"
    param4 = "35"
    result3 = kyf_activity_db.selectone(kyf_activity_sql, param3)
    result4 = kyf_activity_db.selectone(kyf_activity_sql, param4)

    print("result3", result3)
    print("result4", result4)
if __name__ == '__main__':
    test_my_connet()
    print("-----------------")
    test_my_connet()














