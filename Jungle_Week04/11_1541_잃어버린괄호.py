# 1541
# 식을 최소로 만드는 그리디 문제

# 최소 - 최대를 해야 최소
# - 왼쪽은 모두 그냥두고
# - 오른쪽은 모두 괄호 처리
import sys
input = sys.stdin.readline

exp = input().split('-')
ans = 0

for i in exp[0].split('+'):
    ans += int(i)

for j in exp[1:]:
    for k in j.split('+'):
        ans -= int(k)

print(ans)
