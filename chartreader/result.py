from distutils.log import Log
import math
from sqlite3 import Date
import sys
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
        print(self.__chart.coordinates[0][0])


        for index, valuePair in self.__chart.coordinates:
            try:
                # print(self.__chart.coordinates[index][0])
                # if(self.__chart.coordinates[index][0] == self.__dateAxis.values[index][0]):
                # dataxval = self.__dateAxis.values[index][1]
                # doesExist = (self.__chart.coordinates[index][0] == index)
                # cochind = self.__chart.coordinates[24][1]
                # cochval = self.__chart.coordinates[index][1]
                self.__dateMapped.append([self.__dateAxis.values[index][1], valuePair])

            except IndexError:
                self.__dateMapped.append([self.__dateAxis.values[index][1], 0])

    def mapM(self):
        # 10^((756+y)/255)
        for index, value in self.__dateMapped:
            self.__fullMapped.append((index, math.pow(10,((756+value)/255))))            

    # def mapLogValue(self):
        

        # for index, value in self.__dateMapped:
        #     print("index %s, value: %s" % (index,value))

        # print(self.__dateAxis.values[0][1])
        # print(self.__dateAxis.values[40][1])

        # for index, value in self.__dateAxis.values:
        #     print(self.__dateAxis.values[index])
        #     # print("value: ",value, " mapped: ", self.__dateMapped[index])
        #     # self.__dateMapped[index] = value

    def simpleLogChart(self):
        with open('output/1.csv', 'w', newline='\n') as f:
            writer = csv.writer(f, delimiter=';')
            # for value in self.__chart.getConverted():
            #     writer.writerow(value)
            writer.writerow(["Day","Log-Value"])
            for index, value in self.__fullMapped:
                # 'tog: %s choatWert: %s' % (index,value)
                writer.writerow([index,value])
        


    def logToCsv(self):
        with open('output/1.csv', 'w') as f:
            writer = csv.writer(f)
            # for value in self.__chart.getConverted():
            #     writer.writerow(value)
            for value in self.__fullMapped():
                writer.writerow(value)
