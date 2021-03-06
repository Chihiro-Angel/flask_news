# Flask项目

## 1. 项目分析

# 项目预览:101.200.50.132

### 新经资讯网

- 一款新闻展示的Web项目，主要为用户提供最新的金融资讯、数据
- 以抓取其他网站数据和用户发布作为新闻的主要来源
- 基于 Flask 框架，以 **前后端不分离** 的形式实现具体业务逻辑

技术实现

- 基于 Python 3 + Flask 框架实现
- 数据存储使用 Redis + MySQL 实现
- 第三方扩展：
  - 七牛云：文件存储平台
  - 云通信：短信验证码平台

### 功能模块

- 新闻模块
  - 首页新闻列表
  - 新闻详情
- 用户模块
  - 登录注册/个人信息修改
  - 新闻收藏/发布
- 后台管理

### 具体需求

1. 首页
   - 根据分类进行新闻列表展示
   - 上拉加载更多数据
   - 点击新窗口跳转到新闻详情页
   - 顶部显示用户登录信息，未登录显示登录/注册按钮
   - 右侧显示新闻点击排行
2. 注册
   - 用户账号为手机号
   - 图片验证码正确后才能发送短信验证码
   - 短信验证码每60秒发送一次
   - 条件出错时有相应的错误提示
3. 登录
   - 用手机号与密码登录
   - 错误时有相应的提示
4. 新闻详情
   - 新闻内容 html 数据展示
   - 用户点击收藏可以收藏当前新闻
   - 根据当前登录用户显示收藏状态
   - 用户可以评论该新闻
   - 其他用户可以回复某一条评论
   - 右侧显示新闻点击排行
   - 如果当前新闻由具体作者发布，右侧显示作者信息，并且可以关注作者
5. 个人中心
   - 显示个人头像、昵称(未设置时显示为用户手机号)
   - 提供我的关注、我的粉丝入口
   - 提供修改基本资料入口
   - 提供头像设置入口
   - 提供密码修改入口
   - 提供我的收藏入口
   - 提供新闻发布入口
   - 提供我发布的新闻的入口
6. 个人信息修改
   - 可以修改用户名
   - 可以修改个人头像
   - 登陆手机号不能修改
   - 上传新头像后页面立即显示新头像
7. 我的关注
   - 以分页的形式展示数据
   - 每页展示4个我关注的用户
   - 可以在当前页面进行取消关注
   - 点击关注用户的昵称跳转到用户信息页面
8. 我的收藏
   - 以分页的形式展示数据
   - 按收藏时间倒序排序
9. 发布新闻
   - 可以发布新闻
   - 可以将新闻页的图片上传到七牛云
   - 发布完新闻跳转到我的新闻列表页面
10. 我发布的新闻
    - 按照发布的时候先后顺序排序，最近新闻排在前面
    - 显示当前我发布新闻的新闻状态
    - 点击审核通过的新闻直接跳转到新闻详情页
    - 审核中的无法点击
    - 未审核通过的新闻可以重新发布
    - 点击审核失败的新闻跳转到新闻发布页面，并填充具体新闻内容
11. 查看其他人用户页面
    - 显示他人的头像、昵称、粉丝数
    - 可以点击关注和取消关注按钮进行关注操作
    - 展示他发布的新闻
    - 点击新闻在新窗口中打开展示新闻详情
12. 退出
    - 提供退出功能
13. 后台-登录
    - 提供后台登录页面
    - 如果当前用户已登录，进入到登录页面之后直接跳转到后台主页
14. 后台-用户统计
    - 登录到后台界面之后展示用户统计界面
    - 显示用户总人数
    - 展示当前月用户新增人数
    - 展示当前日新增数
15. 后台-用户列表
    - 按注册时间顺序排序用户列表
    - 显示用户注册时间
    - 显示用户上次登录时间
16. 后台-新闻审核
    - 展示待审核新闻内容
    - 点击进入新闻审核界面
    - 可以对新闻进行审核
    - 如果审核不通过，需要有拒绝原因
17. 新闻版式编辑
    - 进入默认展示所有新闻数据
    - 可以根据新闻标题搜索新闻
18. 新闻分类管理
    - 展示所有分类列表
    - 可以添加/修改分类

## 2.项目框架搭建

### 搭建虚拟环境

- 安装第三方库virtualenv和virtualenvwrapper

```bash
pip install virtualenv
# Ubuntu
pip install virtualenvwrapper
# Windows
pip install virtualenvwrapper-win
```

- 添加环境变量

- 我的电脑--->>属性--->>高级系统设置--->>环境变量--->>系统变量

- 新建:

  ​	**变量名:** WORKON_HOME

  ​	**变量值:** 自己定义的虚拟环境目录

- **创建虚拟环境**

```
mkvirtualenv 虚拟环境名称
例 ：
mkvirtualenv py_flask
```

- **使用虚拟环境**

```
workon 虚拟环境名称

例 ：
workon py_flask
```

- **退出虚拟环境**

```
deactivate
```

- **删除虚拟环境**

```
rmvirtualenv 虚拟环境名称

例 ：删除虚拟环境py3_flask

先退出：deactivate
再删除：rmvirtualenv py3_flask
```

### GIT版本控制

``````python
# 创建git版本控制
git init
# Ubuntu创建忽略文件
touch .gitignore
# Windows创建忽略文件
type nul>.gitignore
# 设置忽略文件内容
.idea
*.py[cod]

# 添加所有文件到暂存区
git add .
# 配置当前项目git提交信息(更改为本人信息,方便管理，如不配置则使用全局配置)
git config user.name 'xxxxxxxxx'
git config user.email 'xxxxxxxx'
# 提交到仓库并填写注释
git commit -m '立项'
``````



- ### 回滚代码

- 回滚到上一版本

```bash
$ git reset --hard HEAD~1
```

- 查看所有提交版本记录

```
$ git reflog
```

- 回到指定版本

```bash
$ git reset --hard 提交id
```

### 创建项目

新建项目，创建 `manage.py`、`config.py`和`.gitignore` 文件

**第三方库**

```
pip install flask
pip install redis
pip install pymysql
pip install flask-wtf
pip install flask-script
pip install flask-migrate
pip install flask-session
pip install flask-sqlalchemy
```



- **manage.py入口文件**

- **此入口文件为Linux系统开启方法,windows系统下需要安装Flask-Script第三方扩展启动**
- **并在Pycharm设置启动参数runserver启动**
- **windows系统页可以更改manage.run()为app.run()启动**

```python
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db, models

# manage.py是程序启动的入口，只关心启动的相关参数以及内容

# 通过指定的配置名字创建对应配置的app
# 指定环境
app = create_app('development')

manager = Manager(app)
# 将 app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

```

- **config.py配置文件**

```python
import logging
from redis import StrictRedis


class Config(object):
    """项目配置"""

    SECRET_KEY = "iECgbYWReMNxkRprrzMo5KAQYnb2UeZ3bwvReTSt+VSESW0OB8zbglT+6rEcDW9X"

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 在请求结束时候，如果指定此配置为 True ，那么 SQLAlchemy 会自动执行一次 db.session.commit()操作
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # Session保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定 Session 保存的 redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 7

    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

```

- **.gitignore排除项文件**
- **添加**
  - .idea
  - *.py[cod]
  - logs/log*
  - migrations

**注意:**

​	**在logs目录下额外添加.keepgit文件,因为在git提交时,没有必要提交日志文件,但是git提交又不能提交空文件夹,所以创建.keepgit文件,这样在git提交时不会报错**

- **创建业务逻辑文件夹info**

- **init.py初始化配置文件**

```python
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
# 可以用来指定 session 保存的位置
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from config import config

# 初始化数据库
db = SQLAlchemy()

# 变量注释,指定变量类型(使用全局变量无法智能提示时)
redis_store = None  # type: StrictRedis


def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    # 配置日志,并且传入配置名字，获取指定配置所对应的日志等级
    setup_log(config_name)
    # 创建Flask对象
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])
    # 通过app初始化
    db.init_app(app)
    # 初始化 redis 存储对象
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT,
                              decode_responses=True)
    # 开启当前项目 CSRF 保护，只做服务器验证功能
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)

    # 注册蓝图
    from .modules.index import index_blu
    app.register_blueprint(index_blu)

    return app

```

- **在info目录下创建models.py数据库文件**

```python
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from info import constants
from . import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


# 用户收藏表，建立用户与其收藏新闻多对多的关系
tb_user_collection = db.Table(
    "info_user_collection",
    db.Column("user_id", db.Integer, db.ForeignKey("info_user.id"), primary_key=True),  # 新闻编号
    db.Column("news_id", db.Integer, db.ForeignKey("info_news.id"), primary_key=True),  # 分类编号
    db.Column("create_time", db.DateTime, default=datetime.now)  # 收藏创建时间
)

tb_user_follows = db.Table(
    "info_user_fans",
    db.Column('follower_id', db.Integer, db.ForeignKey('info_user.id'), primary_key=True),  # 粉丝id
    db.Column('followed_id', db.Integer, db.ForeignKey('info_user.id'), primary_key=True)  # 被关注人的id
)


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "info_user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    avatar_url = db.Column(db.String(256))  # 用户头像路径
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间
    is_admin = db.Column(db.Boolean, default=False)
    signature = db.Column(db.String(512))  # 用户签名
    gender = db.Column(  # 订单的状态
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN")

    # 当前用户收藏的所有新闻
    collection_news = db.relationship("News", secondary=tb_user_collection, lazy="dynamic")  # 用户收藏的新闻
    # 用户所有的粉丝，添加了反向引用followed，代表用户都关注了哪些人
    followers = db.relationship('User',
                                secondary=tb_user_follows,
                                primaryjoin=id == tb_user_follows.c.followed_id,
                                secondaryjoin=id == tb_user_follows.c.follower_id,
                                backref=db.backref('followed', lazy='dynamic'),
                                lazy='dynamic')

    # 当前用户所发布的新闻
    news_list = db.relationship('News', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("当前属性不可读")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "nick_name": self.nick_name,
            "avatar_url": constants.QINIU_DOMIN_PREFIX + self.avatar_url if self.avatar_url else "",
            "mobile": self.mobile,
            "gender": self.gender if self.gender else "MAN",
            "signature": self.signature if self.signature else "",
            "followers_count": self.followers.count(),
            "news_count": self.news_list.count()
        }
        return resp_dict

    def to_admin_dict(self):
        resp_dict = {
            "id": self.id,
            "nick_name": self.nick_name,
            "mobile": self.mobile,
            "register": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "last_login": self.last_login.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return resp_dict


class News(BaseModel, db.Model):
    """新闻"""
    __tablename__ = "info_news"

    id = db.Column(db.Integer, primary_key=True)  # 新闻编号
    title = db.Column(db.String(256), nullable=False)  # 新闻标题
    source = db.Column(db.String(64), nullable=False)  # 新闻来源
    digest = db.Column(db.String(512), nullable=False)  # 新闻摘要
    content = db.Column(db.Text, nullable=False)  # 新闻内容
    clicks = db.Column(db.Integer, default=0)  # 浏览量
    index_image_url = db.Column(db.String(256))  # 新闻列表图片路径
    category_id = db.Column(db.Integer, db.ForeignKey("info_category.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("info_user.id"))  # 当前新闻的作者id
    status = db.Column(db.Integer, default=0)  # 当前新闻状态 如果为0代表审核通过，1代表审核中，-1代表审核不通过
    reason = db.Column(db.String(256))  # 未通过原因，status = -1 的时候使用
    # 当前新闻的所有评论
    comments = db.relationship("Comment", lazy="dynamic")

    def to_review_dict(self):
        resp_dict = {
            "id": self.id,
            "title": self.title,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status,
            "reason": self.reason if self.reason else ""
        }
        return resp_dict

    def to_basic_dict(self):
        resp_dict = {
            "id": self.id,
            "title": self.title,
            "source": self.source,
            "digest": self.digest,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "index_image_url": self.index_image_url,
            "clicks": self.clicks,
        }
        return resp_dict

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "title": self.title,
            "source": self.source,
            "digest": self.digest,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "content": self.content,
            "comments_count": self.comments.count(),
            "clicks": self.clicks,
            "category": self.category.to_dict(),
            "index_image_url": self.index_image_url,
            "author": self.user.to_dict() if self.user else None
        }
        return resp_dict


class Comment(BaseModel, db.Model):
    """评论"""
    __tablename__ = "info_comment"

    id = db.Column(db.Integer, primary_key=True)  # 评论编号
    user_id = db.Column(db.Integer, db.ForeignKey("info_user.id"), nullable=False)  # 用户id
    news_id = db.Column(db.Integer, db.ForeignKey("info_news.id"), nullable=False)  # 新闻id
    content = db.Column(db.Text, nullable=False)  # 评论内容
    parent_id = db.Column(db.Integer, db.ForeignKey("info_comment.id"))  # 父评论id
    parent = db.relationship("Comment", remote_side=[id])  # 自关联
    like_count = db.Column(db.Integer, default=0)  # 点赞条数

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "content": self.content,
            "parent": self.parent.to_dict() if self.parent else None,
            "user": User.query.get(self.user_id).to_dict(),
            "news_id": self.news_id,
            "like_count": self.like_count
        }
        return resp_dict


class CommentLike(BaseModel, db.Model):
    """评论点赞"""
    __tablename__ = "info_comment_like"
    comment_id = db.Column("comment_id", db.Integer, db.ForeignKey("info_comment.id"), primary_key=True)  # 评论编号
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("info_user.id"), primary_key=True)  # 用户编号


class Category(BaseModel, db.Model):
    """新闻分类"""
    __tablename__ = "info_category"

    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    name = db.Column(db.String(64), nullable=False)  # 分类名
    news_list = db.relationship('News', backref='category', lazy='dynamic')

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "name": self.name
        }
        return resp_dict
```

- **在info下创建constants.py常量文件**

```python
# 图片验证码Redis有效期， 单位：秒
IMAGE_CODE_REDIS_EXPIRES = 300

# 短信验证码Redis有效期，单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 七牛空间域名
QINIU_DOMIN_PREFIX = "http://oyucyko3w.bkt.clouddn.com/"

# 首页展示最多的新闻数量
HOME_PAGE_MAX_NEWS = 10

# 用户的关注每一页最多数量
USER_FOLLOWED_MAX_COUNT = 4

# 用户收藏最多新闻数量
USER_COLLECTION_MAX_NEWS = 10

# 其他用户每一页最多新闻数量
OTHER_NEWS_PAGE_MAX_COUNT = 10

# 点击排行展示的最多新闻数据
CLICK_RANK_MAX_NEWS = 10

# 管理员页面用户每页多最数据条数
ADMIN_USER_PAGE_MAX_COUNT = 10

# 管理员页面新闻每页多最数据条数
ADMIN_NEWS_PAGE_MAX_COUNT = 10
```

