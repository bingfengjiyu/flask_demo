# coding =utf-8

from . import app_cart


@app_cart.route("/cart")
def cart():
    return "cart page"



