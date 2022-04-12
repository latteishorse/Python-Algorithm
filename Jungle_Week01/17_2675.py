# 2675
# 문자열 반복

#  -> 런타임 오류
# n, t = input().split()
# for i in range (len(t)):
#     print(str(t[i]) * int(n), end='')

#  --------

t = int(input())
for i in range(t):
    a, b = input().split()
    text = ''
    for i in b:
        text += i * int(a)
    print(text)
