import numpy as np


class NeuralNetwork(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # Set number of nodes in input, hidden and output layers.
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Initialize weights
        self.weights_input_to_hidden = np.random.normal(0.0, self.input_nodes**-0.5, 
                                       (self.input_nodes, self.hidden_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.hidden_nodes**-0.5, 
                                       (self.hidden_nodes, self.output_nodes))
        self.lr = learning_rate
        
        #### TODO: Set self.activation_function to your implemented sigmoid function ####
        #
        # Note: in Python, you can define a function with a lambda expression,
        # as shown below.
        #self.activation_function = lambda x : 1/(1+np.exp(-x))  # Replace 0 with your sigmoid calculation.
        
        ### If the lambda code above is not something you're familiar with,
        # You can uncomment out the following three lines and put your 
        # implementation there instead.
        #
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))  # Replace 0 with your sigmoid calculation here
        self.activation_function = sigmoid
                    

    def train(self, features, targets):
        ''' Train the network on batch of features and targets. 
        
            Arguments
            ---------
            
            features: 2D array, each row is one data record, each column is a feature
            targets: 1D array of target values
        
        '''
        n_records = features.shape[0]
        delta_weights_i_h = np.zeros(self.weights_input_to_hidden.shape)
        delta_weights_h_o = np.zeros(self.weights_hidden_to_output.shape)
        for X, y in zip(features, targets):
            # Implement the forward pass function below
            final_outputs, hidden_outputs = self.forward_pass_train(X)  
            # Implement the backproagation function below
            delta_weights_i_h, delta_weights_h_o = self.backpropagation(final_outputs, hidden_outputs, X, y, 
                                                                        delta_weights_i_h, delta_weights_h_o)
        self.update_weights(delta_weights_i_h, delta_weights_h_o, n_records)


    def forward_pass_train(self, X):
        ''' Implement forward pass here 
         
            Arguments
            ---------
            X: features batch

        '''
        #### Implement the forward pass here ####
        ### Forward pass ###
        # TODO: Hidden layer - Replace these values with your calculations.
        
        hidden_inputs = np.dot(X, self.weights_input_to_hidden) # signals into hidden layer #1x2
        print("hidden_inputs")
        print(hidden_inputs.shape)
        hidden_outputs = self.activation_function(hidden_inputs) # signals from hidden layer
        print("hidden_outputs")
        print(hidden_outputs.shape)
        # TODO: Output layer - Replace these values with your calculations.
        final_inputs = hidden_outputs # signals into final output layer
        final_outputs = np.dot(final_inputs[None, :], self.weights_hidden_to_output) # signals from final output layer #1x2 . 2x1
        print("final_outputs")
        print(final_outputs.shape)
        return final_outputs, hidden_outputs

    def backpropagation(self, final_outputs, hidden_outputs, X, y, delta_weights_i_h, delta_weights_h_o):
        ''' Implement backpropagation
         
            Arguments
            ---------
            final_outputs: output from forward pass
            y: target (i.e. label) batch
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers

        '''
        #### Implement the backward pass here ####
        ### Backward pass ###

        # TODO: Output error - Replace this value with your calculations.
        error = y - final_outputs# Output layer error is the difference between desired target and actual output.
        # TODO: Backpropagated error terms - Replace these values with your calculations.
        output_error_term = error*final_outputs*(1-final_outputs) #1x1
        
        # TODO: Calculate the hidden layer's contribution to the error
        hidden_error = output_error_term*self.weights_hidden_to_output   #2x1
        print("hidden_error")
        print(hidden_error.shape)#2x1

        hidden_error_term = hidden_error*hidden_outputs[:, None]*(1-hidden_outputs[:, None]) #2x1
        print("hidden_error_term")        
        print(hidden_error_term.shape) #2x1

        # Weight step (input to hidden)
        print("hidden_outputs")        
        
        print(hidden_outputs.shape)
        
        print("output_error_term")        
      
        print(output_error_term.shape)
        print("delta_weights_i_h")        
        
        print(delta_weights_i_h.shape)        
        
        delta_weights_i_h += X[:, None]*hidden_error_term.T #3x1 . 1x2
        print("delta_weights_h_o")        
        
        print(delta_weights_h_o.shape)
        # Weight step (hidden to output)
        
        delta_weights_h_o += np.multiply(hidden_outputs[:, None], output_error_term)
        return delta_weights_i_h, delta_weights_h_o

    def update_weights(self, delta_weights_i_h, delta_weights_h_o, n_records):
        ''' Update weights on gradient descent step
         
            Arguments
            ---------
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers
            n_records: number of records

        '''
        self.weights_hidden_to_output += self.lr*delta_weights_h_o/n_records # update hidden-to-output weights with gradient descent step
        self.weights_input_to_hidden += self.lr*delta_weights_i_h/n_records # update input-to-hidden weights with gradient descent step
        print("h to o")
        print(self.weights_hidden_to_output)
        print("i to h")
        print(self.weights_input_to_hidden)

    def run(self, features):
        ''' Run a forward pass through the network with input features 
        
            Arguments
            ---------
            features: 1D array of feature values
        '''
        
        #### Implement the forward pass here ####
        # TODO: Hidden layer - Replace these values with your calculations.
        hidden_inputs = np.dot(features, self.weights_input_to_hidden) # signals into hidden layer
        hidden_outputs = self.activation_function(hidden_inputs) # signals from hidden layer

        # TODO: Output layer - Replace these values with your calculations.
        final_inputs = hidden_outputs # signals into final output layer
        final_outputs = np.dot(final_inputs[None, :], self.weights_hidden_to_output) # signals from final output layer
        
        print(final_outputs)
        return final_outputs


#########################################################
# Set your hyperparameters here
##########################################################
iterations = 10000
learning_rate = 0.5
hidden_nodes = 2
output_nodes = 1
