import cv2
import numpy as np
import os

class ObjectRecognizer:

    class __ObjectRecognizer:
        def __init__(self):
            self.net = self.setNeuralNetwork()

        def setNeuralNetwork(self):
            net = cv2.dnn.readNet(self.loadModel(), self.loadConfiguration())
            return net

        def loadModel(self):
            script_dir = os.path.dirname(__file__)
            rel_path = "utills/yolov3.weights"
            return os.path.join(script_dir, rel_path)

        def loadConfiguration(self):
            script_dir = os.path.dirname(__file__)
            rel_path = "utills/yolov3.cfg"
            return os.path.join(script_dir, rel_path)


    instance = None

    def __init__(self):
        print(self.instance)

        if not ObjectRecognizer.instance:
            ObjectRecognizer.instance = ObjectRecognizer.__ObjectRecognizer()

        self.threshold = 0.5
        self.objects = []
        self.classes = []
        self.boxes = []
        self.indices = None
        self.confidences = []
        self.class_ids = []

    def loadClasses(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "utills/yolov3_classes.txt"
        return os.path.join(script_dir, rel_path)

    def generateOutputLayers(self, net):
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        return output_layers

    def drawPrediction(self, image, class_id, x, y, w, h, classes, distance_label):
        label = str(classes[class_id])
        color = (0, 0, 255)
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, label + " " + distance_label, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    def performObjectRecognition(self, image):
        Width = image.shape[1]
        Height = image.shape[0]
        scale = 0.00392
        classesFiles = self.loadClasses()
        with open(classesFiles, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

        net = self.instance.net

        blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(self.generateOutputLayers(net))

        conf_threshold = self.threshold
        nms_threshold = 0.4     # non-maximum supression

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.1:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    self.class_ids.append(class_id)
                    self.confidences.append(float(confidence))
                    self.boxes.append([x, y, w, h])
        self.indices = cv2.dnn.NMSBoxes(self.boxes, self.confidences, conf_threshold, nms_threshold)

    def backingupImage(self, image):
        cv2.imwrite("../../assets/images/RecognitionResults/RecognitionRestuls.png", image)