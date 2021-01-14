# ！/home/yang/PythonProjects python
# -*- coding: utf-8 -*-
# author:yang  time:19-7-18 下午3:16


from flask import current_app, abort, render_template, g, request, jsonify
from info import db
from info.utils.common import user_login_data
from info.constants import CLICK_RANK_MAX_NEWS
from info.models import News, Comment, User, CommentLike
from info.modules.news import news_blu
from info.utils.response_code import RET, error_map


@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    user = g.user
    comment = Comment()
    # 查询新闻数据
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)
    # 对象字典添加到字典列表中
    news_dict = []
    for news in news_list:
        news_dict.append(news.to_basic_dict())
    news = None
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
    #  校验报404错误
    if not news:
        abort(404)
    # 进入详情页后要更新新闻的点击次数
    news.clicks += 1
    # 判断是否收藏该新闻，默认值为 false
    is_collected = False
    # 判断用户是否登录，判断用户是否收藏过该新闻
    if user:
        if news in user.collection_news:
            is_collected = True

    # 获取当前新闻最新的评论,按时间排序
    comments = []
    try:
        comments = Comment.query.filter(Comment.news_id == news_id).order_by(Comment.create_time.desc()).all()
    except Exception as e:
        current_app.logger.error(e)
    comment_like_ids = []
    if user:
        try:
            comment_ids = [comment.id for comment in comments]
            comment_likes = CommentLike.query.filter(CommentLike.comment_id.in_(comment_ids),
                                                     CommentLike.user_id == g.user.id)
            comment_like_ids = [comment_like.comment_id for comment_like in comment_likes]
        except Exception as e:
            current_app.logger.error(e)
    comment_dict_list = []
    for comment in comments:
        comment_dict = comment.to_dict()
        comment_dict["is_like"] = False
        if comment.id in comment_like_ids:
            comment_dict["is_like"] = True
        comment_dict_list.append(comment_dict)

    is_followed = False
    if news.user and user:
        if news.user in user.followers:
            is_followed = True

    data = {
        "news": news.to_dict(),
        "news_dict": news_dict,
        "user": user.to_dict() if user else None,
        "is_collected": is_collected,
        'is_followed': is_followed,
        "comments": comment_dict_list,
    }
    # print("data[news]\n", data[news])
    # print("news_views_data \n", data)
    # print("\n", news, "\n")

    return render_template('news/detail.html', data=data)


@news_blu.route("/news_collect", methods=['POST'])
@user_login_data
def news_collect():
    """新闻收藏"""
    user = g.user
    # 获取参数
    news_id = request.json.get("news_id")
    action = request.json.get("action")
    # 判断参数
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")
    if not all([news_id, action]):
        return jsonify(errno=RET.NODATA, errmsg="无数据")
    # action在不在指定的两个值：'collect', 'cancel_collect'内
    if action not in ('collect', 'cancel_collect'):
        return jsonify(errno=RET.DATAERR, errmsg="数据错误")
    # 查询新闻,并判断新闻是否存在
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="没有查询到数据")
    if not news:
        return jsonify(errno=RET.NODATA, errmsg="该新闻不存在，无数据")
    # 收藏/取消收藏
    if action == 'cancel_collect':
        #  取消收藏
        if news in user.collection_news:
            user.collection_news.remove(news)
    else:
        # 收藏
        if news not in user.collection_news:
            user.collection_news.append(news)
            print(user.collection_news)
    return jsonify(errno=RET.OK, errmsg="成功")


