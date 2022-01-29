from reader import Reader
from chart import *
import numpy as np
import cv2 as cv

def init():
    global img
    global chartCoo
    img = cv.imread('./input/1.png')

def fetchBluestByProximity():
    chartCoo = []
    for xColumnIndex in range(len(img[1])):
        n, yBluestIndex = Chart.readTheBluestValue(img[:,xColumnIndex])
        img[yBluestIndex,xColumnIndex] = [150,120,200] # img [y,x]
        chartCoo.append([xColumnIndex, yBluestIndex]) # chartVal [x, y]
    # print(chartCoo)
    cv.imshow('test1',img)
    cv.waitKey(0)

def main():
    init()
    fetchBluestByProximity()

if __name__ == "__main__":
    main()