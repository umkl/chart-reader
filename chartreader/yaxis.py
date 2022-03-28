import math
import os
import cv2
from pytesseract import Output
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd =  r'C:\Users\Lea\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class LogAxis:
    """
        Class for 10-Logarithm-Values on YAxis

        img {cv2.image} -- input image containing yaxis
        values {[number, number]} -- list for log-values on each row/y-axis or preciser
        valuesNoOffset {[number, number]} -- list for log-values on each row/y-axis or preciser with no Offset (according to pixel values on image)
    """

    originHeight = 72  # vertical distance from y=height to x-axis. must be negated (-72 = 72 from bottom)
    originGrayVal = 178  # grayscale value for the origin pixel

    def __init__(self, imgPath):
        self.__imgPath = imgPath
        self.__img = cv2.imread(imgPath)
        self.__gray = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        self.__values = self.getYAxisValuesOffset()
        self.__valuesNoOffset = self.getYAxisValues()
        self.__unitSteps = self.getYAxisUnitSteps()
        self.__valuesUnitSteps = self.getPositionOfNumbers()

    def setValues(self, val):
        self.__values = val

    def getValues(self):
        return self.__values

    def delValues(self):
        del self.__values

    values = property(fget=getValues, fset=setValues, fdel=delValues, doc=None)

    def setValuesNoOffset(self, val):
        self.__valuesNoOffset = val

    def getValuesNoOffset(self):
        return self.__valuesNoOffset

    def delValuesNoOffset(self):
        del self.__valuesNoOffset

    valuesNoOffset = property(fget=getValuesNoOffset, fset=setValuesNoOffset, fdel=delValuesNoOffset, doc=None)

    def getOriginXPos(self):
        width = self.__gray.shape[1]

        for i in range(width):
            if self.__gray[-self.originHeight, i] == self.originGrayVal:
                return i

    def getYAxisValuesOffset(self):
        origin_x_pos = self.getOriginXPos()
        height = self.__gray.shape[0]

        axis_end_y = -1
        for i in range(height - self.originHeight, 0, -1):
            # Spalte von da y-Achse wird von unten noch oben durch gonga (Werte umdraht weil links oben = 0/0)
            if self.__gray[i, origin_x_pos] == 255:  # Wonn d Achse aufhead, oiso da Grauwert s erste moi weiß is
                axis_end_y = i + 1
                break

        axis_values = [*range(axis_end_y, height - self.originHeight + 1)]

        return axis_values

    def getYAxisValues(self):  # relative to origin height (0 in result = -72 in image)
        values = self.getYAxisValuesOffset()

        for i in values:
            i = i - self.originHeight

        return values

    def getYAxisUnitSteps(self):
        x_pos = self.getOriginXPos() - 1

        axis_values = self.__values
        axis_values.reverse()

        unit_steps = []

        for i in axis_values:
            if self.isUnitStep(x_pos, i):
                unit_steps.append(i)

        return unit_steps

    def isUnitStep(self, x, y):
        if self.__gray[y, x] == 255:
            return False

        for i in range(1, 5):
            if self.__gray[y - i, x] != 255:
                return False

        if self.__gray[y, x - 6] == 255 and self.__gray[y, x - 8] == 255:
            return False

        return True

    def getPositionOfNumbers(self):
        # get the position of every numeric text in the image
        results = pytesseract.image_to_data(self.__imgPath, lang="eng", config='-c tessedit_char_whitelist=01.',
                                            output_type=Output.DICT)
        origin_x_pos = self.getOriginXPos()
        values_unit_steps = {}

        for i in range(0, len(results["text"])):
            if (results["left"][i] + results["width"][i] < origin_x_pos):
                top = results["top"][i]
                height = results["height"][i]
                number = results["text"][i]

                unitStepIndex = np.where(self.__unitSteps < top & self.__unitSteps > top + height)
                unitStep = self.__unitSteps[unitStepIndex]
                values_unit_steps[unitStep] = number

        return values_unit_steps

    # Calculate value from y position with offset
    def getValueOfPosition(self, yValue):
        unitStepBefore = 0
        unitStepAfter = 0

        for i in range(0, len(self.__unitSteps)):
            unitStep = self.__valuesUnitSteps.keys()[i]
            if (unitStep == yValue): return self.__valuesUnitSteps.get(unitStep)
            if (unitStep < yValue & (unitStep > unitStepAfter or unitStepAfter == 0)):
                unitStepAfter = unitStep
            if (unitStep > yValue & (unitStep < unitStepBefore or unitStepBefore == 0)):
                unitStepBefore = unitStep

        unitStepDiff = unitStepBefore - unitStepAfter
        yDiff = yValue - unitStepAfter

        valueRelation = 1 - yDiff / unitStepDiff
        valueBefore = self.__valuesUnitSteps.get(unitStepBefore)
        logBefore = math.log10(valueBefore)

        return math.pow(10, logBefore + valueRelation)


# 200 von xachse
# 255 * log()
# 255*log(wert)=y
# wert= 10^((1000+y)/255)
# wert = 10^((756+y)/255)

# 0 = 648
# 1 = 639
# 2 = 384
# d = 264
# 9

# x = 100

# hobs do eine do, damits nd beim import ausgführt wird
if __name__ == "__main__":
    # for root, dirs, files in os.walk('../docs/Beispiele'):
    #     for filename in files:
    #         if filename.endswith('.png'):
    #             imgPath = os.path.join(root, filename)
    #             axis = LogAxis(imgPath)
    #             axis.getYAxisUnitSteps()
    imgPath = '../docs/Beispiele/Run 22/00.0-15.0-02.0-20000.0-10.0-20.0-00.0-02.0-10.0-NONE.png'
    axis = LogAxis(imgPath)
    axis.getValueOfPosition(308)

