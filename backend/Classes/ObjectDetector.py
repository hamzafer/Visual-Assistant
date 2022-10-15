import cv2 as cv
import numpy as np
from backend.Classes.ImageSegmentizer import ImageSegmentizer

class ObjectDetector:
    def __init__(self, helper):
        self.objectsCount = 0
        self.helper = helper
        self.positions = []
        self.regions = []
        self.helper = None

    def getDetectionResults(self, img, rawImage):
        segmentizer = ImageSegmentizer()
        enhancedImage = segmentizer.getSegmentationResults(img, rawImage)
        modifiedImage = enhancedImage.copy()
        return self.performObjectDetection(enhancedImage, modifiedImage)

    def detectObjectPosition(self):
        self.positions.clear()
        for i in range(self.objectsCount):
            self.positions.append(self.regions[i].getObjectPosition())

    def performObjectDetection(self, img, rawImage):
        self.measureRegionsConfidence(img)
        self.countObjects()
        self.detectObjectPosition()
        detectedObjects = self.generateRegionProposal(rawImage)
        cv.imshow("Object Detection Result", detectedObjects)
        self.backingupImage(detectedObjects)
        cv.waitKey()
        cv.destroyAllWindows()
        return detectedObjects

    def generateRegionProposal(self, img):
        modifiedImg = img.copy()
        for item in self.positions:
            for i in range(int(item[1]), int(item[1]) + int(item[3])):
                for j in range(int(item[0]), int(item[0]) + int(item[2])):
                    if (i >= 700):
                        i -= 5
                    if (j >= 700):
                        j -= 5
                    modifiedImg[:, :, 0][i, j] = 255
                    modifiedImg[:, :, 1][i, j] = 255
                    modifiedImg[:, :, 2][i, j] = 255

        imgRows, imgCols, layers = img.shape
        for i in range(imgRows):
            for j in range(imgCols):
                if (modifiedImg[:, :, 0][i, j] == 255 and modifiedImg[:, :, 1][i, j] == 255 and modifiedImg[:, :, 2][i, j] == 255):
                    modifiedImg[:, :, 0][i, j] = img[:, :, 0][i, j]
                    modifiedImg[:, :, 1][i, j] = img[:, :, 1][i, j]
                    modifiedImg[:, :, 2][i, j] = img[:, :, 2][i, j]
                else:
                    modifiedImg[:, :, 0][i, j] = 30
                    modifiedImg[:, :, 1][i, j] = 50
                    modifiedImg[:, :, 2][i, j] = img[:, :, 2][i, j]
        return modifiedImg

    def measureRegionsConfidence(self, img):
        confidenceFinder = self.helper
        self.regions = confidenceFinder.getObjects(img)

    def countObjects(self):
        self.objectsCount = self.regions.__len__()
        return self.objectsCount

    def backingupImage(self, img):
        cv.imwrite("../../assets/images/DetectionResults/DetectionResults.png", img)