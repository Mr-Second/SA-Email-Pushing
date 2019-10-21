from Server.Mail import MySendMail
from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import *
import time
import re

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)


@app.route('/', methods=["GET", "POST"])
def hello():
    return 'hello'


@app.route('/sendEmail', methods=["GET", "POST"])
def sendEmail():
    data = request.json
    print(data)
    if "_url" in data and "_payload" in data:
        flag = MySendMail(data["_url"], str(time.strftime('%Y-%m-%d %H:%M:%S')), data["_payload"])
        if flag:
            return "Y"
        else:
            return "N"
    return "N"


@app.route('/sendEmailBatch', methods=["GET", "POST"])
def sendEmailBatch():
    data = request.json
    flag = True
    if "_url" in data and "_payload" in data:
        for url in data["_url"]:
            flag = MySendMail(url, str(time.strftime('%Y-%m-%d %H:%M:%S')), data["_payload"]) and flag
        if flag:
            return "Y"
        else:
            return "N"
    return "N"


@app.route('/validateEmailAddress', methods=["GET", "POST"])
def validateEmailAddress():
    data = request.json
    if "_url" in data:
        p = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if p.match(data["_url"]):
            print("有效邮箱地址")
            return "Y"
        else:
            print("无效邮箱地址")
            return "N"
    return "N"


if __name__ == '__main__':
    app.run(debug=True)

