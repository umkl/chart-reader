import csv
import math
from datetime import timedelta
import os

from chart import Chart
from xaxis import DateAxis
from yaxis import LogAxis


class Result:
    def __init__(self, chart: Chart, dateaxis: DateAxis, logaxis: LogAxis, output_path):
        self.__dateAxis = dateaxis
        self.__logAxis = logaxis
        self.__chart = chart
        self.__outputPath = output_path

        self.__dateMapped = []  # array consisting of: key: pixelValX - value: date
        self.__logMapped = []  # array consisting of: key: pixelValY - value: log
        # chart pixelwerte - abgezogen pixelwerte - auf dateaxis und logaxis gemapped
        self.__fullMapped = []

    def mapDate(self):
        chart_offset = self.__chart.coordinates[0][0]

        for index, valuePair in self.__chart.coordinates:
            try:
                self.__dateMapped.append(
                    [self.__dateAxis.values[index - chart_offset][1], valuePair])
            except IndexError:
                self.__dateMapped.append(
                    [self.__dateAxis.values[index - chart_offset][1], 0])

    def mapLogValues(self):
        for xValue, yValue in self.__chart.coordinates:
            try:
                self.__logMapped.append(
                    [xValue, self.__logAxis.getFromGraphPosition(yValue)])
            except IndexError:
                self.__logMapped.append([xValue, 0])
                
    def mapLogValuesEasy(self):
        for index, value in self.__dateMapped:
            try:
                self.__fullMapped.append(
                    [index, self.__logAxis.getFromGraphPosition(value)])
            except IndexError:
                self.__fullMapped.append([index, 0])

    def logTest(self):
        yval = self.__chart.coordinates[1][1]
        print(self.__logAxis.getFromGraphPosition(yval))

    def mapM(self):  # mapping the values according to input/1.png manually
        # 10^((756+y)/255)
        for index, value in self.__dateMapped:
            self.__fullMapped.append(
                (index, math.pow(10, ((756 + value) / 255))))

    def createFullMapped(self):
        for xValue, yValue in self.__chart.coordinates:
            dateval = self.__dateMapped[xValue]
            self.__fullMapped.append(
                (self.__dateMapped[xValue], self.__logMapped[xValue][1]))

    def simpleLogChart(self):
        os.makedirs(os.path.dirname(self.__outputPath), exist_ok=True)
        with open(self.__outputPath, 'w', newline='\n') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["DATE", "BALANCE USD"])
            for index, value in self.__fullMapped:

                days = index
                start = self.__dateAxis.startDateTime
                delta = timedelta(days)
                offset = start + delta

                writer.writerow([offset.strftime("%d.%m.%Y %H:%M"), value])
        print("CSV-File saved to {}.".format(self.__outputPath))

    def logToCsv(self):
        with open(self.__outputPath, 'w') as f:
            writer = csv.writer(f)
            for value in self.__fullMapped:
                writer.writerow(value)
