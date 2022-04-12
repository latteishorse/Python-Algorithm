# 1085

#한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.


# 1. 한수의 위치에서 w, h 또는 0, 0을 빼서
# 2. 둘 중 작은 값을 선택

#  코드작성

x, y, w, h = map(int, input().split())
dx = abs(x - w)
dy = abs(y - h)

if x > dx and y > dx and dy > dx :
    print(dx)
elif x < dx and y > x and dy > x :
    print(x)
elif y > dy and x > dy and dx > dy :
    print(dy)
elif y < dy and x > y and dx > y :
    print(y)
elif x == y or dx == dy :
    if x > dx : 
        print(dx)
    elif x < dx :
        print(x)

#  -------------------------

# python max, min 

x,y,w,h=map(int,input().split())
print(min(x, y, w-x, h-y))