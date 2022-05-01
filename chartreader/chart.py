import numpy as np

"""global helper functions"""
global getFragValuesBetween, linear_pitch_function, getPointArrayOnFunction, get_color_proximity, get_linear_function_from_coo


def getColorProximity(color_a, color_b):  # + rgb
    [rA, gA, bA] = color_a
    [rB, gB, bB] = color_b
    return np.abs(np.array([rA - rB, gA - gB, bA - bB]))


def getFragValuesBetween(occ, point_ax, point_ay, point_bx, point_by):
    distance = np.abs(point_bx - point_ax)
    itr = 0
    funcvals = get_linear_function_from_coo([point_ax, point_ay], [point_bx, point_by])
    k = funcvals['k']
    d = funcvals['d']
    preciseValuesBetween = []
    while itr < distance:
        pointAYonNewFragment = k * (point_ax + itr) + d
        preciseValuesBetween.append([point_ax + itr, pointAYonNewFragment])
        itr = itr + occ
    return preciseValuesBetween


def linearPitchFunction(x, k):  # f(x)=k*x+d
    return k * x


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
            [204, 102, 51], img_col[index]))
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
        self.__pixelCoordinates = []
        self.__coordinates = []

        self.chartStartValue = getChartStartValue(img)
        self.chartEndValue = self.getChartEndValue(img)
        self.definePixelCoordinates(img)
        self.defineCoordinatesByPixelCoordinates(self.pixelCoordinates)

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

    def defineCoordinatesByPixelCoordinates(self, origin_pixel_coordinates):
        for pixelCoordinate in origin_pixel_coordinates:
            self.coordinates.append(
                [pixelCoordinate[0] - 102, 648 - pixelCoordinate[1]])