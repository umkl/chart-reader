from fileinput import close
from re import A, I
import numpy as np
import cv2 as cv

global getColorProximity
global sumOfArray

def getColorProximity(colorA, colorB):#+ rgb
    [rA,gA,bA] = colorA
    [rB,gB,bB] = colorB
    return np.abs(np.array([rA-rB, gA-gB, bA-bB]))

def sumOfArray(inputar):
    arr = 0
    for i in inputar:
        arr += i
    return arr


class Chart:

    def __init__(self,bValues):
        self.bValues = bValues

    def loadImageIntoPixels(self, url):
        img = cv.imread('./input/1.png')
        # cv2.imshow('image',img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        self.ar = img
    
    def readTheBluestValue(imgCol):
        # 3366cc - r: 51, g: 102, b: 204
        blue = [204,102,51] # b g r 
        closestVicinity = 765
        closestIndex = 0
        closestIndexes = []
        for index in range(len(imgCol)):
            # print(sumOfArray(getColorProximity(blue,imgCol[index])))
            # if(blue == blue):
                # print(imgCol[index])
                # print(blue)
            # # print(getColorProximity(blue,imgCol[index]))
            vicinity = sumOfArray(getColorProximity(blue,imgCol[index]))#color irrelevant
            if(vicinity == closestIndex or vicinity < 10):
                    closestIndexes.append(index)
            if(vicinity < closestVicinity):
                # print("closest vicinity was: ", closestVicinity, closestIndex,getColorProximity(blue,imgCol[index]))
                closestVicinity = vicinity
                closestIndex = index
                
                    
        return closestVicinity, closestIndex, closestIndexes
        # return [1,2]

    def readTheDarkestValue(row):#input: [r,g,b]
        brightest = 255 + 255 + 255
        brightestIndex = [255,255,255]
        # print(row)
        for i in row:
            if(sumOfArray(i) > brightest):
                brightest = sumOfArray(i)
                brightestIndex = i
        return brightestIndex

    def getPath():#input: [[r,g,b]]
        return [1,2,3]



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

