# 5904
import sys
input = sys.stdin.readline

n = int(input())
k, leng = 0, 3

while leng < n: 
    k += 1
    leng = 2*leng + (k+3) 

# moo(k, leng, input number)
def moo(k, leng, num):

    # moo s(0) 일때
    if k == 0:
        if num == 1:
            return 'm'
        else:
            return 'o'

    # 중간 지점
    # len(s(k)) = 2* len(s(k-1)) + k + 3
    # lo = 2 l + k + 3
    # lo-k-3 // 2 = l
    # k-1 

    leng = (leng-k-3) // 2
    k -= 1

    # 앞쪽에 있을 경우
    if num <= leng:
        return moo(k, leng, num)

    # leng 다음에 있을 경우
    elif num == leng + 1:
        return 'm'

    # 뒤쪽에 있을 경우
    # leng + k + 3 + 1
    elif num > leng + k + 4: 
        return moo(k, leng, num - leng - k - 4)

    else:
        return 'o'


print(moo(k, leng, n))
