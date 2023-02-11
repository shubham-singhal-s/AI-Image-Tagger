from flask import Flask, request
from flask_cors import CORS, cross_origin
from tensorflow import keras
from PIL import Image
from tensorflow.keras.applications.nasnet import preprocess_input
from keras.metrics import AUC, Precision, Recall
import numpy as np
import json

app = Flask("Tagging")
CORS(app)

########CUSTOM METRICS############
# auc = AUC(multi_label=True, thresholds=[0.4])
# precision = Precision(thresholds=[0.4])
# recall = Recall(thresholds=[0.4])
# def AUC_metric(y_true, y_pred):
#     return auc(y_true, y_pred)

# def precision_metric(y_true, y_pred):
#     return precision(y_true, y_pred)

# def recall_metric(y_true, y_pred):
#     return recall(y_true, y_pred)
##################################

base_path = '../model/'
f = open(base_path + 'labels.json')

mappings = json.load(f)
model = keras.models.load_model(base_path, compile=False)

def get_images(image):
    X = []
    im = Image.open(image.stream)
    im = im.resize(size=(331,331))
    im = np.asarray(im)
    im_processed = preprocess_input(im)
    if im_processed.shape == (331, 331, 3):
        X.append(im_processed)
    return np.array(X)

def getLabels(image):
    image_proc = get_images(image)
    if len(image_proc) == 0:
        return "Could not process image"
    labels = model.predict(image_proc)[0]
    tags = []
    for i, k in enumerate(mappings.keys()):
        obj = {}
        obj['label'] = k
        obj['value'] = str(labels[i])
        tags.append(obj)
    labels = np.where(labels >= 0.4)[0]
    keys = list(mappings.keys())
    print(labels)
    labels = [keys[int(i)] for i in labels]
    return tags


@app.route('/image', methods=['POST'])
def upload():
    if request.method == "POST":
        if len(request.files) > 0:
            image = request.files["image"]
            labs = getLabels(image)
            return {"data": getLabels(image)}
    return {"data": "Nothing Found"}

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)