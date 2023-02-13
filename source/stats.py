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
# def upload_image():
# 	if 'file' not in request.files:
# 		flash('No file part')
# 		return redirect(url_for("index"))
# 	file = request.files['file']
# 	if file.filename == '':
# 		flash('No image selected for uploading')
# 		return redirect(url_for("index"))
# 	if file and allowed_file(file.filename):
# 		filename = secure_filename(file.filename)
#
# 		image = Image(file)
# 		prediction = image.classify()
#
# 		# using session to make filename and prediction available for db insert
# 		session['org_filename'] = filename
# 		session['prediction'] = prediction
#
# 		# preparing image to be displayed in web view
# 		uri = image.prepare_to_display()
# 		image.get_filename()
#
# 		# save the image locally on the server, if UPLOAD_FOLDER does not exist - create it
# 		os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
# 		image.save(current_app.config['UPLOAD_FOLDER'])
#
# 		print('Uploaded image new filename: ' + image.get_filename())
#
# 		return render_template('verify.html', prediction=prediction, bytesImage=uri)
# 	else:
# 		flash('Allowed image types are -> png, jpg, jpeg')
# 		return redirect(url_for("index"))
#
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
#
# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# @app_stats.route('/verify', methods=['POST'])
# def verify():
# 	print(request.method)
# 	if request.method == 'POST':
# 		if request.form.get('yes') == 'yes':
# 			session['correct'] = True
# 			print("True")
# 		elif request.form.get('no') == 'no':
# 			session['correct'] = False
# 			print("false")
# 		else:
# 			pass # Unknown
# 	elif request.method == 'GET':
# 		print("No Post Back Call")
# 	insert_to_db()
# 	return redirect(url_for("index"))
#
# def insert_to_db():
# 	db = get_db()
# 	db.execute(
# 		"INSERT INTO results (createdOn, originalFilename, classifiedAs, correct, userId)"
# 		" VALUES (?, ?, ?, ?, ?)",
# 		(datetime.datetime.now(), session['org_filename'], session['prediction'], session['correct'], current_user.id)
# 	)
# 	db.commit()
# 	return redirect(url_for("index"))

