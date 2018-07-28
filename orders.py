# coding:utf-8

from flask import Blueprint

# 创建一个蓝图对象
app_orders=Blueprint("app_orders",__name__)


@app_orders.route("/get_orders")
def get_orders():
    return "get orders"


