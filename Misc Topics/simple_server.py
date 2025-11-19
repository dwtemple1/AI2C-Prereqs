from flask import Flask
from flask import request
import os
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
def hello_world():
    result = "<h1>Hello, world</h1>"
    if request.args:
        result += "\n- Server received: " + json.dumps({key: val for key, val in request.args.items()})
    return result


@app.route("/teapot")
def error_val():
    return "I'm a teapot", 418

@app.route("/requestType", methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
def request_type():
    return f"Server received {request.method} HTTP request"

@app.route("/api")
def api():
    result = {}
    for file in os.listdir():
        if not os.path.isdir(file):
            result[file] = {
                "size": os.stat(file).st_size,
                "last_modified": os.stat(file).st_mtime,
                "created": os.stat(file).st_mtime,
                "ext": os.path.splitext(file)[1],
                "type": "file",
            }
        else:
            result[file] = {"type": "dir"}

    return json.dumps(result)

def run():
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    run()
