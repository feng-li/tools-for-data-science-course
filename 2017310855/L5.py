#pip install numpy
#pip install scipy
from numpy import array
from scipy import linalg
Matrix_A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Matrix_B = array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
Matrix_U = array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
#1.Verify the equality of solve(solve(Matrix_A)) and Matrix_A.
linalg.inv(linalg.inv(Matrix_A)) - Matrix_A < 1e-16
#2.Verify the equality of t(t(Matrix_A)) and Matrix_A.
Matrix_A.T.T - Matrix_A < 1e-16
#3.Verify the equality of Matrix_A * solve(Matrix_A) and unit matrix.
linalg.det(linalg.inv(Matrix_A)) * linalg.det(Matrix_A) - Matrix_U < 1e-16
#4.Verify the equality of t(Matrix_A + Matrix_B) and (t(Matrix_A) + t(Matrix_B)).
(Matrix_A + Matrix_B).T - (Matrix_A.T + Matrix_B.T) < 1e-16
#5.Verify the equality of t(Matrix_A * Matrix_B) and t(Matrix_B) * t(Matrix_A).
(Matrix_A * Matrix_B).T - Matrix_B.T * Matrix_A.T < 1e-16