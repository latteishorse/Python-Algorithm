# 2261
# 분할정복으로 접근
import sys

a = input()
arr = []
temp = input().split()
temp = list(map(int, temp))
arr.append(temp)
for i in range(1, int(a)) :
    temp = input().split()
    temp = list(map(int, temp))
    arr.append(temp)
pa = len(arr)
arr = list(set(map(tuple,arr)))
aa = len(arr)
def length(a, b) :
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 #두 점 사이의 거리를 구합니다.
def smaller(a, b) :
    if a < b : return a
    else : return b # 두 값중 작은 것을 반환합니다.
def minimum(si, ei) : #list의 start index와 end index를 받아 그 사이의 존재하는 가장 거리가 가까운 두 점의 거리의 제곱을 반환합니다.
    lon = ei - si
    if lon == 1 :
        return 0
    elif lon == 2 :
        return length(arr[si], arr[si+1])
    elif lon == 3 :
        a = length(arr[si], arr[si+1])
        b = length(arr[si], arr[si+2])
        c = length(arr[si+1], arr[si+2])
        return smaller(a, smaller(b,c))
    lon = (si+ei)// 2
    mid = arr[lon][0]
    p1 = minimum(si, lon) #분할 합니다.
    p2 = minimum(lon, ei) #상동
    pt = 0
    ttemp = []
    if p1 < p2 : pt = p1
    else : pt = p2
    pm = pt**(1/2)
    for i in range(si, ei) :
        if (mid - arr[i][0])**2 <= pt :
            ttemp.append(arr[i])
    ttemp.sort(key = lambda element:element[1]) #y좌표에 따라 정렬합니다.
    mini = pt
    len_ttemp = len(ttemp)
    if  len_ttemp >= 2 :
        for i in range(len_ttemp-1) :
            for j in range(i+1,len_ttemp) :
                if (ttemp[j][1] - ttemp[i][1])**2 > pt : break #직선 거리가 왼쪽 혹은 오른 쪽 파티션의 최솟값보다 먼 것들에 대해서는 연산하지 않습니다.
                elif ttemp[j][0] < mid and ttemp[i][0] < mid : continue #선에 걸친 것이 아닌 같은 파티션에 존재하는 값들을 걸러냅니다.
                elif ttemp[j][0] > mid and ttemp[j][0] > mid : continue
                a = length(ttemp[j], ttemp[i])
                if a < mini : mini = a
    ttemp = []
    return mini
if pa != aa : #똑같은 좌표가 존재한다 = 가장 가까운 두 점 -> 0
    print("0")
else :
    arr.sort()
    print(minimum(0, len(arr)))

# ---

