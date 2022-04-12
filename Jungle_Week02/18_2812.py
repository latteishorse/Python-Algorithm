# 숫자를 뽑아서 큰 수를 만듦
# 
# 리스트에 일렬로 배치해두고 
# 조합으로 뽑아보며 가장 높은 수를 갱신해가는 방식으로 접근하면 될듯

# 주어진 수
N, K = map(int, input().split())
num = list(input())
stack = []
ctr = K
for i in range(N):
    while stack and stack[-1] < num[i] and ctr > 0:
        stack.pop()
        ctr -= 1
    stack.append(num[i])

print(''.join(stack))
