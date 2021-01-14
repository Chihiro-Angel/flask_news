# ！/home/yang/PythonProjects python
# -*- coding: utf-8 -*-
# author:yang  time:19-7-23 上午11:53


from flask import Blueprint

# 1. 创建蓝图
admin_blu = Blueprint("admin", __name__, url_prefix="/admin")

from .views import *


@admin_blu.before_request
def check_admin():
    # 限制非管理员访问管理员页面
    is_admin = session.get('is_admin', False)
    if not is_admin and not request.url.endswith(url_for('admin.login')):
        return redirect('/')
