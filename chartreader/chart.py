from fileinput import close
from re import A, I
from const import * 
import numpy as np
import cv2 as cv
import sympy as sy

global linearPitchFunction, getPointArrayOnFunction, getColorProximity, getLinearFunctionFromCoo # sumOfArray
def getColorProximity(colorA, colorB):#+ rgb
    [rA,gA,bA] = colorA
    [rB,gB,bB] = colorB
    return np.abs(np.array([rA-rB, gA-gB, bA-bB]))

def getLinearFunctionFromCoo(cooP1, cooP2): # cooP1[x,y], cooP2[x,y] # https://www.grund-wissen.de/informatik/python/scipy/sympy.html
    k, d = sy.symbols("k d")# f(x)=k*x+d
    equations = [
        sy.Eq(cooP1[0]*k+d, cooP1[1]),
        sy.Eq(cooP2[0]*k+d, cooP2[1]),
    ]
    return sy.solve(equations)

# def sumOfArray(inputar):
#     arr = 0
#     for i in inputar:
#         arr += i
#     return arr

def linearPitchFunction(x,k): # f(x)=k*x+d
        return k*x

def getPointArrayOnFunction( occ, xPoint1, xPoint2,yPoint1, yPoint2):##get coordinates of fractions between two pixels/points
    pitch = yPoint1-yPoint2
    points = []
    xVal = 0
    while xVal < xPoint2-xPoint1:
        points.append(linearPitchFunction(xVal,pitch))
        xVal+=occ
    return points

class Chart:
    

    def __init__(self,img):
        # self.__img = img
        self.__pixelCoordinates =[]
        self.__coordiantes = []
        self.initCoordinates(img)
    def setcoordinates(self, coordinates):
        self.__coordinates = coordinates
    def getcoordinates(self):
        return self.__coordinates
    def delcoordinates(self):
        del self.__coordinates
    coordinates=property(getcoordinates, setcoordinates, delcoordinates)
    def setPixelCoordinates(self, pixelCoordinates):
        self.__pixelCoordinates = pixelCoordinates
    def getPixelCoordinates(self):
        self.updateCoordinatesAccordingPixelCoordinates()
        return self.__pixelCoordinates
    def delPixelCoordinates(self):
        del self.__pixelCoordinates
    pixelCoordinates=property(getPixelCoordinates, setPixelCoordinates, delPixelCoordinates)
    
    def initCoordinates(self,img):
        for column in range(CHARTSTARTX, CHARTSTARTY):
            xCoordinate = self.retrieveTheBluestValueFromColumn(img[:,column])
            self.pixelCoordinates.append([xCoordinate, column])
            
    def retrieveTheBluestValueFromColumn(self, imgCol):
        closestIndexes = []
        for index in range(len(imgCol)):
            vicinity = sum(getColorProximity(BLUE,imgCol[index]))#color irrelevant
            if (vicinity < 10):#
                closestIndexes.append(index) # print("closest vicinity was: ", closestVicinity, closestIndex,getColorProximity(blue,imgCol[index]))
        return round(sum(closestIndexes)/len(closestIndexes))

    def updateCoordinatesAccordingPixelCoordinates(self):
        self.coordinates = [1,1,1]

    def getLinearFunctionFromCoo(self, cooP1, cooP2): # cooP1[x,y], cooP2[x,y] # https://www.grund-wissen.de/informatik/python/scipy/sympy.html
        k, d = sy.symbols("k d")# f(x)=k*x+d
        equations = [
            sy.Eq(cooP1[0]*k+d, cooP1[1]),
            sy.Eq(cooP2[0]*k+d, cooP2[1]),
        ]
        return sy.solve(equations)


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

