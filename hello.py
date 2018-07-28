from flask import Flask,url_for

app=Flask(__name__,
          static_folder="static",
          static_url_path="/static",
          template_folder="templates",)




# class MyConfig():
#     DEBUG=True
#     ITCAST="python"
#
#
# app.config.from_object(MyConfig)


@app.route("/")
def hello():
    print (app.config.get("ITCAST"))
    return "hello itcast"


@app.route("/index")
@app.route("/hi")
def index():
    return "index1"

@app.route("/python",methods=["GET","POST"])
def post_only():
    return "post_only"

@app.route("/redirect")
def redirect_post_only():
    return '<a href="%s">post_only</a>' % url_for("post_only")



if __name__ == '__main__':
    app.run(debug=True)

