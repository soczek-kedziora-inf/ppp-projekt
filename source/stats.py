import cv2
from flask import Blueprint,current_app, render_template, url_for, request,redirect, flash
import os
from flask import session
from db import get_db
import datetime
from flask_login import current_user

app_stats = Blueprint('stat',__name__)

@app_stats.route('/stats', methods=['POST'])
def show_stats():
    results = get_prev_classifications(current_user.id)
    print(results)
    return render_template("stats.html", res=results)

def get_prev_classifications(user_id):
    db = get_db()
    results = db.execute(
        "SELECT * FROM results WHERE userId = ?", (user_id,)
    ).fetchall()
    return results

@app_stats.route('/ret', methods=['POST'])
def return_to_index():

    return redirect(url_for("index"))

