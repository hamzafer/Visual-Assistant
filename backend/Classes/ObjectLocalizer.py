import os
from backend.Classes.Object import Object


class ObjectLocalizer:
    def __init__(self, item=None, scale=None):
        self.ppi = 144.21
        self.item = item
        self.scale = scale

    def loadHeights(self):
        script_dir = os.path.dirname(__file__)
        rel_path = 'utills/yolov3_heights.txt'
        return os.path.join(script_dir, rel_path)

    def getDetectedObject(self, label, identity):
        self.item = Object()
        self.item.name = label
        self.item.id = identity
        return self.item

    def calculateCoordinates(self, x, y, w, h):
        self.item.coordinates = {
            'x': x,
            'y': y,
            'w': w,
            'h': h
        }

    def computeLocation(self, heights, n_person):
        inches = self.ppi / self.item.coordinates['h']
        if (n_person == -1):
            object_height = float(heights[self.item.id])
        else:
            object_height = n_person
        return object_height * inches

    def measureDistance(self, obj, image_height, n_person = -1):
        heightsFiles = self.loadHeights()
        with open(heightsFiles, 'r') as f:
            heights = [line.strip() for line in f.readlines()]
        self.item = self.getDetectedObject(obj.name, obj.id)
        self.calculateCoordinates(obj.coordinates['x'], obj.coordinates['y'], obj.coordinates['w'], obj.coordinates['h'])
        self.scale = image_height
        if self.item.coordinates['y'] + self.item.coordinates['h'] < self.scale:
            object_distance = self.computeLocation(heights, n_person)
        else:
            object_distance = 0
        return object_distance
