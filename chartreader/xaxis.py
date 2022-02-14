from const import * 


class DateAxis:
    """
        Class for DateValues on XAxis

        img {cv2.image} -- input image containing xaxis
        values {[number, date]} -- list for dates on each column/x-axis or preciser  
        valuesNoOffset {[number, number]} -- list for dates on each row/x-axis or preciser with no Offset (according to pixel values on image)
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

    def detectAxis(self):
        someColumn = []
        for i in img[1,i]:
            someColumn.append([i,4])#y,x
        return someColumn

        