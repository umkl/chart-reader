from xaxis import DateAxis 
from yaxis import LogAxis

class Result:
    def __init__(self):
        self.__dateAxis = DateAxis
        self.__logAxis = LogAxis
        
    def logToCsv(self):
        for value in self.__dateAxis.values():
            print("log not implemented")
    
