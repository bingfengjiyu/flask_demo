# coding:utf-8

from flask import Flask,session,request
from flask_script import Manager

app=Flask(__name__)

manager=Manager(app)


@app.route("/")
def index():
    print ("index called")
    return "index called"


if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=5000)
    manager.run()
