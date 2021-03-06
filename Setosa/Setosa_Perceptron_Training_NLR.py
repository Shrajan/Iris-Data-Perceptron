##############################################################################
'''
    Project Name: Neural Network to classify Different specices of Iris flowers.
    File Name   : Perceptron Setosa without learning rate.

    Code Author : Shrajan Bhandary
    Created on  : 11 March 2019
    Module Name : COMP5600M - Bio-Inspired Computing

    Program Description:
        The python program describes the perceptron algorithm to classify 
        sertosa vs non-sertosa. This program does not implement the 
        learning rate. 

'''
##########################    PROGRAM START    ################################

# Importing the required libraries.
# numpy is required for performing mathematical operations.
# csv is used to access files that have data separated using commas.
import numpy as np
import csv

# The program is training for Setosa vs Non-Setosa.
REQUIRED_CLASS = 'Iris-setosa'

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


# Generate 5 random input weights using numpy.
training_weights  = np.random.normal(size=5,scale = 0.5)

# Number of epochs.
no_of_iterations = 0

# To ensure training data does not repeat.
unique_random_list = []

# Declare a variable to extract particular data from the input set.
index_value = 0

# Varible to count the number of misclassifications.
no_of_misclassifications = 0

while ( no_of_iterations < 150 ):

    # To access unique set of data in every iteration, define a boolean variable.
    is_unique_index = False
    while ( is_unique_index == False ):

        # Create unique random index values and append them into the list.
        index_value = np.random.randint(0,150)
        if ( index_value in unique_random_list ):
            pass
        else:
            is_unique_index = True
            unique_random_list.append(index_value)
    
    # Declaring the training samples obtained from the input data set.
    training_samples = []
    training_samples.append(float(input_data_set[index_value][0].split(',')[0]))
    training_samples.append(float(input_data_set[index_value][0].split(',')[1]))
    training_samples.append(float(input_data_set[index_value][0].split(',')[2]))
    training_samples.append(float(input_data_set[index_value][0].split(',')[3]))
    training_samples.append(1)

    # Converting list to array.
    array_training_samples = np.asarray(training_samples)
    
    # Retrieving the class of the sample.
    class_train_sample = input_data_set[index_value][0].split(',')[4]

    # Calculating the dot product of the training samples and the training weights.
    dot_product = np.dot(training_weights,array_training_samples)

    # Check the class of the sample.
    if ( class_train_sample == REQUIRED_CLASS):

        # Checking the value of the dot product
        if (dot_product < 0 ):
            pass

        else:
            # Edit the training weights and increment the number of misclassifications.
            training_weights = np.subtract(training_weights,array_training_samples)
            no_of_misclassifications += 1 

    elif ( class_train_sample != REQUIRED_CLASS ):

        if (dot_product >= 0):
            pass

        else:
            # Edit the training weights and increment the number of misclassifications.
            training_weights = np.add(training_weights,array_training_samples)
            no_of_misclassifications += 1 

    # Increase the steps by 1
    no_of_iterations += 1    

    # Variable to determine the accuracy of the network.
    network_accuracy = (  (no_of_iterations- no_of_misclassifications) / float (no_of_iterations) ) * 100

    # Display the misclassification count and network accuracy after each iteration.
    print (f"The number of misclassifications after {no_of_iterations} iterations without learning rate is: {no_of_misclassifications}")
    print (f"The accuracy of the network after {no_of_iterations} iterations without learning rate is: {network_accuracy:.4} %")

# Display the final training weights.
print(f"The training weights of the perceptron are: {training_weights}")

###########################    PROGRAM END    ################################