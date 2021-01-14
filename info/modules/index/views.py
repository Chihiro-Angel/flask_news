# ！/home/yang/PythonProjects python
# -*- coding: utf-8 -*-
# author:yang  time:19-7-16 下午4:02
from flask import current_app, render_template, session, request, jsonify, g

from info.utils.common import user_login_data
from info.utils.response_code import RET, error_map
from info.constants import CLICK_RANK_MAX_NEWS, HOME_PAGE_MAX_NEWS
from info.models import User, News, Category
from . import index_blu


# 测试
@index_blu.route('/')
@user_login_data
def index():

    # user
    # user_id = session.get("user_id", None)
    # print("55555", user_id)
    # user = None
    # if user_id:  # 已登录
    #     # 根据`user_id`获取`用户信息
    #     try:
    #         user = User.query.get(user_id)
    #     except BaseException as e:
    #         current_app.logger.error(e)

    user = g.user

    # news
    news_list_ = []
    try:
        news_list_ = News.query.order_by(News.clicks.desc()).limit(CLICK_RANK_MAX_NEWS).all()
    except BaseException as e:
        current_app.logger.error(e)

    categories = []
    try:
        categories = Category.query.all()
    except BaseException as e:
        current_app.logger.error(e)

    data = {
        "user": user.to_dict() if user else None,
        "news_dict": [news.to_basic_dict() for news in news_list_],
        "categories": categories,
    }
    # print(type(data))
    # print("user", data["user"])
    # print()
    # print("news_dict", data["news_dict"])
    # print()
    # print("categories", data["categories"])

    return render_template('news/index.html', data=data)


@index_blu.route('/news_list')
def news_list():
    """
    获取首页新闻数据
    :return:
    """

    # 1. 获取参数,并指定默认为最新分类,第一页,一页显示10条数据
    cid = request.args.get("cid", 1)
    # print("cid", cid)
    cur_page = request.args.get("page", 1)
    # print("page", cur_page)
    per_count = request.args.get("per_count", HOME_PAGE_MAX_NEWS)
    # print("per_count", per_count)
    # 2. 校验参数
    if not all([cid, cur_page]):
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])
    # 默认选择最新数据分类
    try:
        cid = int(cid)
        cur_page = int(cur_page)
        per_count = int(per_count)
    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    filter_list = [News.status == 0]
    if cid != 1:
        filter_list.append(News.category_id == cid)  # [News.status == 0, News.category_id == cid]

    # 3. 查询数据
    try:
        pn = News.query.filter(*filter_list).order_by(News.create_time.desc()).paginate(cur_page, per_count)
    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg=error_map[RET.DBERR])

    # print(pn)
    # 将模型对象列表转成字典列表
    data = {
        "news_list": [news.to_basic_dict() for news in pn.items],
        "total_page": pn.pages
    }
    # print(data["news_list"])
    # print(data["total_page"])
    # 返回数据
    return jsonify(errno=RET.OK, errmsg=error_map[RET.OK], data=data)
