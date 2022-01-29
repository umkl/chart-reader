from fileinput import close
from re import A, I
import numpy as np
import cv2 as cv

global getColorProximity
global sumOfArray
global linearPitchFunction
global getPointArrayOnFunction

def getColorProximity(colorA, colorB):#+ rgb
    [rA,gA,bA] = colorA
    [rB,gB,bB] = colorB
    return np.abs(np.array([rA-rB, gA-gB, bA-bB]))

def sumOfArray(inputar):
    arr = 0
    for i in inputar:
        arr += i
    return arr

def linearPitchFunction(x,k): # f(x)=k*x+d
        return k*x


class Chart:
    global BLUE; BLUE = [204,102,51] # b g r 
    global CHARTSTARTX; CHARTSTARTX=122+1
    global CHARTSTARTY; CHARTSTARTY=1231

    def __init__(self,img):
        # self.__img = img
        self.coordiantes = []
        self.initCoordinates(img)
    def setcoordinates(self, coordinates):
        self.__coordinates = coordinates
    def getcoordinates(self):
        return self.__coordinates
    def delcoordinates(self):
        del self.__coordinates
    coordiantes=property(getcoordinates, setcoordinates, delcoordinates)
    
    def initCoordinates(self,img):
        for column in range(len(img)):
            xCoordinate = self.retrieveTheBluestValueFromColumn(img[column])
            self.coordiantes.append([xCoordinate, column])
            
    def retrieveTheBluestValueFromColumn(self, imgCol):
        # 3366cc - r: 51, g: 102, b: 204
        closestVicinity = 765
        closestIndex = 0
        closestIndexes = []
        for index in range(CHARTSTARTX, CHARTSTARTY):
            # print(sumOfArray(getColorProximity(blue,imgCol[index])))
            # if(blue == blue):
            # print(imgCol[index])
            # print(blue)
            # # print(getColorProximity(blue,imgCol[index]))
            vicinity = sumOfArray(getColorProximity(BLUE,imgCol[index]))#color irrelevant
            if(vicinity < 10):
                    closestIndexes.append(index)
            if(vicinity < closestVicinity):
                closestIndexes.append(index)
                # print("closest vicinity was: ", closestVicinity, closestIndex,getColorProximity(blue,imgCol[index]))
                closestVicinity = vicinity
                closestIndex = index                                    
        return np.abs(sum(closestIndexes)/len(closestIndexes))

def getPointArrayOnFunction( occ, xPoint1, xPoint2,yPoint1, yPoint2):##get coordinates of fractions between two pixels/points
    pitch = yPoint1-yPoint2
    points = []
    xVal = 0
    while xVal < xPoint2-xPoint1:
        points.append(linearPitchFunction(xVal,pitch))
        xVal+=occ
    return points

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

