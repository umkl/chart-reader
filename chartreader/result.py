from distutils.log import Log
from sqlite3 import Date
from xaxis import DateAxis
from yaxis import LogAxis
from chart import Chart
import csv


class Result:
    def __init__(self, chart: Chart, dateaxis: DateAxis, logaxis: LogAxis):
        self.__dateAxis = dateaxis
        self.__logAxis = logaxis
        self.__chart = chart

        self.__dateMapped = [] # array consisting of: key: pixelValX - value: date
        self.__logMapped = [] # array consisting of: key: pixelValY - value: log
        self.__fullMapped = [] # chart pixelwerte - abgezogen pixelwerte - auf dateaxis und logaxis gemapped 
        

    # def mapOlles(self):
    #     for index, value in self.__dateAxis.values:
    #         self.__dateMapped[index] = value
    #     for index, value in self.__logAxis.values:
    #         self.__logMapped[index] = value
        
    #     for x, y in self.__chart.coordinates: # x ought to be the key and y the value
    #         self.__fullMapped.append([self.__dateMapped[x],self.__logMapped[y]])

    def mapDate(self):
        for index, value in self.__dateAxis.values:
            self.__dateAxis.values[index] = [index, 22]
        for index, value in self.__dateAxis.values:
            print(self.__dateAxis.values[index])
            # print("value: ",value, " mapped: ", self.__dateMapped[index])
            # self.__dateMapped[index] = value

    def simpleLogChart(self):
        # for index, value in self.__dateAxis.values:
        #     self.__dateMapped.append([self.__dateAxis.values[index], self.__chart.coordinates[index]])

        print(self.__chart.pixelCoordinates[0])
        # for index, value in self.__chart.coordinates:
        #     print()
           


    def logToCsv(self):
        with open('output/1.csv', 'w') as f:
            writer = csv.writer(f)
            # for value in self.__chart.getConverted():
            #     writer.writerow(value)
            for value in self.__fullMapped():
                writer.writerow(value)
