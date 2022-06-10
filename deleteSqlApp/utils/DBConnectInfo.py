import pymysql
from pydantic import BaseModel

from deleteSqlApp.utils.YmlUtil import YmlUtil
from deleteSqlApp.model.ExecuteResult import ExecuteResult


class DBConnectInfo():

    @staticmethod
    def connectDb(filePath: str):
        licai_db = YmlUtil.readDbYml(filePath)
        # 打开数据库连接
        conn = pymysql.connect(
            host=licai_db.host,
            user=licai_db.username,
            password=licai_db.password,
            port=licai_db.port,
            database=licai_db.database,
            charset="utf8"  # 编码
        )
        return conn

    @staticmethod
    def delete_licai(filePath: str) -> ExecuteResult:
        licai_conn = DBConnectInfo.connectDb(filePath)

        try:
            # 使用cursor()方法获取操作游标
            cursor = licai_conn.cursor()

            # sql语句
            sql = "SELECT * FROM licai.client_registration_info WHERE id = '1';"
            print("sql", sql)

            # 执行sql语句
            try:
                cursor.execute(sql)
                # 将sql提交到数据库执行
                print("# 将sql提交到数据库执行")
                licai_conn.commit()
                print("commit")
                result1 = cursor.fetchall()
                print(result1)

            except:
                print("# 发生错误回滚")
                # 发生错误回滚
                licai_conn.rollback()
        finally:
            # 关闭数据库连接
            licai_conn.close()

        result = ExecuteResult(result=True,message=result1)
        return result

    @staticmethod
    def delete_kytz_dev(filePath: str) -> ExecuteResult:
        kytz_dev_conn = DBConnectInfo.connectDb(filePath)
        try:
            # 使用cursor()方法获取操作游标
            cursor = kytz_dev_conn.cursor()

            # sql语句
            sql = "SELECT * FROM licai.client_registration_info WHERE id = '1';"
            print("sql", sql)

            # 执行sql语句
            try:
                cursor.execute(sql)
                # 将sql提交到数据库执行
                print("# 将sql提交到数据库执行")
                kytz_dev_conn.commit()
                print("commit")
                result1 = cursor.fetchall()
                print(result1)

            except:
                print("# 发生错误回滚")
                # 发生错误回滚
                kytz_dev_conn.rollback()
        finally:
            # 关闭数据库连接
            kytz_dev_conn.close()

        result = ExecuteResult(result=True, message=result1)
        return result

    @staticmethod
    def delete_kyf_activity(filePath: str) -> ExecuteResult:
        kyf_activity_conn = DBConnectInfo.connectDb(filePath)
        try:
            # 使用cursor()方法获取操作游标
            cursor = kyf_activity_conn.cursor()

            # sql语句
            sql = "SELECT * FROM licai.client_registration_info WHERE id = '1';"
            print("sql", sql)

            # 执行sql语句
            try:
                cursor.execute(sql)
                # 将sql提交到数据库执行
                print("# 将sql提交到数据库执行")
                kyf_activity_conn.commit()
                print("commit")
                result1 = cursor.fetchall()
                print(result1)

            except:
                print("# 发生错误回滚")
                # 发生错误回滚
                kyf_activity_conn.rollback()
        finally:
            # 关闭数据库连接
            kyf_activity_conn.close()

        result = ExecuteResult(result=True, message=result1)
        return result




