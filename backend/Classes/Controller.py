from backend.Classes.ObjectRecognizer import ObjectRecognizer
from backend.Classes.ObjectLocalizer import ObjectLocalizer
from backend.Classes.ImagePreprocessor import ImagePreprocessor
from backend.Classes.FeatureExtractor import FeatureExtractor
from backend.Classes.SceneElaborator import SceneElaborator
from backend.Classes.FaceDetection import FaceDetection
from backend.Classes.Object import Object

import cv2

class ServerController:
    def __init__(self):

        # Singleton pattern
        self.recognizer = ObjectRecognizer()
        # End of Singleton pattern

        # face detector
        self.face_detector = FaceDetection()
        # end of face detector

        # Scene Elaborator
        self.scene_elaborator = SceneElaborator()
        # end of Scene Elaborator

        self.localizer = ObjectLocalizer()

    def getEnvironmentLabelled(self, image):
        return self.scene_elaborator.understandScene(image)

                                                        # Controller will ask recognizer, localizer and
    def getEnvironmentUnderstanding(self, image, env):       # scenario eleborator to perform their operations
        # preprocessor = ImagePreprocessor()
        #image = preprocessor.getPreprocessingResults(image)
        if (env == "1"):
            environment = self.getEnvironmentLabelled(image)
            return environment
        else:
            final_image, objects, distances =  self.getLabelledObjects(image)
            featureExtractor = FeatureExtractor(self.recognizer)
            #final_image = featureExtractor.extractFeatures(final_image)
            return {
                'final_image': final_image,
                'objects': objects,
                'distances': distances
            }

    def getObjectPosition(self, object):
        return self.localizer(self, object)


    def checkEmptyObject(self, object_name):
        return object_name == "null"

    def findPerson(self, object_name):
        return object_name == "person"

    def getLabelledObjects(self, image):                      # From here recoginizer take the frame
        self.recognizer.performObjectRecognition(image)       #  and perform object recoginition on it
        find_person = False
        distances = []
        objects = []

        pending_objects = []
        pending_distances = []

        for i in self.recognizer.indices:
            i = i[0]
            box = self.recognizer.boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            if not (self.checkEmptyObject(self.recognizer.classes[self.recognizer.class_ids[i]])):
                if not (self.findPerson(self.recognizer.classes[self.recognizer.class_ids[i]])):
                    obj = self.createObject(self.recognizer.classes[self.recognizer.class_ids[i]],
                                            self.recognizer.class_ids[i], x, y, w, h)

                    obj_distance = self.localizer.measureDistance(obj, image.shape[0])
                    objects.append(obj)
                    distances.append(obj_distance)

                    self.recognizer.drawPrediction(image, self.recognizer.class_ids[i],
                                                   round(x), round(y), round(w), round(h), self.recognizer.classes,
                                                   str(round(obj_distance, 1)) + "ft")
                else:
                    obj = self.createObject(self.recognizer.classes[self.recognizer.class_ids[i]],
                                            self.recognizer.class_ids[i], x, y, w, h)

                    obj_distance = self.localizer.measureDistance(obj, image.shape[0])
                    pending_objects.append(obj)
                    pending_distances.append(obj_distance)
                    find_person = True

        if (find_person):

            print("performing face detection")

            faces, confidences = self.face_detector.detect_face(image)

            detected_faces = len(faces)
            pending_person = len(pending_objects)


            # if (detected_faces > pending_person - detected_faces):
            if (True):
                # loop through detected faces
                for face, conf in zip(faces, confidences):

                    (startX, startY) = face[0], face[1]
                    (endX, endY) = face[2], face[3]

                    obj = self.createObject("person", 0, startX, startY, endX - startX, endY - startY)
                    obj_distance = self.localizer.measureDistance(obj, image.shape[0], 6.5)
                    objects.append(obj)
                    distances.append(obj_distance)

                    self.recognizer.drawPrediction(image, 0, round(startX), round(startY), round(endX - startX), round(endY - startY),
                                                   self.recognizer.classes,
                                                   str(round(obj_distance, 1)) + "ft")
            else:
                # loop through the pending objects
                for i in range(len(pending_objects)):
                    temp_obj = pending_objects[i]
                    temp_distance = pending_distances[i]

                    objects.append(temp_obj)
                    distances.append(temp_distance)

                    self.recognizer.drawPrediction(image, 0, int(temp_obj.coordinates['x']), int(temp_obj.coordinates['y']),
                                                   int(temp_obj.coordinates['w']), int(temp_obj.coordinates['h']),
                                                   self.recognizer.classes, str(round(temp_distance, 1)) + "ft")

        return image, objects, distances

    def createObject(self, name, identity, x, y, w, h):
        obj = Object()
        obj.name = name
        obj.id = identity
        obj.coordinates = {
            'x': x,
            'y': y,
            'w': w,
            'h': h,
        }
        return obj
