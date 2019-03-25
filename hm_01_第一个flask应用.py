from flask import Flask


# 1.创建web应用
app = Flask(__name__)


@app.route("/")  # 路由: 让视图函数绑定对应的URL, 当访问URL时, 会调用该视图函数
def index():
    a = 10 / 20
    return "hello flask"


if __name__ == '__main__':
    # 万能ip 0.0.0.0  外网/局域网请求都可以监听
    # debug=True 是否开启调试模式  1> 可以在页面上显示python错误  2> 更新代码时, 自动重启服务器

    # 2.运行应用(启动flask内置的测试服务器, 并且将请求转发给web应用)
    app.run(host="0.0.0.0", port=8000, debug=True)