# 5639
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def postorder(start, end):
    if start > end:
        return
    else:
        root = preorder[start]
        mid = end + 1
        for i in range(start + 1, end + 1):
            if root < preorder[i]:
                mid = i
                break
        postorder(start+1, mid-1)
        postorder(mid, end) 
        print(root) 

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(0, len(preorder)-1)
