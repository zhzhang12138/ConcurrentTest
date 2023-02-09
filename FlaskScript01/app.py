import os
import threading

from flask import Flask
from settings import Config

from db_count import Sync_data

app = Flask(__name__)


@app.route("/", methods=["get"])
def count_plus_one():
    Sync_data().count_plus_one()
    # # 进程ID
    # pid = os.getpid()
    # print("进程ID ---", pid)
    # # 线程ID
    # th = threading.current_thread().ident
    # print("线程ID ---", th)
    return "get success"


if __name__ == '__main__':
    app.run(Config.HOST, port=Config.PORT)
