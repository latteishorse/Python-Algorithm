# 2748
# Memoization (top down)
# O(n^2)
# 재귀를 사용하는 경우
# array 에 append
# stack의 limit이 있다

# 1 - recursion
def fib_naive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_naive(n-1) + fib_naive(n-2)

print(fib_naive(int(input())))

# 2 - dp, recursion
fib_array = [0,1]

def fib_recur_dp(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
        fib_array.append(fib)
        return fib

print(fib_recur_dp(int(input())))

# Tabulation (Bottom up)
# 가장 작은 sub-problem 부터 array를 채워감
# for loop로 array 채워감
# O(n)

# 3 - for loop
def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_array=[0,1]

    for i in range(2, n+1):
        num = fib_array[i-1] + fib_array[i-2]
        fib_array.append(num)
    return fib_array[n]

print(fib_dp(int(input())))