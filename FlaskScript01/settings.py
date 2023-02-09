# -*- coding:utf-8 -*-
# @FileName  :settings.py
# @Time      :2023/2/8 09:24
# @Author    :Kolt
import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "fd98330dad85045242bd271ceb736681")

    HOST = "0.0.0.0"
    PORT = 8080
    DEBUG = True

    SQL_HOST = "*.*.*.*"
    SQL_PORT = 3306
    SQL_USER = "root"
    SQL_PASSWD = "123456"
    SQL_DB = "concurrency"
