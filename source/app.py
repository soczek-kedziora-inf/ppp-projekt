import os
import sqlite3


from flask import Flask, render_template 
from flask_login import (
    LoginManager,
    current_user,
)
from oauthlib.oauth2 import WebApplicationClient

from db import init_db_command
from user import User
from classify import app_classify
from login import app_login

app = Flask(__name__)
app.register_blueprint(app_classify)
app.register_blueprint(app_login)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['UPLOAD_FOLDER'] = "./resources/uploaded/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 102

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403

try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template('index.html', user = current_user)
    else:
        return render_template('login.html')


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
