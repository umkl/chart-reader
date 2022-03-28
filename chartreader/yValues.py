from PIL import Image
from pytesseract import Output
import pytesseract
import argparse
import cv2
pytesseract.pytesseract.tesseract_cmd =  r'C:\Users\Lea\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# construct the argument parser and parse the arguments
# import image
from yaxis import LogAxis


class YValues:
    def __init__(self, imagePath):
        self.__imagePath = imagePath
        self.__logAxis = LogAxis

    def getOriginXPos(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        width = gray.shape[1]
        origin_x_pos = -1
        for i in range(width):
            if gray[-72, i] == 178:
                origin_x_pos = i

        return origin_x_pos

    def positionOfNumbers(self):
        # get the position of every numeric text in the image
        results = pytesseract.image_to_data(self.__imagePath, lang="eng", config='-c tessedit_char_whitelist=01', output_type=Output.DICT)
        img = cv2.imread(self.__imagePath)
        origin_x_pos = self.getOriginXPos(img)

        for i in range(0, len(results["text"])):
            if(results["left"][i] + results["width"][i] < origin_x_pos):
                # extract the bounding box coordinates of the text region from
                # the current result
                top = results["top"][i]
                height = results["height"][i]
                # extract the OCR text itself along with the confidence of the
                # text localization
                number = results["text"][i]
                print(number)


test = YValues('D:/HTL/4. Klasse/aud/chartreader/docs/Beispiele/Run 9/00.0-08.0-35.0-35.0-40.0-30.0-01.0-04.0-02.0-NONE.png')
test.positionOfNumbers()