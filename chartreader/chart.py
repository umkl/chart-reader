from fileinput import close
from lib2to3.pgen2.token import INDENT
from re import A, I
from const import *
import numpy as np
import cv2 as cv
import sympy as sy

"""global helper functions"""
global getFragValuesBetween, linearPitchFunction, getPointArrayOnFunction, getColorProximity, getLinearFunctionFromCoo  # sumOfArray


def getColorProximity(colorA, colorB):  # + rgb
    [rA, gA, bA] = colorA
    [rB, gB, bB] = colorB
    return np.abs(np.array([rA-rB, gA-gB, bA-bB]))


# cooP1[x,y], cooP2[x,y] # https://www.grund-wissen.de/informatik/python/scipy/sympy.html
def getLinearFunctionFromCoo(cooP1, cooP2):
    k, d = sy.symbols("k d")  # f(x)=k*x+d
    # k = sy.S('k')
    # d = sy.S('d')
    equations = [
        sy.Eq(cooP1[0]*k+d, cooP1[1]),
        sy.Eq(cooP2[0]*k+d, cooP2[1]),
    ]

    solution = sy.solve(equations)
    k = solution[k]
    d = solution[d]

    return {'k': sy.N(k), 'd': sy.N(d)}


# pixelA[x,y],pixelB[x,y]
def getFragValuesBetween(occ, pointAX, pointAY, pointBX, pointBY):
    distance = np.abs(pointBX - pointAX)
    itr = 0  # iterator for each fragment between points
    funcvals = getLinearFunctionFromCoo([pointAX, pointAY], [pointBX, pointBY])
    k = funcvals['k']
    d = funcvals['d']
    preciseValuesBetween = []
    while itr < distance:
        # increasing pointAX by the fragment iterator and using this new xvalue with
        pointAYonNewFragment = k * (pointAX + itr) + d
        preciseValuesBetween.append([pointAX+itr, pointAYonNewFragment])
        itr = itr + occ
    return preciseValuesBetween


def linearPitchFunction(x, k):  # f(x)=k*x+d
    return k*x


# get coordinates of fractions between two pixels/points
def getPointArrayOnFunction(occ, xPoint1, xPoint2, yPoint1, yPoint2):
    pitch = yPoint1-yPoint2
    points = []
    xVal = 0
    while xVal < xPoint2-xPoint1:
        points.append(linearPitchFunction(xVal, pitch))
        xVal += occ
    return points


class Chart:
    """Class for the chart values

        img {cv2.image} -- input image containing chart
        coordinates {number[,]} -- coordinates with offset - according to the coordinate-system
        pixelCoordinates {number[,]} -- coordinates without offset - according to the pixels on the image
    """

    def __init__(self, img):
        # self.__img = img
        self.__pixelCoordinates = []
        self.__coordinates = []

        self.chartStartValue = self.getChartStartValue(img)
        self.chartEndValue = self.getChartEndValue(img)
        # retriving pixel values by bluest value
        self.definePixelCoordinates(img)
        self.defineCoordinatesByPixelCoordinates(self.pixelCoordinates)
        # self.chartEndValue

    def setcoordinates(self, coordinates):
        self.__coordinates = coordinates

    def getcoordinates(self):
        return self.__coordinates

    def delcoordinates(self):
        del self.__coordinates
    coordinates = property(getcoordinates, setcoordinates, delcoordinates)

    def setPixelCoordinates(self, pixelCoordinates):
        self.__pixelCoordinates = pixelCoordinates

    def getPixelCoordinates(self):
        return self.__pixelCoordinates

    def delPixelCoordinates(self):
        del self.__pixelCoordinates
    pixelCoordinates = property(
        getPixelCoordinates, setPixelCoordinates, delPixelCoordinates)

    def getChartStartValue(self, img):
        for columnIndex in range(0, len(img[0])):
            val = img[:, columnIndex]
            try:
                bluest = self.retrieveTheBluestValueFromColumn(val)
                return columnIndex
            except ZeroDivisionError:
                continue

    def getChartEndValue(self, img):
        for columnIndex in range(self.chartStartValue, len(img[0])):
            val = img[:, columnIndex]
            try:
                bluest = self.retrieveTheBluestValueFromColumn(val)
                continue
            except ZeroDivisionError:
                return columnIndex

    def definePixelCoordinates(self, img):
        for column in range(self.chartStartValue, self.chartEndValue):
            try:
                secolumn = img[:, column]
                yCoordinate = self.retrieveTheBluestValueFromColumn(
                    img[:, column])
            except ZeroDivisionError:
                yCoordinate = 0
            self.pixelCoordinates.append([column, yCoordinate])

    def retrieveTheBluestValueFromColumn(self, imgCol):
        closestIndexes = []
        for index in range(len(imgCol)):
            vicinity = sum(getColorProximity(
                BLUE, imgCol[index]))  # color irrelevant
            if (vicinity < 10):
                # print("closest vicinity was: ", closestVicinity, closestIndex,getColorProximity(blue,imgCol[index]))
                closestIndexes.append(index)
        return round(sum(closestIndexes)/len(closestIndexes))

    def getPixelValuesFrag(self, occ):
        for itr in range(len(self.pixelCoordinates)):
            pointAX = self.pixelCoordinates[itr, 0]  # [[x,y]]
            pointBX = self.pixelCoordinates[itr+1, 0]  # [x,y]
            pointAY = self.pixelCoordinates[itr, 1]
            pointBY = self.pixelCoordinates[itr+1, 1]
        return getFragValuesBetween(occ, pointAX, pointBX, pointAY, pointBY)

    def defineCoordinatesByPixelCoordinates(self, originPixelCoordinates):
        for pixelCoordinate in originPixelCoordinates:
            self.coordinates.append(
                [pixelCoordinate[0]-XINDENT, YINDENT-pixelCoordinate[1]])


# img = cv.imread('input/1.png',1)
# # print(img.shape)
# rows, cols, _ = img.shape
# cv.imshow('1.jpg',img)
# print(img[343,160]) # 343 = y, 160 = x

# cv.waitKey(0)

# for i in range(row):
#     for j in range(cols):
#         # print(img[i,j])
#         print("current image values: " + str(i)+ str(j))
#         if(img[i,j] == [0,0,0]):
#             print("black")
#         # k = img[1,j,2]
#         # print(k)
# print(cols)
# print(img[124,309])
# for i in range(cols):
#     print("current index: ",str(i-1), ":" , img[100,i-1])


# img = cv2.imread('input/1.png')
# cv2.imshow('machine learning', img)
# B, G, R = img[100,100]
# print(B, G, R)

# img = cv2.imread('input/1.png',cv2.IMREAD_COLOR)
# print(img)
# img_file = 'images/TriColor.png'
# img = cv2.imread(img_file, cv2.IMREAD_COLOR)           # rgb
# alpha_img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED) # rgba
# gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # grayscale

# print (type(img))

# print 'RGB shape: ', img.shape        # Rows, cols, channels
# print 'ARGB shape:', alpha_img.shape
# print 'Gray shape:', gray_img.shape
# print 'img.dtype: ', img.dtype
# print 'img.size: ', img.size

# reader = Reader()
# print(reader.imagePath)
# print('ob')
