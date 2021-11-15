import numpy as np

A = np.array([[2,1,1],
             [1,1,0],
             [0,1,-3]])

b = np.array([2,2,1])

x = np.linalg.solve(A,b)
print("Result of x , y , z are : ",x)