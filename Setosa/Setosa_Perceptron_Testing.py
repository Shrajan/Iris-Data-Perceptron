##############################################################################
'''
    Project Name: Neural Network to classify Different specices of Iris flowers.
    File Name   : Perceptron Setosa Testing.

    Code Author : Shrajan Bhandary
    Created on  : 11 March 2019
    Module Name : COMP5600M - Bio-Inspired Computing

    Program Description:
        The python program tests the samples given to it with a set of 
        pre-trained weights. This program can be test with weights obtained
        using both with and without learning rate.

'''
##########################    PROGRAM START    ################################

# Importing the required libraries.
# numpy is required for performing mathematical operations.
# csv is used to access files that have data separated using commas.
import numpy as np
import csv

# The program is testing for Setosa vs Non-Setosa.
REQUIRED_CLASS = 'Iris-setosa'

# Defining a stopping creterion.
STOP_VALUE = 50

# Pre-trained weight list obtained without learning rate. Comment line 32 to test with learning rate.
PRE_TRAINED_WEIGHTS =  [3,-5,  0,  0, 0]

# Pre-trained weight list obtained with learning rate. Comment line 30 to test without learning rate.
#PRE_TRAINED_WEIGHTS =  [ 0.026011,   -0.31588819,  0.33366101,  0.10699001, -0.43724017]

# Converting list to array.
PRE_TRAINED_WEIGHTS_ARRAY = np.asarray(PRE_TRAINED_WEIGHTS,dtype=np.float32)

# Creating a list to store the input data set.
input_data_set = []

# Open 'iris.data' file and access the each row of the data.
with open('iris.data', newline='') as csvfile:

    # Store the contents of the file in a list.
    flower_data = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # Iterate through all the data
    for every_row in flower_data:
        
        # Check for empty rows by determing the length.
        if (len(every_row) != 0):

            # Append every row of the file to the list.
            input_data_set.append(every_row)

# Number of epochs.
no_of_iterations = 0

# Declare a variable to extract particular data from the input set.
index_value = 0

# Varible to count the number of misclassifications.
no_of_misclassifications = 0

# Boolean to start or stop the testing.
test_stop = False

while ( (no_of_iterations < 150) and (not test_stop) ):

    # Change the test data after every iteration.
    index_value = no_of_iterations
    
    # Declaring the training samples obtained from the input data set.
    testing_samples = []
    testing_samples.append(float(input_data_set[index_value][0].split(',')[0]))
    testing_samples.append(float(input_data_set[index_value][0].split(',')[1]))
    testing_samples.append(float(input_data_set[index_value][0].split(',')[2]))
    testing_samples.append(float(input_data_set[index_value][0].split(',')[3]))
    testing_samples.append(1)

    # Converting list to array.
    array_testing_samples = np.asarray(testing_samples)
    
    # Retrieving the class of the sample.
    class_test_sample = input_data_set[index_value][0].split(',')[4]

    # Calculating the dot product of the training samples and the training weights.
    test_dot_product = np.dot(PRE_TRAINED_WEIGHTS,array_testing_samples)
    
    # Check the class of the sample.
    if ( class_test_sample == REQUIRED_CLASS  ):

        # Checking the value of the dot product
        if ( test_dot_product < 0 ):
            print(f"The test sample belongs to class: {class_test_sample} and it was Classified Correctly")

        else:
            print(f"The test sample belongs to class: {class_test_sample} and it was Classified Incorrectly")
            no_of_misclassifications += 1

    elif ( class_test_sample != REQUIRED_CLASS ):

        if ( test_dot_product >= 0):
            print(f"The test sample belongs to class: {class_test_sample} and it was Classified Correctly")

        else:
            print(f"The test sample belongs to class: {class_test_sample} and it was Classified Incorrectly")
            no_of_misclassifications += 1

    # Check if the number of misclassifications exceed the stopping criterion.
    if ( no_of_misclassifications >= STOP_VALUE ):
        test_stop = True

    # Increase the steps by 1
    no_of_iterations += 1    

# Variable to determine the accuracy of the network.
network_accuracy = ((no_of_iterations- no_of_misclassifications) / float (no_of_iterations)) * 100

# Display the misclassification count and network accuracy.
print (f"Testing of the network was stopped after {no_of_iterations} iterations.")
print (f"The number of misclassifications is: {no_of_misclassifications}.")
print (f"The accuracy of the network is: {network_accuracy} %.")

###########################    PROGRAM END    ################################