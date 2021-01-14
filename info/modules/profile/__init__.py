# ！/home/yang/PythonProjects python
# -*- coding: utf-8 -*-
# author:yang  time:19-7-22 下午2:06


from flask import Blueprint

profile_blu = Blueprint('profile', __name__, url_prefix='/profile')


from . import views
