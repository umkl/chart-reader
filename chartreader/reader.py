import cv2 as cv

class Reader:
    def __init__(self,imagePath):
        self.imagePath = imagePath

    def loadImageIntoPixels(url):
        img = cv.imread(url)
        # cv2.imshow('image',img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return img

        