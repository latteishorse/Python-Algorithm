# 1181

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

# 선택정렬
#--------

# 아이디어
# 1. 문자열 변환 후 len으로 개수 카운트
# 2. 개수가 적은 순서대로 sort

# 3. 길이가 짧은 것 부터 출력하면서 
# 4. 길이가 같으면 입력 받은 값 첫 문자를 아스키 코드로 변환
# 아스키는 숫자 -> 대문자 -> 소문자 순서

# 5. 아스키 코드로 변환된 수 대소 여부 판별하여 사전순으로 출력

# ---------
# sort는 문자도 정렬 가능
# https://kingofbackend.tistory.com/98

import sys

n = int(sys.stdin.readline())
b = []

for _ in range(n):
    b.append(sys.stdin.readline().strip())

b = list(set(b))
b.sort(key=lambda x : len(x))

print("\n".join(b))

# br = sorted(b)

# for j in br:
#     print(j)
