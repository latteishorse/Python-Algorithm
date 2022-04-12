N = input() # 영향 없음
b = list(map(int, input().split()))

M = input() # 영향 없음
c = list(map(int, input().split()))
d = sorted(b) # 이분 탐색 전 정렬 필요


def bin(d, key):
    pl = 0
    pr = len(b) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        if d[pc] == key:
            return 1 
        elif d[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1 
    return 0

for i in c:
    print(bin(d,i))