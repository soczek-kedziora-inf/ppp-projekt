from db import get_db
import numpy as np
import cv2
import datetime
import model
import os
import io
import base64
from flask_login import current_user
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from PIL import Image as PILImage


class Image:
    def __init__(self, file):
        if (current_user.id):
            self.userId = current_user.id
        self.prediction = ''
        self.filename = ''
        self.image = self.set_image(file)


    def set_image(self, file):
        filestr = file.read()
        file_bytes = np.fromstring(filestr, np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        return image;


    def classify(self):
        image = self.preprocess_image(self.image)
        prediction = model.loaded_model.predict(image)
        prediction_labeled = decode_predictions(prediction)
        self.prediction = prediction_labeled
        return prediction_labeled[0][0][1]


    def preprocess_image(self, image, size=(299, 299)):
        image = cv2.resize(image, size)
        array = preprocess_input(image)
        array = np.expand_dims(array, 0)
        return array


    def get_filename(self):
        if (current_user.id):
            db = get_db()
            imageId = db.execute(
                "SELECT max(id) FROM results WHERE classifiedAs = ? and userId = ?",
                (self.prediction[0][0][1], self.userId)
            ).fetchone()
            self.filename = str(imageId[0]) + '.png'
            return self.filename
        return None;


    def save(self, path):
        full_path = os.path.join(path, self.filename)
        print(full_path)
        print(os.getcwd())
        if not cv2.imwrite(full_path, self.image):
            print("Could not write image")


    def prepare_to_display(self):
        img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        img = self.resize(img)
        img = PILImage.fromarray(img.astype("uint8"))
        rawBytes = io.BytesIO()
        img.save(rawBytes, "JPEG")
        rawBytes.seek(0)
        img_base64 = base64.b64encode(rawBytes.getvalue()).decode('ascii')
        mime = "image/jpeg"
        uri = "data:%s;base64,%s" % (mime, img_base64)

        return uri


    def resize(self, image, height=400):
        aspect_ratio = float(image.shape[1])/float(image.shape[0])
        width = height/aspect_ratio
        image = cv2.resize(image, (int(height), int(width)))

        return image