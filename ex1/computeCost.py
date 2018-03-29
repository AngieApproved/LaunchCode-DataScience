import numpy as np
import matplotlib.pyplot as plt

def computeCost(X, y, theta):
    """
       computes the cost of using theta as the parameter for linear 
       regression to fit the data points in X and y
    """
   
    data = np.loadtxt('ex1data1.txt', delimiter=',')

    m = len(y)      #number of training samples
    #X = data[:, 0]
    #y = data[:, 1]
    
    # You need to return the following variables correctly 
    
    predictions = X.dot(theta)
    sqErrors = (predictions - y) ** 2
    

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
#               You should set J to the cost.
    #print(X.shape)
    #print(theta.shape)
    #print(y.shape)
    
# Initial
## Update 2


    ### append a ones column to the front of the data set
    #data.insert(0, 'Ones', 1)
    
    ### set X (training data) and y (target variable)
#    cols = data.shape[1]
#    X = data.iloc[:, 0:cols-1]
#    y = data.iloc[:, cols-1:cols]
#    
#    
#    ###convert from data frames to numpy matrices
#    X = np.matrix(X.values)
#    y = np.matrix(y.values)
#    theta = np.matrix(np.array([0, 0]))
    

   
    #it = np.ones(shape = (m, 2))
    #it[:, 1] = X
    
    #theta = np.zeros(shape = (2, 1))
    #iterations = 1500
    #alpha = 0.01
    
    
    J = (1.0 / (2 * m)) * sum(sqErrors)
    
# =========================================================================

    return J


