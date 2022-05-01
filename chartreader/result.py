import csv
import os
from datetime import timedelta

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
        self.__fullMapped = []  # fully mapped chart

    def mapValues(self):
        self.mapDateValues()
        self.mapLogValues()

    def mapDateValues(self):
        chart_offset = self.__chart.coordinates[0][0]

        for index, valuePair in self.__chart.coordinates:
            try:
                self.__dateMapped.append(
                    [self.__dateAxis.values[index - chart_offset][1], valuePair])
            except IndexError:
                self.__dateMapped.append(
                    [self.__dateAxis.values[index - chart_offset][1], 0])

    def mapLogValues(self):
        for index, value in self.__dateMapped:
            try:
                self.__fullMapped.append(
                    [index, self.__logAxis.getFromGraphPosition(value)])
            except IndexError:
                self.__fullMapped.append([index, 0])

    def logChart(self):
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
