# Pre-Trained Model Example using Keras on PyCharm
#Import Statements
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
#Assigning Weights
model = ResNet50(weights='imagenet')
img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
#Checking or predicting using Pre-Trained Models
preds = model.predict(x)
##print('Predicted:', decode_predictions(preds, top=3)[0])
for values in decode_predictions(preds, top=3)[0] :
    if float(values[2]) >= 0.55:
        print( "The picture is", values[1])