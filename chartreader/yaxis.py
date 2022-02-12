from const import *
import cv2

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

    # def defineValues():
    #     for i in range(1000):

img = cv2.imread('../docs/Beispiele/Run 9/00.0-08.0-35.0-35.0-40.0-30.0-01.0-04.0-02.0-NONE.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)

# originYPos = -72
# originXPos = 103
# originHexVal = '#b0b0b0'
# while (originXPos < 0)
#
#
# cv2.imshow('img', img)
# cv2.waitKey(0)

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
