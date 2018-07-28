# coding:utf-8

from flask import Flask, jsonify,redirect,url_for
from flask import make_response
import json

app=Flask(__name__)


@app.route("/")
def index():
    # resp=make_response("index page python itcast")
    # resp.status="666 itcast python"
    # resp.headers['city']="深圳"
    #
    # return resp

    return "index page","666 itcast python",{"city":"深圳"}


@app.route("/person")
def get_person():
    p={
        "name":"asd",
        "age":12
    }
    return jsonify(p)



@app.route("/login")
def login():
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
