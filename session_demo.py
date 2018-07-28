# coding:utf-8

from flask import Flask,session

app=Flask(__name__)

app.config["SECRET_KEY"]="fwhfkwe214143490148jff"


@app.route("/login")
def login():
    # 保存session数据
    session["name"]="python"
    return "login success"



@app.route("/")
def index():
    # 获取session数据
    name=session.get("name")

    return "hello %s" % name

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
