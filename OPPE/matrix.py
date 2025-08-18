# # Matrix A (2x3)
# A = [[1, 2, 3],
#      [4, 5, 6]]

# # Matrix B (3x2)
# B = [[7, 8],
#      [9, 10],
#      [11, 12]]

# # Result will be 2x2
# result = [[0, 0],
#           [0, 0]]

# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j] += A[i][k] *B[k][j]

# for row in result:
#     print(row)

def matrix_multiply(A,B):
    result = [[0, 0],
           [0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Matrix A (2x3)
A = [[1, 2, 3],
     [4, 5, 6]]

# Matrix B (3x2)
B = [[7, 8],
     [9, 10],
     [11, 12]]

print(matrix_multiply(A,B))