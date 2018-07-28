# coding:utf-8

from flask import Flask,render_template,request
from flask_wtf import FlaskForm    # 表单类的父类
from wtforms import StringField,PasswordField,SubmitField   # 表单的字段类型
from wtforms.validators import DataRequired,EqualTo

app=Flask(__name__)

app.config["SECRET_KEY"]="hfwejhy237489237ifsf"

class RegisterForm(FlaskForm):
    username=StringField(label=u"用户名",validators=[DataRequired()])
    password=PasswordField(label=u"密码",validators=[DataRequired()])
    password2=PasswordField(label=u"确认密码",validators=[DataRequired(),EqualTo("password",u"密码不一致")])
    submit=SubmitField(label=u"提交")


@app.route("/register",methods=["GET","POST"])
def register():
    form=RegisterForm()
    # 对表单数据进行验证
    if form.validate_on_submit():
        # 表示用户的数据符合要求
        username=form.username
        password=form.password
        password2=form.password2
        print username,password,password2
        return "success"
    else:
        if request.method=="GET":
            return render_template("register.html",form=form,errmsg="")
        else:
            return render_template("register.html", form=form,errmsg=u"填写信息有误")

    return render_template("register.html",form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
