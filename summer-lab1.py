#### Lab 1, py labs
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv

def dist(a,b):
    print( abs(a-b))

def maxMin(xs):
    smol = min(xs)
    bigg = max(xs)
    print("max: ", smol, "  min: ",bigg)

def evenNums(xs):
    evens = []
    for num in xs:
        if num%2==0:
            evens.append(num)
    return evens

def squareEvens(xs):
    evens = evenNums(xs)
    squares = []
    for i in evens:
        squares.append(i**2)
    return squares
        

def count(element, xs):
    count = 0
    for i in xs:
        if i == element:
            count=count+1
    return count

def readNGraph(csvPath):
    data = pd.read_csv(csvPath)
    colunn1 = data.iloc(0)
    column2 = data.iloc(1)
    data.plot()
    
    
    

dist(1,2)

xs = [1,3,4,2,45,6,3,1]
maxMin(xs)

print("evens: ",evenNums(xs))

print("evens squared: ",squareEvens(xs))

print("3 occurs: " ,count(3, xs), " times")

readNGraph('Lab1.csv')

