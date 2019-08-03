##############################################################################
'''
    Project Name: Neural Network to classify Different specices of Iris flowers.
    File Name   : Import Data and Plot two perceptrons

    Code Author : Shrajan Bhandary
    Created on  : 11 March 2019
    Module Name : COMP5600M - Bio-Inspired Computing

    Program Description:
        The program open the file that contains flower data. Access each row of 
        the file and separate information on different species. Use the 
        retrieved data and plot them using the library.

'''
##########################    PROGRAM START    ################################

# Importing the required libraries.
# numpy is required for performing mathematical operations.
# csv is used to access files that have data separated using commas.
# matplotlib.plot is used to display plots.
import numpy as np        
import csv
import matplotlib.pyplot as PLOT

# Creating a list of all the different attribute of the flowers. Each species of 
# of Iris has different sepal length, sepal width, petal width and petal length.
IRIS_SETOSA_SEPAL_LENGTH = []
IRIS_SETOSA_SEPAL_WIDTH = []
IRIS_SETOSA_PETAL_LENGTH = []
IRIS_SETOSA_PETAL_WIDTH = []

IRIS_VERSICOLOR_SEPAL_LENGTH = []
IRIS_VERSICOLOR_SEPAL_WIDTH = []
IRIS_VERSICOLOR_PETAL_LENGTH = []
IRIS_VERSICOLOR_PETAL_WIDTH = []

IRIS_VIRGINICIA_SEPAL_LENGTH = []
IRIS_VIRGINICIA_SEPAL_WIDTH = []
IRIS_VIRGINICIA_PETAL_LENGTH = []
IRIS_VIRGINICIA_PETAL_WIDTH = []

# Open 'iris.data' file and access the each row of the data.
with open('iris.data', newline='') as csvfile:

    # Store the contents of the file in a list.
    FLOWER_DATA = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # Declare a variable to obtain information about different species.
    COUNTER = 0

    # Iterate through all the data
    for EVERY_ROW in FLOWER_DATA:

        # The first 50 rows of the file contain data about the iris setosa species.
        if 0 <= COUNTER <= 49:

            IRIS_SETOSA_SEPAL_LENGTH.append(float(EVERY_ROW[0].split(',')[0]))
            IRIS_SETOSA_SEPAL_WIDTH.append(float(EVERY_ROW[0].split(',')[1]))
            IRIS_SETOSA_PETAL_LENGTH.append(float(EVERY_ROW[0].split(',')[2]))
            IRIS_SETOSA_PETAL_WIDTH.append(float(EVERY_ROW[0].split(',')[3]))

        # The second 50 rows of the file contain data about the iris versicolor species.
        elif 49 < COUNTER < 100:

            IRIS_VERSICOLOR_SEPAL_LENGTH.append(float(EVERY_ROW[0].split(',')[0]))
            IRIS_VERSICOLOR_SEPAL_WIDTH.append(float(EVERY_ROW[0].split(',')[1]))
            IRIS_VERSICOLOR_PETAL_LENGTH.append(float(EVERY_ROW[0].split(',')[2]))
            IRIS_VERSICOLOR_PETAL_WIDTH.append(float(EVERY_ROW[0].split(',')[3]))

        # The last 50 rows of the file contain data about the iris virginica species.
        elif 99 < COUNTER < 150:

            IRIS_VIRGINICIA_SEPAL_LENGTH.append(float(EVERY_ROW[0].split(',')[0]))
            IRIS_VIRGINICIA_SEPAL_WIDTH.append(float(EVERY_ROW[0].split(',')[1]))
            IRIS_VIRGINICIA_PETAL_LENGTH.append(float(EVERY_ROW[0].split(',')[2]))
            IRIS_VIRGINICIA_PETAL_WIDTH.append(float(EVERY_ROW[0].split(',')[3]))
        
        # Increment the counter after each loop.
        COUNTER += 1 

# Plot length vs width of all three flower species in the same plot.

PLOT.scatter(IRIS_SETOSA_SEPAL_WIDTH, IRIS_SETOSA_SEPAL_LENGTH, color = 'red' , marker = 'x' )
PLOT.scatter(IRIS_VERSICOLOR_SEPAL_WIDTH, IRIS_VERSICOLOR_SEPAL_LENGTH, color = 'green' , marker = 'o' )
PLOT.scatter(IRIS_VIRGINICIA_SEPAL_WIDTH, IRIS_VIRGINICIA_SEPAL_LENGTH, color = 'blue' , marker = '*' )
PLOT.scatter(IRIS_SETOSA_PETAL_WIDTH, IRIS_SETOSA_PETAL_LENGTH, color = 'red' , marker = 'x' )
PLOT.scatter(IRIS_VERSICOLOR_PETAL_WIDTH, IRIS_VERSICOLOR_PETAL_LENGTH, color = 'green' , marker = 'o' )
PLOT.scatter(IRIS_VIRGINICIA_PETAL_WIDTH, IRIS_VIRGINICIA_PETAL_LENGTH, color = 'blue' , marker = '*' )
PLOT.title('LENGTH vs WIDTH')
PLOT.xlabel('Width')
PLOT.ylabel('Length')

# Creating linear classifier - 1 using equation of a line given by X - 0.8 = 0.
x1_axis = []
y1_axis = []

# Generating coordinates of the line.
COUNT = 0.8
while ( COUNT < 5 ):
    x1_axis.append(0.8)
    y1_axis.append(COUNT)
    COUNT += 0.1

# Diplaying the linear classifier - 1.
PLOT.plot(x1_axis,y1_axis , color = 'black' )

# Creating linear classifier - 2 using equation of a line given by 3Y - 5X = 0.
x2_axis = []
y2_axis = []

# Generating coordinates of the line.
COUNT = 0.0
while ( COUNT < 4 ):
    x2_axis.append(COUNT)
    y2_axis.append((COUNT*5)/3)
    COUNT += 0.1

# Diplaying the linear classifier - 2.
PLOT.plot(x2_axis,y2_axis , color = 'orange' )

# Assigning legend labels and displaying the plot.
LEGEND_NAMES = ['Percepton - 1','Percepton - 2','Iris Setosa', 'Iris Versicolor', 'Iris Virginica' ]

PLOT.legend(LEGEND_NAMES)
PLOT.show()

