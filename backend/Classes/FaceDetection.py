import cv2
import numpy as np
import os

class FaceDetection:

    class __FaceDetection:
        def __init__(self):
            self.net = self.setNeuralNetwork()

        def setNeuralNetwork(self):
            net = cv2.dnn.readNetFromCaffe(self.loadProto(), self.loadModel())
            return net

        def loadProto(self):
            script_dir = os.path.dirname(__file__)
            rel_path = "utills/deploy.prototxt"
            return os.path.join(script_dir, rel_path)

        def loadModel(self):
            script_dir = os.path.dirname(__file__)
            rel_path = "utills/res10_300x300_ssd_iter_140000.caffemodel"
            return os.path.join(script_dir, rel_path)

    instance = None

    def __init__(self):
        print(self.instance)

        if not FaceDetection.instance:
            FaceDetection.instance = FaceDetection.__FaceDetection()

    def detect_face(self, image, threshold=0.5):

        (h, w) = image.shape[:2]

        # preprocessing input image
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net = self.instance.net
        net.setInput(blob)

        # apply face detection
        detections = net.forward()

        faces = []
        confidences = []

        # loop through detected faces
        for i in range(0, detections.shape[2]):
            conf = detections[0, 0, i, 2]

            # ignore detections with low confidence
            if conf < threshold:
                continue

            # get corner points of face rectangle
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')

            faces.append([startX, startY, endX, endY])
            confidences.append(conf)

        # return all detected faces and
        # corresponding confidences
        return faces, confidences
