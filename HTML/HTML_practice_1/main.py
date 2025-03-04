# 

import os.path

from flask import Flask, send_from_directory

app = Flask(__name__)


def root_dir():
    return os.path.abspath(os.path.dirname(__file__))


@app.after_request
def add_header(r):
    """Disable caching. Source: https://stackoverflow.com/questions/34066804/disabling-caching-in-flask
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers[
        "Cache-Control"
    ] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r


@app.route("/")
@app.route("/<path:path>")
def get_resource(path="index.html"):
    return send_from_directory(root_dir(), path)


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)
    # ip, port 로 구성되어 있고, port 번호는 1~10000 : 잘 안 씀 (기존에 정해진게 있기 때문)
    # 127.0.0.1 은 로컬주소를 의미함 (내 컴퓨터에서만 접근 가능)