from reader import Reader
from chart import *
import numpy as np
import cv2 as cv
import sympy as sy

INPUTFILE='./input/1.png'
XINDENT=102
YINDENT=648
YINDENTTOP=94

def init():
    global img; img = cv.imread(INPUTFILE)
    global chart; chart = Chart(img)

def main():
    init()
    present()

def evaluate(img):
    print("ok")
    # img[150:200,10:100] = [255,100,250]
    # cv.imshow('ex1',img)
    # getPointArrayOnFunction(0.1, 10, xPoint2,yPoint1, yPoint2)
    # values = Reader.loadImageIntoPixels('./input/1.png')
    # res = Chart.readTheDarkestValue(values[132])

def present():    
    # cv.line(img,(0,0),(511,511),(255,0,0),5)
    for val in chart.pixelCoordinates:
        # print(val)
        img[val[0], val[1]] = [255,150,180]
    print(chart.pixelCoordinates)
    cv.imshow('img 1',img)
    # print(img[343,160])
    cv.waitKey(0)

def drawByAvg():
    op = sumOfArray(getColorProximity([51,102,204],[51,102,204]))
    for colIndex in range(CHARTSTARTX, CHARTSTARTY):
        n, i, d = Chart.readTheBluestValue(img[:,colIndex])
        avg = sum(d) / len(d)
        img[round(avg),colIndex] = [150,120,200]

def equationSysX():
    k = sy.S('k')
    d = sy.S('d')
    x = sy.S('x')
    # sy.Eq(x**2 +1, 3*x -1)
    # print(getPointArrayOnFunction(10, 0.1, 2, 3))
    print(sy.solve( sy.Eq(101,((100*x)/399)*400+x )))

if __name__ == "__main__":
    main()