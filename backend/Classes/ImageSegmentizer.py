import cv2
import numpy as np
from backend.Classes.ImagePreprocessor import ImagePreprocessor

class ImageSegmentizer:
    def __init__(self):
        return

    def getSegmentationResults(self, img, modifiedImg):
        preprocessor = ImagePreprocessor()
        img = preprocessor.getPreprocessingResults(img)
        modifiedImg = img.copy()
        self.performSegmentation(img, modifiedImg)
        return modifiedImg

    def applyMedianBlur(self, img):
        kernelSize = 5
        cv2.medianBlur(img, kernelSize, img)
        return img

    def applyMinFilter(self, img):
        # Deep cloning image
        maskSize = 3
        maskRows = maskSize
        maskCols = maskSize
        filteredImg = img.copy()
        centerX = int(maskRows / 2)
        centerY = int(maskCols / 2)
        imgRows, imgCols = img.shape
        for r in range(imgRows - maskRows):
            for c in range(imgCols - maskCols):
                min = 255
                for i in range(maskRows):
                    for j in range(maskCols):
                        intensity = img[i + r, j + c]
                        if (intensity < min):
                            min = intensity
                b = min
                filteredImg.itemset((r, c), b)
        return filteredImg

    def applyLaplacianFilter(self, img):
        threshold = 2
        offset = 10 - threshold
        sharpedImg = img.copy()
        sharpeningMask = np.array(
            [[1, 1, 1],
             [1, -8, 1],
             [1, 1, 1]]
        )
        imgRows, imgCols = img.shape
        maskRows, maskCols = sharpeningMask.shape
        centerX = int(maskRows / 2)
        centerY = int(maskCols / 2)
        for r in range(imgRows - maskRows):
            for c in range(imgCols - maskCols):
                sum = 0
                product = 1
                for i in range(maskRows):
                    for j in range(maskCols):
                        product = sharpeningMask[i, j] * img[i + r, j + c]
                        sum += product
                # Thresholding
                if (round(sum / (maskRows * maskCols)) < threshold):
                    sharpedImg[centerX + r, centerY + c] = threshold
                elif (round(sum / (maskRows * maskCols)) > threshold + offset):
                    sharpedImg[centerX + r, centerY + c] = 255
                else:
                    sharpedImg[centerX + r, centerY + c] = round(sum / (maskRows * maskCols))
        return sharpedImg

    def applyHighboostFilter(self, img):
        threshold = 3
        dullImg = img.copy()
        boostingMask = np.array(
            [[-1, -1, -1],
             [-1, 9, -1],
             [-1, -1, -1]]
        )
        imgRows, imgCols = img.shape
        maskRows, maskCols = boostingMask.shape
        centerX = int(maskRows / 2)
        centerY = int(maskCols / 2)
        for r in range(imgRows - maskRows):
            for c in range(imgCols - maskCols):
                sum = 0
                product = 1
                for i in range(maskRows):
                    for j in range(maskCols):
                        product = boostingMask[i, j] * img[i + r, j + c]
                        sum += product
                # Thresholding
                if (round(sum / (maskRows * maskCols)) < threshold):
                    dullImg[centerX + r, centerY + c] = threshold
                else:
                    dullImg[centerX + r, centerY + c] = round(sum / (maskRows * maskCols))
        return dullImg

    def processSegmentation(self, greyScaleImg, segmentedColorImg):
        threshold = 8
        sharpedImg = self.applyLaplacianFilter(greyScaleImg)
        cv2.imshow("Sharpend Image", sharpedImg)
        dullImg = self.applyHighboostFilter(greyScaleImg)
        cv2.imshow("Dull Image", dullImg)
        segmentedGreyImg = greyScaleImg.copy()
        imgRows, imgCols = segmentedGreyImg.shape
        for i in range(imgRows):
            for j in range(imgCols):
                if (dullImg[i, j] <= threshold):
                    segmentedGreyImg[i, j] = 0
                else:
                    segmentedGreyImg[i, j] = 255
        cv2.imshow("Segmented Image grayscale", segmentedGreyImg)

        for i in range(imgRows):
            for j in range(imgCols):
                if (dullImg[i, j] > threshold):
                    segmentedColorImg[:, :, 0][i, j] = 255
                    segmentedColorImg[:, :, 1][i, j] = 255
                    segmentedColorImg[:, :, 2][i, j] = 255
                if (sharpedImg[i, j] == 255):
                    segmentedColorImg[:, :, 0][i, j] = 0
                    segmentedColorImg[:, :, 1][i, j] = 0
                    segmentedColorImg[:, :, 2][i, j] = 0
        cv2.imshow("Segmented Color Image", segmentedColorImg)
        return segmentedColorImg

    def performSegmentation(self, colorImg, rawImage):
        cv2.imshow("Preprocess Image", colorImg)
        greyScaleImg = cv2.cvtColor(colorImg, cv2.COLOR_RGB2GRAY)
        greyScaleImg = self.applyMedianBlur(greyScaleImg)
        greyScaleImg = self.applyMinFilter(greyScaleImg)
        img = self.processSegmentation(greyScaleImg, colorImg)
        self.backingupImage(img)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def backingupImage(self, img):
        cv2.imwrite("../../assets/images/SegmentedResults/SegmentedResults.png", img)