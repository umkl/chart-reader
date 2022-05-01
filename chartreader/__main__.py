"""python imports"""
import sys
import os

import cv2

"""3rd imports"""
import numpy
import cv2 as cv
import sympy as sy

"""imports from our implementation"""
from chart import *
from const import *
from result import *

# from PIL import Image
# import matplotlib.pyplot as plt

def main():
    if 2 > len(sys.argv) < 2:
        print("USAGE 'python main.py {InputFilePath} {OutputFilePath}'")
        return

    image = getImage(sys.argv[1])

    """initialize all classes for _DI_"""
    init(image, sys.argv[2])

    """trying out current functionalities"""
    # testsomestuff()

    """display manipulated pixels using the opencv-window"""
    # present(image)

    """log to csv by using result class"""
    log()


def getImage(input_path):
    return cv2.imread(input_path)


def init(image, output_path):
    # creating a global version of the image
    global img
    img = image

    global chart
    chart = Chart(img)

    global dateAxis
    dateAxis = DateAxis(img)
    
    global logaxis; logaxis = LogAxis(img)

    # combining all data from all 3 sections(chart, dateaxis, logaxis) and the output Path together
    # -> applying tests, logging to csv
    global result
    result = Result(chart, dateAxis, logaxis, output_path)


def log():
    result.mapDate() 
    result.mapLogValuesEasy()
    # result.createFullMapped()
    result.simpleLogChart()
    
    # result.mapM() # map values to beispiel 1 
    # result.simpleLogChart()
    # result.logTest()
    # result.simpleLogChart()


def present():

    cv.imshow("Image:", img)
    cv.waitKey(0)

    # pil for windows/macos
    # 1
    # img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # im_pil = Image.fromarray(img2)
    # im_pil.show()

    # 2
    # plt_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # imgplot = plt.imshow(plt_image)
    # cv.waitKey(0)


"""test functions:"""


def testsomestuff():
    for index, value in range(logaxis.values):
        print(value)
        # print("index: %s, value: %s" % [index, value])

    # drawFromChartOnImage()
    # print(getLinearFunctionFromCoo([100,120],[101, 130]))
    # extractValuesFromCoordinates()
    # drawCoordinatesOnImage()
    # result.logToCsv()
    # testDateAxis()


def drawFromChartOnImage():
    for i in chart.pixelCoordinates:
        img[i[1], i[0]] = [150, 120, 200]


def testDateAxis():
    print(dateAxis.values)


def drawCoordinatesOnImage():
    # cv.line(img,(0,0),(511,511),(255,0,0),5)

    for val in chart.getConverted():
        img[val[1], val[0]] = [255, 150, 180]  # img[y,x] - flipped format
    # print(chart.pixelCoordinates)


def drawByAvg():
    op = sum(getColorProximity([51, 102, 204], [51, 102, 204]))
    for colIndex in range(CHARTSTARTX, CHARTSTARTY):
        n, i, d = Chart.readTheBluestValue(img[:, colIndex])
        avg = sum(d) / len(d)
        img[round(avg), colIndex] = [150, 120, 200]


def equationSysX():
    k = sy.S('k')
    d = sy.S('d')
    x = sy.S('x')
    # sy.Eq(x**2 +1, 3*x -1)
    # print(getPointArrayOnFunction(10, 0.1, 2, 3))
    print(sy.solve(sy.Eq(101, ((100 * x) / 399) * 400 + x)))


def extractValuesFromCoordinates():
    # print(getFragValuesBetween(0.2,10,12,100,120))
    # k = sy.S('k')
    # d = sy.S('d')
    # k,d = getLinearFunctionFromCoo([10,12],[100, 120])
    # print(d.values())
    # x = sy.S('x')
    # sol = sy.solve( sy.Eq(1000, 3*x -1) )
    # print(sol[0]*2)
    # print(chart.pixelCoordinates)
    # print(getFragValuesBetween(0.1,10,20,100,200))
    # img[150:200,10:100] = [255,100,250]
    # cv.imshow('ex1',img)
    # getPointArrayOnFunction(0.1, 10, xPoint2,yPoint1, yPoint2)
    # values = Reader.loadImageIntoPixels('./input/1.png')
    # res = Chart.readTheDarkestValue(values[132])
    return 0


# makes the file importable, so code does not get executed by importing our lib
if __name__ == "__main__":
    main()
