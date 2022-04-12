# 17608

n = int(input())
li = list(int(input()) for _ in range(n))

view = 1
Max = li[-1]

for i in range(n-1, -1,-1):
    if li[i] > Max:
        view += 1
        Max = li[i]

print(view)