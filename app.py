import json
from flask import Flask, request

app = Flask(__name__)

dataCollection = {
    "data1": {
        "name": "sudo",
        "email": "sudo@sudox.com"
    }
}


@app.route("/")
def hello_world():
    return "<h1>sudo user x </h1>"


@app.route("/data", methods=['GET', 'POST'])
def data():
    # content_type = request.headers.get('Content-Type')
    if request.method == 'POST':
        dataCollection["new data"] = request.json
        return dataCollection
    else:
        return dataCollection


if __name__ == "__main__":
    app.run(debug=True)
