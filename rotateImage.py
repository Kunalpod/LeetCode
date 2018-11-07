#https://leetcode.com/problems/rotate-image/

def rotate(self, matrix):
    n = len(matrix)
    #In-place rotation by 90 degrees

    #Step 1: Reverse  individual rows
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    #Step 2: Interchange rows and columns for one-half of matrix (one-side of diagonal)
    for i in range(n):
        for j in range(i+1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    #Step 3: Reverse  back individual rows and matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    matrix.reverse()
