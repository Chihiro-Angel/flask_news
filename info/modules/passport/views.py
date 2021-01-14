# ！/home/yang/PythonProjects python
# -*- coding: utf-8 -*-
# author:yang  time:19-7-16 下午4:14


import re
import random
from datetime import datetime
from flask import request, current_app, abort, make_response, Flask, jsonify, session
from info.models import User
from info import redis_store, constants, db
from . import passport_blu
from info.utils.captcha.captcha import captcha
from info.utils.response_code import RET, error_map


app = Flask(__name__)


@passport_blu.route('/image_code')
def get_image_code():
    """
    生成图片验证码
    :return:
    """
    # 1. 获取参数
    image_code_id = request.args.get('image_Code')
    print(image_code_id)
    # 2. 校验参数
    if not image_code_id:
        return abort(403)
    # 3. 生成图片验证码
    name, text, image_data = captcha.generate_captcha()
    # text = session

    print(text)
    # 4. 保存图片验证码
    try:
        redis_store.setex('ImageCode_' + image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        abort(500)

    # 5.返回图片验证码
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/jpg'
    return response


# 短信验证码
@passport_blu.route('/sms_code', methods=["POST"])
def send_sms_code():
    """
    发送短信的逻辑
    :return:
    """
    # 1.将前端参数转为字典

    mobile = request.json.get('mobile')
    # print("mobile", mobile)
    image_code = request.json.get('image_code')
    image_code_id = request.json.get('image_code_id')
    print("image_code", image_code)
    print("image_code_id", image_code_id)
    # 2. 校验参数(参数是否符合规则，判断是否有值)
    # 判断参数是否有值
    if not all([mobile, image_code, image_code_id]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')
    if not re.match(r'^1[3456789]\d{9}$', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式错误')
    # 3. 先从redis中取出真实的验证码内容
    try:
        real_image_code = redis_store.get('ImageCode_' + image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='获取图片验证码失败')
    # 4. 与用户的验证码内容进行对比，如果对比不一致，那么返回验证码输入错误
    if not real_image_code:
        return jsonify(errno=RET.DBERR, errmsg="验证码已经过期")
    if real_image_code.lower() != image_code.lower():
        return jsonify(errno=RET.DATAERR, errmsg='图片验证码不一致')

    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询用户信息失败')
    if user:
        return jsonify(errno=RET.DATAEXIST, errmsg='手机号已注册')
    # 5. 如果一致，生成短信验证码的内容(随机数据)
    sms_code = '%06d' % random.randint(0, 999999)
    print("验证码{}".format(sms_code))
    # 6. 发送短信验证码
    # 保存验证码内容到redis
    try:
        redis_store.set('SMSCode_' + mobile, sms_code, constants.SMS_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')

    # 发送短信验证码
    # try:
    #     ccp = sms.CCP()
    #     ccp.send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES / 60], 1)
    #     # print("result", result)
    #     result = 0
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.THIRDERR, errmsg='发送短信异常')
    # 7. 告知发送结果
    # if result == 0:
    #     print("发送成功")
    #     return jsonify(errno=RET.OK, errmsg='发送成功')
    # else:
    #     return jsonify(errno=RET.THIRDERR, errmsg='发送失败')


# 注册
@passport_blu.route('/register', methods=["POST"])
def register():
    """
    注册功能
    :return:
    """

    # 1. 获取参数和判断是否有值
    mobile = request.json.get('mobile')
    sms_code = request.json.get('smscode')
    password = request.json.get('password')

    if not all([mobile, sms_code, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    if not re.match(r'1[3456789]\d{9}$', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式错误')
    # 2. 从redis中获取指定手机号对应的短信验证码的
    try:
        real_sms_code = redis_store.get('SMSCode_' + mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询数据失败')
    # 3. 校验验证码
    if not real_sms_code:
        return jsonify(errno=RET.NODATA, errmsg='短信验证码已过期')

    if real_sms_code != sms_code:
        return jsonify(errno=RET.DATAERR, errmsg='短信验证码错误')

    try:
        redis_store.delete('SMSCode_' + mobile)
    except Exception as e:
        current_app.logger.error(e)

    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询用户数据失败')
    else:
        if user is not None:
            return jsonify(errno=RET.DATAEXIST, errmsg='手机号已注册')
    # 4. 初始化 user 模型，并设置数据并添加到数据库
    user = User()
    user.mobile = mobile
    user.nick_name = mobile
    user.password = password
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')

    # 5. 保存用户登录状态
    session['user_id'] = user.id
    session['mobile'] = mobile
    session['nick_name'] = mobile
    # 6. 返回注册结果
    return jsonify(errno=RET.OK, errmsg='注册成功')


# 登陆功能
@passport_blu.route('/login', methods=["POST"])
def login():
    """
    登陆功能
    :return:
    """

    # 1. 获取参数和判断是否有值
    mobile = request.json.get('mobile')
    password = request.json.get('password')

    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')

    if not re.match(r'1[3456789]\d{9}$', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式错误')
    # 2. 从数据库查询出指定的用户
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询数据失败')
    # 3. 校验密码
    if user is None or not user.check_password(password):
        return jsonify(errno=RET.DATAERR, errmsg='用户名或密码错误')
    # 4. 保存用户登录状态
    session['user_id'] = user.id
    session['mobile'] = user.mobile

    session['nick_name'] = user.nick_name

    user.last_login = datetime.now()
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')
    # 5. 登录成功返回
    return jsonify(errno=RET.OK, errmsg='OK')


@passport_blu.route("/logout", methods=['POST'])
def logout():
    """
    清除session中的对应登录之后保存的信息
    :return:
    """
    # 返回结果
    # print(session)
    session.pop('user_id')
    # print("1", session['user_id'])
    session.pop("nick_name")
    # print("2", session.pop("nick_name"))
    session.pop("mobile")
    # print("3", session.pop("mobile"))
    # session.clear()
    # session.pop('user_id')
    # session.pop('nick_name')
    # session.pop('mobile')
    # print(session)
    return jsonify(errno=RET.OK, errmsg='OK')


# if __name__ == '__main__':
#     app.run(debug=True)
