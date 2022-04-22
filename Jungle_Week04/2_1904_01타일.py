# 1904

# 00, 1 타일
# n = 1 
# 1 -> 1

# n = 2
# 00, 11 -> 2

# n = 3
# 100, 001, 111 -> 3

# n = 4
# 0000, 1100, 0011, 1001, 1111 -> 5

# n = 5
# 00001, 10000, 00100, 10011, 11001, 11100, 00111, 11111 -> 8

# f(n) = f(n-1) + f(n-2)

# bottom - up : 통과
# list append 전 수 크기 줄이기

def tile(n):
    tileArr = [0,1,2]
    if n == 1:
        return 1
    elif n == 2:
        return 2

    for i in range(3, n+1):
        num = tileArr[i-1] + tileArr[i-2]
        tileArr.append(num % 15746)
    return tileArr[n]

print(tile(int(input())))

# top - down: 메모리 초과
# import sys
# sys.setrecursionlimit(10**6)

# tileArr = [0,1,2]
# def tile(n):
#     if n < len(tileArr):
#         return tileArr[n]
#     else:
#         num = tile(n-1) + tile(n-2)
#         tileArr.append(num)
#         return num
    
# print(tile(int(input())))

# 