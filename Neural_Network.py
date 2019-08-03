##############################################################################
'''
    Project Name: Neural Network to classify Different specices of Iris flowers.
    File Name   : Neural Network

    Code Author : Shrajan Bhandary
    Created on  : 11 March 2019
    Module Name : COMP5600M - Bio-Inspired Computing

    Program Description:
        The python program consists of a neural network built using three 
        previously trained perceptron algorithms. The program inputs four 
        values: Sepal length, Sepal width, Petal length and Petal width. The 
        network produces the following desired classification: 
        versicolor = (1, 0, 0), setosa = (0,1,0), virginica = (0,0,1). 

'''
##########################    LIBRARY IMPORTS AND FUNCTION DEFINITIONS    ################################

# Importing the required libraries.
# numpy is required for performing mathematical operations.
import numpy as np                                                             

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

# Obtain the four different inputs from the user.
# The inputs are accepted as string and hence need to be converted to floating value.
petal_length = float (input('Enter the Petal length of the flower: '))
petal_width = float (input('Enter the Petal wdith of the flower: '))
sepal_length = float (input('Enter the Sepal length of the flower: '))            
sepal_width = float (input('Enter the Sepal width of the flower: '))

# Create an array to store all the inputs together.
# The fifth element is set to 1 to multiply with the bias.
flower_attributes = np.array([ sepal_length, sepal_width, petal_length, petal_width, 1 ])

# Implementing the neural network with three nodes that classify different species.
# Calling the three neural nodes and appending the result of the perceptrons to the output list.
output_neural_network = []
output_neural_network.append(NeuralNetVersicolor(flower_attributes))
output_neural_network.append(NeuralNetSetosa(flower_attributes))
output_neural_network.append(NeuralNetVirginica(flower_attributes))

# Display the output of the neural network.
# versicolor = (1, 0, 0), setosa = (0,1,0), virginica = (0,0,1).
print (f"The output of the neural network is: {output_neural_network}")

########################################    PROGRAM END    ############################################





