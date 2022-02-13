import os
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


# look at origin pixel to determine whether it is actually the origin
# we cannot expect the origin to be on the same x-coordinate, due to values of varying lengths on the y-axis' legend

# originYPos = -72. pixel
# pos san von links unten
# originHexVal = '#b0b0b0'

# while (originXPos < 0)
#
#
# cv2.imwrite('gray.jpg', gray)
# cv2.imshow('img', img)
# cv2.waitKey(0)


def getOriginXPos(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    width = gray.shape[1]
    origin_x_pos = -1
    for i in range(width):
        if gray[-72, i] == 178:
            origin_x_pos = i

    return origin_x_pos

# hobs do eine do, damits nd beim import ausgführt wird
if __name__ == "__main__":
    for root, dirs, files in os.walk('../docs/Beispiele'):
        for filename in files:
            if filename.endswith('.png'):
                originX = getOriginXPos(os.path.join(root, filename))
                print('Chart origin for ' + filename + ' is in position: -72/' + str(originX))
