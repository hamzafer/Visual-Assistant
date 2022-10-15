import cv2 as cv
import numpy as np
from backend.Classes.ObjectDetector import ObjectDetector

class FeatureExtractor:
    helper = None

    def __init__(self, helper):
        self.helper = helper

    def getExtractedFeatures(self, img, rawImage):
        detector = ObjectDetector(self.helper)
        detectedObjects = detector.getDetectionResults(img, rawImage)
        return self.extractFeatures(detectedObjects)

    def extractFeatures(self, img):
        cloneImg = img.copy()
        img = self.detectCorners(img)
        featuresImg = self.reassembleImage(img, cloneImg)
        self.backingupImage(featuresImg)
        return featuresImg

    def reassembleImage(self, img, cloneImg):
        imgRows, imgCols, layers = img.shape
        for i in range(imgRows):
            for j in range(imgCols):
                if (cloneImg[:, :, 0][i, j] == 30 and cloneImg[:, :, 1][i, j] == 50):
                    img[:, :, 0][i, j] = cloneImg[:, :, 0][i, j]
                    img[:, :, 1][i, j] = cloneImg[:, :, 1][i, j]
                    img[:, :, 2][i, j] = cloneImg[:, :, 2][i, j]
        return img

    def detectCorners(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv.cornerHarris(gray, 2, 3, 0.04)
        dst = cv.dilate(dst, None)
        img[dst > 0.01 * dst.max()] = [0, 255, 0]
        return img

    def backingupImage(self, img):
        cv.imwrite("../../assets/images/FeaturesResults/FeaturesResults.png", img)