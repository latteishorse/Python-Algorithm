# 2748
# Tabulation (Bottom up)
# 가장 작은 sub-problem 부터 array를 채워감
# for loop로 array 채워감
# O(n)

# 3 - for loop

zero = [1,0,1]
one = [0,1,1]

def fib(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[num],one[num])

tc = int(input())
for _ in range(tc):
    fib(int(input()))