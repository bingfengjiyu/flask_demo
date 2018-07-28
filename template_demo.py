# coding:utf-8

from flask import Flask,render_template

app=Flask(__name__)



@app.route("/")
def index():
    context={
        "name":"python",
        "age":12
    }
    return render_template("index.html",**context)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
