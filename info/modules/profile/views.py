# ！/home/yang/PythonProjects python
# -*- coding: utf-8 -*-
# author:yang  time:19-7-22 下午2:06
from flask import render_template, g, redirect, abort, request, jsonify, current_app
from info import db
from info.constants import USER_COLLECTION_MAX_NEWS, QINIU_DOMIN_PREFIX, USER_FOLLOWED_MAX_COUNT
from info.models import tb_user_collection, News, Category, User
from info.modules.profile import profile_blu
from info.utils.response_code import RET, error_map
from info.utils.common import user_login_data
from info.utils.image_storage import storage


@profile_blu.route('/user_info')
@user_login_data
def user_info():
    # 如果用户登陆则进入个人中心
    # 如果没有登陆,跳转主页
    # 返回用户数据
    user = g.user
    if not user:
        return redirect("/")

    return render_template("news/user.html", data={"user": user.to_dict()})


@profile_blu.route('/base_info', methods=["GET", "POST"])
@user_login_data
def base_info():
    """
    用户基本信息
    :return:
    """
    user = g.user
    if not user:
        return abort(403)

    if request.method == "GET":
        return render_template('news/user_base_info.html', data={"user": user.to_dict()})
    # POST处理
    signature = request.json.get("signature")
    print(signature)
    nick_name = request.json.get("nick_name")
    print(nick_name)
    gender = request.json.get("gender")
    print(gender)

    if not all([signature, nick_name, gender]):
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    if gender not in ["MAN", "WOMAN"]:
        return jsonify(errno=RET.PARAMERR, errmsg='性别错误')

    # 修改用户模型
    user.signature = signature
    user.nick_name = nick_name
    user.gender = gender

    return jsonify(errno=RET.OK, errmsg=error_map[RET.OK])


@profile_blu.route('/pic_info', methods=["GET", "POST"])
@user_login_data
def pic_info():
    # 如果是GET请求,返回用户数据
    user = g.user
    if not user:
        return abort(404)
    if request.method == "GET":
        return render_template('news/user_pic_info.html', data={"user_info": user.to_dict()})

    # 如果是POST请求表示修改头像
    # 1. 获取到上传的图片
    try:
        img_bytes = request.files.get("avatar").read()  # 读取出上传的文件  bytes
        # 将文件上传给文件服务器
        # 2. 上传头像
        # 使用自已封装的storage方法去进行图片上传
        try:
            file_name = storage(img_bytes)
            # 记录头像的URL
            user.avatar_url = file_name

        except BaseException as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.THIRDERR, errmsg=error_map[RET.THIRDERR])

    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    return jsonify(errno=RET.OK, errmsg=error_map[RET.OK], data={"user_info": user.to_dict()})


@profile_blu.route('/pass_info', methods=["GET", "POST"])
@user_login_data
def pass_info():
    # print("修改密码")
    user = g.user
    if not user:
        return abort(403)
    if request.method == "GET":
        # print("修改密码")
        return render_template('news/user_pass_info.html')

    # 1. 获取参数
    old_password = request.json.get("old_password")
    # print("old_password",  old_password)
    new_password = request.json.get("new_password")
    # print("new_password", new_password)
    # 2. 校验参数
    if not all([old_password, new_password]):
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    # 3. 判断旧密码是否正确
    if not user.check_password(old_password):
        return jsonify(errno=RET.PARAMERR, errmsg="密码错误")

    # 4. 设置新密码
    user.password = new_password

    # 返回
    return jsonify(errno=RET.OK, errmsg=error_map[RET.OK])


@profile_blu.route('/collection')
@user_login_data
def user_collection():
    user = g.user
    if not user:
        return abort(403)
    # 获取当前页码
    p = request.args.get("p", 1)

    try:
        p = int(p)
    except BaseException as e:
        current_app.logger.error(e)
        return abort(403)

    # 查询当前用户收藏的所有新闻  指定页码  根据收藏时间倒序
    news_list = []
    cur_page = 1
    total_page = 1
    try:
        pn = user.collection_news.order_by(tb_user_collection.c.create_time.desc()).paginate(p,
                                                                                             USER_COLLECTION_MAX_NEWS)
        news_list = [news.to_basic_dict() for news in pn.items]
        cur_page = pn.page
        total_page = pn.pages

    except BaseException as e:
        current_app.logger.error(e)

    data = {
        "news_list": news_list,
        "cur_page": cur_page,
        "total_page": total_page
    }
    # 后端渲染收藏的新闻
    return render_template('news/user_collection.html', data=data)


