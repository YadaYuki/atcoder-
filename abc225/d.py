from collections import deque
N,Q = map(int,input().split())

front_and_back = []

for _ in range(N):
    front_and_back.append([None,None])

ans = []
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x,y =  query[1:]
        front_and_back[x-1][1] = y - 1 # xの後部がy
        front_and_back[y-1][0] = x - 1 # yの前部がx
    elif query[0] == 2:
        x,y =  query[1:]
        front_and_back[x-1][1] = None # xの後部が
        front_and_back[y-1][0] = None # yの前部がx
    elif query[0] == 3:
        x = query[1]
        Q = deque()
        # append prev
        Q.append(x)
        item = front_and_back[x-1]
        while item[0] != None:
            Q.appendleft(item[0] + 1)
            item = front_and_back[item[0]]
        
        # append back
        item = front_and_back[x-1]
        while item[1] != None:
            Q.append(item[1] + 1)
            item = front_and_back[item[1]]
        ans.append(Q)
        
for item in ans:
    print("{} ".format(len(item)),end="")
    for q in item:
        print("{} ".format(q),end="")
    print()





