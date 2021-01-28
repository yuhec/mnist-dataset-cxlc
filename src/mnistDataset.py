import Algorithmia
from tensorflow.keras.models import load_model
import autokeras as ak
import tensorflow as tf
from autokeras.keras_layers import CastToFloat32

from .front import front

client = Algorithmia.client()

model_path = client.file("data://laetitia/mnistDatasetCxlc/my_model.h5").getFile().name
model = tf.keras.models.load_model(model_path, custom_objects={'CastToFloat32': CastToFloat32})

def apply(input):
  o = front(input, model)
  return o
