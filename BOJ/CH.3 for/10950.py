# 10950
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# input 갯수를 입력 받은 값으로 변수를 만들어서 지정해야됨
# 입력 받은 수를 for문에서 돌려서 테스트 케이스마다 실행

a = int(input())

for i in range(1, a+1) :
    a = a + 1
    if i != a :
        b, c = map(int, input().split())
        print(b+c)
    elif i == a :
        break