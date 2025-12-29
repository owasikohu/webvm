from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

dir = os.path.join(os.getcwd(), "statics")


@app.route("/")
def index():
    filename = "index.html" 
    path = os.path.join(dir, filename)
   
    try:
        return send_file(path)
    except:
        abort(404)


@app.route("/read")
def read_file():
    filename = request.args.get("file", "")
    path = os.path.join(dir, filename)

    try:
        return send_file(path)
    except:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
