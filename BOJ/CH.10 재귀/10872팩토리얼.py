# 10872

# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))