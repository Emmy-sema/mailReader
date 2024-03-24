import os

from flask import Flask, request, send_file
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/gmail', methods=["GET"])
def gmail():
    print("users endpoint reached...")
    if request.method == "GET":
        from getPermission import  getPermission
        from getEmails import  getEmail_json

        getPermission()
        getEmail_json()
        with open("emails.json", "r") as f:
            data = json.load(f)
            return flask.jsonify(data)


@app.route('/audio', methods=["POST"])
def audio():
    if request.method == "POST":
        from speach import voice
        return send_file(voice(request.data.decode("utf-8")))

if __name__ == "__main__":
    app.run("localhost", 6969)
