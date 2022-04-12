# def recur(n):
#     if n == 1:
#         print('1')
#     else:
#         for _ in range(n):
#             recur(n-1)

# n = int(input())
# recur(n)

# ----
global result
def adjacent(x):
    return True

def dfs(x):
    # 종료 조건
    if x == N:
        result += 1

    # 종료 전 실행 루프
    else:

        for i in range(N):
            # row[x] = i
            if adjacent(x):
                dfs(x + 1)

result = 0
N = int(input())
dfs(0)
print(result)