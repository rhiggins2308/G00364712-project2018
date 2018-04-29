# Robert Higgins (G00364712) - Final Submission 2018-04-29
# 52167-Programming & Scripting
# Project 2018

# generate Boxplots for Fishers Iris Dataset
def getData():
    return numpy.genfromtxt('data/iris.csv', delimiter=',')

import numpy
import matplotlib.pyplot as pl

iris = getData()
# for various histogram plots, change the y-value in the iris array
# values 0 <= y <= 3 are acceptable
# 0 = petal length
# 1 = petal width
# 2 = sepal length
# 3 = sepal width
pl.boxplot(iris[:,3])
pl.show()