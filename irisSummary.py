# Robert Higgins (G00364712) - Final Submission 2018-04-29
# 52167-Programming & Scripting
# Project 2018
# Summary Statistics for Fisher's Iris Dataset

# Reference List
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
# https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html
# https://docs.scipy.org/doc/numpy-1.14.0/user/quickstart.html
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# Function to import data from iris.csv into python array
def getData():
    return numpy.genfromtxt('data/iris.csv', delimiter=',')

# Function to calculate the column mean
def getMean(sample):
    return numpy.mean(sample)

# Function to find the column median value
def getMedian(sample):
    return numpy.median(sample)

# Function to find the max column value
def getMax(sample):
    return numpy.max(sample)

# Function to find the min column value
def getMin(sample):
    return numpy.min(sample)

# Import numpy class to allow analysis of the numerical data
import numpy

# call getData() function to import data from iris.csv
iris = getData()

# Series of commands to output summary data to Terminal window
print("Fisher's Iris Data Set: Summary Statistics")
print("------------------------------------------")
print("")
print("Petal Length (cm)")
print("-----------------")
print("Min:", getMin(iris[:,0])) # Call getMin function and print Min column value to Terminal
print("Max:", getMax(iris[:,0]))
print("Range:", getMax(iris[:,0])-getMin(iris[:,0]))
print("")
print("Petal Width (cm)")
print("-----------------")
print("Min:", getMin(iris[:,1])) # Call getMin function and print Min column value to Terminal
print("Max:", getMax(iris[:,1])) # Call getMax function and print Max column value to Terminal 
print("Range:", getMax(iris[:,1])-getMin(iris[:,1])) # Difference between Max and Min values is the range of the column data
print("")
print("Sepal Length (cm)")
print("-----------------")
print("Min:", getMin(iris[:,2])) # Call getMin function and print Min column value to Terminal
print("Max:", getMax(iris[:,2])) # Call getMax function and print Max column value to Terminal
print("Range:", getMax(iris[:,2])-getMin(iris[:,2])) # Difference between Max and Min values is the range of the column data
print("")
print("Sepal Width (cm)")
print("-----------------")
print("Min:", getMin(iris[:,3])) # Call getMin function and print Min column value to Terminal
print("Max:", getMax(iris[:,3])) # Call getMax function and print Max column value to Terminal
print("Range:", getMax(iris[:,3])-getMin(iris[:,3])) # Difference between Max and Min values is the range of the column data
print("")
print("Mean Average (cm)")
print("-----------------")
print("Petal Length:", getMean(iris[:,0])) # Call getMean function and print Mean column value to Terminal
print("Petal Width:", getMean(iris[:,1]))
print("Sepal Length:", getMean(iris[:,2]))
print("Sepal Width:", getMean(iris[:,3]))
print("")
print("Median Values (cm)")
print("-----------------")
print("Petal Length:", getMedian(iris[:,0])) # Call getMedian function and print Median column value to Terminal
print("Petal Width:", getMedian(iris[:,1]))
print("Sepal Length:", getMedian(iris[:,2]))
print("Sepal Width:", getMedian(iris[:,3]))
print("")

# open a writeable file to contain the summary data
f = open("irisSummary.txt", 'w')

# Series of commands to output summary data to file
f.write("Fisher's Iris Data Set: Summary Statistics\n")
f.write("------------------------------------------\n")
f.write("\n")
f.write("Petal Length (cm)\n")
f.write("-----------------\n")
f.write("Min: ")
f.write(str(getMin(iris[:,0])))
f.write("\n")
f.write("Max: ")
f.write(str(getMax(iris[:,0])))
f.write("\n")
f.write("Range: ")
f.write(str(getMax(iris[:,0])-getMin(iris[:,0])))
f.write("\n\n")
f.write("Petal Width (cm)\n")
f.write("-----------------\n")
f.write("Min: ")
f.write(str(getMin(iris[:,1])))
f.write("\n")
f.write("Max: ")
f.write(str(getMax(iris[:,1])))
f.write("\n")
f.write("Range: ")
f.write(str(getMax(iris[:,1])-getMin(iris[:,1])))
f.write("\n\n")
f.write("Sepal Length (cm)\n")
f.write("-----------------\n")
f.write("Min: ")
f.write(str(getMin(iris[:,2])))
f.write("\n")
f.write("Max: ")
f.write(str(getMax(iris[:,2])))
f.write("\n")
f.write("Range: ")
f.write(str(getMax(iris[:,2])-getMin(iris[:,2])))
f.write("\n\n")
f.write("Sepal Width (cm)\n")
f.write("-----------------\n")
f.write("Min: ")
f.write(str(getMin(iris[:,3])))
f.write("\n")
f.write("Max: ")
f.write(str(getMax(iris[:,3])))
f.write("\n")
f.write("Range: ")
f.write(str(getMax(iris[:,3])-getMin(iris[:,3])))
f.write("\n\n")
f.write("Mean Average (cm)\n")
f.write("-----------------\n")
f.write("Petal Length: ")
f.write(str(getMean(iris[:,0])))
f.write("\n")
f.write("Petal Width: ")
f.write(str(getMean(iris[:,1])))
f.write("\n")
f.write("Sepal Length: ")
f.write(str(getMean(iris[:,2])))
f.write("\n")
f.write("Sepal Width: ")
f.write(str(getMean(iris[:,3])))
f.write("\n\n")
f.write("Median Values (cm)\n")
f.write("-----------------\n")
f.write("Petal Length: ")
f.write(str(getMedian(iris[:,0])))
f.write("\n")
f.write("Petal Width: ")
f.write(str(getMedian(iris[:,1])))
f.write("\n")
f.write("Sepal Length: ")
f.write(str(getMedian(iris[:,2])))
f.write("\n")
f.write("Sepal Width: ")
f.write(str(getMedian(iris[:,3])))
f.close()