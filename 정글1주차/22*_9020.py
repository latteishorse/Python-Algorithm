# 9020
# 골드바흐
# def Goldbach():
#     check = [False, False] + [True] * 10000
#     for i in range(2, 101):
#         if check[i] == True:
#             # i의 배수임을 판단
#             for j in range(2*i, 10001, i):
#                 check[j] = False

#     #  
#     T = int(input())

#     for _ in range(T):
#         n = int(input())
#         A = n // 2
#         B = A

#         for _ in range(10000):
#             if check[A] and check[B]:
#                 print(A, B)
#                 break
#             A -= 1
#             B += 1

# Goldbach()


# -----
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
#

t = int(input())

for _ in range(t):
    n = int(input())

    for a in range(n//2, 0, -1):
        if is_prime(a) and is_prime(n-a):
            print(a, n-a)
            # break 없으면 모두 찾음
            break

    # for a in range(n//2):
    #     if is_prime(a) and is_prime(n-a):
    #         print(a, n-a)
    #         # break 없으면 모두 찾음
    #         break
# ---- 