# 11022
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

import sys
a = int(input())

for i in range(1, a+1) :
    a = a + 1
    if i != a :
        b, c = map(int, sys.stdin.readline().split())
        print("Case #"+str(i)+":",str(b),"+",str(c),"=",b+c)
    elif i == a :
        break