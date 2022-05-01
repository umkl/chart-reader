import math
import os

import cv2
import pytesseract
from pytesseract import Output

# THANKS WINDOWS
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'


class LogAxis:
    """
        Class for 10-Logarithm-Values on YAxis

        img {cv2.image} -- input image containing yaxis
        values {[number, number]} -- list for log-values on each row/y-axis or preciser
        valuesNoOffset {[number, number]} -- list for log-values on each row/y-axis or preciser with no Offset (according to pixel values on image)
    """

    # vertical distance from y=height to x-axis. must be negated (-72 = 72 from bottom)
    originHeight = 72
    originGrayVal = 178  # grayscale value for the origin pixel

    def __init__(self, img):
        self.__img = img
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

    valuesNoOffset = property(
        fget=getValuesNoOffset, fset=setValuesNoOffset, fdel=delValuesNoOffset, doc=None)

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
            # Wonn d Achse aufhead, oiso da Grauwert s erste moi weiß is
            if self.__gray[i, origin_x_pos] == 255:
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

        unit_steps = [self.__values[0]]

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
        resize_time = 4
        y_axis_x_pos = self.getOriginXPos()

        # Y-Value at X-Axis is 0
        values_unit_steps = {self.__values[0]: 0}

        for unit_step in self.__unitSteps:
            img = getCroppedImage(self.__img, x_starter=0, x_end=y_axis_x_pos,
                                  y_starter=unit_step - 8, y_end=unit_step + 8)
            img = cv2.resize(img, None, fx=resize_time,
                             fy=resize_time, interpolation=cv2.INTER_CUBIC)
            result = pytesseract.image_to_data(img, config='-c tessedit_char_whitelist=10.',
                                               output_type=Output.DICT)

            for i in range(0, len(result["text"])):
                number = result["text"][i]
                if number.strip() != '':
                    if number == '1.00000':
                        number = '100000'
                    values_unit_steps[unit_step] = number
            try:
                if values_unit_steps[unit_step]:
                    continue
            except KeyError:
                values_unit_steps[unit_step] = '1'

        return values_unit_steps

    def getFromGraphPosition(self, y_value):
        y_value_converted = (y_value - self.__values[0]) * -1
        return self.getValueOfPosition(y_value_converted)

    # Calculate value from y position with offset
    def getValueOfPosition(self, y_value):
        unitStepBefore = self.__unitSteps[0]
        unitStepAfter = 0

        for i in range(0, len(self.__valuesUnitSteps)):
            unitStep = list(self.__valuesUnitSteps.keys())[i]
            if unitStep == y_value:
                return self.__valuesUnitSteps.get(unitStep)
            if unitStep < y_value and (unitStep > unitStepAfter or unitStepAfter == 0):
                unitStepAfter = unitStep
            if unitStep > y_value and (unitStep < unitStepBefore or unitStepBefore == 0):
                unitStepBefore = unitStep

        unitStepDiff = unitStepBefore - unitStepAfter
        yDiff = y_value - unitStepAfter

        valueRelation = 1 - yDiff / unitStepDiff
        valueBefore = float(self.__valuesUnitSteps.get(unitStepBefore))
        if valueBefore == 0:
            logBefore = 0
        else:
            logBefore = math.log10(valueBefore)

        return math.pow(10, logBefore + valueRelation)


def getCroppedImage(image, x_starter, x_end, y_starter, y_end):
    return image[y_starter:y_end, x_starter:x_end]


# 200 von xachse
# 255 * log()
# 255*log(wert)=y
# wert= 10^((1000+y)/255)
# wert = 10^((756+y)/255)
# wert = 10^((offset from bottom+y)/pixelheightofonecolumn)

# 0 = 648
# 1 = 639
# 2 = 384
# d = 264
# 9

# x = 100


# look at origin pixel to determine whether it is actually the origin
# we cannot expect the origin to be on the same x-coordinate, due to values of varying lengths on the y-axis' legend

# originYPos = -72. pixel von links unten
# originHexVal = '#b0b0b0'


# hobs do eine do, damits nd beim import ausgführt wird
if __name__ == "__main__":
    for root, dirs, files in os.walk('../docs/Beispiele'):
        for filename in files:
            if filename.endswith('.png'):
                imgPath = os.path.join(root, filename)
                print(imgPath)
                axis = LogAxis(imgPath)
                print(axis.getValueOfPosition(250))
