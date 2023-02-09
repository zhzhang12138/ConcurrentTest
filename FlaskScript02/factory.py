# -*- coding:utf-8 -*-
# @FileName  :factory.py
# @Time      :2023/2/8 09:50
# @Author    :Kolt


from flask import Flask
from flask_cors import CORS
from settings import Config
from sources.web import new_web_api_blueprint


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)
    CORS(app=app)
    app.register_blueprint(new_web_api_blueprint)

    return app
