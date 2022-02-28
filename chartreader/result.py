from xaxis import DateAxis 
from yaxis import LogAxis
from chart import Chart
import csv

class Result:
    def __init__(self, chart):
        self.__dateAxis = DateAxis
        self.__logAxis = LogAxis
        self.__chart = chart
        
    def logToCsv(self):
        with open('output/1.csv', 'w') as f:
            writer = csv.writer(f)
            for value in self.__chart.getConverted():
                writer.writerow(value)
