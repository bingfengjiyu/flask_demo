# coding:utf-8


from flask import Flask,abort

app=Flask(__name__)

@app.route("/")
def index():
    abort(404)
    return "index page"

# 自定义错误处理方法,在发生特定错误的时候,flask会调用
@app.errorhandler(404)
def handler_404(e):
    return u"发生404错误"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
