import numpy as np
import matplotlib.pyplot as plt

def computeCost(X, y, theta):
    """
       computes the cost of using theta as the parameter for linear 
       regression to fit the data points in X and y
    """
   
    data = np.loadtxt('ex1data1.txt', delimiter=',')



    m = y.size      #number of training samples
    X = data[:, 0]
    y = data[:, 1]
    
    predictions = X.dot(theta).flatten()
    sqErrors = (predictions - y) **2
    

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
#               You should set J to the cost.

   
    it = np.ones(shape = (m, 2))
    it[:, 1] = X
    
    theta = np.zeros(shape = (2, 1))
    iterations = 1500
    alpha = 0.01
    
    J = (1.0 / (2 * m)) * sqErrors.sum()

# =========================================================================

    return J


