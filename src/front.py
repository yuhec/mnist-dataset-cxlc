import cv2
import tensorflow as tf
import pandas as pd
import numpy as np

def front(img_path, model):
    try:
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (28,28))

        predicted_y = model(img)

        # Prepare output
        prediction = dict()
        prediction['best_probabilities'] = np.max(predicted_y)
        prediction['number_selected'] = np.argmax(predicted_y)

        return prediction

    except Exception as e:
        return e