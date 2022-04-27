# 멀티탭 구멍 N
# 전기 용품의 총 사용횟수 K

# 사용순서대로 수 하나씩

# 2, 7
# 2 3 2 3 1 2 7

# 2 3 2 3 
# 3 pop
# 1 append
# 1 pop
# 7 append

# 2 - 3
# 3- 2
# 1- 1, 7 -1

# [][] 배열 n개에 n개를 넣고,
# 움직임을 최소화

# 
N, K = map(int, input().split())
tap = list(map(int, input().split()))

# tapNum = [0] * (K+1)

# for i in tap:
#     tapNum[i] += 1

# i = max(tapNum)
# high = tapNum.index(i)
# tapNum[i] = 0

# j = max(tapNum)
# hi = tapNum.index(j)

plug = tap[:N]
unplug = tap[N:]

cnt = 0
while unplug:
    plug.append(unplug.pop(0))

    if plug[0] ==unplug[0] or plug[1] == unplug[0]:
        unplug.pop(0)

        # plug.pop()
        # cnt += 1

    # elif plug[1] == plug[-1]:
    #     del list[1]
    else:

        plug.append(unplug.pop(0))

        plug.pop(0)

        cnt += 1

    print(plug)
    print(cnt)    

    # if plug[0] == high or plug[0] == hi:
    #     # plug.pop(0)
    #     print(1)
    # # if plug[0] == plug[-1] or plug[1] == plug[-1]:
    # # if plug[1] == high or plug[1] == hi:
    #     print(2)        
    # else:
    #     plug.pop(0)
    #     cnt += 1
    # print(plug)

    # print(cnt)

# cnt = 0
# while unplug:
#     plug.append(unplug.pop(0))
#     if plug[0] == plug[-1] or plug[1] == plug[-1]:
#         plug.pop(0)
#         cnt += 1

#     # elif plug[1] == plug[-1]:
#     #     del list[1]
#     else:
#         plug.pop(0)
#         # cnt += 1

#     print(plug)
#     print(cnt)    
