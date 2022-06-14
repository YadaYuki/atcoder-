from collections import deque
a,N = map(int,input().split())

cost = [-1] * (10 ** 6)

Q = deque()

Q.append(1)

def tail_to_head_int(a):
    digit = len(str(a)) 
    return a // 10 + a % 10 * (10 ** (digit - 1))


cost[1] = 0

digit_N = len(str(N))

while len(Q) > 0:
    x = Q.popleft()
    xa = x * a

    digit_xa = len(str(xa))


    if digit_xa <= digit_N:
        if cost[xa] == -1:
            cost[xa] = cost[x] + 1
            if xa == N:
                print(cost[xa])
                exit()
            Q.append(xa)

    if x >= 10 and x % 10 != 0:
        xp = tail_to_head_int(x)
        if cost[xp] == -1:
            cost[xp] = cost[x] + 1
            if xp == N:
                print(cost[xp])
                exit()
            Q.append(xp)
    
print(cost[N])