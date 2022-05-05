# 5622
import sys; input = sys.stdin.readline
n = str(input().strip().upper())

times = 0
for i in n:
    time = i
    if time == '1':
        times += 2
    elif time =='A' or time == 'B' or time == 'C':
        times += 3
    elif time =='D' or time == 'E' or time == 'F':
        times += 4
    elif time =='G' or time == 'H' or time == 'I':
        times += 5
    elif time =='J' or time == 'K' or time == 'L':
        times += 6
    elif time =='M' or time == 'N' or time == 'O':
        times += 7
    elif time =='P' or time == 'Q' or time == 'R' or time == 'S':
        times += 8
    elif time =='T' or time == 'U' or time == 'V':
        times += 9
    elif time =='W' or time == 'X' or time == 'Y' or time =='Z':
        times += 10
    else :
        times += 11
print(times)
