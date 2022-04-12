# 1427 sort
# 내림차순 정렬

n = int(input())
b = []

for i in str(n):
    b.append(int(i))

br = sorted(b, reverse=True)

for i in br:
    print(i, end = '')


