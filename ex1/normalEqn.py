import numpy as np

def normalEqn(X,y):
    """ Computes the closed-form solution to linear regression
       normalEqn(X,y) computes the closed-form solution to linear
       regression using the normal equations.
    """
    theta = 0
# ====================== YOUR CODE HERE ======================
# Instructions: Complete the code to compute the closed form solution
#               to linear regression and put the result in theta.
#
    
    # theta = (X^T * X)^-1 * X^T * y
    
    xTx = X.T.dot(X)
    XtX = np.linalg.inv(xTx)
    XtX_xT = XtX.dot(X.T)
    theta = XtX_xT.dot(y)
    

# ---------------------- Sample Solution ----------------------


# -------------------------------------------------------------

    return theta

# ============================================================

