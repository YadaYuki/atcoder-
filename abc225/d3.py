N,Q = map(int,input().split())

trains = [[None,None] for _ in range(N)] 
ans =[]
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        _,x,y = query
        trains[x-1][1] = y-1
        trains[y-1][0] = x-1
    elif query[0] == 2:
        _,x,y = query
        trains[x-1][1] = None
        trains[y-1][0] = None
    else:
        _,x = query
        x -= 1
        while trains[x][0] != None:
            x = trains[x][0]
        ans_i = []
        while x != None:
            ans_i.append(x+1)
            x = trains[x][1]
        ans.append(ans_i)

for i in ans:
    print(len(i),end=' ')
    print(*i)
            
        
