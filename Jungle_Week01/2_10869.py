# 10869

# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

A, B = map(int, input().split())
print(A+B, A-B, A*B, int(A/B), A%B, sep='\n')