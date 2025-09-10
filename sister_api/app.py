from flask import Flask, send_file

app = Flask(__name__)

@app.route("/html10kb")
def html10kb():
    return send_file("files/file_10kb.html")

@app.route("/html100kb")
def html100kb():
    return send_file("files/file_100kb.html")

@app.route("/html1mb")
def html1mb():
    return send_file("files/file_1mb.html")

@app.route("/html5mb")
def html5mb():
    return send_file("files/file_5mb.html")

@app.route("/html10mb")
def html10mb():
    return send_file("files/file_10mb.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
