# 10872
# case 1

# def factorial(n) :
#     ans = 1
#     if n > 0:
#         ans = n * factorial(n-1)        
#     return ans
# n = int(input())
# print(factorial(n))

#  ----------------
# case 2

# def factorial(n):
#     return n * factorial(n-1) if n > 1 else 1

# n = int(input())
# print(factorial(n))

# ------------
# case 3

def factorial(n: int) -> int:
    if n > 0 :
        return n * factorial(n-1)
    else :
        return 1

n = int(input())
print(factorial(n))