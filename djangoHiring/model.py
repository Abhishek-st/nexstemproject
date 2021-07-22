import numpy as np

#Load weights
weights = np.load("D:/cortexProject/nexstem/djangoHiring/weights.npy")


def my_function(X, W):
    '''
            Parameters:
                    X (float): A tensor of shape (200, 4)
                    W (float): A tensor of shape (200, 1)

            Returns:
                    y (int): A value between 1 to 4 
    '''
    X = np.array(X)
    y = np.argmax(X.T.dot(W))
    return y


def predictOutcome(N):
    y = my_function(N, weights)
    return y