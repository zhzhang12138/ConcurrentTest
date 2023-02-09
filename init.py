# -*- coding:utf-8 -*-
# @FileName  :db_count.py
# @Time      :2023/2/8 09:25
# @Author    :Kolt
import pymysql

from FlaskScript01.settings import Config


class Sync_data(object):
    """
    同步数据到数据库
    """

    def __init__(self):
        self.db_conn, self.db_cursor = self.get_db_course(Config.SQL_HOST, Config.SQL_PORT, Config.SQL_USER,
                                                          Config.SQL_PASSWD, Config.SQL_DB)

    def get_db_course(self, SQL_HOST, SQL_PORT, SQL_USER, SQL_PASSWD, SQL_DB):
        """
        数据库链接 - 游标
        """
        PY_MYSQL_CONN_DICT = {
            "host": SQL_HOST,
            "port": SQL_PORT,
            "user": SQL_USER,
            "passwd": SQL_PASSWD,
            "db": SQL_DB
        }
        # 数据库连接
        db_conn = pymysql.connect(**PY_MYSQL_CONN_DICT)
        # 游标
        db_cursor = db_conn.cursor(cursor=
                                   pymysql.cursors.DictCursor)

        return db_conn, db_cursor

    def count_plus_one(self):
        """
        重置-计数
        """
        print("重置---flask_01_count")
        execute_sql = "UPDATE flask_01_count SET count = 0 WHERE id = 1"
        self.db_cursor.execute(execute_sql)
        self.db_conn.commit()

        print("重置---flask_02_count")
        execute_sql = "UPDATE flask_02_count SET count = 0 WHERE id = 1"
        self.db_cursor.execute(execute_sql)
        self.db_conn.commit()

        print("重置---gin_01_count")
        execute_sql = "UPDATE gin_01_count SET count = 0 WHERE id = 1"
        self.db_cursor.execute(execute_sql)
        self.db_conn.commit()


if __name__ == '__main__':
    Sync_data().count_plus_one()
