# 예제는 잘 되는데...

# n, w, L = map(int, input().split())
# trucks = list(map(int, input().split()))

# time = 1
# weight = 0
# q = []

# for truck in trucks:

#     while weight + truck > L or len(q) >= w:

#         time, front_weight = q.pop(0)
#         weight -= front_weight

#     q.append((time + w, truck))
#     weight += truck
#     time += 1


# print(q[-1][0])

# ----
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
 
# 길이만큼 다리를 만듦
bridge = [0] * w
time = 0
 
while bridge:
    time += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)

print(time)