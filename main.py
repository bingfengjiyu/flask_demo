# coding:utf-8

from flask import Flask
from goods import get_goods
from users import register
from orders import app_orders
from cart import app_cart

app = Flask(__name__)

app.route("/register")(register)

app.route("/get_goods")(get_goods)

app.register_blueprint(app_orders)

app.register_blueprint(app_cart)



@app.route("/", methods=["GET", "POST"])
def index():
    # 循环引用解决方案,推迟一方的导入,让另一方先执行

    return "index page"


if __name__ == '__main__':
    print app.url_map
    app.run()
