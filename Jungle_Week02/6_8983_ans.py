import sys
input = sys.stdin.readline

m, n, l = map(int,input().split())
lane = sorted(list(map(int, input().split())))

count = 0
for _ in range(n):
    x, y = map(int, input().split())

    left = 0
    right = len(lane) - 1

    if l >= y:
        while left <= right:
            mid = (left + right) // 2
            xg = lane[mid]

            if (y <= l and xg-l <= x <= xg + l) and (x - (xg-l) >= y and x - xg + y <= l):
                count += 1
                break
                
            if x>= xg:
                left = mid + 1
            
            else:
                right = mid - 1
print(count)

