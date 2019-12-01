import numpy as np
import math
 
Mat = np.matrix([[0.68, 0.05, -0.11, 0.08],
                 [-0.11, 0.84, 0.28, 0.06],
                 [-0.08, 0.15, 1.0, -0.12],
                 [0.21, -0.13, 0.27, 1.0]
])
 
B = [2.15, -0.83, 1.16, 0.44]
 
x_last = [-1, -1, -1, -1]
x_new = B.copy()
 
eps = 0.00000001
 
C = Mat.copy();
 
for i in range(Mat.shape[0]):
  for j in range(Mat.shape[0]):
    if (i == j):
      C[i, j] = C[i, j]* (-1) + 1
    else:
      C[i, j] *= -1
 
def check_eps():
  ans = True
  for i in range(len(x_last)):
    ans = ans and (abs(x_last[i] - x_new[i]) < eps)
  return ans;
 
while not check_eps():
  x_last = x_new.copy();
  for i in range(len(x_last)):
    x_new[i] = B[i]
    for j in range(len(x_last)):
      x_new[i] += x_last[j] * C[i, j];
 
print(x_new)