- **在info目录下创建modules包,在modules包下创建index包**
- **init.py初始化文件**

```python
from flask import Blueprint

# 创建蓝图对象
index_blu = Blueprint('index', __name__)

from . import views
```

- **views.py视图文件**

```python
from . import index_blu


# 测试
@index_blu.route('/')
def index():
    return '<h1>index-text</h1>'
```

- #### 迁移数据库

```bash
# 生成迁移文件夹
python manage.py db init
# 生成指定版本迁移文件
python manage.py db migrate -m 'initial'
# 执行迁移
python manage.py db upgrade
```

- #### 添加测试数据

  - 进入MYSQL,选择创建好的数据库info

  ```mysql
  # 选择数据库
  use info
  # 添加数据
  source #拖入测试数据,先添加新闻分类表,在添加新闻表
  ```

## 3.登陆注册

### 1.注册

**分析**

- 用户账号为手机号
- 有图片验证码功能
- 点击图片验证码刷新图片验证码
- 图片验证码正确后才能发送短信验证码
- 短信验证码每60秒发送一次
- 条件出错时有相应的错误提示

#### **1.1-图片验证码**

- #### 分析 :

- **验证码保存在redis中,redis是以键值对方式存储,所以前端传递一个参数当作键值,验证码为vlaue值**

- **游览器发起图片验证码请求/passports/image_code?image_Code=xxxxxxxxx**

- **后端接收请求,获取前端传递的参数,生成图片验证码,保存到redis中**

- **返回图片给前端**

- ### 前端实现

- `info/static/news/js/main.js`

```javascript
function generateImageCode() {
    // 图片验证码请求/passports/image_code?image_Code=xxxxxxxxx
    // 生成随机码
    imageCodeId = generateUUID()
    // 生成url
    var url = '/passports/image_code?image_Code=' + imageCodeId
    // 给图片验证码img设置src属性
    $('.get_pic_code').attr('src', url)

}
```

- ### 后端实现

```bash
# 安装图图像处理标准库
pip install pillow
```

- 写视图函数前要实例化蓝图,并注册蓝图
- `info/modules/passport/views.py`

```python
from flask import request, current_app, abort, make_response

from info import redis_store, constants
from . import passport_blu
from info.utils.captcha.captcha import captcha


@passport_blu.route('/passport/image_code')
def get_image_code():
    '''
    生成图片验证码
    :return:
    '''
    # 1. 获取参数
    # 2. 校验参数
    # 3. 生成图片验证码
    # 4. 保存图片验证码
    # 5.返回图片验证码

```

#### 1.2-短讯验证码

**发送短信验证码实现流程：**

1. 接收前端发送过来的请求参数
2. 检查参数是否已经全部传过来
3. 判断手机号格式是否正确
4. 检查图片验证码是否正确，若不正确，则返回
5. 删除图片验证码
6. 生成随机的短信验证码
7. 使用第三方SDK发送短信验证码

- ## 接口设计

- URL：/passport/sms_code

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名        | 类型   | 是否必须 | 参数说明                 |
| ------------- | ------ | -------- | ------------------------ |
| mobile        | string | 是       | 手机号                   |
| image_code    | string | 是       | 用户输入的图片验证码内容 |
| image_code_id | string | 是       | 真实图片验证码编号       |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ### 后端实现

- `passport/views.py`

```python
@passport_blu.route('/sms_code', methods=["POST"])
def send_sms_code():
    """
    发送短信的逻辑
    :return:
    """
    # 1.将前端参数转为字典
    # 2. 校验参数(参数是否符合规则，判断是否有值)
    # 判断参数是否有值
    # 3. 先从redis中取出真实的验证码内容
    # 4. 与用户的验证码内容进行对比，如果对比不一致，那么返回验证码输入错误
    # 5. 如果一致，生成短信验证码的内容(随机数据)
    # 6. 发送短信验证码
    # 保存验证码内容到redis
    # 7. 告知发送结果
```

- ### 前端实现

- `main.js` 文件的 `sendSMSCode` 方法中

```javascript
    // 发送短信验证码
    var params = {
        'mobile': mobile,
        'image_code': imageCode,
        'image_code_id': imageCodeId
    }

    $.ajax({
        // 请求地址
        url: '/passport/sms_code',
        // 请求方式
        type: 'post',
        // 请求参数
        data: JSON.stringify(params),
        // 数据类型
        contentType: 'application/json',
        success: function (response) {
            if (response.errno == "0") {
                // 代表发送成功
                var num = 60
                var t = setInterval(function () {

                    if (num == 1) {
                        // 代表倒计时结束
                        // 清除倒计时
                        clearInterval(t)

                        // 设置显示内容
                        $(".get_code").html("点击获取验证码")
                        // 添加点击事件
                        $(".get_code").attr("onclick", "sendSMSCode();");
                    }else {
                        num -= 1
                        // 设置 a 标签显示的内容
                        $(".get_code").html(num + "秒")
                    }
                }, 1000)
            }else {
                // 代表发送失败
                // 表示后端出现了错误，可以将错误信息展示到前端页面中
                $("#register-sms-code-err").html(resp.errmsg);
                $("#register-sms-code-err").show();
                // 将点击按钮的onclick事件函数恢复回去
                $(".get_code").attr("onclick", "sendSMSCode();");
                // 如果错误码是4004，代表验证码错误，重新生成验证码
                if (resp.errno == "4004") {
                    generateImageCode()
            }
        }
    })
```

#### 1.3-注册实现

- ### 接口设计

- URL：/passport/register

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名   | 类型   | 是否必须 | 参数说明   |
| -------- | ------ | -------- | ---------- |
| mobile   | string | 是       | 手机号     |
| smscode  | string | 是       | 短信验证码 |
| password | string | 是       | 密码       |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ### 后端实现

- `passport/views.py`

```python
@passport_blu.route('/register', methods=["POST"])
def register():
    """
    注册功能
    :return:
    """

    # 1. 获取参数和判断是否有值
    # 2. 从redis中获取指定手机号对应的短信验证码的
    # 3. 校验验证码
    # 4. 初始化 user 模型，并设置数据并添加到数据库
    # 5. 保存用户登录状态
    # 6. 返回注册结果
```



- ### 前端实现

- `main.js`注册表单提交

```js
// 发起注册请求
var params = {
        "mobile": mobile,
        "smscode": smscode,
        "password": password,
    }

    $.ajax({
        url:"/passport/register",
        type: "post",
        data: JSON.stringify(params),
        contentType: "application/json",
        success: function (resp) {
            if (resp.errno == "0"){
                // 刷新当前界面
                location.reload()
            }else {
                $("#register-password-err").html(resp.errmsg)
                $("#register-password-err").show()
            }
        }
    })
```

### 2.登陆/登出

#### 2.1-登陆实现

- ### 接口设计

- URL：/passport/login

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名   | 类型   | 是否必须 | 参数说明 |
| -------- | ------ | -------- | -------- |
| mobile   | string | 是       | 手机号   |
| password | string | 是       | 密码     |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ### 后端实现

- `passport/views.py` 

```python
@passport_blu.route('/login', methods=["POST"])
def login():
    """
    登陆功能
    :return:
    """

    # 1. 获取参数和判断是否有值
    # 2. 从数据库查询出指定的用户
    # 3. 校验密码
    # 4. 保存用户登录状态
    # 5. 登录成功返回
```

- ### 前端实现

- `main.js`  登录表单提交

```js
    var params = {
        "mobile": mobile,
        "password": password,
    }

    $.ajax({
        url:"/passport/login",
        method: "post",
        data: JSON.stringify(params),
        contentType: "application/json",
        success: function (resp) {
            if (resp.errno == "0") {
                // 刷新当前界面
                location.reload();
            }else {
                $("#login-password-err").html(resp.errmsg)
                $("#login-password-err").show()
            }
        }
    })
```

#### 2.2-登陆账号状态

- #### 首页右上角内容逻辑显示

- #### 需求

  - 当前用户未登录时，登录/注册按钮
  - 当用户已登录时，显示用户头像和昵称，并提供退出入口

- #### 功能分析

  - 需要在用户请求首页的时候去数据库查询用户数据
  - 如果查询到用户数据，则传入模板中，进行渲染，再进行返回
  - 如果未查询到，返回用户数据为 None，模板代码中自行判断

- #### 代码实现

  - `index/views.py` 对原有根路由函数进行改造：

```python
@index_blu.route('/')
def index():
    # 获取到当前登录用户的id
	# 返回给前端查询结果
```

- `index.html` 

```html
<div class="header_con">
    <div class="header">
        <a href="#" class="logo fl"><img src="../../static/news/images/logo.png" alt="logo"></a>
        <ul class="menu fl">
            <li class="active" data-cid="0"><a href="javascript:;">最新</a></li>
            <li data-cid="1"><a href="javascript:;">股市</a></li>
            <li data-cid="2"><a href="javascript:;">债市</a></li>
            <li data-cid="3"><a href="javascript:;">商品</a></li>
            <li data-cid="4"><a href="javascript:;">外汇</a></li>
            <li data-cid="5"><a href="javascript:;">公司</a></li>
        </ul>

        {# 判断用户是否登录 #}
        {% if data.user %}
            {# 如果登录，则显示用户信息 #}
            <div class="user_login fr">
                <img src="
                        {% if data.user.avatar_url %}{{ data.user.avatar_url }}{% else %}../../static/news/images/person01.png{% endif %}"
                     class="lgin_pic">
                <a href="#">{{ data.user.nick_name }}</a>
                <a href="#">退出</a>
            </div>
        {% else %}
            {# 如果没有登录，则显示登录注册按钮 #}
            <div class="user_btns fr">
                <a href="javascript:;" class="login_btn">登录</a> / <a href="javascript:;" class="register_btn">注册</a>
            </div>

        {% endif %}
    </div>
</div>
```



#### 2.3-CSRFToken 跨站请求伪造

- ## 理清思路

目前登录注册发起的 POST 请求均未进行 csrf_token 校验，根据 csrf_token 校验原理，具体操作步骤有以下几步：

1. 后端生成 csrf_token 的值，在前端请求登录或者注册界面的时候将值传给前端，传给前端的方式可能有以下两种：
   - 在模板中的 From 表单中添加隐藏字段
   - 将 csrf_token 使用 cookie 的方式传给前端
2. 在前端发起请求时，在表单或者在请求头中带上指定的 csrf_token
3. 后端在接受到请求之后，取到前端发送过来的 csrf_token，与第1步生成的 csrf_token 的值进行校验
4. 如果校验对 csrf_token 一致，则代表是正常的请求，否则可能是伪造请求，不予通过

而在 Flask 中，CSRFProtect 这个类专门进行 csrf_token **校验**操作，所以需要做以下几件事情：

- 生成 csrf_token 的值

- 将 csrf_token 的值传给前端浏览器

- 在前端请求时带上 csrf_token 值

- ## 完成代码逻辑


- 将 csrf_token 的值传给前端浏览器
  - 实现思路：可以在请求勾子函数中完成此逻辑

`info/__init__.py`

```python
@app.after_request
def after_request(response):
    # 调用函数生成 csrf_token
    csrf_token = generate_csrf()
    # 通过 cookie 将值传给前端
    response.set_cookie("csrf_token", csrf_token)
    return response
```

- 在前端请求时带上 csrf_token 值
  - 根据登录和注册的业务逻辑，当前采用的是 ajax 请求
  - 所以在提交登录或者注册请求时，需要在请求头中添加 `X-CSRFToken` 的键值对

```js
$.ajax({
    url:"/passport/register",
    type: "post",
    headers: {
        "X-CSRFToken": getCookie("csrf_token")
    },
    data: JSON.stringify(params),
    contentType: "application/json",
    success: function (resp) {
        if (resp.errno == "0"){
            // 刷新当前界面
        location.reload()
        }else {
            $("#register-password-err").html(resp.errmsg)
            $("#register-password-err").show()
        }
    }
})
```

#### 2.4-登出功能实现

- 登录出功能本质就是删除之前登录保存到服务的 session 数据

- ### 后端代码实现

- `possport/views.py` 

```python
@passport_blu.route("/logout", methods=['POST'])
def logout():
    """
    清除session中的对应登录之后保存的信息
    :return:
    """
    # 返回结果
```

- ### 前端代码实现

- `news/main.js` 

```javascript
function logout() {
    $.ajax({
        url: "/passport/logout",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        success: function (resp) {
            // 刷新当前界面
            location.reload()
        }
    })
}
```

## 4.新闻首页

- ## 需求：

- 中间展示新闻分类信息

- 右侧显示新闻点击排行

- 根据分类进行新闻列表展示

- 下拉加载更多数据

- 点击新窗口跳转到新闻详情页

- ## 重点功能分析

- 新闻列表页需要实现下拉加载更多的交互逻辑

- 在用户下拉之后，新增的新闻数据直接拼接到页面的最下方，无需要更新整个页面

- 使用 ajax 请求，请求完毕之后拼接界面元素



### 1.点击排行

- 请求首页时去数据库查询按点击量排行的10条新闻

```python
@index_blu.route('/')
def index():
    # 获取到当前登录用户的id
    # 右侧新闻排行
    # 按照点击量排序查询出点击最高的前10条新闻
    # 将对象字典添加到列表中
	# 返回数据

```

- `index.html`添加点击排行并使用过滤器显示排行标签

```html
    <div class="rank_con fr">
        <div class="rank_title">
            <h3>点击排行</h3>
        </div>
        <ul class="rank_list">
            {% for new in data.news_dict %}
                <li><span class="{{ loop.index0 | indexClass }}">{{ loop.index }}</span><a href="#">{{ new.title }}</a></li>
            {% endfor %}
        </ul>
    </div>
```

- 在 **utils** 目录下创建 `common.py` 文件，并添加以下代码：

```python
def do_index_class(index):
    """自定义过滤器，过滤点击排序html的class"""
    if index == 0:
        return "first"
    elif index == 1:
        return "second"
    elif index == 2:
        return "third"
    else:
        return ""
```

- `info/__init__.py`注册过滤器

```python
# 注册自定义过滤器
from info.utils.common import do_index_class
app.add_template_filter(do_index_class, "indexClass")
```



### 2.新闻分类

- ### 需求:

  - 在请求主页的时候去查询新闻分类，第1个分类为选中状态

- `index/views.py`