# 发布新闻
@profile_blu.route('/news_release', methods=['GET', 'POST'])
@user_login_data
def news_release():
    # 判断用户是否登录
    user = g.user
    if not user:
        return abort(403)

    if request.method == "GET":
        # 查询所有的分类信息, 再传入模板
        categories = []
        try:
            categories = Category.query.all()
        except BaseException as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg=error_map[RET.DBERR])

        if len(categories):
            categories.pop(0)

        print("categories", categories)

        return render_template("news/user_news_release.html", data={"categories": categories})
    print("post")
    # POST处理
    title = request.form.get("title")
    print("title", title)
    category_id = request.form.get("category_id")
    print("category_id", category_id)
    digest = request.form.get("digest")
    print("digest", digest)
    content = request.form.get("content")
    print("content", content)
    if not all([title, category_id, digest, content]):
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    try:
        category_id = int(category_id)
    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    # 生成一个新的新闻模型
    news = News()
    news.title = title
    news.category_id = category_id
    news.digest = digest
    news.content = content
    news.source = "个人发布"  # 新闻来源
    news.user_id = user.id  # 新闻作者id
    news.status = 1  # 新闻审核状态

    try:
        img_bytes = request.files.get("index_image").read()
        file_name = storage(img_bytes)
        news.index_image_url = QINIU_DOMIN_PREFIX + file_name
    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    # 添加到数据库中
    db.session.add(news)

    return jsonify(errno=RET.OK, errmsg=error_map[RET.OK])


@profile_blu.route('/news_list')
@user_login_data
def user_news_list():
    # 判断用户是否登录
    user = g.user
    if not user:
        return abort(403)
    # 获取当前页码
    p = request.args.get("p", 1)

    try:
        p = int(p)
    except BaseException as e:
        current_app.logger.error(e)
        return abort(403)

    # 查询当前用户发布的所有新闻  指定页码  根据发布时间倒序
    news_list = []
    cur_page = 1
    total_page = 1
    try:
        pn = user.news_list.order_by(News.create_time.desc()).paginate(p, USER_COLLECTION_MAX_NEWS)
        news_list = [news.to_review_dict() for news in pn.items]
        cur_page = pn.page
        total_page = pn.pages

    except BaseException as e:
        current_app.logger.error(e)

    data = {
        "news_list": news_list,
        "cur_page": cur_page,
        "total_page": total_page
    }
    # 后端渲染收藏的新闻
    return render_template("news/user_news_list.html", data=data)


@profile_blu.route('/user_follow')
@user_login_data
def user_follow():
    # 获取页数
    p = request.args.get("p", 1)
    try:
        p = int(p)
    except Exception as e:
        current_app.logger.error(e)
        p = 1

    user = g.user

    follows = []
    current_page = 1
    total_page = 1
    try:
        paginate = user.followed.paginate(p, USER_FOLLOWED_MAX_COUNT, False)
        # 获取当前页数据
        follows = paginate.items
        # 获取当前页
        current_page = paginate.page
        # 获取总页数
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    user_dict_li = []

    for follow_user in follows:
        user_dict_li.append(follow_user.to_dict())
    data = {
        "users": user_dict_li,
        "total_page": total_page,
        "current_page": current_page
    }
    return render_template('news/user_follow.html', data=data)


@profile_blu.route('/other_info')
@user_login_data
def other_info():
    user = g.user

    # 去查询其他人的用户信息
    other_id = request.args.get("user_id")

    if not other_id:
        abort(404)

    # 查询指定id的用户信息
    other = None
    try:
        other = User.query.get(other_id)
    except Exception as e:
        current_app.logger.error(e)

    if not other:
        abort(404)

    # 判断当前登录用户是否关注过该用户
    is_followed = False
    if other and user:
        if other in user.followed:
            is_followed = True

    data = {
        "is_followed": is_followed,
        "user": user.to_dict() if user else None,
        "other_info": other.to_dict()
    }
    return render_template('news/other.html', data=data)


@profile_blu.route('/other_news_list')
def other_news_list():
    """返回指定用户的发布的新闻"""

    # 1. 取参数
    other_id = request.args.get("user_id")
    page = request.args.get("p", 1)

    # 2. 判断参数
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    try:
        other = User.query.get(other_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询失败")

    if not other:
        return jsonify(errno=RET.NODATA, errmsg="当前用户不存在")

    try:
        paginate = other.news_list.paginate(page, USER_COLLECTION_MAX_NEWS, False)
        # 获取当前页数据
        news_li = paginate.items
        # 获取当前页
        current_page = paginate.page
        # 获取总页数
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询失败")

    news_dict_list = []
    for news_item in news_li:
        news_dict_list.append(news_item.to_basic_dict())

    data = {
        "news_list": news_dict_list,
        "total_page": total_page,
        "current_page": current_page
    }
    return jsonify(errno=RET.OK, errmsg="OK", data=data)
