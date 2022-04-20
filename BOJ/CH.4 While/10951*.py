# 10951
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while 1:
    a, b = map(int, input().split())
    print(a+b)

# 오답
# ------------

# 값이 입력되지 않을 때도 while 구문이 종료될 수 있도록 해야됨
# https://gururuglasses.tistory.com/46

while True:
    try:
        a, b = map(int, input().split())
        0 < a and b < 10
        print(a+b)
    except:
        break

