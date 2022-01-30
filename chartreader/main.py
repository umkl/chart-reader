from reader import Reader
from chart import *
from const import *

import numpy as np
import cv2 as cv
import sympy as sy

def main(): 
    # init()
    # print(getLinearFunctionFromCoo([100,120],[101, 130]))
    evaluate()
    # present()

def init():
    global img; img = cv.imread(INPUTFILE)
    global chart; chart = Chart(img)

def evaluate():
    # print(getFragValuesBetween(0.2,10,12,100,120))
    # k = sy.S('k')
    # d = sy.S('d')
    # k,d = getLinearFunctionFromCoo([10,12],[100, 120])    
    # print(d.values())
    # x = sy.S('x')
    # sol = sy.solve( sy.Eq(1000, 3*x -1) )
    # print(sol[0]*2)

    

    x = sy.S('x')
    a, b, c = sy.symbols("a b c")

    eq = sy.Eq( a*x**2 + b*x + c, 0)

    # Gleichung allgemein mit x als Variable lösen:

    # sy.solve( eq, x )
    # # Ergebnis: (-b + sqrt(-4*a*c + b**2))/(2*a), -(b + sqrt(-4*a*c + b**2))/(2*a)]

    # # Gleichung mit Parametern a=1, b=3, c=2 lösen:

    # sy.solve( eq.subs( {a:1, b:-3, c:2} ) )

    # for i in getLinearFunctionFromCoo([10,12],[100, 120]):
    #     print(i)
    
    # k, d = sy.symbols("k, d")# f(x)=k*x+d
    k = sy.S('k')
    d = sy.S('d')
    
    equations = [
        sy.Eq(100*k+d, 120),
        sy.Eq(10*k+d, 12),
    ]
    solution = sy.solve(equations)
    k = solution[k]
    print(sy.N(k))
    

    # Ergebnis: [1, 2]

    # x = sy.S('x')
    # # a, b, c = sy.symbols("a b c")

    # eq = sy.Eq(3*x**2 + 3*x + 3, 0)

    # # Gleichung allgemein mit x als Variable lösen:

    # print(sy.solve( eq, x ))
    # Ergebnis: (-b + sqrt(-4*a*c + b**2))/(2*a), -(b + sqrt(-4*a*c + b**2))/(2*a)]

    # Gleichung mit Parametern a=1, b=3, c=2 lösen:

    # print(sy.solve( eq.subs( {a:1, b:-3, c:2} ) ))
    # Ergebnis: [1, 2]




    return 0
    # img[150:200,10:100] = [255,100,250]
    # cv.imshow('ex1',img)
    # getPointArrayOnFunction(0.1, 10, xPoint2,yPoint1, yPoint2)
    # values = Reader.loadImageIntoPixels('./input/1.png')
    # res = Chart.readTheDarkestValue(values[132])

def present():    
    # cv.line(img,(0,0),(511,511),(255,0,0),5)
    for val in chart.pixelCoordinates:
        # print(val)
        img[val[0], val[1]] = [255,150,180]
    # print(chart.pixelCoordinates)
    cv.imshow(INPUTFILE,img)
    # print(img[343,160])
    cv.waitKey(0)

def drawByAvg():
    op = sum(getColorProximity([51,102,204],[51,102,204]))
    for colIndex in range(CHARTSTARTX, CHARTSTARTY):
        n, i, d = Chart.readTheBluestValue(img[:,colIndex])
        avg = sum(d) / len(d)
        img[round(avg),colIndex] = [150,120,200]

def equationSysX():
    k = sy.S('k')
    d = sy.S('d')
    x = sy.S('x')
    # sy.Eq(x**2 +1, 3*x -1)
    # print(getPointArrayOnFunction(10, 0.1, 2, 3))
    print(sy.solve( sy.Eq(101,((100*x)/399)*400+x )))

if __name__ == "__main__":
    main()