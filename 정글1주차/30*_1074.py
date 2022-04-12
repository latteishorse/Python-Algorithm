# 1074
# z
# - 행, 열이 2배 증가하면 경로 수는 4배 증가
# - 화살표 움직이듯 오른쪽 이동하면 c값 +1 , 아래로 이동하면 r값 +2
# - 2^(n-1)을 하여 섹터를 4개로 나눔

N, r, c = map(int, input().split())
def sol(N, r, c):
	if N == 0:
		return 0
	return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))
print(sol(N, r, c))


# # 
# 2 *(r%2)
# +(c%2) 
# + 4 *
# # 2^(1/2)로 나누고 행렬을 반으로 나눔
# sol(N-1, int(r/2), int(c/2))