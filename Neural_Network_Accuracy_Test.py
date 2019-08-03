###################################################################################
'''
    Project Name: Neural Network to classify Different specices of Iris flowers.
    File Name   : Neural Network Accuracy Test

    Code Author : Shrajan Bhandary
    Created on  : 11 March 2019
    Module Name : COMP5600M - Bio-Inspired Computing

    Program Description:
        The python program consists of a method to test the accuracy of the 
        neural network built using three previously trained perceptron algorithms. 
        The program obtains data set from a file and extracts four values: 
        Sepal length, Sepal width, Petal length and Petal width. The network 
        produces the following classification: versicolor = (1, 0, 0), 
        setosa = (0,1,0), virginica = (0,0,1). The accuracy is tested by comparing
        the actual class of the flower and the result.

'''
##########################    LIBRARY IMPORTS AND FUNCTION DEFINITIONS    ################################

# Importing the required libraries.
# numpy is required for performing mathematical operations.
# csv is used to access files that have data separated using commas.
import numpy as np    
import csv                                                         

# Creating a artificial neural node using as function that classifies setosa and non-setosa species.
# The input to the neural node is the information of the flower.
def NeuralNetSetosa ( test_attributes ):

    # A perceptron was trained using different species of Iris flowers and classifies setosa and 
    # non-setosa types with the weights below.
    SETOSA_WEIGHT_ARRAY = np.array([ 0.33629258, -0.64072985,  0.38371641, -0.50472013, -0.48306456])

    # Calculate the dot product of the weights and the inputs.
    setosa_dot_product = np.dot( SETOSA_WEIGHT_ARRAY , test_attributes )

    return int( setosa_dot_product < 0 )

# Creating a artificial neural node using as function that classifies versicolor and non-versicolor species.
# The input to the neural node is the information of the flower.
def NeuralNetVersicolor ( test_attributes ):

    # A perceptron was trained using different species of Iris flowers and classifies versicolor and 
    # non-versicolor types with the weights below.
    VERSICOLOR_WEIGHT_ARRAY = np.array( [ 0.52184259,  0.64195552, -0.0083266,  -0.2385559,  0.87197588])

    # Calculate the dot product of the weights and the inputs.
    versicolor_dot_product = np.dot( VERSICOLOR_WEIGHT_ARRAY , test_attributes )

    return int( versicolor_dot_product < 0 )

# Creating a artificial neural node using as function that classifies virginica and non-virginica species.
# The input to the neural node is the information of the flower.
def NeuralNetVirginica ( test_attributes ):

    # A perceptron was trained using different species of Iris flowers and classifies virginica and 
    # non-virginica types with the weights below.
    VIRGINICA_WEIGHT_ARRAY = np.array([ 1.04778438,  1.19006768, -2.05880321, -0.16194426,  0.48242611])

    # Calculate the dot product of the weights and the inputs.
    virginica_dot_product = np.dot( VIRGINICA_WEIGHT_ARRAY , test_attributes )

    return int( virginica_dot_product < 0 )

######################################    MAIN PROGRAM STARTS    ##########################################

# Define the list of different flower classes.
FLOWER_CLASS = [ 'Iris-versicolor', 'Iris-setosa', 'Iris-virginica'  ]

# Define the different possible output combinations as a list.
OUTPUT_COMB = [ [1,0,0] , [0,1,0] , [0,0,1 ] ]

# Define number of test samples
SAMPLE_QUANTITY = 150

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

while ( no_of_iterations < SAMPLE_QUANTITY ):

    # Change the test data after every iteration.
    index_value = no_of_iterations
    
    # Declaring the training samples obtained from the input data set.
    flower_attributes = []
    flower_attributes.append(float(input_data_set[index_value][0].split(',')[0]))
    flower_attributes.append(float(input_data_set[index_value][0].split(',')[1]))
    flower_attributes.append(float(input_data_set[index_value][0].split(',')[2]))
    flower_attributes.append(float(input_data_set[index_value][0].split(',')[3]))
    flower_attributes.append(1)

    # Converting list to array.
    array_flower_attributes = np.asarray(flower_attributes)
    
    # Retrieving the class of the sample.
    class_test_flower = input_data_set[index_value][0].split(',')[4]

    # Implementing the neural network with three nodes that classify different species.
    # Calling the three neural nodes and appending the result of the perceptrons to the output list.
    output_neural_network = []
    output_neural_network.append(NeuralNetVersicolor(array_flower_attributes))
    output_neural_network.append(NeuralNetSetosa(array_flower_attributes))
    output_neural_network.append(NeuralNetVirginica(array_flower_attributes))
    
    # Check the class of the sample.
    if ( class_test_flower == FLOWER_CLASS[0]  ):

        # Checking the value of the dot product
        if ( output_neural_network == OUTPUT_COMB[0] ):
            pass

        else:
            no_of_misclassifications += 1

    elif ( class_test_flower == FLOWER_CLASS[1]  ):

        # Checking the value of the dot product
        if ( output_neural_network == OUTPUT_COMB[1] ):
            pass

        else:
            no_of_misclassifications += 1

    elif ( class_test_flower == FLOWER_CLASS[2]  ):

        # Checking the value of the dot product
        if ( output_neural_network == OUTPUT_COMB[2] ):
            pass

        else:
            no_of_misclassifications += 1

    # Increase the steps by 1
    no_of_iterations += 1

# Variable to determine the accuracy of the network.
network_accuracy = ((no_of_iterations - no_of_misclassifications) / float (no_of_iterations)) * 100

# Display the misclassification count and network accuracy.
print (f"The number of samples tested: {SAMPLE_QUANTITY}")
print (f"The number of misclassifications is: {no_of_misclassifications}.")
print (f"The accuracy of the network is: {network_accuracy} %.")

########################################    PROGRAM END    ############################################





