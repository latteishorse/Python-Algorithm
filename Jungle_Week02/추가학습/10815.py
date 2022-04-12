# 1920
N = input() # 영향 없음
b = list(map(int, input().split()))

M = input() # 영향 없음
c = list(map(int, input().split()))
d = sorted(b) # 이분 탐색 전 정렬 필요

def bin_search(d, key):
    pl = 0           # 검색 범위 맨 앞 원소의 인덱스
    pr = len(b) - 1  # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        if d[pc] == key:
            return 1    # 검색 성공
        elif d[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:
            break
    return 0            # 검색 실패

for i in c:
    print(bin_search(d, i), end=' ')

