# coding=utf-8

from flask import Blueprint


app_cart=Blueprint("cart",__name__,template_folder="templates")

from .view import cart







