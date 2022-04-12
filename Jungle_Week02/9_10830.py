# 10830

# 행렬 곱 
# def matrix(arr1, arr2):
#     answer = [len(arr2[0])*[0] for i in range (len(arr1)) ]
#     for i in range (len(answer)):
#         for j in range(len(answer[i])):
#             for k in range (len(arr1[i])):
#                 answer[i][j] += arr1[i][k] * arr2[k][j]
#     return answer

# # numpy
# import numpy as np

# def matrix(arr1, arr2):
#     answer = np.dot(arr1, arr2).tolist()
#     return answer

# ----
# np.matmul(a,b) 사용
# import numpy as np

# a = np.array([1,2],[3,4])

# print(np.matmul(a,a))

# -------

# def matrix(arr1, arr2):
#     answer = [len(arr2[0])*[0] for i in range (len(arr1)) ]
#     for i in range (len(answer)):
#         for j in range(len(answer[i])):
#             for k in range (len(arr1[i])):
#                 answer[i][j] += arr1[i][k] * arr2[k][j]
#     return answer

# def matrix_mul(mat_a, mat_b):
#     length = len(mat_a)
#     temp = [[0] * length for _ in range(length)]
#     for i in range(length):
#         for j in range(length):
#             for k in range(length):
#                 temp[i][j] += mat_a[i][k] * mat_b[k][j]
#     return temp

# ----
# import sys
# input = sys.stdin.readline

# n, b = map(int, input().split())
# mat = [list(map(int,input().split())) for _ in range(n)]

# def matrix_mul(mat_a, mat_b):
#     length = len(mat_a)
#     temp = [[0] * length for _ in range(length)]
#     for i in range(length):
#         for j in range(length):
#             for k in range(length):
#                 temp[i][j] += mat_a[i][k] * mat_b[k][j]
#     return temp

# -----

def mul(n,matrix1,matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000

    return result

# 2분할
def devide(n,b,matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n,matrix,matrix)
    else:
        tmp = devide(n,b//2,matrix)
        if b%2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),matrix)

# 입력
n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

result = devide(n,b,a)
for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()