from reader import Reader
from chart import *
import numpy as np
import cv2 as cv

def init():
    global img
    img = cv.imread('./input/1.png')

def fetchBluestByProximity():
    for columnIndex in range(len(img[1])):
        n, i = Chart.readTheBluestValue(img[:,columnIndex])
        img[i,columnIndex] = [150,120,200] # img [y,x]
    cv.imshow('test1',img)
    cv.waitKey(0)

def main():
    init()
    fetchBluestByProximity()
    

if __name__ == "__main__":
    main()