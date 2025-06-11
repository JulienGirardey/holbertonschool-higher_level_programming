#!/usr/bin/python3
"""
task_04_flask

this module contains 5
functions to handle the path
with flask API
"""
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def username(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    if not new_user or "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user["username"]
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
