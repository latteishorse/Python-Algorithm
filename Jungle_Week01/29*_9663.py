# 9663
# N-queen
# https://sung-jun.tistory.com/m/112
# https://woonys.tistory.com/entry/%EC%A0%95%EA%B8%80%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90-5%EC%9D%BC%EC%B0%A8-TIL-%EC%9E%AC%EA%B7%80-%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98?category=961588

# 9663
# N-queen

#내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
        
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)