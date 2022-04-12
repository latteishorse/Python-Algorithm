# n = int(input())
# nums = [1,2,3]

# def solver(j):
#     global cnt
#     for i in nums:
#         if j + i < N:
#             solver(j + i)
#         elif j + i == N:
#             cnt += 1

# for _ in range(n):
#     N = int(input())
#     cnt = 0
#     for j in nums:
#         solver(j)
#     print(cnt)

#
n = int(input())

def solver(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solver(n-1) + solver(n-2) + solver(n-3)
        
for i in range(n):
    a = int(input())
    print(solver(a))