@news_blu.route('/news_comment', methods=["POST"])
@user_login_data
def add_news_comment():
    """添加评论"""
    # 用户是否登陆
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")
    # 获取参数
    news_id = request.json.get("news_id")
    comment_str = request.json.get("comment")
    parent_id = request.json.get("parent_id")
    # print(news_id)
    # print(comment_str)
    # print(parent_id)
    # 判断参数是否正确
    if not all([news_id, comment_str]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不足")
    # 查询新闻是否存在并校验
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询数据失败")
    if not news:
        return jsonify(errno=RET.NODATA, errmsg="该新闻不存在")
    # 初始化评论模型，保存数据
    comment = Comment()
    comment.user_id = user.id
    comment.news_id = news_id
    comment.content = comment_str
    # 配置文件设置了自动提交,自动提交要在return返回结果以后才执行commit命令,如果有回复
    try:
        db.session.add(comment)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存评论数据失败")
    # 评论,先拿到回复评论id,在手动commit,否则无法获取回复评论内容
    if parent_id:
        try:
            parent_id = int(parent_id)
            comment.parent_id = parent_id
        except BaseException as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])
    # 返回响应

    return jsonify(errno=RET.OK, errmsg="评论成功", data=comment.to_dict())


# 评论点赞
@news_blu.route('/comment_like', methods=['POST'])
@user_login_data
def comment_like():
    # 判断用户是否登录
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg=error_map[RET.SESSIONERR])

    # 获取参数
    comment_id = request.json.get("comment_id")
    action = request.json.get("action")
    # 校验参数
    if not all([comment_id, action]):
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])
    if action not in ["add", "remove"]:
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    # 判断该评论是否存在
    try:
        comment = Comment.query.get(comment_id)
    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg=error_map[RET.DBERR])
    if not comment:
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    # 获取到要被点赞的评论模型
    commentlike = CommentLike()
    commentlike.comment_id = comment_id
    commentlike.user_id = user.id

    # action的状态,如果点赞,则查询后将用户id和评论id添加到数据库
    try:
        comment_id = commentlike.query.get(comment_id)
    except Exception as e:
        current_app.logger.error(e)
    try:
        user_id = commentlike.query.get(user.id)
    except Exception as e:
        current_app.logger.error(e)
        if action == "add":
            try:
                comment_like_model = CommentLike.query.filter(commentlike.user_id == user.id,
                                                              commentlike.comment_id == Comment.id).first()
            except Exception as e:
                current_app.logger.error(e)
            # 点赞评论
            comment_like_model = CommentLike()
            comment_like_model.comment_id = comment_id
            comment_like_model.user_id = user.id
            db.session.add(comment_like_model)
            # 更新点赞次数
            Comment.like_count += 1
        # 取消点赞评论,查询数据库,如果以点在,则删除点赞信息
        else:
            # 更新点赞次数
            comment_like_model = CommentLike.query.filter(commentlike.user_id == user.id,
                                                          commentlike.comment_id == Comment.id).first()
            if comment_like_model:
                db.session.delete(comment_like_model)
                Comment.like_count -= 1

    # json返回结果
    return jsonify(errno=RET.OK, errmsg=error_map[RET.OK])


@news_blu.route('/followed_user', methods=["POST"])
@user_login_data
def followed_user():
    """关注或者取消关注用户"""

    # 获取自己登录信息
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg="未登录")

    # 获取参数
    user_id = request.json.get("user_id")
    print("user_id", user_id)
    action = request.json.get("action")
    print("action", action)

    # 判断参数
    if not all([user_id, action]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    if action not in ("follow", "unfollow"):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 获取要被关注的用户
    try:
        other = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询错误")

    if not other:
        return jsonify(errno=RET.NODATA, errmsg="未查询到数据")

    if other.id == user.id:
        return jsonify(errno=RET.PARAMERR, errmsg="请勿关注自己")

    # 根据要执行的操作去修改对应的数据
    if action == "follow":
        if other not in user.followed:
            # 当前用户的关注列表添加一个值
            user.followed.append(other)
        else:
            return jsonify(errno=RET.DATAEXIST, errmsg="当前用户已被关注")
    else:
        # 取消关注
        if other in user.followed:
            user.followed.remove(other)
        else:
            return jsonify(errno=RET.DATAEXIST, errmsg="当前用户未被关注")

    return jsonify(errno=RET.OK, errmsg="操作成功")
