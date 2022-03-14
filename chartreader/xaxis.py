import os

import cv2
from datetime import date


class DateAxis:
    """
        Class for DateValues on XAxis

        img {cv2.image} -- input image containing xaxis
        values {[number, date]} -- list for dates on each column/x-axis or preciser  
        valuesNoOffset {[number, number]} -- list for dates on each row/x-axis or preciser with no Offset (according to pixel values on image)
    """

    def __init__(self, img):
        self.__img = img
        self.__imgInGrayscale = convertImageIntoGrayscale(img)
        self.__values = None
        self.__valuesNoOffset = None

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


# Y-Offset always the same => Hardcode
yStarterOffset = -72
# startDate always the same => Hardcode
startDate = date(2018, 1, 1)
# endDate always the same => Hardcode
endDate = date(2019, 3, 1)


def convertImageIntoGrayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def getXStarterValue(image):
    width = image.shape[1]
    for index in range(width):
        if image[yStarterOffset, index] == 178:
            return index + 1


def getXEndValue(image, xStarter):
    width = image.shape[1]
    for index in range(width)[xStarter:]:
        if image[yStarterOffset, index] == 255:
            return index - 2

""" depr
def getThreeMonthsSeparators(image):
    width = image.shape[1]
    seperator = []
    for index in range(width):
        if image[yStarterOffset, index] == 168:
            seperator.append(index)
    return seperator
"""


def getPixelsPerDay(graphStartValue, graphEndValue, daysBetween):
    return daysBetween / (graphEndValue - graphStartValue)


def getValues(image):
    image = convertImageIntoGrayscale(image)
    print(filename)
    starter_value = getXStarterValue(image)
    end_value = getXEndValue(image, starter_value)
    days_between = (endDate - startDate).days
    print('Day per pixel')
    print(getPixelsPerDay(starter_value, end_value, days_between))


# Gschnorrt vo da y-Axis
if __name__ == "__main__":
    for root, dirs, files in os.walk('../docs/Beispiele'):
        for filename in files:
            if filename.endswith('.png'):
                img = cv2.imread(os.path.join(root, filename))
                getValues(img)