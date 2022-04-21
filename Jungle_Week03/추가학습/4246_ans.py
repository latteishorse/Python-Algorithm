import sys
input = sys.stdin.readline
 
def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        ans.append(*preorder)
        return
        
    root = inorder.index(preorder[0])

    postorder(preorder[1:root+1], inorder[:root])
    postorder(preorder[root+1:], inorder[root+1:])
    ans.append(preorder[0])
 
testcase = int(input())
for _ in range(testcase):
    ans = []
    n = int(input()) 
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    postorder(preorder, inorder)
    print(*ans)
