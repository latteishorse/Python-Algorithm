# 10871
# 1

N, X = map(int, input().split())
a =  []

for i in range (1, N+1):
     b = input()
     a.append(b)

def check(a):
    return a > X

result = list(filter(check, a))
print(result)

# ----------------------------------
# 2

N, X = map(int,input().split())
num = list(map(int, input().split()))

for i in range(N):
    if num[i] < X:
        print(num[i], end = " ")
