# 1946

# 둘 중에 하나는 높아야한다
# 둘다 높아도 된다
# 둘다 낮으면 안된다 -> 둘다 낮은 경우를 카운트해서 전체에서 빼주는 방향으로 접근하면 어떨까?
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort()

    minRank = score[0][1]
    cnt = 1

    for i in range(N):
        rank = score[i][1]
        if rank < minRank:
            minRank = rank
            cnt += 1
    print(cnt)


    # ans = 1
    # end = score[0][1]

    # for p, s in score[1:]:
    #     if p >= end:
    #         ans += 1
    #         end = s
    