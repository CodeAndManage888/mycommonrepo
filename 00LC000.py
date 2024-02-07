# ------------------------------------------------------------------------
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize parameters
input_layer_size = 2  # Number of features
hidden_layer_size = 2  # Number of hidden nodes
output_layer_size = 1  # Number of output nodes

np.random.seed(42)  # For reproducibility
weights_input_hidden = np.random.uniform(size=(input_layer_size, hidden_layer_size))
weights_hidden_output = np.random.uniform(size=(hidden_layer_size, output_layer_size))
bias_hidden = np.zeros((1, hidden_layer_size))
bias_output = np.zeros((1, output_layer_size))

# Training parameters
learning_rate = 0.1
epochs = 10000

# Sample data (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Training the network
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_activation = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_activation, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    # Backward propagation
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activation)

    # Updating weights and biases
    weights_hidden_output += hidden_layer_activation.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

# Display final weights and biases
print("Final weights from input to hidden layer:", weights_input_hidden)
print("Final weights from hidden to output layer:", weights_hidden_output)
print("Final bias of hidden layer:", bias_hidden)
print("Final bias of output layer:", bias_output)
# ------------------------------------------------------------------------



# ------------------------------------------------------------------------
# Given a linked list, determine if it has a cycle in it.
# Follow up: Can you solve it without using extra space?
# ------------------------------------------------------------------------

'''
# ------------------------------------------------------------------------
# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2 are not
# zero-based.
# Note: You may assume that each input would have exactly one solution.
# Input: numbers={2, 7, 11, 15}, target=9 Outpu: [1,2]
# ------------------------------------------------------------------------
def twoSum(numbers, target):
    # Write your code here
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
    return []
# ------------------------------------------------------------------------
# The main function
# ------------------------------------------------------------------------
if __name__ == "__main__":
    # Read in a list of integers
    line = input().strip()
    numbers = [int(x) for x in line.split(',')]
    # Sort the input list
    numbers.sort()
    print(numbers)
    # Read in the target
    target = int(input())
    # Find the two numbers that add up to the target
    print(twoSum(numbers, target))
# ------------------------------------------------------------------------
'''