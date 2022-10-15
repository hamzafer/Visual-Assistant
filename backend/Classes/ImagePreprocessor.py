import cv2
import numpy as np

class ImagePreprocessor:
    def __init__(self):
        return

    def getPreprocessingResults(self, image):
        return self.performPreprocessing(image)

    def resizingImage(self, image):
        # Standard scale is 700x700 pixels
        standardScale = 500
        height, width, layers = image.shape
        if (height > standardScale or width > standardScale):
            maximumSize = max(height, width)
            scalePercent = standardScale / maximumSize
            width = int(width * scalePercent)
            height = int(height * scalePercent)
            dim = (width, height)
            return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        else:
            return image

    def equalizeContrast(self, image):
        intensitiesValues = np.arange(256, dtype=np.float)
        probabilitiesValues = np.arange(256, dtype=np.float)
        for i in range(256):
            intensitiesValues[i] = 0

        rows, columns = image.shape
        for i in range(rows):
            for j in range(columns):
                intensitiesValues[image[i, j]] += 1

        for k in range(256):
            probabilitiesValues[k] = intensitiesValues[k] / (rows * columns)

        # Apply histogram equalization transformation function
        newIntensityValues = np.arange(256, dtype=np.float)
        for i in range(256):
            newIntensityValues[i] = 0

        transformedImg = image.copy()
        for i in range(256):
            sum = 0
            for j in range(i):
                sum += probabilitiesValues[j]
            newIntensityValues[i] = round(sum * 255)
        for i in range(rows):
            for j in range(columns):
                transformedImg[i, j] = newIntensityValues[image[i, j]]
        return transformedImg


    def normalizeImage(self, image):
        # Because it is an 8-bit image
        image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
        channels = cv2.split(image)
        channels[0] = self.equalizeContrast(channels[0])
        cv2.merge(channels, image)
        image = cv2.cvtColor(image, cv2.COLOR_YCrCb2RGB)
        return image

    def sharpeningImage(self, image):
        laplacianKernel = np.array(
            [[0, -1, 0],
             [-1, 5, -1],
             [0, -1, 0]]
        )
        return cv2.filter2D(image, -1, laplacianKernel)

    def performPreprocessing(self, image):
        #image = self.resizingImage(image)
        image = self.normalizeImage(image)
        return image

    def backingupImage(self, image):
        cv2.imwrite("../../assets/images/PreprocessingResults/PreprocessingResults.png", image)