import sys
sys.setrecursionlimit(1000000)
# i,jをゴールとする
# この時i-1,jまたはi,j-1のどちらかはスタート地点か途中の線路になる
# マスi,jでスタートがすでにされている時のスコアをs[i][j]とすると
# ans[i][j]=A[i][j]+min(s[i-1][j], s[i][j-1])+Cで表現できる
# また、s[i][j]はそのマスがスタートか、それより手前のどこかをスタートにしているので
# s[i][j]=min(A[i][j], s[i-1][j]+C, s[i][j-1]+C)で表現できる
# 先にs[i][j]を計算してそのあとans[i][j]を計算するようにすれば答えをえる事ができる
H,W,C=[int(i) for i in input().split()]
A=[]
for i in range(H):
    A.append([int(i) for i in input().split()])
s=[[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i==0 and j==0: # スタート地点の場合
            s[i][j]=A[i][j]
        elif i==0:
            s[i][j]=min(A[i][j], s[i][j-1]+C)
        elif j==0:
            s[i][j]=min(A[i][j], s[i-1][j]+C)
        else:
            s[i][j]=min(A[i][j], s[i-1][j]+C, s[i][j-1]+C)
maxv=10**13
ans=[[maxv for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i==0 and j==0:
            continue
        elif i==0:
            ans[i][j]=A[i][j]+s[i][j-1]+C
        elif j==0:
            ans[i][j]=A[i][j]+s[i-1][j]+C
        else:
            ans[i][j]=A[i][j]+min(s[i-1][j], s[i][j-1])+C
minv=maxv
for i in range(H):
    for j in range(W):
        if minv>ans[i][j]:
            minv=ans[i][j]
 
# i>i'の場合を考える
s=[[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W-1, -1, -1):
        if i==0 and j==W-1: # スタート地点の場合
            s[i][j]=A[i][j]
        elif i==0:
            s[i][j]=min(A[i][j], s[i][j+1]+C)
        elif j==W-1:
            s[i][j]=min(A[i][j], s[i-1][j]+C)
        else:
            s[i][j]=min(A[i][j], s[i-1][j]+C, s[i][j+1]+C)
maxv=10**13
ans=[[maxv for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W-1, -1, -1):
        if i==0 and j==W-1:
            continue
        elif i==0:
            ans[i][j]=A[i][j]+s[i][j+1]+C
        elif j==W-1:
            ans[i][j]=A[i][j]+s[i-1][j]+C
        else:
            ans[i][j]=A[i][j]+min(s[i-1][j], s[i][j+1])+C
for i in range(H):
    for j in range(W):
        if minv>ans[i][j]:
            minv=ans[i][j]
print(minv)