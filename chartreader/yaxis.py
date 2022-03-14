import os
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd =  r'C:\Users\Lea\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


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

# originYPos = -72. pixel von links unten
# originHexVal = '#b0b0b0'

def getOriginXPos(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    width = gray.shape[1]
    origin_x_pos = -1
    for i in range(width):
        if gray[-72, i] == 178:
            origin_x_pos = i

    return origin_x_pos


def getYAxisValues(img):
    origin_x_pos = getOriginXPos(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height = gray.shape[0]

    axis_end_y = -1
    for i in range(height - 72, 0, -1):
        if gray[i, origin_x_pos] == 255:
            axis_end_y = i
            break

    axis_values = range(axis_end_y, height - 71)
    return axis_values

def positionOfNumbers(imgPath):
    # get the position of every numeric text in the image
    results = pytesseract.image_to_data(imgPath, lang="eng", config='-c tessedit_char_whitelist=0123456789')

    for i in range(0, len(results["text"])):
        # extract the bounding box coordinates of the text region from
        # the current result
        top = results["top"][i]
        height = results["height"][i]
        # extract the OCR text itself along with the confidence of the
        # text localization
        number = float(results["text"][i])
        print(number);

# hobs do eine do, damits nd beim import ausgführt wird
if __name__ == "__main__":
    for root, dirs, files in os.walk('../docs/Beispiele'):
        for filename in files:
            if filename.endswith('.png'):
                img = cv2.imread(os.path.join(root, filename))
                yValues = getYAxisValues(img)
                print('Y-Axis in image ' + filename + ' is represented by the following pixels: ' + str(yValues))

