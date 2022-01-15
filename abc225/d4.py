N,Q = map(int,input().split())


trains = [[None,None] for _ in range(N)]
ans =[]
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x,y = map(lambda x:x-1,q[1:])
        trains[x][1] = y
        trains[y][0] = x
    elif q[0] == 2:
        x,y = map(lambda x:x-1,q[1:])
        trains[x][1] = None
        trains[y][0] = None
    else:
        x = q[1]-1
        head_train = x
        while trains[head_train][0] != None:
            head_train = trains[head_train][0]
        ans_i = [head_train + 1]
        tail_train = head_train
        while trains[tail_train][1] != None:
            tail_train = trains[tail_train][1]
            ans_i.append(tail_train+1)
        ans.append(ans_i)
        

for i in ans:
    print(len(i),end=' ')
    print(*i)
