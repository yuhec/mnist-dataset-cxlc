import cv2

def front(img_path, model):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28,28))

    prediction = model(img)

    return prediction