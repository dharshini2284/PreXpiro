import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("backend/models/fruit_classifier.h5")

class_names = list(model.output_shape)[-1]

def predict_fruit(img_path, class_indices):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    idx = np.argmax(preds)
    return list(class_indices.keys())[list(class_indices.values()).index(idx)]
