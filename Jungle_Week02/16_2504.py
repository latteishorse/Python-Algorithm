# 2504
# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

# ([])
bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        # [) 이면 잘못 닫히는 경우이므로 0
        if not stack or stack[-1] == "[":
            answer = 0
            break

        # 괄호가 닫히는 경우
        if bracket[i-1] == "(":
            answer += tmp

        stack.pop()
        tmp //= 2

    else: # ]인 경우
        # 안에 값이 들어있는지 확인

        if not stack or stack[-1] == "(":
            answer = 0
            break
        # 괄호가 닫히는 경우
        # [] 사이에 값이 없다는 뜻
        if bracket[i-1] == "[":
            answer += tmp

        # [ pop ([[]])
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)

# ---
# 재귀적 접근
import sys
input = sys.stdin.readline

s = list(input().rstrip())[::-1]

def cal(start):
    r = 0
    while s:
        a = s.pop()
        if a == "(" or a == "[":
            r += cal(a)
        elif start == "(" and a == ")":
            return 2 * max(1,r)
        elif start == "[" and a == "]":
            return 3 * max(1,r)
    
    # 리스트가 비었는데 최종 return 하지 못했다는 것은 괄호에 문제가 있음을 의미
    print(0)
    sys.exit()

ans = 0    
while s:
    ans += cal(s.pop())
print(ans)