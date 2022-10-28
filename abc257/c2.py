N = int(input())
S = list(input())
W = list(map(int,input().split()))

d = [[W[i],S[i]] for i in range(N)]

d.sort()
adults = []
children = []

for i in  range(N):
    if S[i] == "1":
        adults.append(W[i])
    else:
        children.append(W[i])

ans = len(adults)

adult_cnt = 0
left_adult_cnt = len(adults)
children_cnt = 0
left_children_cnt = len(children)
# print(d)
for i in range(N):
    w,s = d[i]
    if s == "0":
        children_cnt += 1
        left_children_cnt -= 1
    else:
        adult_cnt += 1
        left_adult_cnt -= 1
    if i < N-1:
        if d[i][0] != d[i+1][0]:
            ans = max(ans,children_cnt + left_adult_cnt)
    else:
        ans = max(ans,children_cnt + left_adult_cnt)

print(ans)
