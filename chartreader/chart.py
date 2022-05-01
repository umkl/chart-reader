from const import *
import numpy as np
import sympy as sy

"""global helper functions"""
global getFragValuesBetween, linear_pitch_function, getPointArrayOnFunction, get_color_proximity, get_linear_function_from_coo


def getColorProximity(color_a, color_b):  # + rgb
    [rA, gA, bA] = color_a
    [rB, gB, bB] = color_b
    return np.abs(np.array([rA - rB, gA - gB, bA - bB]))


# cooP1[x,y], cooP2[x,y] # https://www.grund-wissen.de/informatik/python/scipy/sympy.html
def getLinearFunctionFromCoo(coo_p1, coo_p2):
    k, d = sy.symbols("k d")  # f(x)=k*x+d
    # k = sy.S('k')
    # d = sy.S('d')
    equations = [
        sy.Eq(coo_p1[0] * k + d, coo_p1[1]),
        sy.Eq(coo_p2[0] * k + d, coo_p2[1]),
    ]

    solution = sy.solve(equations)
    k = solution[k]
    d = solution[d]

    return {'k': sy.N(k), 'd': sy.N(d)}


# pixelA[x,y],pixelB[x,y]
def getFragValuesBetween(occ, point_ax, point_ay, point_bx, point_by):
    distance = np.abs(point_bx - point_ax)
    itr = 0  # iterator for each fragment between points
    funcvals = get_linear_function_from_coo([point_ax, point_ay], [point_bx, point_by])
    k = funcvals['k']
    d = funcvals['d']
    preciseValuesBetween = []
    while itr < distance:
        # increasing pointAX by the fragment iterator and using this new xvalue with
        pointAYonNewFragment = k * (point_ax + itr) + d
        preciseValuesBetween.append([point_ax + itr, pointAYonNewFragment])
        itr = itr + occ
    return preciseValuesBetween


def linearPitchFunction(x, k):  # f(x)=k*x+d
    return k * x


# get coordinates of fractions between two pixels/points
def getPointArrayOnFunction(occ, x_point1, x_point2, y_point1, y_point2):
    pitch = y_point1 - y_point2
    points = []
    xVal = 0
    while xVal < x_point2 - x_point1:
        points.append(linear_pitch_function(xVal, pitch))
        xVal += occ
    return points


def retrieveTheBluestValueFromColumn(img_col):
    closestIndexes = []
    for index in range(len(img_col)):
        vicinity = sum(getColorProximity(
            BLUE, img_col[index]))  # color irrelevant
        if vicinity < 10:
            closestIndexes.append(index)
    return round(sum(closestIndexes) / len(closestIndexes))


def getChartStartValue(img):
    for columnIndex in range(0, len(img[0])):
        val = img[:, columnIndex]
        try:
            retrieveTheBluestValueFromColumn(val)
            return columnIndex
        except ZeroDivisionError:
            continue


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

        self.chartStartValue = getChartStartValue(img)
        self.chartEndValue = self.getChartEndValue(img)
        # retrieving pixel values by bluest value
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

    def setPixelCoordinates(self, pixel_coordinates):
        self.__pixelCoordinates = pixel_coordinates

    def getPixelCoordinates(self):
        return self.__pixelCoordinates

    def delPixelCoordinates(self):
        del self.__pixelCoordinates

    pixelCoordinates = property(
        getPixelCoordinates, setPixelCoordinates, delPixelCoordinates)

    def getChartEndValue(self, img):
        for columnIndex in range(self.chartStartValue, len(img[0])):
            val = img[:, columnIndex]
            try:
                retrieveTheBluestValueFromColumn(val)
                continue
            except ZeroDivisionError:
                return columnIndex

    def definePixelCoordinates(self, img):
        for column in range(self.chartStartValue, self.chartEndValue):
            try:
                yCoordinate = retrieveTheBluestValueFromColumn(img[:, column])
            except ZeroDivisionError:
                yCoordinate = 0
            self.pixelCoordinates.append([column, yCoordinate])

    def getPixelValuesFrag(self, occ):
        for itr in range(len(self.pixelCoordinates)):
            pointAX = self.pixelCoordinates[itr, 0]  # [[x,y]]
            pointBX = self.pixelCoordinates[itr + 1, 0]  # [x,y]
            pointAY = self.pixelCoordinates[itr, 1]
            pointBY = self.pixelCoordinates[itr + 1, 1]
        return getFragValuesBetween(occ, pointAX, pointBX, pointAY, pointBY)

    def defineCoordinatesByPixelCoordinates(self, origin_pixel_coordinates):
        for pixelCoordinate in origin_pixel_coordinates:
            self.coordinates.append(
                [pixelCoordinate[0] - XINDENT, YINDENT - pixelCoordinate[1]])