# 11170

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    countZero = 0
    
    for j in range(a, b+1):
        w = str(j)
        countZero += w.count('0')
    print(countZero)