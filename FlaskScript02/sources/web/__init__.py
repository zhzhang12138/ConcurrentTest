# -*- coding:utf-8 -*-
# @FileName  :__init__.py
# @Time      :2023/2/8 09:52
# @Author    :Kolt
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api
from sources.web.WebAPI import HealthExamination

new_web_api_blueprint = Blueprint("new_web_api", __name__, url_prefix="/")
new_web_api = Api(app=new_web_api_blueprint)

# 并发请求
new_web_api.add_resource(HealthExamination, "/")
