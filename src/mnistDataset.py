import Algorithmia
# from tensorflow.keras.models import load_model
import autokeras as ak

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages

client = Algorithmia.client()

def load_model():
    # Get file by name
    # Open file and load model
    file_path = 'data://.my/mnistDatasetCxlc/saved_model.pb'
    model_path = client.file(file_path).getFile().name
    # Open file and load model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        return model

# model = load_model("data://.my/mnistDatasetCxlc/saved_model.pb", custom_objects=ak.CUSTOM_OBJECTS)
model = load_model()

def apply(input):
    o = front(input, model)
    return o
