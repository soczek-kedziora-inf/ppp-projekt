from tensorflow.keras.applications import Xception
from tensorflow.keras.models import load_model

from keras import Model
# Wczytanie modelu Xception
def getModel():
    global loaded_model
    try:
        loaded_model = load_model('../resources/prediction_model')
    except (ImportError, IOError):
        loaded_model = Xception()
        loaded_model.compile()
        loaded_model.save("../resources/prediction_model")
