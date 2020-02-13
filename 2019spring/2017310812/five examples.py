# 1 (A')' = A
import numpy as np
matrixNum1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrixNum2 = matrixNum1.T
matrixNum3 = matrixNum2.T
print(matrixNum1 == matrixNum3)


# 2 A(B + C) = AB + AC
import numpy as np
matrixNum1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrixNum2 = np.matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
matrixNum3 = np.matrix([[19, 20, 21], [22, 23, 24], [25, 26, 27]])
matrixNum4 = matrixNum1.dot(matrixNum2 + matrixNum3)
matrixNum5 = matrixNum1.dot(matrixNum2) + matrixNum1.dot(matrixNum3)
print(matrixNum4 == matrixNum5)


# 3 |AB| = |A|*|B|
import numpy as np
matrixNum1 = np.matrix([[1, 2, 3], [4, 5, 7], [7, 8, 10]])
matrixNum2 = np.matrix([[10, 11, 12], [13, 14, 16], [16, 17, 19]])
Num1 = np.linalg.det(matrixNum1.dot(matrixNum2))
Num2 = np.linalg.det(matrixNum1)*np.linalg.det(matrixNum1)
print(abs(Num1 == Num2)<1e-2)

# 4 Solve an equation group with the usage of the Cramer's Rule (P102 19.1)
matrixNum1 = np.matrix([[2, -1, 3, 2], [3, -3, 3, 2], [3, -1, -1, 2], [3, -1, 3, -1]])
matrixNum2 = np.matrix([[6, 5, 3, 4]])
print(np.linalg.solve(matrixNum1, matrixNum2.T))

# 5 ((A)^(-1))^(-1) = A
matrixNum1 = np.matrix([[1, 2, 3], [4, 5, 7], [7, 8, 10]])
print((matrixNum1.I).I)