```python
@index_blu.route('/')
def index():
    ...
    # 获取新闻分类数据
    # 定义列表保存分类数据
        # 拼接内容
    # 返回数据

```

- `index.html`数据展示

```html
<ul class="menu fl">
    {% for category in data.categories %}
        <li class="{% if loop.index0 == 0 %}active{% endif %}" data-cid="{{ category.id }}"><a href="javascript:;">{{ category.name }}</a></li>
    {% endfor %}
</ul>
```



### 3.新闻列表数据

- 新闻列表数据只是当前页面的一部分

- 点击分类时需要去获取当前分类下的新闻数据

- 并在展示的时候需要更新新闻列表界面，不需要整体页面刷新

- 所以新闻数据也使用 ajax 的方式去请求后台接口进行获取

- ## 接口设计

- URL：/news_list

- 请求方式：GET

- 传入参数：JSON格式

- 参数

| 参数名   | 类型   | 是否必须 | 参数说明                           |
| -------- | ------ | -------- | ---------------------------------- |
| cid      | string | 是       | 分类id                             |
| page     | int    | 否       | 页数，不传即获取第1页              |
| per_page | int    | 否       | 每页多少条数据，如果不传，默认10条 |

- 返回类型：JSON

| 参数名               | 类型   | 是否必须 | 参数说明             |
| -------------------- | ------ | -------- | -------------------- |
| errno                | int    | 是       | 错误码               |
| errmsg               | string | 是       | 错误信息             |
| cid                  | string | 是       | 当前新闻数据的分类id |
| totalPage            | int    | 否       | 总页数               |
| currentPage          | int    | 否       | 当前页数             |
| news                 | list   | 否       | 新闻列表数据         |
| news.title           | string | 是       | 新闻标题             |
| news.source          | string | 是       | 新闻来源             |
| news.digest          | string | 是       | 新闻摘要             |
| news.create_time     | string | 是       | 新闻时间             |
| news.index_image_url | string | 是       | 新闻索引图           |

- ### 后端实现

- `index/views.py`

```python
@index_blu.route('/news_list')
def news_list():
    """
    获取首页新闻数据
    :return:
    """

    # 1. 获取参数,并指定默认为最新分类,第一页,一页显示10条数据

    # 2. 校验参数

	  # 默认选择最新数据分类

    # 3. 查询数据

    # 将模型对象列表转成字典列表
	#返回数据
```

- ### 前端实现

- `index.js`

- 在首页加载函数时调用`updateNewsData`更新新闻数据

- 自动加载下页数据

```javascript
$(function () {
    // 首页加载后加载新闻数据
    updateNewsData()
    // 首页分类切换
    $('.menu li').click(function () {
        var clickCid = $(this).attr('data-cid')
        $('.menu li').each(function () {
            $(this).removeClass('active')
        })
        $(this).addClass('active')

        if (clickCid != currentCid) {
            // 记录当前分类id
            currentCid = clickCid

            // 重置分页参数
            cur_page = 1
            total_page = 1
            updateNewsData()
        }
    })

    //页面滚动加载相关
    $(window).scroll(function () {

        // 浏览器窗口高度
        var showHeight = $(window).height();

        // 整个网页的高度
        var pageHeight = $(document).height();

        // 页面可以滚动的距离
        var canScrollHeight = pageHeight - showHeight;

        // 页面滚动了多少,这个是随着页面滚动实时变化的
        var nowScroll = $(document).scrollTop();

        if ((canScrollHeight - nowScroll) < 100) {
            // 判断页数，去更新新闻数据
            if (!data_querying) {
                data_querying = true

                // 如果当前页小于总页数,则加载数据
                if (cur_page < total_page) {
                    cur_page += 1
                    updateNewsData()
                }
            }
        }
    })
})
```



```javascript
function updateNewsData() {
    // 更新新闻数据
    var params = {
        "page": cur_page,
        "cid": currentCid,
    }
    $.get("/news_list", params, function (resp) {
        // 是否查询数据
        data_querying = false
        // 总页数赋值
        if (resp) {
            total_page = resp.data.total_page

            // 先清空原有数据
            if (cur_page == 1) {
                $(".list_con").html('')
            }
            // 显示数据
            for (var i = 0; i < resp.data.news_dict_list.length; i++) {
                var news = resp.data.news_dict_list[i]
                var content = '<li>'
                content += '<a href="#" class="news_pic fl"><img src="' + news.index_image_url + '?imageView2/1/w/170/h/170"></a>'
                content += '<a href="#" class="news_title fl">' + news.title + '</a>'
                content += '<a href="#" class="news_detail fl">' + news.digest + '</a>'
                content += '<div class="author_info fl">'
                content += '<div class="source fl">来源：' + news.source + '</div>'
                content += '<div class="time fl">' + news.create_time + '</div>'
                content += '</div>'
                content += '</li>'
                $(".list_con").append(content)
            }
        }
        else {
            alert(resp.errmsg)
        }
    })
}
```

## 5.新闻详情

### 5.1-基类模板抽取

- ## 分析

- 因为使用的是ajax局部刷新,详情面和首页都有相同的东西，

- 可以将共同内容抽取到基类模板中，再使用其他模板继承基类模板

- ## 抽取

- 在`templates`文件夹下创建基类模板`base.html`

  - 将首页内容全部拷贝到该文件中，将特有的东西留作 block 给子模板实现
  - 抽取出来的block为：
    - 标题
    - script内容
    - 顶部中心
    - 页面内容
    - 点击排行div中的作者信息
  - 具体见以下代码

