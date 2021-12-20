import cv2


class Reader:
    def __init__(self,imagePath):
        self.imagePath = imagePath


    def loadImageIntoPixels(url):
        img = cv2.imread('./input/1.png')
        cv2.imshow('image',img)
        cv2.waitKey(0)
