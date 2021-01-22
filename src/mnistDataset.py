import Algorithmia
from tensorflow.keras.models import load_model
import autokeras as ak

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages

client = Algorithmia.client()

model = load_model("../model_builder/model_autokeras", custom_objects=ak.CUSTOM_OBJECTS)

def apply(input):
    o = front(input, model)
    return o
