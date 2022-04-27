# 2098

# 비트마스크를 통해 방문한 도시를 표시

# https://developmentdiary.tistory.com/406
# https://shoark7.github.io/programming/algorithm/solve-tsp-with-dynamic-programming 
# https://withhamit.tistory.com/246
# https://sdesigner.tistory.com/54 

'''
A,B,C,D를 방문한 경우 1111
A,B,C를 방문한 경우 1110
A,C를 방문한 경우 1010
C를 방문한 경우 0010

'''
import sys
 
def find(now, before):
    # 남아있는 경로를 이미 방문한 적이 있음
    if dp[now][before]:
        return dp[now][before]

    # 모두 방문한 경우
    if before == (1<<n) - 1:
        return path[now][0] if path[now][0] > 0 else sys.maxsize
 
    # 현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = sys.maxsize
    for i in range(1, n):
        # before가 다른 노드를 방문한 적이 있고, 이동하려는 지점이 이동 불가할 때
        if not (before>>i)%2 and path[now][i]:
            # i부터 0까지 순회를 만든 최소 비용
            tmp = find(i, before|(1<<i)) #before | (1<<i) == before + (1<<i) == before에 i값 십진수 변환 후 추가
            # (now~i), (i~0)의 합과 현재까지의 최소 비용과 비교
            cost = min(cost, tmp + path[now][i])
 
    # 메모이제이션
    dp[now][before] = cost
    return cost
 

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)]
 
print(find(0, 1))

'''

def tsp(dists):
    N = len(dists)
    VISITED_ALL = (1 << N) - 1

    # range(N): 방문한 도시
    # 1<<N을 통해 방문한 도시 집합에 대응
    # 초기값은 None
    cache = [[None] * (1 << N) for _ in range(N)]


    INF = float('inf')
    
    def find_path(last, visited):

        # 시작 도시와 방문 도시의 경로가 존재하면 경로값 반환, 없다면 무한 반환
        if visited == VISITED_ALL:
            return dists[last][0] or INF

        # 이미 계산했다면 (None이 아니므로) 값 바로 반환
        if cache[last][visited] is not None:
            return cache[last][visited]
            
        # 
        tmp = INF        
        for city in range(N):
            # 첫계산이라면
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                # 방문하지 않은 모든 도시를 모두 방문해서 그 중 최소값을 선택해야 한다
                tmp = min(tmp,find_path(city, visited | (1 << city)) + dists[last][city])
            
        cache[last][visited] = tmp
        return tmp
                

    return find_path(0, 1 << 0)
    '''