import math


def rotateMatirx(matrix):
    n = len(matrix[0])
    for i in range(0, math.floor(n/2)):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n-i-1]
            matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = temp

    print(matrix)


rotateMatirx([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print([[1, 2, 3], [1, 2, 3], [1, 2, 3]])


# 1 1 1        m00 m01 m02
# 2 2 2        m10 m11 m12
# 3 3 3        m20 m21 m22

# 1 2 3        m02 m12 m22
# 1 2 3        m01 m11 m21
# 1 2 3        m00 m10 m20


# m20= m00
# m22 = m20
# m02 = m22
# m00 = m02
