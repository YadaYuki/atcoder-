N,Q = map(int,input().split())

head_and_tail = [] # i番目の電車に連結されている前後の電車

for _ in range(N):
    head_and_tail.append([None,None])


ans = []

for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 3:
        head_train = query[1] - 1
        while head_and_tail[head_train][0] != None:
            head_train = head_and_tail[head_train][0]
        trains = []
        while head_train != None:
            trains.append(head_train + 1)
            head_train = head_and_tail[head_train][1]
        ans.append(trains)
    else:
        q,x,y = query
        if q == 1:
            head_and_tail[x-1][1] = y - 1
            head_and_tail[y-1][0] = x - 1
        if q == 2:
            head_and_tail[x-1][1] = None
            head_and_tail[y-1][0] = None



for i in range(len(ans)):
    print(len(ans[i]),end=" ")
    for j in range(len(ans[i])):
        print(ans[i][j],end=" ")
    print()
