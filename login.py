# coding:utf-8

from flask import Flask, render_template, redirect, url_for,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# 创建sqlalchemy的数据库链接对象
db = SQLAlchemy(app)


@app.route("/login", methods=["POST"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    if not all([username,password]):
        resp={
            "code":1,
            "message":"invalid params"
        }
        return jsonify(resp)

    if username=="admin" and password=="python":
        resp={
            "code":0,
            "message":"login success"
        }
        return jsonify(resp)
    else:
        resp={
            "code":2,
            "message":"login faild"
        }
        return jsonify(resp)



