N,Q = map(int,input().split())

trains = [[None,None] for _ in range(N)] # [[prev,tail],...]
ans = []
for _ in range(Q):
    query= list(map(int,input().split()))
    if query[0] == 3:
        _,x = query
        x-=1
        # search head
        while trains[x][0] != None:
            x = trains[x][0]
        a = []
        while x != None:
            a.append(x+1)
            x = trains[x][1]
        ans.append(a)
    else:
        q,x,y = query
        x -= 1
        y -= 1
        if q == 1:
            trains[x][1] = y
            trains[y][0] = x
        else:
            trains[x][1] = None
            trains[y][0] = None
for i in range(len(ans)):
    print(len(ans[i]),*ans[i])