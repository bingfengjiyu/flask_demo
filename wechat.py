# coding:utf-8
import hashlib

from flask import Flask, render_template, redirect, url_for
from flask import abort
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

WECHAT_TOKEN="itcast"

@app.route("/wechat8002", methods=["GET", "POST"])
def wechat():
    # 获取参数
    signature=request.args.get("signature")
    timestamp=request.args.get("timestamp")
    nonce=request.args.get("nonce")
    echostr=request.args.get("echostr")

    # 进行参数计算
    # 放入列表
    li=[WECHAT_TOKEN,timestamp,nonce]
    # 进行排序
    li.sort()
    # 拼接字符串
    tmp_str="".join(li)

    # 进行sha1加密
    sign=hashlib.sha1(tmp_str).hexdigest()

    if signature!=sign:
        abort(403)
    else:
        return echostr

    # 如果与微信传过来的参数相匹配,则返回echostr
    # 否则,报错


if __name__ == '__main__':
    app.run(port=8002)
