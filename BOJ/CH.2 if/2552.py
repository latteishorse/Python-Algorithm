# 2552

h, m = map(int, input().split())
t = int(input())

h = ((t+m)//60 + h)%24
m = (m+t)%60

print(h, m)

# h, m = map(int, input().split())
# t = int(input())

# h += t//60
# m += t%60

# if m >= 60 :
#     h += 1
#     m -= 60

# if h >= 24:
#     h -= 24

# print(h,m) 
