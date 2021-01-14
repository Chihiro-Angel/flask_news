# ！/home/yang/PythonProjects python
# -*- coding: utf-8 -*-
# author:yang  time:19-7-18 下午3:16


from flask import Blueprint


# 1. 创建蓝图
news_blu = Blueprint("news_blu", __name__, url_prefix="/news")

from .views import *