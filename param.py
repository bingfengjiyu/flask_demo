from flask import Flask,request

app=Flask(__name__,
          static_folder="static",
          static_url_path="/static",
          template_folder="templates",)


class MyConfig():
    DEBUG=True
    ITCAST="python"


app.config.from_object(MyConfig)


@app.route("/")
def param_test():
    name=request.args.get("name")
    return "hello %s" % name

@app.route("/upload")
def upload():
    pic_file=request.files.get("pic")
    # pic_data=pic_file.read()
    # with open("./upload_img","wb")as f:
    #     f.write(pic_data)
    if pic_file:
        pic_file.save("./upload_img")
        return "success"
    else:
        return "false"



if __name__ == '__main__':
    app.run()
