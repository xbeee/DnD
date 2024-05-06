# зависимости
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, emit, send
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask_cors import CORS
from datetime import timedelta, datetime
import json

# настройки прилажения
api = Flask(__name__)
CORS(api, supports_credentials=True)
# настройки JWT
api.config["JWT_SECRET_KEY"] = "super-secret"
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=999999)
jwt = JWTManager(api)
# настройки БД
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///code-rock.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(api)
# настройки сокетов
socketio = SocketIO(api)