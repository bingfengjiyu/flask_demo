# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,or_

app=Flask(__name__)

# 配置中设置数据库
class Config():
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql://root:mysql@127.0.0.1:3306/db_python02"
    # 让sqlalchemy跟踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS=True


app.config.from_object(Config)

# 创建sqlalchemy的数据库链接对象
db=SQLAlchemy(app)


class Roles(db.Model):
    __tablename__="tbl_roles"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship("User",backref="role")
    def __repr__(self):
        return "Role: %s" % self.name


class User(db.Model):
    __tablename__="tbl_users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(128),unique=True)
    password=db.Column(db.String(128))
    role_id=db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))   #指明外键

    def __repr__(self):
        return "User: %s" % self.name



if __name__ == '__main__':
    # 删除数据库所有表
    db.drop_all()
    # 创建数据库所有表
    db.create_all()

    role1=Roles(name="admin")
    db.session.add(role1)
    db.session.commit()

    role2=Roles(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)

    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()
    print Roles.query.all()
    print Roles.query.get(2)
    print Roles.query.get(200)
    print Roles.query.first()
    print Roles.query.first_or_404()
    print Roles.query.get_or_404(2)
    print Roles.query.count()
    print Roles.query.paginate()
    print "-"*40
    print User.query.filter_by(name="wang")
    print User.query.filter_by(name="wang").all()
    print User.query.filter_by(name="wang",id=2).all()
    print User.query.filter(User.name=="wang").all()
    print User.query.filter(User.name!="wang").all()
    print User.query.filter(or_(User.name=="wang",User.email.endswith("163.com"))).all()
    print User.query.filter(and_(User.name=="wang",User.email.endswith("163.com"))).all()

    print User.query.order_by(User.id).all()
    print User.query.order_by(User.id.desc()).all()[0]

    print User.query.filter_by(name="wang").update({"name":"li"})
    db.session.commit()
    user=User.query.get(1)
    db.session.delete(user)
    db.session.commit()



