from datetime import date, datetime

import cv2


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
        self.__values = []
        self.__valuesNoOffset = []
        self.initValues()

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

    def initValues(self):
        days_between = (self.endDateTime - self.startDateTime).days
        graph_starter_value = self.getXStarterValue(self.__imgInGrayscale)
        graph_end_value = self.getXEndValue(self.__imgInGrayscale, self.getXStarterValue(self.__imgInGrayscale))
        pixel_per_day = getPixelsPerDay(graph_starter_value, graph_end_value, days_between)

        for i in range(graph_end_value - graph_starter_value):
            self.__values.append([i, i * pixel_per_day])

    # Y-Offset always the same => Hardcode
    yStarterOffset = -72
    # startDate always the same => Hardcode
    startDateTime = datetime(2018, 1, 1, 0, 0, 0)
    # endDate always the same => Hardcode
    endDateTime = datetime(2021, 3, 1, 0, 0, 0)

    def getXStarterValue(self, image):
        width = image.shape[1]
        for index in range(width):
            if image[self.yStarterOffset, index] == 178:
                return index + 1

    def getXEndValue(self, image, xStarter):
        width = image.shape[1]
        for index in range(width)[xStarter:]:
            if image[self.yStarterOffset, index] == 255:
                return index - 2


def convertImageIntoGrayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def getPixelsPerDay(graphStartValue, graphEndValue, daysBetween):
    return daysBetween / (graphEndValue - graphStartValue)
