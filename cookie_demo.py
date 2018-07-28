# coding:utf-8

from flask import Flask,make_response,request

app=Flask(__name__)

@app.route("/")
def index():
    resp=make_response("index page")
    # 默认浏览器关闭cookie就失效
    # resp.set_cookie("itcast","python")
    # 通过max_age设置有效期
    resp.set_cookie("itcast1","python",max_age=3600)
    return resp

@app.route("/get_cookie")
def get_cookie():
    cookie=request.cookies.get("itcast1")
    return cookie


@app.route("/del_cookie")
def del_cookie():
    resp=make_response("delete success")
    # 通过对象中的delete_cookie删除cookie
    resp.delete_cookie("itcast1")
    return resp



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
