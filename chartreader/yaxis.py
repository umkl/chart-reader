import os
import cv2


class LogAxis:
    """
        Class for 10-Logarithm-Values on YAxis

        img {cv2.image} -- input image containing yaxis
        values {[number, number]} -- list for log-values on each row/y-axis or preciser
        valuesNoOffset {[number, number]} -- list for log-values on each row/y-axis or preciser with no Offset (according to pixel values on image)
    """

    originHeight = -72;
    originGrayVal = 178;

    def __init__(self, img):
        self.__img = img
        self.__values = __getYAxisValuesOffset(img)
        self.__valuesNoOffset = __getYAxisValues(img)

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

    def __getOriginXPos(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        width = gray.shape[1]
        origin_x_pos = -1
        for i in range(width):
            if gray[originHeight, i] == originGrayVal:
                origin_x_pos = i

        return origin_x_pos

    def __getYAxisValues(img):
        origin_x_pos = __getOriginXPos(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height = gray.shape[0]

        axis_end_y = -1
        for i in range(height - originHeight, 0, -1): # Spalte von da y-Achse wird von oben noch unten durch gonga
            if gray[i, origin_x_pos] == 255: # Wonn d Achse aufhead, oiso da Grauwert s erste moi ned weiß is
                axis_end_y = i
                break

        axis_values = range(axis_end_y, height - (originHeight + 1))

        return axis_values

    def __getYAxisValuesOffset(img):
        values = __getYAxisValues(img)
        for i in len(values):
            values[i] += 72
        return values


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
    for root, dirs, files in os.walk('../docs/Beispiele'):
        for filename in files:
            if filename.endswith('.png'):
                img = cv2.imread(os.path.join(root, filename))
                yValues = getYAxisValues(img)
                print('Y-Axis in image ' + filename + ' is represented by the following pixels: ' + str(yValues))
