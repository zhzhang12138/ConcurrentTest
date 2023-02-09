# -*- coding:utf-8 -*-
# @FileName  :WebAPI.py
# @Time      :2023/2/8 09:52
# @Author    :Kolt
import os
import threading

from flask_restful import Resource

from Util.db_count import Sync_data


class HealthExamination(Resource):
    def get(self):
        """
        并发请求
        """
        # Sync_data().count_plus_one()
        # # 进程ID
        # pid = os.getpid()
        # print("进程ID ---", pid)
        # # 线程ID
        # th = threading.current_thread().ident
        # print("线程ID ---", th)
        print("get success")
        return "get success"