复制`index.html`文件内容到`bash.html`抽取内容

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block titleBlock %}{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="../../static/news/css/reset.css">
    {% block cssBlock %}
    {% endblock %}
    <link rel="stylesheet" type="text/css" href="../../static/news/css/main.css">
    <script type="text/javascript" src="../../static/news/js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript" src="../../static/news/js/main.js"></script>
    {% block scriptBlock %}{% endblock %}
</head>
<body>
<div class="header_con">
    <div class="header">
        <a href="/" class="logo fl"><img src="../../static/news/images/logo.png" alt="logo"></a>
        {% block categoryblock %}
            <ul class="menu fl">
                {% for category in data.category_list %}
                    {% if loop.index == 1 %}
                        <li class="active" data-cid="{{ category.id }}"><a href="javascript:;">{{ category.name }}</a>
                        </li>
                    {% else %}
                        <li data-cid="{{ category.id }}"><a href="javascript:;">{{ category.name }}</a></li>
                    {% endif %}
                {% endfor %}
                {#            <li class="active" data-cid="0"><a href="javascript:;">最新</a></li>#}
                {#            <li data-cid="1"><a href="javascript:;">股市</a></li>#}
                {#            <li data-cid="2"><a href="javascript:;">债市</a></li>#}
                {#            <li data-cid="3"><a href="javascript:;">商品</a></li>#}
                {#            <li data-cid="4"><a href="javascript:;">外汇</a></li>#}
                {#            <li data-cid="5"><a href="javascript:;">公司</a></li>#}
            </ul>
        {% endblock %}
        {# 判断用户是否登录 #}
        {% if data.user %}
            {# 如果登录，则显示用户信息 #}
            <div class="user_login fr">
                <img src="
                        {% if data.user.avatar_url %}{{ data.user.avatar_url }}{% else %}../../static/news/images/person01.png{% endif %}"
                     class="lgin_pic">
                <a href="#">{{ data.user.nick_name }}</a>
                <a href="javascript:;" onclick="logout()">退出</a>
            </div>
        {% else %}
            {# 如果没有登录，则显示登录注册按钮 #}
            <div class="user_btns fr">
                <a href="javascript:;" class="login_btn">登录</a> / <a href="javascript:;" class="register_btn">注册</a>
            </div>

        {% endif %}
    </div>
</div>

<div class="conter_con">
    {% block contentblock %}

    {% endblock %}
    {% block rankBlock %}
        <div class="rank_con fr">
            {% block authorblock %}

            {% endblock %}
            <div class="rank_title">
                <h3>点击排行</h3>
            </div>
            <ul class="rank_list">
                {% for new in data.news_dict %}
                    <li><span class="{{ loop.index0 | index_class }}">{{ loop.index }}</span><a
                            href="#">{{ new.title }}</a>
                    </li>
                {% endfor %}
            </ul>
        </div>
    {% endblock %}
</div>
{% block bottomblock %}
    <div class="footer">
        <div class="footer_links">
            <a href="">关于我们</a>
            <span>|</span>
            <a href="">联系我们</a>
            <span>|</span>
            <a href="">招聘人才</a>
            <span>|</span>
            <a href="">友情链接</a>
        </div>
        <p class="copyright">
            CopyRight © 2018 新经资讯信息技术有限公司 All Rights Reserved<br/>
            电话：010-****888 京ICP备*******8号
        </p>
    </div>
{% endblock %}


<!-- 登录表单 -->
<form class="login_form_con">
    <div class="login_form">
        <div class="login_title">
            <h3>登 录</h3>
            <a href="javascript:;" class="shutoff"></a>
        </div>
        <div class="form_group">
            <input id="mobile" type="text" name="mobile" autocomplete="off">
            <div class="input_tip">手机号</div>
            <div id="login-mobile-err" class="error_tip">手机号不能为空</div>
        </div>
        <div class="form_group">
            <input id="password" type="password" name="password">
            <div class="input_tip">密码(不少于6位)</div>
            <div id="login-password-err" class="error_tip">密码不能为空</div>
        </div>
        <input type="submit" name="" value="登 录" class="input_sub">
        <div class="down_link">还没有账号？<a href="javascript:;" class="to_register">立即注册</a></div>
    </div>
    <div class="mask"></div>
</form>

<!-- 注册表单 -->
<form class="register_form_con">
    <div class="register_form">
        <div class="register_title">
            <h3>注 册</h3>
            <a href="javascript:;" class="shutoff"></a>
        </div>
        <div class="form_group">
            <input type="text" name="mobile" autocomplete="off" id="register_mobile" class="phone_input">
            <div class="input_tip">手机号</div>
            <div id="register-mobile-err" class="error_tip">手机号不能为空</div>
        </div>
        <div class="form_group">
            <input type="text" name="code_pwd" id="imagecode" class="code_pwd">
            <div class="input_tip">图形验证码</div>
            <img src="../../static/news/images/pic_code.png" class="get_pic_code" onclick="generateImageCode()">
            <div id="register-image-code-err" class="error_tip">图形码不能为空</div>
        </div>
        <div class="form_group">
            <input type="text" name="smscode" id="smscode" class="code_pwd">
            <div class="input_tip">手机验证码</div>
            <a href="javascript:;" class="get_code" onclick="sendSMSCode()">点击获取验证码</a>
            <div id="register-sms-code-err" class="error_tip">验证码不能为空</div>
        </div>
        <div class="form_group">
            <input type="password" name="password" id="register_password" class="pass_input">
            <div class="input_tip">密码(不少于6位)</div>
            <div id="register-password-err" class="error_tip">密码不能为空</div>
        </div>
        <div class="form_group2 clearfix">
            <input type="checkbox" class="agree_input" checked>
            <p>同意使用条款，并已阅读"跟帖评论自律管理承诺书"</p>
            <div class="error_tip">请勾选</div>
        </div>
        <input type="submit" name="" value="注 册" class="input_sub">
        <div class="down_link">已有账号？<a href="javascript:;" class="to_login">立即登录</a></div>
    </div>
    <div class="mask"></div>
</form>
</body>
</html>
```

- `index.html` 

```html
{% extends 'news/base.html' %}

{% block titleBlock %}
    首页-新经资讯
{% endblock %}

{% block scriptBlock %}
    <script type="text/javascript" src="../../static/news/js/index.js"></script>
{% endblock %}

{% block contentblock %}
    <ul class="list_con fl">
    </ul>
{% endblock %}
```

- `detail.html` 

```html
{% extends 'news/base.html' %}

{% block titleBlock %}
    文章详情页
{% endblock %}

{% block scriptBlock %}
    <script type="text/javascript" src="../../static/news/js/detail.js"></script>
{% endblock %}

{% block categoryblock %}

{% endblock %}

{% block contentblock %}
    <div class="detail_con fl">
       ...
    </div>

{% endblock %}

{% block authorblock %}
    <div class="author_card">
        ...
    </div>
{% endblock %}
```

- 新建`news`新闻详情模块并注册蓝图
- 测试运行状况

`news/views.py`

```python
@news_blu.route('/<int:news_id>')
def news_detail(news_id):
    data = {}
    return render_template('news/detail.html', data=data)
```

### 5.2-G变量用户登陆

- ### 实现思路：

- 使用装饰器去加载用户数据并记录到 g 变量

- 在当前请求中可以直接使用 g 变量取到用户数据

- ### 代码实现

- 在` common.py` 中装饰器函数

```python
def user_login_data(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # 获取到当前登录用户的id
        user_id = session.get("user_id")
        # 通过id获取用户信息
        user = None
        if user_id:
            from info.models import User
            user = User.query.get(user_id)

        g.user = user
        return f(*args, **kwargs)

    return wrapper
```

- 修改 `index/views.py` 替换之前登陆逻辑,改用g变量
- 使用时添加自定义装饰器`@user_login_data`

```python
@index_blu.route('/')
@user_login_data
def index():
    # 获取到当前登录用户的id
    # user_id = session.get('user_id', None)
    # user = None
    # if user_id:
    #     try:
    #         user = User.query.get(user_id)
    #     except Exception as e:
    #         current_app.logger.error(e)

    # 使用g变量获取用户登陆信息
    user = g.user
```

- 修改 `news/views.py` 视图函数逻辑
- 套用主页点击排行榜代码,并添加用户验证

```python
@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
	......

    data = {
        user = g.user
        ......
        # "user": g.user.to_dict() if g.user else None,
        "user": user.to_dict() if user else None,
    }
    return render_template('news/detail.html', data=data)

```

> g 变量是一个应用上下文变量，类似于一个全局变量，但是 g 变量里面的保存的值是相对于每次请求的，不同的请求，g 变量里面保存的值是不同的，所以同一次请求，可以使用 g 变量来保存值用于进行函数的传递。

### 5.3-新闻数据

- ### 新闻详情页数据

- 点击新闻后查询新闻数据并返回

`news/views.py`

```python
@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    
    ......
    
	# 查询新闻数据
	# 校验报404错误
    # 进入详情页后要更新新闻的点击次数
	# 返回数据

```

- `detail.html`	

```html
<div class="detail_con fl">
    <h3>{{ data.news.title }}</h3>
    <div class="detail_about clearfix">
        <span class="time_souce fl">{{ data.news.create_time }} 来源: {{ data.news.source }}</span>
        <span class="comment fr">{{ data.news.comments_count }}</span>
    </div>
    {{ data.news.content | safe }}
    ...
        {% if data.user %}
            <form action="" class="comment_form" data-newsid="{{ data.news.id }}">
                <div class="person_pic">
                    <img src="{% if data.user.avatar_url %}
                    {{ data.user.avatar_url }}
                {% else %}
                    ../../static/news/images/person01.png
                {% endif %}" alt="用户图标">
                </div>
                <textarea placeholder="请发表您的评论" class="comment_input"></textarea>
                <input type="submit" name="" value="评 论" class="comment_sub">
            </form>
        {% else %}
            <div class="comment_form_logout">
                登录发表你的评论
            </div>
        {% endif %}

        <div class="comment_count">
            {{ data.news.comments_count }}条评论
        </div>
    ...
</div>
```



### 5.4-收藏功能

- ### 需求分析：

- 进入到新闻详情页之后，如果用户已收藏该新闻，则显示已收藏，点击则为取消收藏，反之点击收藏该新闻

- #### 代码实现

代码实现分为以下几步：

- 前端根据后台返回数据显示收藏或者取消收藏按钮

- 后端提供收藏与取消收藏接口

- 前端发起收藏或者取消收藏请求

- #### 前端是否收藏界面展示

- 在新闻详情的视图函数中添加变量 `is_collected`，并在渲染模板时传入

```python
@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    ...
    # 判断是否收藏该新闻，默认值为 false
    is_collected = False
    # 判断用户是否收藏过该新闻
    # 返回数据
```

- 前端根据传入值判断显示哪一个a标签，并使用标签记录当前新闻id，以供后续逻辑使用
- `detail.html`

```html
    <a href="javascript:;" class="collected block-center" data-newid="{{ data.news.id }}" style="display: {% if data.is_collected %} block
    {% else %} none {% endif %};"><span class="out">已收藏</span><span class="over">取消收藏</span></a>
    <a href="javascript:;" class="collection block-center" data-newid="{{ data.news.id }}" style="display: {% if data.is_collected %} none
            {% else %} block {% endif %};">收藏</a>
```

- 

- # 收藏后端接口实现

- ## 接口设计

- URL：/news/news_collect

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名  | 类型   | 是否必须 | 参数说明                                |
| ------- | ------ | -------- | --------------------------------------- |
| news_id | int    | 是       | 新闻id                                  |
| action  | string | 是       | 指定两个值：'collect', 'cancel_collect' |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 代码实现

- 在 `new/views.py` 文件中添加视图函数

```python
@news_blu.route("/news_collect", methods=['POST'])
@user_login_data
def news_collect():
    """新闻收藏"""

    user = g.user
    # 获取参数
    # 判断参数
	# action在不在指定的两个值：'collect', 'cancel_collect'内
    # 查询新闻,并判断新闻是否存在

    # 收藏/取消收藏
    if action == "cancel_collect":
        # 取消收藏
        if XXXXXX:
    else:
        # 收藏
        if XXXXXX:

    # 返回

```

- # 收藏前端逻辑实现

- 在 `detail.js` 中实现收藏和取消收藏请求

```js
    // 收藏
    $(".collection").click(function () {
        var params = {
            "news_id": $(this).attr('data-newid'),
            "action": 'collect'
        }
        $.ajax({
            url: "/news/news_collect",
            type: "post",
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            success: function (resp) {
                if (resp.errno == "0") {
                    // 收藏成功
                    // 隐藏收藏按钮
                    $(".collection").hide();
                    // 显示取消收藏按钮
                    $(".collected").show();
                } else if (resp.errno == "4101") {
                    $('.login_form_con').show();
                } else {
                    alert(resp.errmsg);
                }
            }
        })

    })

    // 取消收藏
    $(".collected").click(function () {
        var params = {
            "news_id": $(this).attr('data-newid'),
            "action": 'cancel_collect'
        }
        $.ajax({
            url: "/news/news_collect",
            type: "post",
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            success: function (resp) {
                if (resp.errno == "0") {
                    // 收藏成功
                    // 隐藏收藏按钮
                    $(".collection").show();
                    // 显示取消收藏按钮
                    $(".collected").hide();
                } else if (resp.errno == "4101") {
                    $('.login_form_con').show();
                } else {
                    alert(resp.errmsg);
                }
            }
        })

    })
```

### 5.5-评论/点赞功能

- #### 需求分析

- 用户如果在登录的情况下，可以进行评论，未登录，点击评论弹出登录框

- 用户可以直接评论当前新闻，也可以回复别人发的评论

- 用户A回复用户B的评论之后，用户A的评论会当做一条主评论进行显示，下面使用灰色框将用户B的评论显示

- # 评论新闻后端实现

- ## 接口设计

- URL：/news/news_comment

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名    | 类型   | 是否必须 | 参数说明       |
| --------- | ------ | -------- | -------------- |
| news_id   | int    | 是       | 新闻id         |
| comment   | string | 是       | 评论内容       |
| parent_id | int    | 否       | 回复的评论的id |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 后端代码实现

- `news/views.py` 

```python
@news_blu.route('/news_comment', methods=["POST"])
@user_login_data
def add_news_comment():
    """添加评论"""

    # 用户是否登陆
    # 获取参数
    # 判断参数是否正确
    # 查询新闻是否存在并校验
    # 初始化评论模型，保存数据
    # 配置文件设置了自动提交,自动提交要在return返回结果以后才执行commit命令,如果有回复
    # 评论,先拿到回复评论id,在手动commit,否则无法获取回复评论内容
    # 返回响应

```

- # 评论新闻前端实现

- `detail.js` 

```js
// 评论提交
$(".comment_form").submit(function (e) {
    e.preventDefault();
    var news_id = $(this).attr('data-newsid')
    var news_comment = $(".comment_input").val();

    if (!news_comment) {
        alert('请输入评论内容');
        return
    }
    var params = {
        "news_id": news_id,
        "comment": news_comment
    };
    $.ajax({
        url: "/news/news_comment",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        data: JSON.stringify(params),
        success: function (resp) {
            if (resp.errno == '0') {
                var comment = resp.data
                // 拼接内容
                var comment_html = ''
                comment_html += '<div class="comment_list">'
                comment_html += '<div class="person_pic fl">'
                if (comment.user.avatar_url) {
                    comment_html += '<img src="' + comment.user.avatar_url + '" alt="用户图标">'
                }else {
                    comment_html += '<img src="../../static/news/images/person01.png" alt="用户图标">'
                }
                comment_html += '</div>'
                comment_html += '<div class="user_name fl">' + comment.user.nick_name + '</div>'
                comment_html += '<div class="comment_text fl">'
                comment_html += comment.content
                comment_html += '</div>'
                comment_html += '<div class="comment_time fl">' + comment.create_time + '</div>'

                comment_html += '<a href="javascript:;" class="comment_up fr" data-commentid="' + comment.id + '" data-newsid="' + comment.news_id + '">赞</a>'
                comment_html += '<a href="javascript:;" class="comment_reply fr">回复</a>'
                comment_html += '<form class="reply_form fl" data-commentid="' + comment.id + '" data-newsid="' + news_id + '">'
                comment_html += '<textarea class="reply_input"></textarea>'
                comment_html += '<input type="button" value="回复" class="reply_sub fr">'
                comment_html += '<input type="reset" name="" value="取消" class="reply_cancel fr">'
                comment_html += '</form>'

                comment_html += '</div>'
                // 拼接到内容的前面
                $(".comment_list_con").prepend(comment_html)
                // 让comment_sub 失去焦点
                $('.comment_sub').blur();
                // 清空输入框内容
                $(".comment_input").val("")
            }else {
                alert(resp.errmsg)
            }
        }
    })
})
```

- # 新闻评论列表

- # 后端实现

- 在新闻详情的视图函数中，添加查询当前新闻评论的逻辑

- `/news/views.py`

```python
@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    ...
    # 获取当前新闻最新的评论,按时间排序
    # 判断用户是否收藏过该新闻
    # 返回收据

```

- # 评论前端实现

- `detail.html` 

```html
        <div class="comment_list_con">
            {% for comment in data.comments %}
                <div class="comment_list">
                    <div class="person_pic fl">
                        <img src="{% if comment.user.avatar_url %}
                {{ comment.user.avatar_url }}
            {% else %}
                ../../static/news/images/person01.png
            {% endif %}" alt="用户图标">
                    </div>
                    <div class="user_name fl">{{ comment.user.nick_name }}</div>
                    <div class="comment_text fl">{{ comment.content }}</div>
                    {% if comment.parent %}
                        <div class="reply_text_con fl">
                            <div class="user_name2">{{ comment.parent.user.nick_name }}</div>
                            <div class="reply_text">
                                {{ comment.parent.content }}
                            </div>
                        </div>
                    {% endif %}
                    <div class="comment_time fl">{{ comment.create_time }}</div>
                    <a href="javascript:;" class="comment_up fr" data-commentid="{{ comment.id }}"
                       data-newsid="{{ comment.news_id }}">赞</a>
                    <a href="javascript:;" class="comment_reply fr">回复</a>
                    <form class="reply_form fl" data-commentid="{{ comment.id }}" data-newsid="{{ data.news.id }}">
                        <textarea class="reply_input"></textarea>
                        <input type="button" value="回复" class="reply_sub fr">
                        <input type="reset" name="" value="取消" class="reply_cancel fr">
                    </form>
                </div>
            {% endfor %}
        </div>
```

- # 回复评论前端实现

- `detail.js`

```js
// 回复评论
if(sHandler.indexOf('reply_sub')>=0)
{
    var $this = $(this)
    var news_id = $this.parent().attr('data-newsid')
    var parent_id = $this.parent().attr('data-commentid')
    var comment = $this.prev().val()

    if (!comment) {
        alert('请输入评论内容')
        return
    }
    var params = {
        "news_id": news_id, 
        "comment": comment, 
        "parent_id": parent_id
    }
    $.ajax({
        url: "/news/news_comment",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        data: JSON.stringify(params),
        success: function (resp) {
            if (resp.errno == "0") {
                var comment = resp.data
                // 拼接内容
                var comment_html = ""
                comment_html += '<div class="comment_list">'
                comment_html += '<div class="person_pic fl">'
                if (comment.user.avatar_url) {
                    comment_html += '<img src="' + comment.user.avatar_url + '" alt="用户图标">'
                }else {
                    comment_html += '<img src="../../static/news/images/person01.png" alt="用户图标">'
                }
                comment_html += '</div>'
                comment_html += '<div class="user_name fl">' + comment.user.nick_name + '</div>'
                comment_html += '<div class="comment_text fl">'
                comment_html += comment.content
                comment_html += '</div>'
                comment_html += '<div class="reply_text_con fl">'
                comment_html += '<div class="user_name2">' + comment.parent.user.nick_name + '</div>'
                comment_html += '<div class="reply_text">'
                comment_html += comment.parent.content
                comment_html += '</div>'
                comment_html += '</div>'
                comment_html += '<div class="comment_time fl">' + comment.create_time + '</div>'

                comment_html += '<a href="javascript:;" class="comment_up fr" data-commentid="' + comment.id + '" data-newsid="' + comment.news_id + '">赞</a>'
                comment_html += '<a href="javascript:;" class="comment_reply fr">回复</a>'
                comment_html += '<form class="reply_form fl" data-commentid="' + comment.id + '" data-newsid="' + news_id + '">'
                comment_html += '<textarea class="reply_input"></textarea>'
                comment_html += '<input type="button" value="回复" class="reply_sub fr">'
                comment_html += '<input type="reset" name="" value="取消" class="reply_cancel fr">'
                comment_html += '</form>'

                comment_html += '</div>'
                $(".comment_list_con").prepend(comment_html)
                // 请空输入框
                $this.prev().val('')
                // 关闭
                $this.parent().hide()
            }else {
                alert(resp.errmsg)
            }
        }
    })
}
```

- # 更新新闻评论条数

- 在评论或回复评论后不能立即更新评论条数,添加评论条数实时统计

- 思路：获取新闻评论 div(comment_list) 的数量，在 detail.js 里面添加以下函数

```js
// 更新评论条数
function updateCommentCount() {
    var length = $(".comment_list").length
    $(".comment_count").html(length + "条评论")
}



// 在评论和回复评论结束后调用updateCommentCount()函数

# 评论js代码处
// 清空输入框内容
$(".comment_input").val("")
updateCommentCount()

# 回复评论js代码处
// 关闭
$this.parent().hide()
updateCommentCount()
```

- # 评论点赞功能

- ## 需求分析

- 后端提供点赞和取消点赞功能

- 当用户点击未点赞按钮，执行点赞逻辑，向后端发起点赞请求，取消点赞则反之

- 在新闻显示完成之后，底部评论会根据当前登录用户显示是否点赞图标

- ## 接口设计

- URL：/news/comment_like

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名     | 类型   | 是否必须 | 参数说明                                  |
| ---------- | ------ | -------- | ----------------------------------------- |
| comment_id | int    | 是       | 评论id                                    |
| action     | string | 是       | 点赞操作类型：add(点赞)，remove(取消点赞) |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 后端代码实现

- `news/views.py` 

```python
@news_blu.route('/comment_like', methods=["POST"])
@user_login_data
def comment_like():
    """
    评论点赞
    :return:
    """
    # 用户是否登陆
    # 取到请求参数
    # 判断参数
    # 获取到要被点赞的评论模型
	# action的状态,如果点赞,则查询后将用户id和评论id添加到数据库
            # 点赞评论
            # 更新点赞次数

        # 取消点赞评论,查询数据库,如果以点在,则删除点赞信息

            # 更新点赞次数

	# 返回结果

```



- # 前端逻辑实现

- 给点赞的 a 标签添加自定义属性，以记录当前点赞的新闻id和评论id，供点赞/取消点赞请求使用

```html
<a href="javascript:;" class="comment_up fr" data-commentid="{{ comment.id }}" data-newsid="{{ data.news.id }}">赞</a>
```

- 实现点赞逻辑

```js
if(sHandler.indexOf('comment_up')>=0)
{
    var $this = $(this);
    var action = "add"
    if(sHandler.indexOf('has_comment_up')>=0)
    {
        // 如果当前该评论已经是点赞状态，再次点击会进行到此代码块内，代表要取消点赞
        action = "remove"
    }

    var comment_id = $(this).attr("data-commentid")
    var params = {
        "comment_id": comment_id,
        "action": action,
    }

    $.ajax({
        url: "/news/comment_like",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        data: JSON.stringify(params),
        success: function (resp) {
            if (resp.errno == "0") {
                // 更新点赞按钮图标
                if (action == "add") {
                    // 代表是点赞
                    $this.addClass('has_comment_up')
                }else {
                    $this.removeClass('has_comment_up')
                }
            }else if (resp.errno == "4101"){
                $('.login_form_con').show();
            }else {
                alert(resp.errmsg)
            }
        }
    })
}
```

- # 是否点赞数据返回

- 在新闻详情视图函数中，如果用户已登录，返回的评论要记录当前用户是否点赞

```python
@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    ...
    # 查询评论数据
    # 如果用户登陆
            # 查询当前新闻所有评论ID,按时间排序
            # 查询当前新闻所有评论哪些被当前用户点赞
            # 取出所有被点赞评论ID
	# 遍历评论id,将评论属性赋值
    comment_dict_list = []
    for comment in comments:
        comment_dict = comment.to_dict()
        # 为评论增加'is_like'字段,判断是否评论
        comment_dict['is_like'] = False
        # 判断用户是否在点赞评论里
        if comment.id in comment_like_ids:
            comment_dict["is_like"] = True
        comment_dict_list.append(comment_dict)

    data = {
        'news': news.to_dict(),
        'news_dict': news_dict,
        'is_collected': is_collected,
        'comments': comment_dict_list,
        "user": g.user.to_dict() if g.user else None
    }
    return render_template('news/detail.html', data=data)
```

- # 点赞计数功能（20190719）

- 实现评论如果有点赞，就显示点赞的条数，并使用自定义属性记录当前条数

- `detail.html`

```html
<a href="javascript:;" class="comment_up
{% if comment.is_like %}
    has_comment_up
{% endif %} fr" 
   data-commentid="{{ comment.id }}" 
   data-likecount="{{ comment.like_count }}"
   data-newsid="{{ data.news.id }}">
{% if comment.like_count > 0 %}
    {{ comment.like_count }}
{% else %}
    赞
{% endif %}</a>
```

- 点赞/取消点赞操作完成之后，更新条数
- `detail.js`

```js
            $.ajax({
                url: "/news/comment_like",
                type: "post",
                contentType: "application/json",
                headers: {
                    "X-CSRFToken": getCookie("csrf_token")
                },
                data: JSON.stringify(params),
                success: function (resp) {
                    if (resp.errno == "0") {
                        // 更新点赞按钮图标
                        var like_count = $this.attr('data-likecount')
                        
                        if (like_count == undefined){
                            like_count = 0
                        }
                        
                        // 更新点赞按钮图标
                        if (action == "add") {
                            like_count = parseInt(like_count) + 1
                            // 代表是点赞
                            $this.addClass('has_comment_up')
                        } else {
                            like_count = parseInt(like_count) - 1
                            $this.removeClass('has_comment_up')
                        }
                        // 更新点赞数据
                        $this.attr('data-likecount', like_count)
                        if (like_count == 0) {
                            $this.html("赞")
                        } else {
                            $this.html(like_count)
                        }
                    } else if (resp.errno == "4101") {
                        $('.login_form_con').show();
                    } else {
                        alert(resp.errmsg)
                    }
                }
            })
```

## 6.个人中心

### 6.1-基类模板抽取

- 个人中心页面和新闻详情页一样，顶部和底部内容类似，可以继承之前抽取的 `base.html`
- `templates/news/user.html`

```html
{% extends 'news/base.html' %}

{% block titleBlock %}
    用户中心
{% endblock %}

{% block authorblock %}

{% endblock %}

{% block rankBlock %}

{% endblock %}

{% block contentblock %}
    <div class="user_menu_con fl">
        <div class="user_center_pic">
            <img src={% if data.user.avatar_url %}
                {{ data.user.avatar_url }}
            {% else %}
                "../../static/news/images/user_pic.png"
            {% endif %} alt="用户图片">
        </div>
        <div class="user_center_name">{{ data.user.nick_name }}</div>

        <ul class="option_list">
            <li class="active"><a href="../../static/news/html/user_base_info.html" target="main_frame">基本资料</a></li>
            <li><a href="../../static/news/html/user_pic_info.html" target="main_frame">头像设置</a></li>
            <li><a href="../../static/news/html/user_follow.html" target="main_frame">我的关注</a></li>
            <li><a href="../../static/news/html/user_pass_info.html" target="main_frame">密码修改</a></li>
            <li><a href="../../static/news/html/user_collection.html" target="main_frame">我的收藏</a></li>
            <li><a href="../../static/news/html/user_news_release.html" target="main_frame">新闻发布</a></li>
            <li><a href="../../static/news/html/user_news_list.html" target="main_frame">新闻列表</a></li>
        </ul>
    </div>

    <div class="user_con fr">
        <iframe src="../../static/news/html/user_base_info.html" frameborder="0" name="main_frame" class="main_frame"
                id="main_frame"></iframe>
    </div>
{% endblock %}

{% block categoryblock %}

{% endblock %}
```

- ## 后端测试

- 创建个人中心`profile`模块并注册蓝图

- `profile/views.py`

```python
@profile_blu.route('/info')
@user_login_data
def user_info():
    # 如果用户登陆则进入个人中心
    # 如果没有登陆,跳转主页
    # 返回用户数据

```

### 6.2-基本资料设置

- ## 需求分析

- 进入界面之后展示用户的基本资料(个性签名、昵称、性别)

- 用户修改之后点击保存向服务器发起请求进行数据保存更新

- ## 默认数据展示

- 将 `static/news/user_base_info.html` 拖动到模板文件夹下的 `templates/news` 文件夹内

- 在 `profile/views.py` 文件中添加路由函数，用于在展示界面时填上默认数据

```python
@profile_blu.route('/base_info')
@user_login_data
def base_info():
    """
    用户基本信息
    :return:
    """
    return render_template('news/user_base_info.html', data={"user": g.user.to_dict()})
```

- 修改 `news/user.html` 中用户基本信息的昵称显示,并将连接指向`base_info`模板

```html
        <div class="user_center_name">{{ data.user.nick_name }}</div>

        <ul class="option_list">
            <li class="active"><a href="{{ url_for('profile.base_info') }}" target="main_frame">基本资料</a></li>
            <li><a href="../../static/news/html/user_pic_info.html" target="main_frame">头像设置</a></li>
            <li><a href="../../static/news/html/user_follow.html" target="main_frame">我的关注</a></li>
            <li><a href="../../static/news/html/user_pass_info.html" target="main_frame">密码修改</a></li>
            <li><a href="../../static/news/html/user_collection.html" target="main_frame">我的收藏</a></li>
            <li><a href="../../static/news/html/user_news_release.html" target="main_frame">新闻发布</a></li>
            <li><a href="../../static/news/html/user_news_list.html" target="main_frame">新闻列表</a></li>
        </ul>
    </div>

    <div class="user_con fr">
        <iframe src="{{ url_for('profile.base_info') }}" frameborder="0" name="main_frame" class="main_frame"
                id="main_frame"></iframe>
    </div>
```

- # 后端接口实现

- ## 接口设计

- URL：/user/base_info

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名    | 类型   | 是否必须 | 参数说明              |
| --------- | ------ | -------- | --------------------- |
| nick_name | string | 是       | 昵称                  |
| signature | string | 是       | 签名                  |
| gender    | string | 是       | 性别, `MAN` / `WOMAN` |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 代码实现

- 因为默认会有原始的用户昵称和个性签名,所以在初次请求时是**GET**请求查询用户数据

- 修改昵称和签名时是**POST**请求,所以同时使用2中请求方式

- `profile/views.py` 

```python
@profile_blu.route('/base_info', methods=["GET", "POST"])
@user_login_data
def base_info():
    # 不同的请求方式，做不同的事情
    # 如果是GET请求,返回用户数据


    # 修改用户数据
    # 获取传入参数

    # 校验参数

	# 修改用户数据

	# 返回

```

- # 前端逻辑实现

- `news/static/user_base_info.js` 

```js
$(function () {

    $(".base_info").submit(function (e) {
        e.preventDefault()

        var signature = $("#signature").val()
        var nick_name = $("#nick_name").val()
        var gender = $(".gender[name='gender']:checked").val()

        if (!nick_name) {
            alert('请输入昵称')
            return
        }
        if (!gender) {
            alert('请选择性别')
        }

        var params = {
            "signature": signature,
            "nick_name": nick_name,
            "gender": gender
        }

        $.ajax({
            url: "/user/base_info",
            type: "post",
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            success: function (resp) {
                if (resp.errno == "0") {
                    // 更新父窗口内容
                    $('.user_center_name', parent.document).html(params['nick_name'])
                    $('#nick_name', parent.document).html(params['nick_name'])
                    $('.input_sub').blur()
                }else {
                    alert(resp.errmsg)
                }
            }
        })
    })
})
```

### 6.3-头像上传

- ## 需求分析

- 用户可以进行头像的修改，上传完毕之后更新个人中心跟头像相关的标签内容

- 上传的头像文件保存到【七牛云】提供的文件存储服务器中

- ## 模板渲染

- 将 `static/news/user_pic_info.html` 拖动到模板文件夹下的 `news` 文件夹内

- `profile/views.py` 测试模板

```python
@profile_blu.route('/pic_info', methods=["GET", "POST"])
@user_login_data
def pic_info():
    user = g.user
    return render_template('news/user_pic_info.html', data={"user_info": user.to_dict()})
```

- `user_pic_info.html` 

```html
<div class="form-group">
    <label class="label01">当前图像：</label>
    <img src="{% if data.user_info.avatar_url %}{{ data.user_info.avatar_url }}{% else %}../../static/news/images/user_pic.png{% endif %}" alt="用户图片" class="now_user_pic">
</div>
```

- `news/user.html` 

```html
            <li><a href="{{ url_for('profile.pic_info') }}" target="main_frame">头像设置</a></li>

```

- # 七牛云存储

- 对于实际项目的作用：

  - 用于在实际项目中存储媒体(图像、音频、视频)文件
  - 节省自己服务器空间，节约宽带，提升媒体文件访问的稳定性
  - 不需要人力物力对重复数据、冗余数据进行清理及判断

- 官网：<https://www.qiniu.com/>

- SDK地址：<https://developer.qiniu.com/sdk#official-sdk>

- GitHub-SDK:<https://github.com/qiniu/python-sdk>

- ## 封装上传图片工具类

- 安装工具包

```
pip install qiniu

```

- 在 `info/utils` 目录下创建 `image_storage.py` 文件
- `image_storage.py`

```python
from qiniu import Auth, put_data

access_key = 'Q3l0L4uo8vTXvLs6UacKg3xHykxxhoZSzmFIlf6w'
secret_key = 'r8Bn58sGxNz1jcD2HY8tbTEiZwecBOg1eZgDcIB3'
# 七牛云创建的储存空间名称
bucket_name = 'news_info'


def storage(data):
    try:
        q = Auth(access_key, secret_key)
        token = q.upload_token(bucket_name)
        ret, info = put_data(token, None, data)
        print(ret, info)
    except Exception as e:
        raise e

    if info.status_code != 200:
        raise Exception('上传图片失败')
    return ret['key']


if __name__ == '__main__':
    file = input('请输入路径')
    with open(file, 'rb') as f:
        storage(f.read())
```

- # 后端接口实现

- ## 接口设计

- URL：/user/pic_info

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名 | 类型 | 是否必须 | 参数说明 |
| ------ | ---- | -------- | -------- |
| avatar | file | 是       | 头像     |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 代码实现

- 在 `profile/views.py` 

```python
@profile_blu.route('/pic_info', methods=["GET", "POST"])
@user_login_data
def pic_info():
    # 如果是GET请求,返回用户数据

    # 如果是POST请求表示修改头像
    # 1. 获取到上传的图片

    # 2. 上传头像

        # 使用自已封装的storage方法去进行图片上传

    # 3. 保存头像地址
    # 拼接url并返回数据

```

- # 前端逻辑实现

- `user_pic_info.js` 

```js
$(function () {

    $(".pic_info").submit(function (e) {
        e.preventDefault()

        // 上传头像
        $(this).ajaxSubmit({
            url: "/user/pic_info",
            type: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    $(".now_user_pic").attr("src", resp.data.avatar_url)
                    $(".user_center_pic>img", parent.document).attr("src", resp.data.avatar_url)
                    $(".user_login>img", parent.document).attr("src", resp.data.avatar_url)
                }else {
                    alert(resp.errmsg)
                }
            }
        })
    })
})
```

### 6.4-修改密码

- ## 需求分析

- 使用原密码和新密码进行密码修改

- ## 模板渲染

- 将 `static/news/user_pass_info.html` 拖动到模板文件夹下的 `news` 文件夹内

- `profile/views.py`测试模板

```python
@profile_blu.route('/pass_info', methods=["GET", "POST"])
@user_login_data
def pass_info():
    return render_template('news/user_pass_info.html')
```

- 修改 `news/user.html` 中密码修改的链接

```html
<li><a href="{{ url_for('profile.pass_info') }}" target="main_frame">密码修改</a></li>
```

- # 后端接口实现

- ## 接口设计

- URL：/user/pass_info

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名       | 类型   | 是否必须 | 参数说明 |
| ------------ | ------ | -------- | -------- |
| old_password | string | 是       | 旧密码   |
| new_password | string | 是       | 新密码   |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 代码实现

- 在 `profile/views.py` 

```python
@profile_blu.route('/pass_info', methods=["GET", "POST"])
@user_login_data
def pass_info():
    # GET请求,返回
    if request.method == "GET":
        return render_template('news/user_pass_info.html')

    # 1. 获取参数


    # 2. 校验参数

    # 3. 判断旧密码是否正确


    # 4. 设置新密码

    # 返回


```

- # 前端逻辑实现

- `user_pass_info.js` 

```js
$(function () {
    $(".pass_info").submit(function (e) {
        e.preventDefault();

        // 修改密码
        var params = {};
        $(this).serializeArray().map(function (x) {
            params[x.name] = x.value;
        });
        // 取到两次密码进行判断
        var new_password = params["new_password"];
        var new_password2 = params["new_password2"];

        if (new_password != new_password2) {
            alert('两次密码输入不一致')
            return
        }

        $.ajax({
            url: "/user/pass_info",
            type: "post",
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            success: function (resp) {
                if (resp.errno == "0") {
                    // 修改成功
                    alert("修改成功")
                    window.location.reload()
                } else {
                    alert(resp.errmsg)
                }
            }
        })
    })
})
```

### 6.5-新闻收藏

- ## 需求分析

- 使用分页的形式展示用户所收藏的新闻

- 可以使用 url 的查询字符串传入不同的页数进行模板渲染不同的数据

- ## 模板渲染

- 将 `static/news/user_collection.html` 拖动到模板文件夹下的 `news` 文件夹内

- `profile/views.py` 测试模块

```python
@profile_blu.route('/collection')
@user_login_data
def user_collection():
    return render_template('news/user_collection.html')
```

- 修改 `news/user.html` 中我的收藏的链接

```html
<li><a href="{{ url_for('profile.user_collection') }}" target="main_frame">我的收藏</a></li>
```

- # 数据加载及模板显示

- ## 收藏数据加载

- 对用户收藏的新闻进行分页返回，默认返回第1页

  - 返回的数据中要告诉前端 总页数、当前页数

```python
@profile_blu.route('/collection')
@user_login_data
def user_collection():
    # 1. 获取参数

    # 2. 判断参数


    # 3. 查询用户指定页数的收藏的新闻

        # 进行分页数据查询

        # 当前页数
        # 总页数
        # 总数据


    # 收藏列表


	# 返回数据


```

- ## 前端模板展示

```html
    <div class="my_collect">
        <h3>我的收藏</h3>
        <ul class="article_list">
            {% for news in data.collections %}
                <li><a href="/news/{{ news.id }}" target="_blank">{{ news.title }}</a><span>{{ news.create_time }}</span></li>
            {% endfor %}
        </ul>

        <div id="pagination" class="page"></div>
        <script>
            $(function() {
                $("#pagination").pagination({
                    currentPage: {{ data.current_page }},
                    totalPage: {{ data.total_page }},
                    callback: function(current) {
                        window.location.href = "/user/collection?p=" + current
                    }
                });
            });
        </script>

    </div>
```



### 6.6-发布新闻

- ## 需求分析（20190722）

- 用户可以在个人中心发布新闻

- 发布完毕新闻需要通过审核才能显示

- 用户发布完新闻跳转到用户新闻列表

- 后台管理员对新闻进行审核

- 如果某条新闻是用户发布的，那么在新闻详情页展示该用户的个人资料

- ## 模板渲染


- `user_news_release.html` 

```html
<form class="release_form">
    <h3>新闻发布</h3>
    <div class="form-group"><label>新闻标题：</label><input type="text" class="input_txt2"></div>
    <div class="form-group">
        <label>新闻分类：</label>
        <select class="sel_opt">
            {% for category in data.categories %}
                <option value="{{ category.id }}">{{ category.name }}</option>
            {% endfor %}
        </select>
    </div>
    ...
</form>
```

- 修改 `news/user.html` 中新闻发布的链接

```html
<li><a href="{{ url_for('profile.news_release') }}" target="main_frame">新闻发布</a></li>
```

- # 后端接口实现

- ## 接口设计

- URL：/user/news_release

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名      | 类型   | 是否必须 | 参数说明    |
| ----------- | ------ | -------- | ----------- |
| title       | string | 是       | 新闻标题    |
| category_id | int    | 是       | 新闻分类_id |
| digest      | string | 是       | 新闻摘要    |
| index_image | file   | 是       | 索引图片    |
| content     | string | 是       | 新闻内容    |
| source      | string | s是      | 新闻来源    |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 代码实现

- 将 `static/news/user_news_release.html` 拖动到模板文件夹下的 `news` 文件夹内

- `profile/views.py`

```python
@profile_blu.route('/news_release', methods=["GET", "POST"])
@user_login_data
def news_release():
    # GET请求
        # 1. 加载新闻分类数据

        # 2. 移除最新分类
        
		# 返回数据

    # 1. 获取要提交的数据


    # 校验参数


    # 3.取到图片，将图片上传到七牛云
    try:
        index_image_data = index_image.read()
        # 上传到七牛云
        key = storage(index_image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数有误")

    # 保存数据

    # 新闻状态,将新闻设置为1代表待审核状态
    news.status = 1

    # 手动设置新闻状态,在返回前commit提交

	# 返回

```

- # 前端逻辑实现

- `user_news_release.js`

```js
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function () {

    $(".release_form").submit(function (e) {
        e.preventDefault()

        // 发布新闻
        $(this).ajaxSubmit({
            url: "/profile/news_release",
            type: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    // 选中索引为6的左边单菜单
                    window.parent.fnChangeMenu(6)
                    // 滚动到顶部
                    window.parent.scrollTo(0, 0)
                }else {
                    alert(resp.errmsg)
                }
            }
        })
    })
})
```

- 修改首页新闻列表数据查询逻辑，在 `index/views.py` 文件中，修改 `get_news_list` 函数逻辑，添加`已审核通过`的条件

```python
@index_blu.route('/newslist')
def get_news_list():
    ...
    # 3. 查询数据并分页
    filters = [News.status == 0]
    # 如果分类id不为0，那么添加分类id的过滤
    if category_id != "0":
        filters.append(News.category_id == category_id)
    ...;
```

### 6.7-新闻列表

- ## 需求分析

- 进行到页面之后加载当前用户发布的所有新闻

- 分页展示，以时间倒序排序

- 显示新闻当前的状态，如果未通过审核，需要显示相关原因

- ## 模板渲染

- 将 `static/news/user_news_list.html` 拖动到模板文件夹下的 `news` 文件夹内

- `profile/views.py` 测试模块

```python
@profile_blu.route('/news_list')
@user_login_data
def user_news_list():
    return render_template('news/user_news_list.html')
```

- `news/user.html`

```html
<li><a href="{{ url_for('profile.user_news_list') }}" target="main_frame">新闻列表</a></li>
```

- # 数据加载及模板显示

- ## 新闻列表数据加载

- 对用户发布的新闻进行分页返回，默认返回第1页

  - 返回的数据中要告诉前端 总页数、当前页数

```python
@profile_blu.route('/news_list')
@user_login_data
def user_news_list():
	# 查询数据

    # 返回数据



```

- ## 前端模板展示

```html
<div class="news_list">
    <h3>新闻列表</h3>
    <ul class="article_list">
        {% for news in data.news_list %}
            <li>
            {% if news.status == 0 %}
                {# 审核通过 #}
                <a href="/news/{{ news.id }}">{{ news.title }}</a><em class="pass">已通过</em><span>{{ news.create_time }}</span>
            {% elif news.status == 1 %}
                {# 审核中 #}
                <a href="javascript:;">{{ news.title }}</a><em class="review">审核中</em><span>{{ news.create_time }}</span>
            {% else %}
                {# 审核不通过 #}
                <a href="javascript:;">{{ news.title }}</a><em class="nopass">未通过</em><span>{{ news.create_time }}</span>
                <b>未通过原因：{{ news.reason }}</b>
            {% endif %}
            </li>
        {% endfor %}
    </ul>
    <div id="pagination" class="page"></div>
    <script>
        $(function(){
            $("#pagination").pagination({
                currentPage: {{ data.current_page }},
                totalPage: {{ data.total_page }},
                callback: function(current) {
                    window.location.href = '/user/news_list?p=' + current
                }
            });
        });
    </script>
</div>
```

## 7.404页面处理

- 需求：在用户访问一些不存在网址的时候弹出404页面

- 实现逻辑：可以使用 app.errorhandle(code_or_exception) 装饰器

- ## 代码实现

- 将 `static/news/404.html` 文件拖到 `templates/news/` 目录下，并继承于基类模板

```html
{% extends 'news/base.html' %}
{% block titleBlock %}
404
{% endblock %}

{% block contentBlock %}
    <div class="error_con">
        <img src="../../static/news/images/not_found.png" alt="404">
        <h3>OOPS!</h3>
        <h4>该内容不存在</h4>
        <p>请检查你输入的网址是否正确，请点击以下按钮返回主页或者发送错误报告</p>
        <a href="/">返回首页</a>
    </div>
{% endblock %}

{% block rankBlock %}
{% endblock %}

{% block bottomBlock %}
{% endblock %}
```

- 404页面时全局生效的,所以在 `info/__init__.py` 文件中的 `create_app` 函数中添加404业务逻辑

```python
def create_app(config_name):
    ...

    @app.errorhandler(404)
    @user_login_data
    def page_not_found(_):
        user = g.user
        data = {"user": user.to_dict() if user else None}
        return render_template('news/404.html', data=data)
```

## 8.新闻详情页用户信息

- ## 需求

- 如果新闻是由用户发布的，需要在详情页显示用户的相关信息

- 并且可以点击 关注/取消关注 对该新闻用户信息进行关注

- 如果当前用户已登录，打开某条用户的新闻，需要显示是否关注过该用户

- ## 代码实现

- 在 `news/detail.html` 

```html
{% block authorblock %}
    {% if data.news.author %}
        <div class="author_card">
            <a href="#" class="author_pic"><img src="{% if data.news.author.avatar_url %}
            {{ data.news.author.avatar_url }}
            {% else %}
            ../../static/news/images/user_pic.png
            {% endif %}" alt="author_pic"></a>
            <a href="#" class="author_name">{{ data.news.author.nick_name }}</a>
            <div class="author_resume">签名：{{ data.news.author.signature }}</div>
            <div class="writings"><span>总篇数</span><b>{{ data.news.author.news_count }}</b></div>
            <div class="follows"><span>粉丝</span><b>{{ data.news.author.followers_count }}</b></div>
            <a href="javascript:;" class="focus fr" data-userid="{{ data.news.author.id }}"
               style="display: {% if data.is_followed %}none{% else %}block{% endif %}">关注</a>
            <a href="javascript:;" class="focused fr" data-userid="{{ data.news.author.id }}"
               style="display: {% if data.is_followed %}block{% else %}none{% endif %}"><span
                    class="out">已关注</span><span class="over">取消关注</span></a>
        </div>
    {% endif %}
{% endblock %}
```

- 在新闻详情`news/views.py`视图函数中中，添加是否关注当前用户

```python
news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):

    ...

    # 当前登录用户是否关注当前新闻作者
    is_followed = False
    # 判断用户是否收藏过该新闻
    if news.user and user:
        if news.user in user.followed:
            is_followed = True

    data = {
        'news': news.to_dict(),
        'news_dict': news_dict,
        'is_followed': is_followed,
        'is_collected': is_collected,
        'comments': comment_dict_list,
        "user": user.to_dict() if user else None
    }
    return render_template('news/detail.html', data=data)
```

## 9.关注与取消关注

- ## 接口设计

- URL：/news/followed_user

- 请求方式：POST

- 传入参数：JSON格式

- 参数

| 参数名  | 类型   | 是否必须 | 参数说明                         |
| ------- | ------ | -------- | -------------------------------- |
| user_id | int    | 是       | 被关注的用户id                   |
| action  | string | 是       | 指定两个值：'follow', 'unfollow' |

- 返回类型：JSON

| 参数名 | 类型   | 是否必须 | 参数说明 |
| ------ | ------ | -------- | -------- |
| errno  | int    | 是       | 错误码   |
| errmsg | string | 是       | 错误信息 |

- ## 代码实现

- `news/views.py` 

```python
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
    action = request.json.get("action")

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
```

- 在 `detail.js` 中实现关注与取消关注的请求

```js
// 关注当前新闻作者
$(".focus").click(function () {
    var user_id = $(this).attr('data-userid')
    var params = {
        "action": "follow",
        "user_id": user_id
    }
    $.ajax({
        url: "/news/followed_user",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        data: JSON.stringify(params),
        success: function (resp) {
            if (resp.errno == "0") {
                // 关注成功
                var count = parseInt($(".follows b").html());
                count++;
                $(".follows b").html(count + "")
                $(".focus").hide()
                $(".focused").show()
            }else if (resp.errno == "4101"){
                // 未登录，弹出登录框
                $('.login_form_con').show();
            }else {
                // 关注失败
                alert(resp.errmsg)
            }
        }
    })
})

// 取消关注当前新闻作者
$(".focused").click(function () {
    var user_id = $(this).attr('data-userid')
    var params = {
        "action": "unfollow",
        "user_id": user_id
    }
    $.ajax({
        url: "/news/followed_user",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        data: JSON.stringify(params),
        success: function (resp) {
            if (resp.errno == "0") {
                // 取消关注成功
                var count = parseInt($(".follows b").html());
                count--;
                $(".follows b").html(count + "")
                $(".focus").show()
                $(".focused").hide()
            }else if (resp.errno == "4101"){
                // 未登录，弹出登录框
                $('.login_form_con').show();
            }else {
                // 取消关注失败
                alert(resp.errmsg)
            }
        }
    })
})
```

## 10.我的关注

- ## 需求分析

- 在个人页面点击 `我的关注` 需要以分页的形式展示当前用户关注的其他用户

- 可以进行取消关注

- 点击进行到作者详情页面

- ## 实现准备

- 将 `static/news/user_follow.html` 拖到 `templates/news/` 目录下

- ## 代码实现

- `/profile/views.py` 

```python
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
        paginate = user.followed.paginate(p, constants.USER_FOLLOWED_MAX_COUNT, False)
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
    data = {"users": user_dict_li, "total_page": total_page, "current_page": current_page}
    return render_template('news/user_follow.html', data=data)
```

- `user_follow.html`

```html
<ul class="card_list_con">

    {% for user in data.users %}
        <li class="author_card card_list">
            <a href="#" class="author_pic"><img src="{% if user.avatar_url %}
            {{ user.avatar_url }}
            {% else %}
            ../../static/news/images/user_pic.png
            {% endif %}" alt="author_pic"></a>
            <a href="#" class="author_name">{{ user.nick_name }}</a>
            <div class="author_resume">{{ user.signature }}</div>
            <div class="writings"><span>总篇数</span><b>{{ user.news_count }}</b></div>
            <div class="follows"><span>粉丝</span><b>{{ user.followers_count }}</b></div>
            <a href="javascript:;" class="focused fr" data-userid="{{ user.id }}"><span class="out">已关注</span><span class="over">取消关注</span></a>
        </li>
    {% endfor %}
</ul>
<div id="pagination" class="page"></div>
<script>
    $(function() {
        $("#pagination").pagination({
            currentPage: {{ data.current_page }},
            totalPage: {{ data.total_page }},
            callback: function(current) {
                window.location = "/user/user_follow?p=" + current
            }
        });
    });
</script>
```

## 11.其他用户界面

- ## 需求

- 从新闻详情页面的作者信息和我的关注的用户列表可以进入其他用户信息界面

- 进入界面之后展示用户的个人信息以及其发布的新闻列表信息

- ## 实现准备

- 将 `static/news/other.html` 拖到 `templates/news` 目录下

- 继承基类模板，抽取相关代码

- ## 代码实现

- `profile/views.py` 

```python
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
        "user": g.user.to_dict() if g.user else None,
        "other_info": other.to_dict()
    }
    return render_template('news/other.html', data=data)
```

- `news/other.html`

```html
{% extends 'news/base.html' %}

{% block titleBlock %}
    用户概况
{% endblock %}

{% block cssBlock %}
    <link rel="stylesheet" type="text/css" href="../../static/news/css/jquery.pagination.css">
{% endblock %}

{% block scriptBlock %}
    <script type="text/javascript" src="../../static/news/js/other.js"></script>
    <script type="text/javascript" src="../../static/news/js/jquery.pagination.min.js"></script>
{% endblock %}

{% block contentblock %}
    <div class="user_menu_con fl">
        <div class="user_center_pic">
            <img src="{% if data.other_info.avatar_url %}
    {{ data.other_info.avatar_url }}
    {% else %}
    ../../static/news/images/user_pic.png
    {% endif %}" alt="用户图片">
        </div>
        <div class="user_center_name">{{ data.other_info.nick_name }}</div>

        <ul class="other_detail">
            <li>性 别：{% if data.other_info.gender == "MAN" %}男
            {% else %}女
            {% endif %}
            </li>
            <li>签 名：{% if data.other_info.signature %}
                {{ data.other_info.signature }}
            {% else %}
                这个人很懒，什么都没留下
            {% endif %}</li>
        </ul>

        <div class="focus_other">
            <a href="javascript:;" class="focus block-center" data-userid="{{ data.other_info.id }}"
               style="display: {% if data.is_followed %}none
               {% else %}block
               {% endif %}">关注</a><br>
            <a href="javascript:;" class="focused block-center" data-userid="{{ data.other_info.id }}"
               style="display: {% if data.is_followed %}block
               {% else %}none
               {% endif %}"><span class="out">已关注</span><span class="over">取消关注</span></a>
        </div>

    </div>

    <div class="user_con fr">
        <div class="other_collect">
            <h3>他的文章</h3>
            <ul class="article_list">
                <li><a href="#">智能音箱“不智能”：这次轮到三星语音助手Bixby被吐槽了</a><span>2018-1-17</span></li>
                <li><a href="#">智能音箱“不智能”：这次轮到三星语音助手Bixby被吐槽了</a><span>2018-1-17</span></li>
                <li><a href="#">智能音箱“不智能”：这次轮到三星语音助手Bixby被吐槽了</a><span>2018-1-17</span></li>
                <li><a href="#">智能音箱“不智能”：这次轮到三星语音助手Bixby被吐槽了</a><span>2018-1-17</span></li>
                <li><a href="#">智能音箱“不智能”：这次轮到三星语音助手Bixby被吐槽了</a><span>2018-1-17</span></li>
                <li><a href="#">智能音箱“不智能”：这次轮到三星语音助手Bixby被吐槽了</a><span>2018-1-17</span></li>
            </ul>

            <div id="pagination" class="page"></div>
            <script>
                $(function () {
                    $("#pagination").pagination({
                        currentPage: 2,
                        totalPage: 3,
                        callback: function (current) {
                            getNewsList(current)
                        }
                    });
                });
            </script>
        </div>

    </div>
{% endblock %}
```

- `profile/views.py`

```python
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
        paginate = other.news_list.paginate(page, constants.USER_COLLECTION_MAX_NEWS, False)
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

```

- `news/other.js` 

```js
function getNewsList(page) {
    var query = decodeQuery()
    var params = {
        "p": page,
        "user_id": query["id"]
    }
    $.get("/user/other_news_list", params, function (resp) {
        if (resp.errno == "0") {
            // 先清空原有的数据
            $(".article_list").html("");
            // 拼接数据
            for (var i = 0; i<resp.data.news_list.length; i++) {
                var news = resp.data.news_list[i];
                var html = '<li><a href="/news/'+ news.id +'" target="_blank">' + news.title + '</a><span>' + news.create_time + '</span></li>'
                // 添加数据
                $(".article_list").append(html)
            }
            // 设置页数和总页数
            $("#pagination").pagination("setPage", resp.data.current_page, resp.data.total_page);
        }else {
            alert(resp.errmsg)
        }
    })
}
```

## 12.新闻后台

### 12.1-创建管理员账户

- `manage.py`添加创建管理员业务逻辑

```python
# 通过命令行创建管理员账号
@manager.option('-n', '-name', dest="name")
@manager.option('-p', '-password', dest="password")
def createsuperuser(name, password):
    if not all([name, password]):
        print("参数不足")

    user = User()
    user.nick_name = name
    user.mobile = name
    user.password = password
    user.is_admin = True

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    print("添加成功")
```

- 在命令行执行

```bash
python manage.py createsuperuser -u 账号 -p 密码
```

### 12.2-管理员登录/登出

- ### 需求分析

- 管理员用户进行登录，并且根据不同的情况报出不同的错误信息

- 如果登录用户是管理员，则直接跳转到后台管理主页

- 

- ### 代码准备

- 在 **templates** 目录下创建 `admin` 文件夹，将 `static/admin/`目录下 `login.html` 与 `index.html` 拖动到 `admin` 目录下

- ### 登陆后端代码实现

- `admin/views.py` 

```python
@admin_blu.route('/index')
def index():
    return render_template('admin/index.html')


@admin_blu.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('admin/login.html')

    # 获取登录参数
    username = request.form.get("username")
    password = request.form.get("password")
    if not all([username, password]):
        return render_template('admin/login.html', errmsg="参数不足")

    try:
        user = User.query.filter(User.mobile == username).first()
    except Exception as e:
        current_app.logger.error(e)
        return render_template('admin/login.html', errmsg="数据查询失败")

    if not user:
        return render_template('admin/login.html', errmsg="用户不存在")

    if not user.check_password(password):
        return render_template('admin/login.html', errmsg="密码错误")

    if not user.is_admin:
        return render_template('admin/login.html', errmsg="用户权限错误")

    session["user_id"] = user.id
    session["nick_name"] = user.nick_name
    session["mobile"] = user.mobile
    session["is_admin"] = True

    # 跳转到后台管理主页
    return redirect(url_for('admin.index'))
```

- ### 前端代码

- `login.html`

```html
	<form method="post" class="login_form">
		<h1 class="login_title">用户登录</h1>
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
		<input type="text" name="username" placeholder="用户名" class="input_txt">
		<input type="password" name="password" placeholder="密码" class="input_txt">
        {% if errmsg %}
            <div class="error_tip" style="display: block">{{ errmsg }}</div>
        {% endif %}
		<input type="submit" value="登 录" class="input_sub">
	</form>
```

- ## 登出后端代码实现

- `admin/views.py`

```python
@admin_blu.route("/logout", methods=['POST'])
def logout():
    """
    清除session中的对应登录之后保存的信息
    :return:
    """
    session.pop('user_id', None)
    session.pop('nick_name', None)
    session.pop('mobile', None)
    session.pop('is_admin', None)

    # 返回结果
    return jsonify(errno=RET.OK, errmsg="OK")
```

- ## 登出前端代码实现

- `user_list.html`

```html
	<script type="text/javascript" src="../../static/admin/js/main.js"></script>

......

<div class="header">
   <a href="#" class="logo fl"><img src="../../static/admin/images/logo.png" alt="logo"></a>
   <a href="javascript:;" class="logout fr" onclick="logout()">退 出</a>
</div>
```

- 在`static/admin/js`文件中创建`main.js`

```javascript
function logout() {
    $.ajax({
        url: "/admin/logout",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        success: function (resp) {
            // 刷新当前界面
            location.reload()
        }
    })
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
```

### 12.3-后台访问权限控制

- ### 需求

- 解决普通用户登录之后访问管理员后台

- 如果是普通用户访问后台的视图函数，直接跳转到主页

- 统一判断管理员入口，除了登录页面，后台的其他页面都要判断是否具有管理员权限

- ### 代码实现

- 在 `modules/admin/__init__.py` 文件中，添加请求勾子函数

```python
@admin_blu.before_request
def check_admin():
    # 限制非管理员访问管理员页面
    is_admin = session.get('is_admin', False)
    if not is_admin and not request.url.endswith(url_for('admin.login')):
        return redirect('/')
```

### 12.4-添加测试用户

- 在项目跟目录下添加`test_users.py`,并执行代码为数据库添加1000个测试用户

```python
def add_test_users():
    users = []
    now = datetime.datetime.now()
    for num in range(0, 10000):
        try:
            user = User()
            user.nick_name = "%011d" % num
            user.mobile = "%011d" % num
            user.password_hash = "pbkdf2:sha256:50000$SgZPAbEj$a253b9220b7a916e03bf27119d401c48ff4a1c81d7e00644e0aaf6f3a8c55829"
            user.last_login = now - datetime.timedelta(seconds=random.randint(0, 2678400))
            users.append(user)
            print(user.mobile)
        except Exception as e:
            print(e)
    with app.app_context():
        db.session.add_all(users)
        db.session.commit()
    print 'OK'
```

### 12.5-用户管理

#### 1.1-用户统计

- ### 需求分析

- 展示当前总人数，月活跃人数，日活跃人数

- 使用图表的形式展示活跃曲线

- ### 后端实现

- `admin/views.py`

```python
@admin_blu.route('/user_count')
def user_count():
        # 总人数
    total_count = 0
    try:
        total_count = User.query.filter(User.is_admin == False).count()
    except Exception as e:
        current_app.logger.error(e)

    # 月新增数
    mon_count = 0
    t = time.localtime()
    begin_mon_date_str = '%d-%02d-01' % (t.tm_year, t.tm_mon)
    # 将字符串转成datetime对象
    begin_mon_date = datetime.strptime(begin_mon_date_str, "%Y-%m-%d")
    try:
        mon_count = User.query.filter(User.is_admin == False, User.create_time > begin_mon_date).count()
    except Exception as e:
        current_app.logger.error(e)

    # 日新增数
    day_count = 0
    begin_day_date = datetime.strptime(('%d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)), "%Y-%m-%d")
    try:
        day_count = User.query.filter(User.is_admin == False, User.create_time > begin_day_date).count()
    except Exception as e:
        current_app.logger.error(e)

    # 拆线图数据

    active_time = []
    active_count = []

    # 取到今天的时间字符串
    today_date_str = ('%d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday))
    # 转成时间对象
    today_date = datetime.strptime(today_date_str, "%Y-%m-%d")

    for i in range(0, 31):
        # 取到某一天的0点0分
        begin_date = today_date - timedelta(days=i)
        # 取到下一天的0点0分
        end_date = today_date - timedelta(days=(i - 1))
        count = User.query.filter(User.is_admin == False, User.last_login >= begin_date,
                                  User.last_login < end_date).count()
        active_count.append(count)
        active_time.append(begin_date.strftime('%Y-%m-%d'))

    # User.query.filter(User.is_admin == False, User.last_login >= 今天0点0分, User.last_login < 今天24点).count()

    # 反转，让最近的一天显示在最后
    active_time.reverse()
    active_count.reverse()

    data = {
        "total_count": total_count,
        "mon_count": mon_count,
        "day_count": day_count,
        "active_time": active_time,
        "active_count": active_count
    }

    return render_template('admin/user_count.html', data=data)
```

- ### 前端实现

- 将 `static/admin/`目录下 `user_count.html` 拖动到 `admin` 目录下

- `user_count.html`

```javascript
......
<div class="spannels">
   <div class="spannel scolor01">
      <em>{{ data.total_count }}</em><span>人</span>
      <b>用户总数</b>
   </div>
   <div class="spannel scolor02">
      <em>{{ data.mon_count }}</em><span>人</span>
      <b>用户月新增数</b>
   </div>
   <div class="spannel2 scolor03">
      <em>{{ data.day_count }}</em><span>人</span>
      <b>用户日新增数</b>
   </div>    
</div>
......
					    xAxis : [
					        {
		                        name: '今天',
					            type : 'category',
					            boundaryGap : false,
					            data : {{ data.active_time | safe}}
					        }
					    ],        
					    yAxis : [
					        {
		                        name: '活跃用户数量',
					            type : 'value'
					        }
					    ],      
					    series : [
					        {
					            name:'active',
					            type:'line',
					            smooth:true,
					            itemStyle: {normal: {areaStyle: {type: 'default'}, color: '#f80'}, lineStyle: {color: '#f80'}},
					            data:{{ data.active_count | safe }}
					        }],
                            ......
                        
```

#### 1.2-用户列表

- ### 需求

- 按用户最后一次登录倒序分页展示用户列表

- ### 后端实现

- `admin/views.py`

```python
@admin_blu.route('/user_list')
def user_list():
    page = request.args.get("p", 1)

    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1

    users = []
    current_page = 1
    total_page = 1

    try:
        paginate = User.query.filter(User.is_admin == False).order_by(User.last_login.desc()).paginate(page,
                                                                                                       constants.ADMIN_USER_PAGE_MAX_COUNT,
                                                                                                       False)
        users = paginate.items
        current_page = paginate.page
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    # 进行模型列表转字典列表
    user_dict_list = []
    for user in users:
        user_dict_list.append(user.to_admin_dict())

    data = {
        "users": user_dict_list,
        "total_page": total_page,
        "current_page": current_page,
    }

    return render_template('admin/user_list.html', data=data)

```

- ### 前端实现

- 将 `static/admin/`目录下 `user_list.html` 拖动到 `admin` 目录下

- `user_list.html`

```html
<div class="pannel">
    <table class="common_table">
        <tr>
            <th>用户名</th>
            <th>电话</th>
            <th>注册时间</th>
            <th>上次登录时间</th>
        </tr>
        {% for user in data.users %}
        <tr>
            <td>{{ user.nick_name }}</td>
            <td>{{ user.mobile }}</td>
            <td>{{ user.register }}</td>
            <td>{{ user.last_login }}</td>
        </tr>
        {% endfor %}
    </table>
</div>

<div class="box">
    <div id="pagination" class="page"></div>
</div>

<script>
    $(function() {
        $("#pagination").pagination({
            currentPage: {{ data.current_page }},
            totalPage: {{ data.total_page }},
            callback: function(current) {
                window.location.href = '/admin/user_list?p=' + current
            }
        });
    });
</script>
```

### 12.6-新闻管理

#### 1.1-新闻审核

- ### 需求分析

- 以分页的形式按新闻创建时间倒序展示出待审核的新闻数据

- 可以使用关键字对新闻标题进行搜索

- 点击审核进入审核详情页面(对新闻只能查看不能编辑)

- 审核不通过需要写明不通过原因

- ### 实现准备

- 将 `static/admin/` 目录下的 `news_review.html`和`news_review_detail.html` 拖到 `templates/admin/` 目录下

- ### 后端代码实现

- `admin/views.py` 

```python
@admin_blu.route('/news_review')
def news_review():
    page = request.args.get("p", 1)
    # 获取搜索框关键字
    keywords = request.args.get("keywords", None)
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1

    news_list = []
    current_page = 1
    total_page = 1

    filters = [News.status != 0]
    # 如果关键字存在，那么就添加关键字搜索
    if keywords:
        filters.append(News.title.contains(keywords))
    try:
        paginate = News.query.filter(*filters) \
            .order_by(News.create_time.desc()) \
            .paginate(page, constants.ADMIN_NEWS_PAGE_MAX_COUNT, False)

        news_list = paginate.items
        current_page = paginate.page
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    news_dict_list = []
    for news in news_list:
        news_dict_list.append(news.to_review_dict())

    context = {
        "total_page": total_page,
        "current_page": current_page,
        "news_list": news_dict_list
    }

    return render_template('admin/news_review.html', data=context)
```

- ### 前端代码实现

- `admin/news_review.html`

```html
<div class="pannel">
    <table class="common_table">
        <tr>
            <th width="3%">id</th>
            <th width="70%">标题</th>
            <th width="15%">发布时间</th>
            <th width="5%">状态</th>
            <th width="8%">管理操作</th>
        </tr>
        {% for news in data.news_list %}
            <tr>
                <td>{{ news.id }}</td>
                <td class="tleft">{{ news.title }}</td>
                <td>{{ news.create_time }}</td>
                <td>{% if news.status == 0 %}
                    已通过
                {% elif news.status == -1 %}
                    未通过
                {% else %}
                    未审核
                {% endif %}</td>
                <td>
                    <a href="{{ url_for("admin.news_review_detail", news_id=news.id) }}" class="review">审核</a>
                </td>
            </tr>
        {% endfor %}
    </table>
</div>

<div class="box">
    <div id="pagination" class="page"></div>
</div>

<script>
    $(function () {
        $("#pagination").pagination({
            currentPage: {{ data.current_page }},
            totalPage: {{ data.total_page }},
            callback: function (current) {
                window.location = '/admin/news_review?p=' + current
            }
        });
    });
</script>
```

- 添加前端 Form 表单中 input 的 name 属性

```html
<form class="news_filter_form">
    <input name="keywords" type="text" placeholder="请输入关键字" class="input_txt">
    <input type="submit" value="搜 索" class="input_sub">
</form>
```

- ### 审核详情界面数据

- 在 `admin/views.py` 中添加新闻审核详情视图函数，接收新闻id为参数

```python
@admin_blu.route('/news_review_detail/<int:news_id>')
def news_review_detail(news_id):
    # 通过id查询新闻
    news = None
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)

    if not news:
        return render_template('admin/news_review_detail.html', data={"errmsg": "未查询到此新闻"})

    # 返回数据
    data = {
        "news": news.to_dict()
    }
    return render_template('admin/news_review_detail.html', data=data)
```

- `news_review.html`

```html
<td>
    <a href="{{ url_for('admin.news_review_detail') }}?news_id={{ news.id }}" class="review">审核</a>
</td>
```

- `news_review_detail.html` 

```html
<div class="form_group">
    <label>新闻标题：</label>
    <input type="text" class="input_txt2" value="{{ data.news.title }}" readonly>
</div>
<div class="form_group">
        <label>新闻分类：</label>
        <div class="category_name">{{ data.news.category.name }}</div>
</div>
<div class="form_group">
    <label>新闻摘要：</label>
    <textarea class="input_multxt" readonly>{{ data.news.digest }}</textarea>
</div>
<div class="form_group">
    <label>索引图片：</label>
    <img src="{{ data.news.index_image_url }}" alt="索引图片" class="index_pic">
</div>
<div class="form_group">
    <label>新闻内容：</label>
    <div class="rich_wrap fl">
        <input class="input_area" id="rich_content" name="content" value="{{ data.news.content }}"></input>
    </div>
</div>

...
<!-- 隐藏字段，用于记录当前新闻id -->
<input name="news_id" value="{{ data.news.id }}" hidden>
```

- ### 新闻审核详情页

- `admin/views.py`

```python
@admin_blu.route('/news_review_action', methods=["POST"])
def news_review_action():
    # 接受参数
    news_id = request.json.get("news_id")
    action = request.json.get("action")

    # 参数校验
    if not all([news_id, action]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    if action not in ("accept", "reject"):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 查询到指定的新闻数据
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询失败")

    if not news:
        return jsonify(errno=RET.NODATA, errmsg="未查询到数据")

    if action == "accept":
        # 代表接受
        news.status = 0
    else:
        # 代表拒绝
        reason = request.json.get("reason")
        if not reason:
            return jsonify(errno=RET.PARAMERR, errmsg="请输入拒绝原因")
        news.status = -1
        news.reason = reason

    return jsonify(errno=RET.OK, errmsg="OK")
```

- `/news_review_detail.js` 

```js
$(".news_review").submit(function (e) {
    e.preventDefault()

    var params = {};
    // 获取到所有的参数
    $(this).serializeArray().map(function (x) {
        params[x.name] = x.value;
    });
    // 取到参数以便判断
    var action = params["action"];
    var news_id = params["news_id"];
    var reason = params["reason"];
    if (action == "reject" && !reason) {
        alert('请输入拒绝原因');
        return;
    }
    params = {
        "action": action,
        "news_id": news_id,
        "reason": reason
    }
    $.ajax({
        url: "/admin/news_review_detail",
        type: "post",
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        data: JSON.stringify(params),
        success: function (resp) {
            if (resp.errno == "0") {
                // 返回上一页，刷新数据
                location.href = document.referrer;
            }else {
                alert(resp.errmsg);
            }
        }
    })
})
```

#### 1.2-新闻版式编辑详情

- ### 需求分析

- 以分页的形式按新闻创建时间倒序展示出新闻数据

- 可以使用关键这这对新闻标题进行搜索

- 点击编辑进入编辑详情页面

- ### 实现准备

- 将 `static/admin/` 目录下的 `news_edit.html` 以及 `news_edit_detail.html` 拖到 `templates/admin/`目录下

- ### 后端代码实现

- `admin/views.py` 

```python
@admin_blu.route('/news_edit')
def news_edit():
    """新闻编辑"""
    page = request.args.get("p", 1)
    keywords = request.args.get("keywords", None)
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1

    news_list = []
    current_page = 1
    total_page = 1

    filters = [News.status == 0]
    # 如果关键字存在，那么就添加关键字搜索
    if keywords:
        filters.append(News.title.contains(keywords))
    try:
        paginate = News.query.filter(*filters) \
            .order_by(News.create_time.desc()) \
            .paginate(page, constants.ADMIN_NEWS_PAGE_MAX_COUNT, False)

        news_list = paginate.items
        current_page = paginate.page
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    news_dict_list = []
    for news in news_list:
        news_dict_list.append(news.to_basic_dict())

    context = {"total_page": total_page, "current_page": current_page, "news_list": news_dict_list}

    return render_template('admin/news_edit.html', data=context)
```

- ### 前端代码实现

- `admin/news_edit.html`

```html
<div class="pannel">            
    <table class="common_table">
        <tr>
            <th width="5%">id</th>
            <th width="60%">标题</th>
            <th width="10%">点击量</th>
            <th width="15%">发布时间</th>
            <th width="10%">管理操作</th>
        </tr>
        {% for news in data.news_list %}
            <tr>
                <td>{{ news.id }}</td>
                <td class="tleft"><a href="/news/{{ news.id }}" target="_blank">{{ news.title }}</a></td>
                <td>{{ news.clicks }}</td>
                <td>{{ news.create_time }}</td>
                <td>
                    <a href="#" class="edit">编辑</a>
                </td>
            </tr>
        {% endfor %}
    </table>
</div>
...
<script>
    $(function() {
        $("#pagination").pagination({
            currentPage: {{ data.current_page }},
            totalPage: {{ data.total_page }},
            callback: function(current) {
                window.location = '/admin/news_edit?p=' + current
            }
        });
    });
</script>
```

- ## 编辑详情界面数据

- ### 新闻编辑提交

- `admin/views.py` 

```python
@admin_blu.route('/news_edit_detail', methods=["GET", "POST"])
def news_edit_detail():
    if request.method == "GET":
        # 查询点击的新闻的相关数据并传入到模板中
        news_id = request.args.get("news_id")

        if not news_id:
            abort(404)

        try:
            news_id = int(news_id)
        except Exception as e:
            current_app.logger.error(e)
            return render_template('admin/news_edit_detail.html', errmsg="参数错误")

        try:
            news = News.query.get(news_id)
        except Exception as e:
            current_app.logger.error(e)
            return render_template('admin/news_edit_detail.html', errmsg="查询数据错误")

        if not news:
            return render_template('admin/news_edit_detail.html', errmsg="未查询到数据")

        # 查询分类数据
        try:
            categories = Category.query.all()
        except Exception as e:
            current_app.logger.error(e)
            return render_template('admin/news_edit_detail.html', errmsg="查询数据错误")

        category_dict_list = []
        for category in categories:
            # 取到分类的字典
            cate_dict = category.to_dict()
            # 判断当前遍历到的分类是否是当前新闻的分类，如果是，则添加is_selected为true
            if category.id == news.category_id:
                cate_dict["is_selected"] = True
            category_dict_list.append(cate_dict)

        # 移除最新的分类
        category_dict_list.pop(0)

        data = {
            "news": news.to_dict(),
            "categories": category_dict_list
        }

        return render_template('admin/news_edit_detail.html', data=data)

    # 获取Post数据
    news_id = request.form.get("news_id")
    title = request.form.get("title")
    digest = request.form.get("digest")
    content = request.form.get("content")
    index_image = request.files.get("index_image")
    category_id = request.form.get("category_id")
    # 判断数据是否有值
    if not all([title, digest, content, category_id]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数有误")

    # 查询指定id的
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询失败")

    if not news:
        return jsonify(errno=RET.NODATA, errmsg="未查询到新闻数据")

    # 尝试读取图片
    if index_image:
        try:
            index_image = index_image.read()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.PARAMERR, errmsg="参数有误")

        # 将标题图片上传到七牛
        try:
            key = storage(index_image)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.THIRDERR, errmsg="上传图片错误")
        news.index_image_url = constants.QINIU_DOMIN_PREFIX + key

    # 设置相关数据
    news.title = title
    news.digest = digest
    news.content = content
    news.category_id = category_id

    return jsonify(errno=RET.OK, errmsg="OK")
```

- `news_review.html` 

```html
<td>
    <a href="{{ url_for('admin.news_edit_detail') }}?news_id={{ news.id }}" class="edit">编辑</a>
</td>
```

- `news_edit_detail.html` 

```html
<div class="form_group">
    <label>新闻标题：</label>
    <input name="title" type="text" class="input_txt2" value="{{ data.news.title }}">
</div>
<div class="form_group">
    <label>新闻分类：</label>
    <select class="sel_opt" name="category_id">
        {% for category in data.categories %}
            <option value="{{ category.id }}" {% if category.is_selected %}selected{% endif %}>{{ category.name }}</option>
        {% endfor %}
    </select>
</div>
<div class="form_group">
    <label>新闻摘要：</label>
    <textarea class="input_multxt" name="digest">{{ data.news.digest }}</textarea>
</div>
<div class="form_group">
    <label>索引图片：</label>
    <img src="{{ data.news.index_image_url }}" alt="索引图片" class="index_pic">
</div>
<div class="form_group">
    <label>上传图片：</label>
    <input type="file" name="index_image" class="input_file">
</div>
<div class="form_group">
    <label>新闻内容：</label>
    <div class="rich_wrap fl">
        <input class="input_area" id="rich_content" name="content" value="{{ data.news.content }}"></input>
    </div>
</div>
{# 添加隐藏字段新闻id #}
<input type="hidden" name="news_id" value="{{ data.news.id }}">
```

- `news_edit_detail.js` 

```js
$(function(){
    $(".news_edit").submit(function (e) {
        e.preventDefault()

        $(this).ajaxSubmit({
            beforeSubmit: function (request) {
                // 在提交之前，对参数进行处理
                for(var i=0; i<request.length; i++) {
                    var item = request[i]
                    if (item["name"] == "content") {
                        item["value"] = tinyMCE.activeEditor.getContent()
                    }
                }
            },
            url: "/admin/news_edit_detail",
            type: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    // 返回上一页，刷新数据
                    location.href = document.referrer;
                } else {
                    alert(resp.errmsg);
                }
            }
        })
    })
})
```

#### 1.3-新闻分类管理

- ### 需求

- 可以修改当前新闻分类名

- 可以添加新闻分类

- ### 实现准备

- 将 `static/admin/news_type.html` 文件拖到 `templates/admin/` 目录下

- ### 后端代码实现

- `admin/views.py` 

```python
@admin_blu.route('/news_type', methods=["GET", "POST"])
def news_type():
    if request.method == "GET":
        # 查询分类数据
        try:
            categories = Category.query.all()
        except Exception as e:
            current_app.logger.error(e)
            return render_template('admin/news_type.html', errmsg="查询数据错误")

        category_dict_li = []
        for category in categories:
            # 取到分类的字典
            cate_dict = category.to_dict()
            category_dict_li.append(cate_dict)

        # 移除最新的分类
        category_dict_li.pop(0)

        data = {
            "categories": category_dict_li
        }

        return render_template('admin/news_type.html', data=data)

    # 新增或者添加分类
    # 取参数
    cname = request.json.get("name")
    # 如果传了cid，代表是编辑已存在的分类
    cid = request.json.get("id")

    if not cname:
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    if cid:
        # 有分类id 代表查询相关数据
        try:
            cid = int(cid)
            category = Category.query.get(cid)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

        if not category:
            return jsonify(errno=RET.NODATA, errmsg="未查询到分类数据")
        category.name = cname
    else:
        category = Category()
        category.name = cname
        db.session.add(category)

    return jsonify(errno=RET.OK, errmsg="OK")
```

- `admin/news_type.html`

```html
<tr>
    <th width="10%">id</th>
    <th width="80%">类别名称</th>
    <th width="10%">管理操作</th>
</tr>

{% for category in data.categories %}
    <tr>
        <td>{{ category.id }}</td>
        <td>{{ category.name }}</td>
        <td><a href="javascript:;" class="edit">编辑</a></td>
    </tr>
{% endfor %}
```

- `news_type.js` 

```js
        // 发起修改分类请求
        $.ajax({
            url: "/admin/news_type",
            method: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function (resp) {
                if (resp.errno == "0") {
                    // 刷新当前界面
                    location.reload();
                } else {
                    $error.html(resp.errmsg).show();
                }
            }
        })
```

