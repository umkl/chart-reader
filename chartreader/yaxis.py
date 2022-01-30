from const import * 

class LogAxis:
    """
        Class for 10-Logarithm-Values on YAxis

        img {cv2.image} -- input image containing yaxis
        values {[number, number]} -- list for log-values on each row/y-axis or preciser
        valuesNoOffset {[number, number]} -- list for log-values on each row/y-axis or preciser with no Offset (according to pixel values on image)
    """

    def __init__(self, img):
        self.__img = img
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