from flask import Blueprint,current_app, render_template, url_for, request,redirect, flash
from werkzeug.utils import secure_filename
import os

app_classify = Blueprint('classify',__name__)
@app_classify.route('/upload', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(url_for("index"))
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(url_for("index"))
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
		print('upload_image filename: ' + filename)
		return render_template('verify.html')
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(url_for("index"))

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
