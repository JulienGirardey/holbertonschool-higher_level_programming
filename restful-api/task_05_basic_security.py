#!/usr/bin/python3
"""
task_05_basic_security

this module contains
several route and 2 authentication:
user and admin
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password":
              generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password":
               generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verif_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Wrong username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token})


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    id_user = get_jwt_identity()
    user = users.get(id_user)
    if not user:
        return jsonify({"error": "401 Unauthorized"}), 401
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    id_user = get_jwt_identity()
    user = users.get(id_user)
    if not user:
        return jsonify({"error": "401 Unauthorized"}), 401
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    id_user = get_jwt_identity()
    user = users.get(id_user)
    if not user or user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"
