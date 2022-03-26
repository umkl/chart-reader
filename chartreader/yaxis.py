import os
import cv2

# TODO (jonik): Lea braucht nur Striche bei de Zoihn
# Spalte links von da y-Achse von unten durchgeh, Obstände zwischen graue Pixel (Logarithmus-Striche) messen.
# Soboid da Obstond greßa is ois da vorherige, wiss ma, dass do a Zoih daneben steht und speichern den y-Wert von dem Strich fiad Lea.

class LogAxis:
    """
        Class for 10-Logarithm-Values on YAxis

        img {cv2.image} -- input image containing yaxis
        values {[number, number]} -- list for log-values on each row/y-axis or preciser
        valuesNoOffset {[number, number]} -- list for log-values on each row/y-axis or preciser with no Offset (according to pixel values on image)
    """

    originHeight = -72
    originGrayVal = 178
    unitStepGrayVal = 160

    def __init__(self, img):
        self.__img = img
        self.__values = self.getYAxisValuesOffset()
        self.__valuesNoOffset = self.getYAxisValues()

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
        gray = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        width = gray.shape[1]
        origin_x_pos = -1
        for i in range(width):
            if gray[self.originHeight, i] == self.originGrayVal:
                origin_x_pos = i

        return origin_x_pos

    def getYAxisValuesOffset(self):
        origin_x_pos = self.getOriginXPos()
        gray = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        height = gray.shape[0]

        axis_end_y = -1
        for i in range(height + self.originHeight, 0, -1): # Spalte von da y-Achse wird von unten noch oben durch gonga (Werte umdraht weil links oben = 0/0, height + weil originHeight negativ)
            if gray[i, origin_x_pos] == 255: # Wonn d Achse aufhead, oiso da Grauwert s erste moi weiß is
                axis_end_y = i + 1
                break

        axis_values = [*range(axis_end_y, height + (self.originHeight + 1))]

        return axis_values

    def getYAxisValues(self):
        values = self.getYAxisValuesOffset()
        for i in values:
            i = i + self.originHeight
        return values

    # Confirmed working for images:
    #   /docs/Beispiele/Run 22/00.0-25.0-30.0-20000.0-24.0-27.0-00.0-02.0-10.0-NONE.png
    #   /docs/Beispiele/Run 22/00.0-75.0-44.0-20000.0-52.0-41.0-00.0-20.0-50.0-NONE.png
    #   /docs/Beispiele/Run 9/00.0-08.0-79.0-80.0-100.0-80.0-01.0-12.0-06.0-NONE.png

    def getYAxisUnitSteps(self):
        x_pos = self.getOriginXPos() - 1
        gray = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)

        axisValues = self.__values
        axisValues.reverse()

        oldDiff = 0
        curDiff = 0
        stepDiff = 0
        lastYValue = 0
        unitSteps = []

        for i in axisValues:
            if self.isUnitStep(gray, x_pos, i):
                # oldDiff = curDiff
                # curDiff = lastYValue - i
                # if curDiff > oldDiff:
                unitSteps.append(i)
                # lastYValue = i

        # stepDiff = unitSteps[0] - unitSteps[1] # could throw an exception

        for i in unitSteps:
            self.__img[i, x_pos] = (0, 0, 255)

        cv2.imshow('img', self.__img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def isUnitStep(self, gray, x, y):
        if gray[y, x] == 255:
            return False

        for i in range(1, 5):
            if gray[y - i, x] != 255:
                return False

        if gray[y, x - 6] == 255 and gray[y, x - 8] == 255:
            return False

        return True




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
    # axis = LogAxis(cv2.imread('../docs/Beispiele/Run 9/00.0-08.0-35.0-35.0-40.0-30.0-01.0-04.0-02.0-NONE.png'))
    # axis.getYAxisUnitSteps()
    for root, dirs, files in os.walk('../docs/Beispiele'):
        for filename in files:
            if filename.endswith('.png'):
                imgPath = os.path.join(root, filename)
                print(imgPath)
                axis = LogAxis(cv2.imread(imgPath))
                axis.getYAxisUnitSteps()
