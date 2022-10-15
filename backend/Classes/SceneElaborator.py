import csv
import os
import cv2 as cv
import numpy as np
import tensorflow.compat.v1 as tf

from keras.applications.inception_resnet_v2 import preprocess_input
from backend.Classes.ImagePreprocessor import ImagePreprocessor
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model

best_model = 'model.11-0.6262.hdf5'
num_classes = 80

class SceneElaborator:

    class __SceneElaborator:
        def __init__(self):
            self.model = self.setNeuralNetwork()
            self.model._make_predict_function()
            self.graph = tf.get_default_graph()

        def setNeuralNetwork(self):
            net = self.loadModel()
            return net

        def loadModel(self):
            model = self.build_model()
            script_dir = os.path.dirname(__file__)
            rel_path = "utills/model.11-0.6262.hdf5"
            model_weights_path = os.path.join(script_dir, rel_path)
            model.load_weights(model_weights_path)

            return model

        def build_model(self):
            base_model = InceptionResNetV2(weights='imagenet', include_top=False)
            x = base_model.output
            x = GlobalAveragePooling2D()(x)
            x = Dense(1024, activation='relu')(x)
            predictions = Dense(num_classes, activation='softmax')(x)
            model = Model(inputs=base_model.input, outputs=predictions)
            return model

    instance = None

    def validateEnvironment(self, environment):
        if environment == "null":
            return "unable"
        else:
            return environment

    def __init__(self):
        print(self.instance)
        self.preprocessor = ImagePreprocessor()
        if not SceneElaborator.instance:
            SceneElaborator.instance = SceneElaborator.__SceneElaborator()

    def understandScene(self, image):

        script_dir = os.path.dirname(__file__)
        rel_path = "utills/scene_classes.csv"
        csv_file = os.path.join(script_dir, rel_path)

        with open(csv_file) as file:
            reader = csv.reader(file)
            scene_classes_list = list(reader)

        scene_classes_dict = dict()
        for item in scene_classes_list:
            scene_classes_dict[int(item[0])] = item[2]

        print('Starting Environment Processing...')
        model = self.instance.model

        cloned_image = image.copy()

        cloned_image = self.preprocessor.resizingImage(cloned_image)

        rgb_img = cv.cvtColor(cloned_image, cv.COLOR_BGR2RGB)
        rgb_img = np.expand_dims(rgb_img, 0).astype(np.float32)
        rgb_img = preprocess_input(rgb_img)
        with self.instance.graph.as_default():
            preds = model.predict(rgb_img)
        prob = np.max(preds)
        class_id = np.argmax(preds)

        return self.validateEnvironment(scene_classes_dict[class_id])