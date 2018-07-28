# coding:utf-8

from flask import Flask,session,request

app=Flask(__name__)


@app.before_first_request
def handle_before_first_req():
    print ("handle before firs req called")


@app.before_request
def handle_before_request():
    print ("handle before_request called")


@app.after_request
def handle_after_request(response):
    print ("handle after_request called")
    return response

@app.teardown_request
def handle_teardown_request(response):
    print ("handle teardown_request called")
    return response


@app.route("/")
def index():
    print ("index called")
    return "index called"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
