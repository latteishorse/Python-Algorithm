# 2675
# 220318

t = int(input())
for i in range(t):
    a, b = input().split()
    text = ''
    for i in b:
        text += int(a) * i
    print(text)