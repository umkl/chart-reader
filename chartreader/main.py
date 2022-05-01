import sys
import cv2
from result import *


def main():
    if 2 > len(sys.argv) < 2:
        print("USAGE 'python main.py {InputFilePath} {OutputFilePath}'")
        return

    image = getImage(sys.argv[1])

    """initialize all classes for _DI_"""
    result = init(image, sys.argv[2])

    """log to csv by using result class"""
    log(result)


def init(image, output_path):
    chart = Chart(image)
    dateAxis = DateAxis(image)
    logAxis = LogAxis(image)

    # combining all data from all 3 sections(chart, dateaxis, logaxis)
    # -> logging to csv
    result = Result(chart, dateAxis, logAxis, output_path)
    return result


def log(result: Result):
    result.mapValues()
    result.logChart()


def getImage(input_path):
    return cv2.imread(input_path)


# makes the file importable, so code does not get executed by importing our lib
if __name__ == "__main__":
    main()
