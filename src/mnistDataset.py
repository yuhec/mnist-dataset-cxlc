import Algorithmia
from tensorflow.keras.models import load_model
import autokeras as ak
import tensorflow as tf
from autokeras.keras_layers import CastToFloat32

from .front import front

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages

client = Algorithmia.client()

model_path = client.file("data://laetitia/mnistDatasetCxlc/my_model.h5").getFile().name
model = tf.keras.models.load_model(model_path, custom_objects={'CastToFloat32': CastToFloat32})

# model = load_model("data://.my/mnistDatasetCxlc/saved_model.pb", custom_objects=ak.CUSTOM_OBJECTS)
# model = load_model()

def apply(input):
  o = front(input, model)
  return o
    #if isinstance(input, str):
     #   path = client.file(input).getFile().name
      #  o = front(path, model)
      # return o
    #else :
     #   return 'Input is not a string...'
