# 1546
import sys ; input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
ans = []

m = max(score)
idx = score.index(m)

for i in score[:m]:
    i = (i/m) * 100
    ans.append(i)

for j in score[m:]:
    j = (j/m) * 100
    ans.append(j)

ans = sum(ans) / len(ans)
print(round(ans,3))
